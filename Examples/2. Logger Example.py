from ultraprint.logging import logger

# Create a logger object
log = logger('example_log', include_extra_info=True, write_to_file=True, log_level='DEBUG')

# Log some messages
log.info('This is an info message')
log.error('This is an error message')
log.warning('This is a warning message')
log.success('This is a success message')
log.debug('This is a debug message')
log.critical('This is a critical message')
