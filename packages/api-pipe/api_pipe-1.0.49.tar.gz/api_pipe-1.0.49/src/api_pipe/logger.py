'''
    logger.py
'''
from pathlib import Path
import logging

from api_pipe import config
from rich.logging import RichHandler

class ClosingFileHandler(logging.FileHandler):
    def emit(self, record):
        super().emit(record)
        self.close()

def stdout(unique_name: str, log_dir: Path, log_level: int, log_words_to_highlight: list) -> logging.Logger:
    '''
        Sets up a logger that logs to stdout

        Uses RichHandler to pretty print logs
    '''
    #stdout handler
    stdout_handler = RichHandler(
        show_time=config.logger_show_time,
        keywords=[w.lower() for w in log_words_to_highlight] + \
                 [w.upper() for w in log_words_to_highlight] + \
                 [w.capitalize() for w in log_words_to_highlight]
    )
    formatter = logging.Formatter(config.logger_formatter)
    stdout_handler.setFormatter(formatter)

    #file handler
    file_handler = ClosingFileHandler(log_dir / f"stdout.log")
    file_handler.setFormatter(logging.Formatter(
        config.logger_formatter
    ))

    #config logger
    logger = logging.getLogger(unique_name)
    logger.setLevel(log_level)

    #add hand;ers
    logger.addHandler(stdout_handler)
    logger.addHandler(file_handler)

    return logger
