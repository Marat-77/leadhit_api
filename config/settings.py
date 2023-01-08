import logging
import logging.config
import time

DB_HOST = 'localhost'
DB_PORT = 27017
DB_TIMEOUT = 5000

ENCODING = 'utf-8'

# Уровень логирования:
# 'CRITICAL' 50
# 'ERROR' 40
# 'WARNING' 30
# 'INFO' 20
# 'DEBUG' 10
# 'NOTSET' 0
LOGGING_CONSOLE_LVL = 'CRITICAL'
LOGGING_FILE_LVL = 'DEBUG'


class UTCFormatter(logging.Formatter):
    """
    Форматер с конвертацией времени в UTC(GMT)
    """
    converter = time.gmtime


logger_config = {
    'version': 1,
    'formatters': {
        'std_format': {
            'format': '{asctime}::{levelname}::{name}::{module}::{funcName}::{message}',
            'style': '{'
        },
        'utc_format': {
            '()': UTCFormatter,
            'format': '{asctime}::{levelname}::{name}::{module}::{funcName}::{message}',
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': LOGGING_CONSOLE_LVL,
            'formatter': 'utc_format',
            'filters': []
        },
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'level': LOGGING_FILE_LVL,
            'filename': './logs/server.log',
            'formatter': 'utc_format',
            'encoding': ENCODING,
            'utc': True,
            'when': 'MIDNIGHT'
        },
    },
    'loggers': {
        'server_logger': {
            'level': 'DEBUG',
            'handlers': ['file'],
        }
    }
}
logging.config.dictConfig(logger_config)
SERVER_LOGGER = logging.getLogger('server_logger')
