from aiohttp.web import RouteTableDef, Request, Response
from .content import initialize as init_article, write_toc

routes = RouteTableDef()


@routes.get('/api/toc')
async def toc(_):
    return Response(text=write_toc(), content_type='text/plain')


@routes.get('/api/initialize')
async def initialize(request: Request):
    title = request.rel_url.query['title']
    date = request.rel_url.query['date']
    init_article(title, date)
    return Response(text="Документ успешно создан.", content_type='text/plain')

