
from mods.utils import log

def main():
    log("Hello, World!")

#is this module/file being used as main module?
if __name__ == "__main__":
    main() # yes, so call the main function

#python -m mods: this runs the main py file