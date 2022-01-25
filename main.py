import logging
import os
from aiohttp_setup import aiohttp_setup as setup_aiohttp
from lib.www import routes

logging.basicConfig(level=logging.DEBUG)

HTTP_HOST = os.getenv('HTTP_HOST', 'localhost')
HTTP_PORT = os.getenv('HTTP_PORT', '8080')
HTTP_ROOT = os.getenv('HTTP_ROOT', 'docs')

if __name__ == '__main__':
    setup_aiohttp(host=HTTP_HOST, port=HTTP_PORT, static_dir=HTTP_ROOT, routes=routes)

