import requests
import pathlib
import time
from logging import getLogger

from bs4 import BeautifulSoup

logger = getLogger(__name__)

# from patent_chart import parser

def google_request_with_retry(url, max_retries=3):
    for i in range(1, max_retries + 1):
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            logger.warning('Failed to request %s. Response code: %s. Error: %s', url, response.status_code, response.text)
            logger.warning('Retrying %s', url)
            time.sleep(i**2)
    return None

def parse_google_patent(patent_unique_id) -> tuple[str, str] | None:
    url = f"https://patents.google.com/patent/{patent_unique_id}/en"

    logger.info('Requesting %s', url)

    # Send an HTTP GET request to fetch the webpage
    response = google_request_with_retry(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    specification = soup.find('section', {'itemprop': 'description'})
    claims = soup.find('section', {'itemprop': 'claims'})

    if specification is None or claims is None:
        logger.warning('Failed to parse %s', url)
        return None

    return specification.text, claims.text

# if __name__ == '__main__':
#     package_dir = pathlib.Path(__file__).parents[1]
#     us_patents_dir = package_dir / 'us_patents_1980-2020'
#     for pdf_path in us_patents_dir.glob('*.pdf'):
#         unique_id = parser.parse_patent_unique_id_from_pdf_path(pdf_path)
#         if unique_id is not None:
#             google_unique_id = f'{unique_id.country_code}{unique_id.patent_number}{unique_id.kind_code or ""}'
#             result = parse_google_patent(google_unique_id)
#             if result is not None:
#                 specification, claims = result
#                 assert specification != ''
#                 assert claims != ''
#             else:
#                 print(f'Failed to parse {unique_id}')
#         else:
#             print(f'Failed to parse {pdf_path}')