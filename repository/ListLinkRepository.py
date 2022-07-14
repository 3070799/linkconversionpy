import random
import string
from typing import List

from model.Link import Link
from repository.LinkRepositoryInterface import LinkRepositoryInterface


class ListLinkRepository(LinkRepositoryInterface):
    links: List[Link] = []

    def find_by_short_url(self, short_url: str) -> Link:
        for link in self.links:
            if link.get_short_url().__eq__(short_url):
                return link
        raise ModuleNotFoundError("Short link not found ")

    def save(self, original_url) -> Link:
        link = Link(original_url, self.generate_short_url(5))
        self.links.append(link)
        return link

    def generate_short_url(self, size: int):
        result = ''.join(random.choice(string.ascii_letters) for i in range(size))
        for link in self.links:
            if link.get_short_url().__eq__(result):
                return self.generate_short_url(size)
        return result
