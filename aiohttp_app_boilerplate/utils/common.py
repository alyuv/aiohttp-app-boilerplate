import datetime
import os
from configparser import ConfigParser


DEFAULT_BUILD_VERSION = '0.0.1'


def utc_now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat(sep=' ')


def read_build_version():
    build_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../build.properties')

    if os.path.exists(build_file):
        config = ConfigParser()

        with open(build_file) as lines:
            lines = '[top]\n' + lines.read()
            config.read_string(lines)

            if 'version' in config['top']:
                return config['top']['version']

    return DEFAULT_BUILD_VERSION