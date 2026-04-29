import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s"
)
def main():
    try:
        logging.debug("Starting the program")
        raise Exception("Something went wrong")
    except Exception:
        #handle the error/exception by logging
        logging.fatal("Unexpected error occured.", exc_info=True)
    logging.debug("Ending the program")

if __name__=="__main__":
    main()