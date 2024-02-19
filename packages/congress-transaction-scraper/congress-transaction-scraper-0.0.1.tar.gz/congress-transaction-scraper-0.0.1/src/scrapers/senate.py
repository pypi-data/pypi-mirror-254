# This tool scrapes the publicly available stock transaction disclosures
# required of all sitting U.S. Senators.

import pandas as pd
import time
from bs4 import BeautifulSoup
from collections.abc import Generator
from urllib.parse import urlparse
from io import StringIO

from .base import TransactionScraper
from ..utils import CSRFSession, ScrapedDisclosure, ScrapedTransaction


class SenateTransactionScraper(TransactionScraper, CSRFSession):
    BASE_URL = "https://efdsearch.senate.gov/"
    LANDING_PATH = "/search/home/"
    HOME_PATH = "/search/"
    SEARCH_PATH = "/search/report/data/"
    RESULTS_PER_PAGE = 100
    START_DATE = "06/01/2023+00:00:00"  # Record keeping begins on 01/01/2012 00:00:00
    SLEEP_LENGTH = 2

    def __init__(self, start_date="06/01/2023+00:00:00", end_date=""):
        self.start_date = start_date
        self.end_date = end_date
        self.url_base = urlparse(SenateTransactionScraper.BASE_URL)

        super().__init__()

        self._accept_terms_of_service()

    def _extract_csrf(self, response):
        soup = BeautifulSoup(response.text, "lxml")
        return soup.find(
            lambda tag: tag.name == "input" and tag.get("name") == "csrfmiddlewaretoken"
        ).get("value")

    def _accept_terms_of_service(self):
        self.get(SenateTransactionScraper.LANDING_PATH, send_csrf=False)
        referer = self.url_base._replace(
            path=SenateTransactionScraper.LANDING_PATH
        ).geturl()
        self.post(
            SenateTransactionScraper.LANDING_PATH,
            data={"prohibition_agreement": "1"},
            headers={"Referer": referer},
        )

    def _get_links_to_disclosures(self, start):
        referer = self.url_base._replace(
            path=SenateTransactionScraper.HOME_PATH
        ).geturl()
        results = self.post(
            SenateTransactionScraper.SEARCH_PATH,
            data={
                "start": str(start),
                "length": str(SenateTransactionScraper.RESULTS_PER_PAGE),
                "report_types": "[11]",
                "filer_types": "[1]",
                "submitted_start_date": "06/01/2023 00:00:00",
                "submitted_end_date": "",
                "candidate_state": "",
                "senator_state": "",
                "office_id": "",
                "first_name": "",
                "last_name": "",
            },
            headers={"Referer": referer},
            extract_csrf=False,
        )

        return results.json()["data"]

    def _get_transactions(self, html):
        soup = BeautifulSoup(html, "lxml")

        if not soup("table"):
            print("No table found")
            return None

        dfs = pd.read_html(StringIO(html))

        if type(dfs[0]) is not pd.core.frame.DataFrame:
            return None
        else:
            return dfs[0]

    def scrape(self) -> Generator[ScrapedDisclosure]:
        start = 0
        while nextResults := self._get_links_to_disclosures(start):
            start += SenateTransactionScraper.RESULTS_PER_PAGE
            for result in nextResults:
                soup = BeautifulSoup(result[3], "html.parser")
                report_url = soup.a["href"]

                disclosure = ScrapedDisclosure(
                    url=report_url,
                    senator=result[2],
                    first_name=result[0],
                    last_name=result[1],
                    disclosure_type=soup.a.text,
                    date=result[4],
                    html=" ",
                )

                disclosure_detail_raw = self.get(report_url, extract_csrf=False).text
                transactions = self._get_transactions(disclosure_detail_raw)
                if transactions is None:
                    # No transactions implies that it's
                    # a scan of a physical (paper) disclosure
                    disclosure.image = True
                else:
                    for transaction in transactions.to_dict(orient="records"):
                        disclosure.transactions.append(
                            ScrapedTransaction.from_dict(transaction)
                        )

                yield disclosure

            time.sleep(SenateTransactionScraper.SLEEP_LENGTH)


def main():
    results = SenateTransactionScraper(SenateTransactionScraper.START_DATE).scrape()
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
