from Controller.ctrl import VectorController
from Domain.Validator import VectorValidator
from Repository.repo import VectorRepository
from Tests.data_examples import data_examples
from UI.console import Console


def main():
    data_examples()

    v = VectorValidator()
    l = VectorRepository(v)
    c = VectorController(l,v)
    cons = Console(c)
    cons.run_console()


main()
