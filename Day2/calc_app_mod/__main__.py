from calc_app_mod.command_loop import command_loop


def main():
    print("Calculator Tool")
    print("Available commands: add, subtract, multiply, divide, clear, exit, history, remove")

    command_loop()

if __name__ == "__main__":
    main()