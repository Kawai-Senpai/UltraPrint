from ultraprint.logging import logger

# Create a logger object
log = logger('example_log')

# Log some messages
log.info('This is an info message')
log.error('This is an error message')
log.warning('This is a warning message')
log.success('This is a success message')
log.debug('This is a debug message')
log.critical('This is a critical message')
