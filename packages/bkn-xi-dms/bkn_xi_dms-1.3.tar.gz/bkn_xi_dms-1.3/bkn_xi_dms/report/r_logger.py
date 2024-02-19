import logging
import colorlog
from colorlog import ColoredFormatter

import colorama


def init_r_logger():
    colorama.init()
    logger1 = logging.getLogger('logger1')
    logger1.setLevel(logging.DEBUG)

    file_handler1 = logging.FileHandler('logfile1.log')
    file_handler1.setLevel(logging.DEBUG)

    # Create a formatter and add it to the file handler
    formatter1 = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler1.setFormatter(formatter1)

    # Add the file handler to the logger
    logger1.addHandler(file_handler1)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_formatter = colorlog.ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s%(message_log_color)s%(message)s%(reset)s",
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'blue',
            'WARNING': 'bold_yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        },
        secondary_log_colors={
            'message': {
                'DEBUG': 'white',
                'INFO': 'white',
                'WARNING': 'bold_yellow',
                'ERROR': 'white',
                'CRITICAL': 'white',
            }
        }
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    file_handler = logging.FileHandler('logapp.log')  
    file_handler.setLevel(logging.DEBUG)

    file_formatter = colorlog.ColoredFormatter(
        "%(asctime)s - %(levelname)s - %(message_log_color)s%(message)s%(reset)s",
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'blue',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        },
        secondary_log_colors={
            'message': {
                'DEBUG': 'green',
                'INFO': 'blue',
                'WARNING': 'cyan',
                'ERROR': 'red',
                'CRITICAL': 'white',
            }
        }
    )
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    init_r_logger._called = True
    return logger