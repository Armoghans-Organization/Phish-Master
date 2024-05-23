import time
from .color import ColorPrinter

def print_dots(num_dots, delay=0.5):
    for _ in range(num_dots):
        print(".", end="", flush=True)  # Print dot without newline
        time.sleep(delay)  # Delay between dots
    print()

def print_colored_dots(num_dots, color='white', delay=0.5):
    for _ in range(num_dots):
        colored_dot = ColorPrinter.colorize(".", color)
        print(colored_dot, end="", flush=True)  # Print dot without newline
        time.sleep(delay)  # Delay between dots
    print()
#############################################
#                 Usage                     #
#############################################

# from dots import print_dots

# dots.print_dots(<any_number>)

# dots.print_colored_dots(<any_number>, 'red')
# dots.print_colored_dots(<any_number>, 'green')
# dots.print_colored_dots(<any_number>, 'yellow')
# dots.print_colored_dots(<any_number>, 'blue')
# dots.print_colored_dots(<any_number>, 'magenta')
# dots.print_colored_dots(<any_number>, 'cyan')
# dots.print_colored_dots(<any_number>, 'white')