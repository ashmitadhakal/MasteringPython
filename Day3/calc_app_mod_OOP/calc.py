import logging
def add(result, operand):
    return result + operand


def sub(result, operand):
    return result - operand


def mul(result, operand):
    return result * operand


def div(result, operand):
    try:
        return result/operand
    except ZeroDivisionError:
        logging.warning(f"Cannot divide by zero.")
        return None
    