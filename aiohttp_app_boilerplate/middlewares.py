import logging
import sys
import traceback
import time

from aiohttp import web
# from formatter_logs import LoggingParameters

LOGGER = logging.getLogger(__name__)


@web.middleware
async def json_response_middleware(request, handler):
    try:
        response = await handler(request)

        if isinstance(response, web.StreamResponse):
            return response

        response, status = response
        return web.json_response(response, status=status)

    except web.HTTPError as e:
        LOGGER.error(f'Handle external exception: {e.args}')
        exc_info = sys.exc_info()
        traceback.print_exception(*exc_info)

        result = {
            'errors': [
                {
                    'status': e.status_code,
                    'title': e.text
                }
            ]
        }

        return web.json_response(result, status=e.status_code)


@web.middleware
async def logging_context_middleware(request, handler):
    # LoggingParameters.set_headers(request.headers)

    start = time.time()

    response = await handler(request)

    LOGGER.info(
        f'{start} - {request.remote} - {request.method} {request.path} - {response.status} - {time.time() - start} - ' +
        request.headers.get('User-Agent', '')
    )

    # LoggingParameters.cleanup()
    return response
