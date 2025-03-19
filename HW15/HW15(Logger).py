# Task Logger
# 11
import logging
from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

log_format = '%(asctime)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(log_format)

# 12
file_handler = TimedRotatingFileHandler(
    '../user_actions.log',
    when='midnight',
    interval=1,
    backupCount=7,
    encoding='utf-8'
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# 13
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

logger.info('message')
logger.error('message')
logger.info('message')
logger.warning('message')
logger.debug('message')
