# import logging
# logging.basicConfig(filename='example.log', level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')
# logging.error('And non-ASCII stuff, too')
# logging.critical('This was Critical')
#
# importing module
import logging

# Create and configure logger
logging.basicConfig(filename="newfile.log", filemode='w')

# Creating an object
log = logging.getLogger()

# Setting the threshold of logger to DEBUG
log.setLevel(logging.DEBUG)

# log.debug("Harmless debug Message")
# log.info("Just an information")
# log.warning("Its a Warning")
# log.error("Did you try to divide by zero")
# log.critical("Internet is down")
