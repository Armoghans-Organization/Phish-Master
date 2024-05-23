class Color:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

class ColorPrinter:
    @staticmethod
    def colorize(text, *styles):
        style_codes = [getattr(Color, style.upper()) for style in styles]
        formatted_text = text
        for style_code in style_codes:
            formatted_text = f"{style_code}{formatted_text}{Color.RESET}"
        return formatted_text

    @staticmethod
    def red(text):
        return ColorPrinter.colorize(text, 'red')

    @staticmethod
    def green(text):
        return ColorPrinter.colorize(text, 'green')

    @staticmethod
    def yellow(text):
        return ColorPrinter.colorize(text, 'yellow')

    @staticmethod
    def blue(text):
        return ColorPrinter.colorize(text, 'blue')

    @staticmethod
    def magenta(text):
        return ColorPrinter.colorize(text, 'magenta')

    @staticmethod
    def cyan(text):
        return ColorPrinter.colorize(text, 'cyan')

    @staticmethod
    def white(text):
        return ColorPrinter.colorize(text, 'white')

    @staticmethod
    def bold(text):
        return ColorPrinter.colorize(text, 'bold')

    @staticmethod
    def underline(text):
        return ColorPrinter.colorize(text, 'underline')

#############################################
#                 Usage                     #
#############################################

# from color import ColorPrinter

# print(color.ColorPrinter.red("This is a red text"))
# print(color.ColorPrinter.green("This is a green text"))
# print(color.ColorPrinter.yellow("This is a yellow text"))
# print(color.ColorPrinter.blue("This is a blue text"))
# print(color.ColorPrinter.magenta("This is a magenta text"))
# print(color.ColorPrinter.cyan("This is a cyan text"))
# print(color.ColorPrinter.white("This is a white text"))
# print(color.ColorPrinter.bold("This is a bold text"))
# print(color.ColorPrinter.underline("This is an underlined text"))
