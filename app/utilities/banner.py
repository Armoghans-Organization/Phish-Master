from .color import ColorPrinter
from .clear import TerminalClear
from .centered import center_print
        
def banner():
    banner_text = """
██████╗ ██╗  ██╗██╗███████╗██╗  ██╗    ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗ 
██╔══██╗██║  ██║██║██╔════╝██║  ██║    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██████╔╝███████║██║███████╗███████║    ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██╔═══╝ ██╔══██║██║╚════██║██╔══██║    ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║     ██║  ██║██║███████║██║  ██║    ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                           
    """
    TerminalClear.clear()
    center_print(ColorPrinter.magenta(banner_text))
        
def print_banner():
    banner()
    center_print(ColorPrinter.blue("      -------------------------------------------------------------------------------------------"))
    center_print(ColorPrinter.cyan("      Welcome to Phish Master - A user-friendly phishing tool."))
    print()
    center_print(ColorPrinter.cyan("      Author: Armoghan-ul-Mohmin"))
    center_print(ColorPrinter.blue("      -------------------------------------------------------------------------------------------"))
    center_print(ColorPrinter.yellow("      Phish Master is designed to help users understand and simulate phishing attacks."))
    center_print(ColorPrinter.yellow("      It is intended for educational purposes and to promote awareness about cybersecurity."))
    center_print(ColorPrinter.blue("      -------------------------------------------------------------------------------------------"))


#############################################
#                 Usage                     #
#############################################
# from banner import print_banner
# banner.print_banner()