import logging

logging.basicConfig(
    #level = logging.WARNING
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
logging.debug("This is a debug message!")
logging.info("This is info message!")
logging.warning("This is a warning message!")
logging.error("This is an error message!")
logging.critical("This is a critical message!")