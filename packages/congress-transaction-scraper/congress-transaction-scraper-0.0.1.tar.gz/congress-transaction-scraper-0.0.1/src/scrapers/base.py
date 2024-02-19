from abc import ABC, abstractmethod

from ..utils import ScrapedDisclosure


class TransactionScraper(ABC):
    @abstractmethod
    def scrape(self) -> ScrapedDisclosure:
        pass
