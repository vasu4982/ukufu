
"""
This file provides rotating logger and stream logger functionality to entire application
"""

import logging
import logging.handlers

from .config import LOG_FILE_SIZE, BACKUP_LOG_COUNT

__author__ = "Narendra Allam"
__copyright__ = "Copyright 2020, Tech Task, ukufu.com"
__credits__ = ["Narendra Allam"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Narendra Allam"
__email__ = "naren@rossum.io"
__status__ = "Development"


def get_logger(name):
        """
        Returns app scpecifig logger
        """
        LOG_FILE_NAME = name.lower() + '.log'
        FORMAT = '%(levelname)7s %(name)10s [file] %(filename)15s [line] %(lineno)d ' \
                 '[func] %(funcName)12s() %(asctime)s, %(msecs)s, %(message)s'

        logging.basicConfig(
                filename = LOG_FILE_NAME,
                filemode = 'a',
                level = logging.DEBUG,
                format = FORMAT,
                datefmt = '%H:%M:%S')

        logger = logging.getLogger(name)

        # Configuring rotating file handler
        fhandler = logging.handlers.RotatingFileHandler(
                LOG_FILE_NAME, maxBytes=LOG_FILE_SIZE, backupCount=BACKUP_LOG_COUNT)

        logger.addHandler(fhandler)

        # Configuring Console handler
        chandler = logging.StreamHandler()
        chandler.setFormatter(logging.Formatter(FORMAT))

        logger.addHandler(chandler)

        return logger