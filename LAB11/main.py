from Controller.ctrl import Controller
from Domain.HospitalDepartment import HospitalDepartments
from Repository.repo import DepartmentRepository
from Tests.DataExamples import DataExamplesDepartment , DataExampleRepository
from UI.Console import Console

def start():

    hospital_departments = HospitalDepartments(1, "Alberto", 3, [])
    department_repository = DepartmentRepository(hospital_departments)
    controller = Controller(hospital_departments, department_repository)
    console = Console(controller)
    DataExamplesDepartment()
    DataExampleRepository()
    console.run_console()


start()
