from model.Link import Link


class LinkServiceInterface:
    def find_original_url_by_short_url(self, short_url: str) -> str:
        pass

    def create(self, original_url) -> Link:
        pass
