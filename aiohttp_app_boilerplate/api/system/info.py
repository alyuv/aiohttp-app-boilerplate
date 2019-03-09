import platform

from aiohttp_app_boilerplate.utils import utc_now


async def info(request):
    settings = request.app['SETTINGS']

    return {
        'data': {
            'server_info': {
                'hostname': platform.node(),
                'os_release': platform.release(),
                'os_version': platform.version()
            },
            'python_version': platform.python_version(),
            'version': settings['product']['version'],
            'deploy_environment': settings['app']['environment'],
        },
        'meta': {
            'generated_at': utc_now(),
            'product': 'App Boilerplate',
            'copyright': 'Copyright 2019 Yuvchenko, All Rights Reserved'
        }
    }, 200
