import logging

logging.basicConfig(level=logging.DEBUG, format= '%{asctime}s', datefmt='%m/%d/%Y %H:%M:%S')
logging.debug('this a debug message')
logging.info('this a info message')
logging.warning('this a warning message')
logging.error('this a error message')
logging.critical('this a critical message')