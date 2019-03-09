from aiohttp import web

from .api import system


routes = [
    web.get('/health', system.health_check, allow_head=False),
    web.get('/metrics', system.metrics, allow_head=False),
    web.get('/info', system.info, allow_head=False),
]
