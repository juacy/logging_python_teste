#https://www.youtube.com/watch?v=tZ2iJ5H99fg

#https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SMTPHandler

import logging
import logging.config

logging.config.fileConfig('config.ini')

logger = logging.getLogger('root')

logger.error('Bananas')