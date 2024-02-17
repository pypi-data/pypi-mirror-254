import re
import time
import asyncio
import uuid
import random
from logging import getLogger
from dataclasses import dataclass
from typing import Callable, Optional, AsyncIterator, Coroutine
from functools import partial

import openai
import tiktoken
from dotenv import load_dotenv

from . import parser
from . import utils
from . import ranking
from .data_structures import GeneratedPassage

logger = getLogger(__name__)

load_dotenv()

# _openai_sync_client = None
# _openai_async_client = None

# def openai_sync_client():
#     global _openai_sync_client
#     if _openai_sync_client is None:
#         _openai_sync_client = openai.OpenAI()
#     return _openai_sync_client

# def openai_async_client():
#     global _openai_async_client
#     if _openai_async_client is None:
#         _openai_async_client = openai.AsyncOpenAI()
#     return _openai_async_client

class GenerationError(Exception):
    pass

RATE_LIMIT_INTERVAL = 60  # seconds

token_rate_limit_by_model_name = {
    'gpt-4': 300_000,
    'gpt-3.5-turbo': 1_000_000,
    'gpt-3.5-turbo-16k': 1_000_000,
    'gpt-3.5-turbo-instruct': 250_000,
}

model_name_to_token_limit = {
    'gpt-4': 8192,
    'gpt-3.5-turbo-16k': 16384,
    'gpt-3.5-turbo': 4096,
    'gpt-3.5-turbo-16k-0613': 16384,
}

def prompt_claim_element_only(claim_element, prior_art_passage, n_passages_per_split=3):
    messages = [
        {"role": "system", "content": f"You work for a law firm. Your task is to interpret a single claim element that I select from the claims of a patent. Then I'm going to give you a passage from the prior art and you need to pick {n_passages_per_split} distinct sub-passages from the passage that you believe are the most similar to the claim element. Please output only those {n_passages_per_split} passages, copied verbatim from the prior art. Do not add any other text besides the verbatim passages."},
        {"role": "user", "content": f"Selected claim element: {claim_element}"},
        {"role": "user", "content": f"Prior art passage: {prior_art_passage}"},
    ]
    return messages

def prompt_summary_full_set_of_claims(summary, claims, claim_element, prior_art_passage, n_passages_per_split=3):
    messages = [
        {"role": "system", "content": f"You work for a law firm. Your task is to read the summary of the written description of a patent and the full set of claims in the patent and interpret a single claim element that I select from the claims of the patent in light of the summary and the full set of claims. Then I'm going to give you a passage from the prior art and you need to pick {n_passages_per_split} distinct sub-passages from the passage that you believe are the most similar to the claim element. Please output only those {n_passages_per_split} passages, copied verbatim from the prior art. Do not add any other text besides the verbatim passages."},
        {"role": "user", "content": f"Summary of the written description of the invention: {summary}"},
        {"role": "user", "content": f"Full set of claims: {claims}"},
        {"role": "user", "content": f"Selected claim element: {claim_element}"},
        {"role": "user", "content": f"Prior art passage: {prior_art_passage}"},
    ]
    return messages

def post_process_selected_passage_gpt4(passage: str) -> list[str]:
    split_strategies = [
        lambda passage: re.split(r'\d+\.', passage),
        lambda passage: passage.split('\n\n'),
        lambda passage: passage.split('\"\n'),
    ]
    for split_strategy in split_strategies:
        split_passages = split_strategy(passage)
        if len(split_passages) > 1:
            break
    # strip newlines, quotes, and whitespace from beginning and end
    split_passages = [p.strip().strip('"') for p in split_passages]
    # filter whitespace only and empty string entries
    split_passages = [p for p in split_passages if p != '']
    # filter out passages that are just a newline
    split_passages = [p for p in split_passages if p != '\n']
        
    return split_passages

@dataclass
class GeneratorConfig:
    model_name: str = 'gpt-4'
    target_n_passages: int = 10
    min_n_splits: int = 1
    generate_passages_prompt_func: Callable[..., list[dict]] = prompt_summary_full_set_of_claims
    post_process_generated_passages_func: Callable[[str], list[str]] = post_process_selected_passage_gpt4

def load_generator_config_from_env():
    return GeneratorConfig()

def num_tokens_in_text(text, model="gpt-3.5-turbo-0613"):
  """Returns the number of tokens in a string."""
  try:
      encoding = tiktoken.encoding_for_model(model)
  except KeyError:
      encoding = tiktoken.get_encoding("cl100k_base")
  return len(encoding.encode(text))

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613"):
  """Returns the number of tokens used by a list of messages."""
  try:
      encoding = tiktoken.encoding_for_model(model)
  except KeyError:
      encoding = tiktoken.get_encoding("cl100k_base")
  if model == "gpt-3.5-turbo-0613":  # note: future models may deviate from this
      num_tokens = 0
      for message in messages:
          num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
          for key, value in message.items():
              num_tokens += len(encoding.encode(value))
              if key == "name":  # if there's a name, the role is omitted
                  num_tokens += -1  # role is always required and always 1 token
      num_tokens += 2  # every reply is primed with <im_start>assistant
      return num_tokens
  else:
      raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
  See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")

def concatenate_completions_for_reranking(completions):
    # concatenate completions and renumber
    # TODO: make 3 a parameter
    concatenated_completions = ''
    for i, completion in enumerate(completions):
        completion_content = completion['choices'][0]['message']['content']
        completion_content1, completion_content = completion_content.split('\n2.')
        completion_content1 = completion_content1.lstrip('1. ')
        completion_content2, completion_content = completion_content.split('\n3.')
        completion_content3 = completion_content
        
        concatenated_completions += f'{int_to_roman(i*3 + 1)}. {completion_content1}\n'
        concatenated_completions += f'{int_to_roman(i*3 + 2)}. {completion_content2}\n'
        concatenated_completions += f'{int_to_roman(i*3 + 3)}. {completion_content3}\n'
    return concatenated_completions, 3 * len(completions)

# Reranking utility functions
def int_to_roman(n: int) -> str:
    if not (0 < n < 4000):
        raise ValueError("Input integer must be between 1 and 3999")
    
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD', 'C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    
    for i in range(len(ints)):
        count = int(n / ints[i])
        result.append(nums[i] * count)
        n -= ints[i] * count
    
    return ''.join(result)

# parse reranked completions
def parse_reranked_completions(reranked_completion, n_completions):
    # First lstrip prelude before 1.
    # Find index of '1. ' and slice
    reranked_completion = reranked_completion[reranked_completion.index('1. '):]
    
    # Split on i. for i in range(1, n_completions + 1)
    # Then lstrip roman numeral and period
    roman_numeral_regex_pattern = r''
    for i in range(1, n_completions + 1):
        roman_numeral_regex_pattern += f'{int_to_roman(i)}\. '
        if i < n_completions:
            roman_numeral_regex_pattern += '|'
    roman_numeral_regex = re.compile(roman_numeral_regex_pattern)
    
    parsed_completions = []
    for i in range(1, n_completions + 1):
        if i == n_completions:
            parsed_completion = reranked_completion
        else:
            parsed_completion, reranked_completion = reranked_completion.split(f'{i+1}. ', maxsplit=1)
        if i == 1:
            parsed_completion = parsed_completion.lstrip('1. ')
        parsed_completion = re.sub(roman_numeral_regex, '', parsed_completion)
        parsed_completion = parsed_completion.lstrip(' "')
        parsed_completion = parsed_completion.rstrip(' \n"')
        parsed_completions.append(parsed_completion)
        
    return parsed_completions


def openai_prompt_select_passages_from_prior_art_portion(all_but_claims, claims, claim_element, prior_art_passage):
    # TODO: make 3 a parameter
    messages = [
        {"role": "system", "content": "You are an associate at a big law firm. Your task is to read the written description and of an invention disclosed in a patent and the full set of claims in the patent and interpret a single claim element that I select from the claims of the patent in light of the written description and the full set of claims. Then I'm going to give you a passage from of prior art and you need to pick three distinct sub-passages from the passage that you believe are the most semantically similar to the claim element interpreted in light of the written description and the full set of claims. Please output only those three passages, each preceded only by the numberings 1., 2., and 3. and a space."},
        {"role": "user", "content": f"Written description of invention: {all_but_claims}"},
        {"role": "user", "content": f"Full set of claims: {claims}"},
        {"role": "user", "content": f"Selected claim element: {claim_element}"},
        {"role": "user", "content": f"Prior art passage: {prior_art_passage}"},
    ]
    return messages

def openai_prompt_rank_selected_passages(all_but_claims, claims, claim_element, chosen_prior_art_passage, n_completions):
    messages = [
        {"role": "system", "content": f"Your task is to read the written description and of an invention disclosed in a patent and the full set of claims in the patent and interpret a single claim element that I select from the claims of the patent in light of the written description and the full set of claims. Then I'm going to give you {n_completions} sub-passages from the prior art passage i presented to you that you chose because they were the most semantically similar to the selected claim element interpreted in light of the written description and the full set of claims. Please rank these {n_completions} passages in descending order of similarity to the selected claim element interpreted in light of the written description and the full set of claims. I will give you passages numbered by roman numerals, for example: 'I. Passage One... II. Passage two... III. Passage three...'. Please output only the integer ranking following by the roman numeral and passage, for example: '1. II. Passage two ... 2. I. Passage one... 3. III Passage three...' if you believe the ranking should be passage two > passage one > passage three."},
        {"role": "user", "content": f"Written description of invention: {all_but_claims}"},
        {"role": "user", "content": f"Claim element: {claim_element}"},
        {"role": "user", "content": f"Prior art passages to rank: {chosen_prior_art_passage}"},
    ]
    return messages

def openai_chat_completion_request_with_retry(model_name, messages, backoff_factor=2, backoff_override=None):
    for i in range(1, 3):
        try:
            # completion = openai_sync_client().chat.completions.create(
            #     model=model_name,
            #     messages=messages
            # )
            completion = openai.ChatCompletion.create(
                model=model_name,
                messages=messages
            )
            return completion
        except openai.OpenAIError as e:
            if backoff_override is not None:
                time.sleep(backoff_override)
            else:
                time.sleep(backoff_factor**i)
            continue
        except Exception as e:
            raise e
    raise Exception("Failed to send chat completion request to OpenAI after 4 retries.")

class FixedWindowRateLimiter:
    def __init__(self, capacity: int, fill_interval: float):
        self.capacity = capacity
        self.fill_interval = fill_interval
        self.last_fill_time = None
        self.tokens = capacity
        self.lock = asyncio.Lock()
        
    async def remove_tokens(self, n: int):
        async with self.lock:
            self.tokens -= n
    
    async def request_and_remove_tokens(self, n: int):
        async with self.lock:
            if self.tokens >= n:
                self.tokens -= n
                return True
            else:
                return False
            
    async def wait_for_tokens(self, n: int, timeout: int = 3600, request_uid: Optional[str] = None):
        if n > self.capacity:
            raise ValueError(f"n tokens must be less than or equal to capacity {self.capacity}")
        start_time = time.monotonic()
        while True:
            if await self.request_and_remove_tokens(n):
                return True
            print(f'request {request_uid} waited {time.monotonic() - start_time} for tokens')
            if time.monotonic() - start_time > timeout:
                print(f'Timed out waiting for tokens for request {request_uid}')
                return False
            await asyncio.sleep(self.fill_interval - (time.monotonic() - self.last_fill_time))

    async def fill_tokens(self):
        async with self.lock:
            self.tokens = self.capacity

    async def refill(self):
        while True:
            await self.fill_tokens()
            self.last_fill_time = time.monotonic()
            await asyncio.sleep(self.fill_interval)

    async def __aenter__(self):
        self.refill_task = asyncio.create_task(self.refill())
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback):
        self.refill_task.cancel()
        return False

async def aopenai_chat_completion_request_with_retry(model_name, messages, backoff_factor=2, backoff_override=None, n_retries=3, rate_limiter: Optional[FixedWindowRateLimiter] = None, **kwargs) -> dict:
    """Send a chat completion request to OpenAI with retries."""
    uid = str(uuid.uuid4())
    for i in range(1, 1 + n_retries):
        try:
            if rate_limiter is not None:
                num_tokens_in_messages = num_tokens_from_messages(messages)
                print(f'Waiting for {num_tokens_in_messages} tokens for request {uid}...')
                if await rate_limiter.wait_for_tokens(num_tokens_in_messages, request_uid=uid):
                    print(f'Got {num_tokens_in_messages} tokens for request {uid}')
                    # completion = await openai_async_client().chat.completions.create(
                    #     model=model_name,
                    #     messages=messages,
                    #     **kwargs
                    # )
                    completion = await openai.ChatCompletion.acreate(
                        model=model_name,
                        messages=messages,
                        **kwargs
                    )
                    n_tokens_in_completion = completion['usage']['completion_tokens']
                    await rate_limiter.remove_tokens(n_tokens_in_completion)
            else:
                # completion = await openai_async_client().chat.completions.create(
                #         model=model_name,
                #         messages=messages,
                #         **kwargs
                #     )
                completion = await openai.ChatCompletion.acreate(
                    model=model_name,
                    messages=messages,
                    **kwargs
                )
            return completion
        # except openai.OpenAIError as e:
        except openai.error.OpenAIError as e:
            logger.error(f"OpenAIError: {e}")
            if backoff_override is not None:
                jitter = random.uniform(-0.10, 0.10)
                await asyncio.sleep(backoff_override * (1 + jitter))
            else:
                jitter = random.uniform(-0.10, 0.10) 
                await asyncio.sleep(backoff_factor**i * (1 + jitter))
            continue
        except Exception as e:
            raise e
    raise Exception(f"Failed to send chat completion request to OpenAI after {n_retries} retries.")


def split_passage_to_meet_model_token_limit(passage: str, prompt_func: Callable[[str], list[dict]], model_name: str, min_n_splits: int = 1) -> list[str]:
    """ 
    Given a passage string, a prompt func that takes only the passage string, and a model, find the smallest number of splits necessary to get messages under token limit and return splits of the passage.
    """
    token_limit = model_name_to_token_limit[model_name]
    min_split_size = 256
    base_num_tokens = num_tokens_from_messages(
        prompt_func(' ' * min_split_size)
    )
    if base_num_tokens > token_limit:
        raise GenerationError("Prompt exceeds token limit by itself.")
    
    passage_splits = []
    passage_split_count = min_n_splits
    while True:
        # Check all splits
        candidate_splits = []
        for i in range(passage_split_count):
            if i == 0:
                candidate_split = passage[:len(passage) // passage_split_count]
            else:
                candidate_split = passage[len(passage) // passage_split_count * i:len(passage) // passage_split_count * (i+1)]
            candidate_splits.append(candidate_split)
        num_tokens = [num_tokens_from_messages(prompt_func(split)) for split in candidate_splits]
        if all([n <= token_limit - 0.05 * token_limit for n in num_tokens]):
            passage_splits = candidate_splits
            break
        passage_split_count += 1

    return passage_splits


def openai_model_id_from_completion(completion: dict) -> str:
    try:
        return f'{completion["model"]}-{completion["system_fingerprint"]}'
    except KeyError:
        return load_generator_config_from_env().model_name


async def agenerate_passages_for_prior_art_splits(prior_art_splits: list[str], prompt_func: Callable[[str], list[dict]], model_name: str, claim_element_id: int, prior_art_id: int, rate_limiter: Optional[FixedWindowRateLimiter] = None) -> list[GeneratedPassage | Exception]:
    # make parallel requests to openai api for prior art splits
    passages: list[GeneratedPassage | Exception] = []
    coros = []
    for prior_art_split in prior_art_splits:
        messages = prompt_func(prior_art_split)
        coros.append(aopenai_chat_completion_request_with_retry(model_name, messages, rate_limiter=rate_limiter))
        
    completions = await asyncio.gather(*coros, return_exceptions=True)
    for i, completion in enumerate(completions):
        if isinstance(completion, Exception):
            print(f'Failed to get completion for prior art split {i} of prior art {prior_art_id} for claim element {claim_element_id}')
            passages.append(completion)
        else:
            selected_passages = completion['choices'][0]['message']['content']
            post_process_generated_passages_func = load_generator_config_from_env().post_process_generated_passages_func
            post_processed_passages = post_process_generated_passages_func(selected_passages)
            # if len(post_processed_passages) == 1:
            #     logger.error(f'Possible error post processing selected passages for claim element {claim_element_id} and prior art {prior_art_id}: \nCompletion: {selected_passages} \nPost-processed: {post_processed_passages}')

            for processed_passage in post_processed_passages:
                # We'll add the start line and end line later
                passages.append(
                    GeneratedPassage(
                        prior_art_source_id=prior_art_id,
                        text=processed_passage,
                        claim_element_id=claim_element_id,
                        model_id=openai_model_id_from_completion(completion)
                    )
                )

    passages = [p for p in passages if not isinstance(p, Exception)]


    return passages

async def agenerate_passages(claim_elements: list[tuple[int, str]], prior_art: tuple[int, str], prompt_func: Callable[[str], list[dict]], model_name: str, target_n_passages: int = 10, min_n_splits:int = 1, rate_limiter: Optional[FixedWindowRateLimiter] = None) -> AsyncIterator[tuple[int, tuple[int, list[str]]]]:
    tasks = []
    for i, claim_element in claim_elements:
        prior_art_splits = split_passage_to_meet_model_token_limit(prior_art[1], partial(prompt_func, claim_element), model_name, min_n_splits=min_n_splits)
        n_passages_per_split = max(target_n_passages // len(prior_art_splits), 1)
        tasks.append(asyncio.create_task(
            agenerate_passages_for_prior_art_splits(prior_art_splits, partial(prompt_func, claim_element, n_passages_per_split=n_passages_per_split), model_name, claim_element_id=i, prior_art_id=prior_art[0], rate_limiter=rate_limiter)
        ))
    
    for coro in asyncio.as_completed(tasks):
        yield await coro

def create_generate_passages_tasks(claim_elements: list[tuple[int, str]], prior_art: tuple[int, str], prompt_func: Callable[[str], list[dict]], model_name: str, target_n_passages: int = 10, min_n_splits:int = 1, rate_limiter: Optional[FixedWindowRateLimiter] = None) -> list[asyncio.Task]:
    tasks = []
    for i, claim_element in claim_elements:
        prior_art_splits = split_passage_to_meet_model_token_limit(prior_art[1], partial(prompt_func, claim_element), model_name, min_n_splits=min_n_splits)
        n_passages_per_split = max(target_n_passages // len(prior_art_splits), 1)
        tasks.append(asyncio.create_task(
            agenerate_passages_for_prior_art_splits(prior_art_splits, partial(prompt_func, claim_element, n_passages_per_split=n_passages_per_split), model_name, claim_element_id=i, prior_art_id=prior_art[0], rate_limiter=rate_limiter)
        ))

    return tasks


def summarize_patent_prompt_func(serialized_patent_spec: str, instruction: str = None):
    if instruction is None:
        instruction = "Summarize the following patent specification in approximately 250 words:"
    return [
        {"role": "user", "content": f"{instruction}"},
        {"role": "user", "content": serialized_patent_spec},
    ]


def summarize_summaries_prompt_func(summaries: list[str], instruction: str = None):
    if instruction is None:
        instruction = "Summarize the following partial summaries of sequential portions of a patent specification in approximately 250 words:"
    return [
        {"role": "user", "content": f"{instruction}"},
        {"role": "user", "content": '\n'.join(summaries)},
    ]

async def asummarize_patent(patent: parser.GoogleParsedPatent, rate_limiter: Optional[FixedWindowRateLimiter] = None):
    generator_config = load_generator_config_from_env()
    serialized_patent_spec = patent.specification

    split_instruction = "Summarize the following portion of a patent specification in approximately 250 words:"
    spec_splits = split_passage_to_meet_model_token_limit(serialized_patent_spec, partial(summarize_patent_prompt_func, instruction=split_instruction), generator_config.model_name)

    if len(spec_splits) == 1:
        summarization_completion = await aopenai_chat_completion_request_with_retry(
            generator_config.model_name, summarize_patent_prompt_func(serialized_patent_spec), rate_limiter=rate_limiter
        )
        summarization = summarization_completion['choices'][0]['message']['content']
    else:
        tasks = []
        # TODO: hack
        for spec_split in spec_splits[:10]:
            tasks.append(
                aopenai_chat_completion_request_with_retry(
                    generator_config.model_name, summarize_patent_prompt_func(spec_split, instruction=split_instruction), rate_limiter=rate_limiter
                )
            )
        completions = await asyncio.gather(*tasks)
        partial_summaries = []
        for completion in completions:
            partial_summaries.append(completion['choices'][0]['message']['content'])

        try:
            summarization_completion = await aopenai_chat_completion_request_with_retry(
                generator_config.model_name, summarize_summaries_prompt_func(partial_summaries), rate_limiter=rate_limiter
            )
            summarization = summarization_completion['choices'][0]['message']['content']
        except GenerationError as e:
            logger.error('Failed to summarize patent %s', patent.unique_id)
            summarization = ''

    return summarization

async def abulk_generate_passages(
        patent: tuple[int, parser.GoogleParsedPatent], 
        prior_art_sources: list[tuple[int, parser.GoogleParsedPatent]], claim_elements: list[tuple[int, str]],
        ranking_params: dict,
        patent_summary: Optional[str] = None,
        ) -> AsyncIterator[GeneratedPassage]:
    # TODO: this function should be refactored to separate concerns
    generator_config = load_generator_config_from_env()
    async with FixedWindowRateLimiter(token_rate_limit_by_model_name[generator_config.model_name], RATE_LIMIT_INTERVAL) as rate_limiter:
        if patent_summary is None:
            patent_summary = await asummarize_patent(patent[1])
        claims = parser.parse_claims_from_google_parsed_patent(patent[1])
        all_patent_claim_elements = []
        for claim in claims:
            all_patent_claim_elements.extend(claim.claim_elements)
        serialized_claims = '\n'.join(all_patent_claim_elements)
        tasks = []
        for prior_art_source_uid, prior_art_source in prior_art_sources:
            serialized_prior_art_source = prior_art_source.specification
            prompt_func = generator_config.generate_passages_prompt_func
            if prompt_func is prompt_summary_full_set_of_claims:
                prompt_func = partial(prompt_func, patent_summary, serialized_claims)
            else:
                raise NotImplementedError(f"Prompt func {prompt_func} not implemented.")

            tasks.extend(
                create_generate_passages_tasks(
                    claim_elements, (prior_art_source_uid, serialized_prior_art_source), 
                    prompt_func,
                    generator_config.model_name,
                    target_n_passages=generator_config.target_n_passages,
                    min_n_splits=generator_config.min_n_splits,
                    rate_limiter=rate_limiter
            ))
        
        for coro in asyncio.as_completed(tasks):
            generated_passages = await coro
            # TODO: once we yield the whole list of generated passages for each awaited task, we can do the ranking step in the caller
            # Find matching claim element
            claim_element_id = generated_passages[0].claim_element_id
            matching_claim_element = [c for c in claim_elements if c[0] == claim_element_id][0]
            if not all([p.claim_element_id == claim_element_id for p in generated_passages]):
                logger.error('Claim element ids do not match')
            
            logger.info(f'Ranking {len(generated_passages)} passages')
            ranked_generated_passages = ranking.rank_passages(generated_passages, matching_claim_element[1], **ranking_params)
            for generated_passage in ranked_generated_passages:
                # TODO: this depends on parsing patent from pdf working properly
                # citation = None
                # try:
                #     citation = utils.cite_passage(generated_passage.text, patent[1])
                # except utils.CitationError as e:
                #     logger.error(e)
                # else:
                #     generated_passage.start_line = citation[0]
                #     generated_passage.end_line = citation[1]
                # TODO: this doesn't need to be a yield, should just return the whole passage set for each claim element
                yield generated_passage