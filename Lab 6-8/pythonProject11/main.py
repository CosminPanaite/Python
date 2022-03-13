from Tests.run_all_tests import run_all_tests
from UserInterface.console import Console


def main():
    run_all_tests()
    ui = Console()
    ui.run_console()



main()
