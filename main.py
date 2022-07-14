
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from DTO.LinkRequest import LinkRequest
from model.Link import Link
from service.DefaultLinkService import DefaultLinkService
from service.LinkServiceInterface import LinkServiceInterface

app = FastAPI()
link_service: LinkServiceInterface = DefaultLinkService()


@app.post("/api/convert")
async def get_short_link(link_request: LinkRequest):
    link: Link = link_service.create(link_request.original_link)
    return link


@app.get("/{short_link}")
async def redirect_with_using_redirect_view(short_link: str):
    s: str = link_service.find_original_url_by_short_url(short_link)
    return RedirectResponse(s, status_code=303)
