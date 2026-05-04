from calc_app_mod_OOP_file_Iterable_config.command import command_loop
import logging
import yaml
from pathlib import Path

CONFIG_FILE ="config.yaml"


def main():

    with open(CONFIG_FILE, encoding="utf-8") as f:
        config = yaml.safe_load(f)

    logging.basicConfig(
        filename=config["log_file"],
        level=config["log_level"],
        format="%(levelname)s: %(message)s",
    )

    print("Calculator Tool")
    print("Available commands: add, subtract, multiply, divide, clear, exit")

    command_loop()

if __name__ == "__main__":
    main()