from calc_app_mod_OOP.command import command_loop
import logging
logging.basicConfig(
    filename="calc_app2.log",
    level=logging.WARNING,
    #level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logging.debug("This is a debug message!")
logging.info("This is info message!")
def main():
    print("Calculator Tool")
    print("Available commands: add, subtract, multiply, divide, clear, exit, history, remove")

    command_loop()

if __name__ == "__main__":
    main()