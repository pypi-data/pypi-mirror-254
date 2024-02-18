'''
    Config

    This file is used to configure the module
'''
import logging

#logger
logger_level = logging.DEBUG
logger_words_to_highlight = [
    "fetching",
    "filtering",
    "converting",
    "importing",
    "exporting",
    "validating",
    "deleting",
    "parsing",
    "getting",
    "writing",
    "reading",
    "found",
    "making",
    "removing",
    "selecting",
    "multiplexing",
    "emptying",
    "creating",
    "initializing",
    "logging",
    "checking",
    "requesting",
    "imported",
    "exported"
]
logger_show_time = False
logger_formatter = "%(message)s"
