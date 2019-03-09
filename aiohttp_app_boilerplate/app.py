import logging

from aiohttp import web

from .middlewares import logging_context_middleware, json_response_middleware
from .routes import routes
from .settings import get_settings, get_settings_files_abs_paths


logger = logging.getLogger(__name__)


def get_app():
    app = web.Application(
        logger=logger,
        middlewares=[
            logging_context_middleware,
            json_response_middleware
        ]
    )

    app.add_routes(routes)

    app['SETTINGS'] = get_settings(get_settings_files_abs_paths())

    return app
