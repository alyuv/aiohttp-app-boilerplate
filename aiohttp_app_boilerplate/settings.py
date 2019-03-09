import configparser
import logging.config
import os

# import formatter_logs

from .utils import read_build_version


def get_settings_files_abs_paths():
    return [
        os.getenv('BASE_CONFIG_FILE_PATH', '/etc/aiohttp-app-boilerplate/config.ini'),
        os.getenv('BASE_LOGGING_CONFIG_FILE_PATH', '/etc/aiohttp-app-boilerplate/logging.ini')
    ]


def get_settings(paths):
    settings = configparser.ConfigParser()

    if not settings.read(paths):
        raise FileNotFoundError(f'One of config files found (tried: {", ".join(paths)})')

    logging.config.fileConfig(settings)
    # formatter_logs.setup_logging(is_pyramid=False)

    settings.set('product', 'version', read_build_version())

    return settings
