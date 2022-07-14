from model.Link import Link
from repository.LinkRepositoryInterface import LinkRepositoryInterface
from repository.ListLinkRepository import ListLinkRepository
from service.LinkServiceInterface import LinkServiceInterface


class DefaultLinkService(LinkServiceInterface):

    repository: LinkRepositoryInterface = ListLinkRepository()

    def find_original_url_by_short_url(self, short_url: str) -> str:
        link: Link = self.repository.find_by_short_url(short_url)
        return link.get_original_url()

    def create(self, original_url) -> Link:
        return self.repository.save(original_url)
