'''
    logger.py
'''
import logging

from api_pipe import config
from rich.logging import RichHandler


def stdout(name: str, log_level) -> logging.Logger:
    '''
        Sets up a logger that logs to stdout

        Uses RichHandler to pretty print logs
    '''
    words_to_highlight = config.logger_words_to_highlight

    handler = RichHandler(
        show_time=config.logger_show_time,
        keywords=[w.lower() for w in words_to_highlight] + \
                 [w.upper() for w in words_to_highlight] + \
                 [w.capitalize() for w in words_to_highlight]
    )

    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    formatter = logging.Formatter(config.logger_formatter)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
