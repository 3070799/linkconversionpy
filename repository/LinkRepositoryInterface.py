from model import Link


class LinkRepositoryInterface:
    def find_by_short_url(self, short_url: str) -> Link:
        pass

    def save(self, original_url) -> Link:
        pass
