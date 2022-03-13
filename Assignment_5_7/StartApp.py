from Assignment_5_7.UI import *
from Assignment_5_7.repository.StudentRepository import StudentRepository
from Assignment_5_7.repository.DisciplineRepository import DisciplineRepository
from Assignment_5_7.repository.GradeRepository import GradeRepository
from Assignment_5_7.domain.StudentValidator import StudentValidator
from Assignment_5_7.domain.DisciplineValidator import DisciplineValidator
from Assignment_5_7.domain.GradeValidator import GradeValidator
from Assignment_5_7.controller.StudentController import StudentController
from Assignment_5_7.controller.DisciplineController import DisciplineController
from Assignment_5_7.controller.GradeController import GradeController
from Assignment_5_7.controller.UndoController import *
import random

def Main():
    '''
    Main Function - Starts application
    '''
    student_validator = StudentValidator()
    discipline_validator = DisciplineValidator()
    grade_validator = GradeValidator()

    student_repo = StudentRepository()
    discipline_repo = DisciplineRepository()
    grade_repo = GradeRepository()

    undo_controller = UndoController()
    grade_controller = GradeController(grade_validator, grade_repo, undo_controller)
    student_controller = StudentController(student_validator, student_repo, undo_controller, grade_controller)
    discipline_controller = DisciplineController(discipline_validator, discipline_repo, undo_controller, grade_controller)


    ui = UI(student_controller, discipline_controller, grade_controller, undo_controller)

    student_controller.addStudent(453, "Raul Romitan")
    student_controller.addStudent(120, "Ruxandra Pop")
    student_controller.addStudent(734, "Paul Pop")
    student_controller.addStudent(293, "Cristian Chirtos")
    student_controller.addStudent(688, "Andrea Banceu")
    student_controller.addStudent(19, "Andreea Talpos")
    student_controller.addStudent(771, "Loredana Purcel")
    student_controller.addStudent(573, "Ina Crisan")
    student_controller.addStudent(905, "Vlad Poltorac")
    student_controller.addStudent(879, "George Rosescu")

    discipline_controller.addDiscipline(1, "Algebra")
    discipline_controller.addDiscipline(2, "English")
    discipline_controller.addDiscipline(3, "Fp")
    discipline_controller.addDiscipline(4, "Sport")
    discipline_controller.addDiscipline(5, "Computing Systems Architecture")
    discipline_controller.addDiscipline(6, "Geometry")
    discipline_controller.addDiscipline(7, "Logic Design")
    discipline_controller.addDiscipline(8, "Math")
    discipline_controller.addDiscipline(9, "Special Mathematics")
    discipline_controller.addDiscipline(10, "Design")

    grade_controller.addGrade(453, 2, 8.0)
    grade_controller.addGrade(879, 7, 3.0)
    grade_controller.addGrade(453, 5, 6.0)
    grade_controller.addGrade(293, 6, 4.0)
    grade_controller.addGrade(120, 4, 10.0)
    grade_controller.addGrade(688, 10, 9.0)
    grade_controller.addGrade(453, 9, 9.0)
    grade_controller.addGrade(905, 2, 10.0)
    grade_controller.addGrade(771, 3, 7.0)
    grade_controller.addGrade(573, 2, 10.0)

    studentsids = []
    disciplineids = []

    def fillStudents():
        firstName = ["Ana", "Maria", "Ana-Maria", "Ruxandra", "Andra", "Andrea", "Andreea", "Ioana", "Georgia", "Tonia", "Ina", "Lorena", "Laura", "Cristina", "Raul", "Cristian", "Daniel", "Alex", "Alexandru", "Andrei", "Sebastian", "Darius", "Victor", "Matei", "Cornel", "Paula", "Horea", "Claudiu", "Daniela", "Octavia", "Mara", "Daria", "Tudor", "Sergiu", "Denis", "Daiana", "Vasile", "Matei", "Sorina"]
        lastName = ["Popa", "Pop", "Niță", "Popescu", "Ionescu", "Nemeș", "Stan", "Dumitrescu", "Dima", "Gheorghiu", "Ioniță", "Marin", "Tudor", "Dobre", "Barbu", "Nistor", "Florea", "Ene", "Georgescu", "Stoica", "Diaconu", "Diaconescu", "Mazilescu", "Ababei", "Aanei", "Nistor", "Mocanu", "Oprea", "Voinea", "Dochioiu", "Albu", "Tabacu", "Manole", "Cristea", "Toma", "Stănescu", "Pușcașu", "Tomescu", "Opt"]
        for i in range(1, 90):
            id = int(i * 23 + 6)
            studentsids.append(id)
            name = str(random.choice(firstName)) + " " + str(random.choice(lastName))
            student_controller.addStudent(id, name)

    def fillDisciplines():
        disciplines = ["Accounting", "Administration of Justice", "Architecture", "Arts", "Biology", "Chemistry", "Chinese", "Computer Science", "Business", "Economics", "Education", "English", "Engineering", "English Fundamentals", "French", "Financial Services", "Geography", "Geology", "History", "Horticulture", "Information Technology Programming", "Math", "Math Essentials", "Physics", "Psychology", "Marketing", "Information Technology Programming", "Health Information Technology", "Energy Technology", "Environmental Science"]
        for i in range(1, 30):
            id = int(i * 27 + 2)
            disciplineids.append(id)
            discipline_controller.addDiscipline(id, disciplines[i])

    def fillGrades():
        for i in range(1, 100):
            studId = random.choice(studentsids)
            discId = random.choice(disciplineids)
            value = random.choice([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0])
            grade_controller.addGrade(studId, discId, value)

    fillStudents()
    fillDisciplines()
    fillGrades()

    ui.loopMenu()

Main()