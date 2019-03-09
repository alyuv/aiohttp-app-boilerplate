from aiohttp import web

from aiohttp_app_boilerplate.app import get_app


def main():
    app = get_app()
    port = app['SETTINGS']['app']['port']
    web.run_app(app, port=port, access_log=None)


if __name__ == '__main__':
    main()
