import logging
logger = logging.getLogger(__name__)
# logger.propagate = False
# logger.info('hello from helper')

#handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')