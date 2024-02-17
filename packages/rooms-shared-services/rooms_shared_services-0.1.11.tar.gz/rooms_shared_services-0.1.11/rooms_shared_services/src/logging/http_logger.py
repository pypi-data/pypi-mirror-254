import logging
from logging.handlers import HTTPHandler

from rooms_shared_services.src.logging.settings import Settings

settings = Settings()


def get_logger(name: str, use_http: bool = False, use_stream: bool = True):
    logger = logging.getLogger(name)
    if use_http:
        http_handler = HTTPHandler(settings.host, settings.path, method="POST", secure=settings.secure, context=None)
        http_handle_format = logging.Formatter("%(levelname)s - %(message)s - %(asctime)s")
        http_handler.setFormatter(http_handle_format)
        logger.addHandler(http_handler)
    if use_stream:
        stream_handler = logging.StreamHandler()
        stream_handle_format = logging.Formatter("%(process)s - %(message)s")
        stream_handler.setFormatter(stream_handle_format)
        logger.addHandler(stream_handler)
        logger.setLevel(level=settings.loglevel)
    return logger
