'''
    logger.py
'''
from pathlib import Path
import logging

from api_pipe import config
from rich.logging import RichHandler


def stdout(name: str, log_dir: Path, log_level: int) -> logging.Logger:
    '''
        Sets up a logger that logs to stdout

        Uses RichHandler to pretty print logs
    '''
    #stdout logger
    words_to_highlight = config.logger_words_to_highlight

    handler = RichHandler(
        show_time=config.logger_show_time,
        keywords=[w.lower() for w in words_to_highlight] + \
                 [w.upper() for w in words_to_highlight] + \
                 [w.capitalize() for w in words_to_highlight]
    )

    #file logger
    file_handler = logging.FileHandler(log_dir / f"{name}.log")
    file_handler.setFormatter(logging.Formatter(
        config.logger_formatter
    ))

    #config logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    formatter = logging.Formatter(config.logger_formatter)
    handler.setFormatter(formatter)

    #add loggers
    logger.addHandler(handler)
    logger.addHandler(file_handler)

    return logger
