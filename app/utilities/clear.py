import os

class TerminalClear:
    @staticmethod
    def clear():
        """Clears the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

#############################################
#                 Usage                     #
#############################################
# from clear import TerminalClear 
# TerminalClear.clear()
