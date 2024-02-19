import logging
import sys
import os
import json

LOG_LEVEL = logging.WARNING
FILE_NAME = 'llm_wrap.log'

def get_logger(name='llm_wrap', log_file=FILE_NAME):
    # Create a logger with the given name
    logger = logging.getLogger(name)

    # Check if the logger already has handlers
    if not logger.handlers:
        # Set the logging level
        logger.setLevel(LOG_LEVEL)

        # Create a formatter
        formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s]: %(message)s')

        # Function to determine if the environment is Heroku
        def is_heroku():
            return 'DYNO' in os.environ

        # Configure handler based on the environment
        if is_heroku():
            # Running on Heroku, output logs to stdout
            stream_handler = logging.StreamHandler(sys.stdout)
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)
        else:
            # Running locally, output logs to a specified file
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

    return logger
