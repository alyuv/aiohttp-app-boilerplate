import prometheus_client
from aiohttp import web


async def metrics(request):
    return web.Response(
        body=prometheus_client.generate_latest(),
        content_type='text/plain',
        charset='utf-8',
        status=200
    )
