from Domain.HospitalDepartment import HospitalDepartments
from Domain.Patients import Patient
from Repository.repo import DepartmentRepository


def DataExamplesDepartment():
    example_list = HospitalDepartments(110, "Jorje", 23, [])
    patient1 = Patient("Adrian", "Lukas", "5000720140105", "covid")
    patient2 = Patient("Adriano", "Luko", "6000574174104", "covid")
    example_list.add_a_patient(patient1)
    example_list.add_a_patient(patient2)
    print(example_list)
    new_list = example_list.get_all_patients()
    for elem in new_list:
        print(elem, end=" ")
    print()
    patient3 = Patient("Dana", "Luko", "6010574174102", "covid")
    example_list.add_a_patient(patient3)
    example_list.delete_patient(0)
    print(example_list)
    patient4 = Patient("Yano", "Luko", "1010574174102", "fever")
    example_list.add_a_patient(patient4)
    example_list.update_a_patient(2, "Kevin", "Lukas", "Covid")
    print(example_list)
    result=example_list.SortByNumericalCode()
    print(result)
    print("***** " "-> second data example" )
def DataExampleRepository():
    patient1 = Patient("Adrian", "Lukas", "5000720140105", "covid")
    patient2 = Patient("Adriano", "Luko", "6000574174104", "covid")
    patient3 = Patient("Luis", "Fabiano", "2010388888888", "pneumonia")
    patient4 = Patient("Adrian", "Lukas", "5000720140105", "covid")
    patient5 = Patient("Adriano", "Luko", "6000574174104", "covid")
    patient6 = Patient("Luis", "Fabiano", "2010388888888", "pneumonia")
    dep1=HospitalDepartments(1, "Andrew", 23,[])
    dep2 = HospitalDepartments(2, "Andrew2",33,[patient1])
    dep3 = HospitalDepartments(3, "Andrew3",44,[patient2,patient3])
    dep4= HospitalDepartments(4,"Velodrom",500,[patient4,patient5,patient6])
    dep5= HospitalDepartments(5,"Roi",200,[])

    department_list=DepartmentRepository(dep1)
    department_list.add_a_department(dep2)
    department_list.add_a_department(dep3)
    print(department_list)
    full_list=department_list.get_all_departments()
    print(full_list)
    department_list.add_a_department(dep4)
    department_list.add_a_department(dep5)
    department_list.update_a_department(0,"Saint Sebastian",3000)
    print(department_list)
    department_list.delete_department_by_index(3)
    print(department_list)
    result=department_list.sortByNumberOfPatients()
    for res in result:
        print(res)
    print("II. second sort method")
    result2=department_list.sortDepartmentsByPatientsAge(30)
    for res2 in result2:
        print(res2)
    print("III. third sort method")
    result3=department_list.sortByNumberOfPatients()
    for res3 in result3:
        print(res3)
