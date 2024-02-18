import unittest
import threading
import asyncio
import time
from unittest.mock import patch

import numpy as np

from patent_chart.redis_utils import r
from patent_chart import settings
from patent_chart.requests import DistributedFixedWindowRateLimiter

# NOTE: REDIS_HOST should be set to the host of the redis server accessible to the test runner
class TestDistributedRateLimiter(unittest.IsolatedAsyncioTestCase):
    class _MockServer:
        def __init__(self):
            self._requests = []
            self._tokens = []
            self._timestamps = []

        async def request(self, request, tokens):
            self._requests.append(request)
            self._tokens.append(tokens)
            self._timestamps.append(time.monotonic())

        def get_requests(self):
            return self._requests
        
        def get_tokens(self):
            return self._tokens
        
        def get_timestamps(self):
            return self._timestamps
    
    def setUp(self):
        r.delete(settings.REDIS_OPENAI_RATE_LIMIT_LAST_FILL_TIME_KEY)
        r.delete(settings.REDIS_OPENAI_RATE_LIMIT_TOKENS_KEY)
        r.delete(settings.REDIS_OPENAI_RATE_LIMIT_LOCK_KEY)

    def start_make_request_loop(self, server):
        asyncio.run(self._make_requests(server))

    async def _make_requests(self, server):
        async with DistributedFixedWindowRateLimiter(10, 1) as limiter:
            for i in range(3):
                tokens = 8
                await limiter.wait_for_tokens(tokens)
                await server.request(i, tokens)
    
    def test_distributed_rate_limiter(self):
        # spawn three threads that each make a series of requests to a mock server
        server = self._MockServer()
        threades = []
        for _ in range(3):
            thread = threading.Thread(target=self.start_make_request_loop, args=(server,))
            thread.start()
            threades.append(thread)

        # Wait for all threades to finish
        for thread in threades:
            thread.join()
        # Ensure that all requests have been made at the end of the test
        expected = []
        for i in range(3):
            expected.extend([i] * 3)

        self.assertEqual(
            sorted(server.get_requests()),
            expected
        )

        timestamps = server.get_timestamps()
        tokens = server.get_tokens()
        bins = np.arange(timestamps[0], timestamps[-1], 1)
        tokens_per_bin = np.zeros(len(bins) - 1)
        i = 1
        for tok, time in zip(tokens, timestamps):
            if time > bins[i]:
                i += 1
            tokens_per_bin[i - 1] += tok

        print(tokens_per_bin)
        self.assertTrue(np.all(tokens_per_bin <= 10))