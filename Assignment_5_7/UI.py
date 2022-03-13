from Assignment_5_7.domain.ValidatorException import ValidatorException
from Assignment_5_7.repository.RepositoryException import RepositoryException
from Assignment_5_7.controller.UndoController import *
from operator import itemgetter

class UI:
    '''
    User Interface Class
    '''
    def __init__(self, student_controller, discipline_controller, grade_controller, undo_controller):
        self._student_controller = student_controller
        self._discipline_controller = discipline_controller
        self._grade_controller = grade_controller
        self._undo_controller = undo_controller

    def mainMenu(self):
        menuString = '\nAvailable commands:\n'
        menuString += '\t 0. Exit\n'
        menuString += '\t 1. Add student or discipline\n'
        menuString += '\t 2. Remove student or discipline\n'
        menuString += '\t 3. Update student or discipline\n'
        menuString += '\t 4. Print student or discipline list\n'
        menuString += '\t 5. Grade student\n'
        menuString += '\t 6. List all grades\n'
        menuString += '\t 7. Search student or discipline by name\n'
        menuString += '\t 8. Search student or discipline by ID\n'
        menuString += '\t 9. All students enrolled at a given discipline, sorted alphabetically\n'
        menuString += '\t 10. All students enrolled at a given discipline, sorted  by descending average grade\n'
        menuString += '\t 11. All students failing at one or more disciplines\n'
        menuString += '\t 12. Students with the best school situation, sorted in descending order of their aggregated average\n'
        menuString += '\t 13. All disciplines sorted in descending order of the average grade received by all students enrolled at that discipline\n'
        menuString += '\t 14. Undo\n'
        menuString += '\t 15. Redo\n'
        print(menuString)

    def subMenu(self):
        submenuString = '\t 1. Student\n'
        submenuString += '\t 2. Discipline\n'
        print(submenuString)

    def loopMenu(self):
        while True:
            self.mainMenu()
            try:
                option = int(input("Pick an option:\n> "))
            except:
                option = 99

            try:
                if option in [1, 2, 3, 4, 7, 8]:
                    self.subMenu()
                    try:
                        sub_option = int(input("Pick a suboption:\n> "))
                    except:
                        sub_option = 99

                if option == 1:
                    if sub_option == 1:
                        self.addStudentUI()
                    elif sub_option == 2:
                        self.addDisciplineUI()
                    else:
                        print("\n>>> Invalid command!")

                elif option == 2:
                    if sub_option == 1:
                        self.deleteStudentUI()
                    elif sub_option == 2:
                        self.deleteDisciplineUI()
                    else:
                        print("\n>>> Invalid command!")

                elif option == 3:
                    if sub_option == 1:
                        self.updateStudentUI()
                    elif sub_option == 2:
                        self.updateDisciplineUI()
                    else:
                        print("\n>>> Invalid command!")

                elif option == 4:
                    if sub_option == 1:
                        self.listStudentsUI()
                    elif sub_option == 2:
                        self.listDisciplinesUI()
                    else:
                        print("\n>>> Invalid command!")

                elif option == 5:
                    self.gradeStudentUI()

                elif option == 6:
                    self.listGradesUI()

                elif option == 7:
                    if sub_option == 1:
                        self.listMatchStudentNameUI()
                    elif sub_option == 2:
                        self.listMatchDisciplineNameUI()
                    else:
                        print("\n>>> Invalid command!")

                elif option == 8:
                    if sub_option == 1:
                        self.listMatchStudentIdUI()
                    elif sub_option == 2:
                        self.listMatchDisciplineIdUI()
                    else:
                        print("\n>>> Invalid command!")

                elif option == 9:
                    self.studentsEnrolledAlphaUI()

                elif option == 10:
                    self.studentsEnrolledAvgUI()

                elif option == 11:
                    self.studentsFailingUI()

                elif option == 12:
                    self.studentsBestStatsUI()

                elif option == 13:
                    self.disciplinesAvgUI()

                elif option == 14:
                    if self._undo_controller.undo() == False:
                        print("\n>>> No more undos. ")

                elif option == 15:
                    if self._undo_controller.redo() == False:
                        print("\n>>> No more redos. ")

                elif option == 0:
                    print("\n\n>>> GOODBYE <<<")
                    return False

                else:
                    print("\n>>> Invalid option!\n")

            except RepositoryException as re:
                print(re)
            except ValidatorException as val:
                print(val)
            except ValueError as ve:
                print(ve)
            except TypeError as te:
                print(te)
            except Exception as e:
                print(e)

    def addStudentUI(self):
        id = input("> Student ID: ")
        name = input("> Student Name: ")
        self._student_controller.addStudent(id, name)

    def addDisciplineUI(self):
        id = input("> Discipline ID: ")
        name = input("> Discipline Name: ")
        self._discipline_controller.addDiscipline(id, name)

    def deleteStudentUI(self):
        id = input("> Student ID: ")
        self._student_controller.deleteStudent(id)

    def deleteDisciplineUI(self):
        id = input("> Discipline ID: ")
        self._discipline_controller.deleteDiscipline(id)
        self._grade_controller.deleteDisciplineGrades(id)

    def updateStudentUI(self):
        id = input("> ID of the student you want to update: ")
        new_name = input("> New name: ")
        self._student_controller.updateStudent(id, new_name)

    def updateDisciplineUI(self):
        id = input("> ID of the discipline you want to update: ")
        new_name = input("> New name: ")
        self._discipline_controller.updateDiscipline(id, new_name)

    def listStudentsUI(self):
        students = self._student_controller.getAllStudents()
        for student in students:
            print("ID: " + str(student.getId()) + " Name: " + str(student.getName()))

    def listDisciplinesUI(self):
        disciplines = self._discipline_controller.getAllDisciplines()
        for discipline in disciplines:
            print("ID: " + str(discipline.getId()) + " Name: " + str(discipline.getName()))

    def gradeStudentUI(self):
        studentID = input("> Student ID: ")
        disciplineID = input("> Discipline ID: ")
        grade_value = input("> Grade: ")
        if self._student_controller.isStudIdUsed(studentID) and self._discipline_controller.isDiscIdUsed(disciplineID):
            self._grade_controller.addGrade(studentID, disciplineID, grade_value)
        else:
            print("\n>>> No matching student id or discipline id")

    def listGradesUI(self):
        grades = self._grade_controller.getAllGrades()
        students = self._student_controller.getAllStudents()
        disciplines = self._discipline_controller.getAllDisciplines()
        for grade in grades:
            sid = grade.getStudentId()
            did = grade.getDisciplineId()
            val = grade.getGradeValue()
            for student in students:
                if int(sid) == int(student.getId()):
                    name = student.getName()
            for discipline in disciplines:
                if int(did) == int(discipline.getId()):
                    disc = discipline.getName()
            print(str(name) + " - " + str(disc) + " - " + str(val))

    def listMatchStudentNameUI(self):
        string = input("> Student name: ")
        students = self._student_controller.searchStudentName(string)
        if students == False:
            print("\n>>> No matching student")
        else:
            for student in students:
                print("ID: " + str(student.getId()) + " Name: " + str(student.getName()))

    def listMatchDisciplineNameUI(self):
        string = input("> Discipline name: ")
        disciplines = self._discipline_controller.searchDisciplineName(string)
        if disciplines == False:
            print("\n>>> No matching discipline")
        else:
            for discipline in disciplines:
                print("ID: " + str(discipline.getId()) + " Name: " + str(discipline.getName()))

    def listMatchStudentIdUI(self):
        id = input("> Student ID: ")
        students = self._student_controller.searchStudentId(id)
        if students == False:
            print("\n>>> No matching student")
        else:
            for student in students:
                print("ID: " + str(student.getId()) + " Name: " + str(student.getName()))

    def listMatchDisciplineIdUI(self):
        id = input("> Discipline Id: ")
        disciplines = self._discipline_controller.searchDisciplineId(id)
        if disciplines == False:
            print("\n>>> No matching discipline")
        else:
            for discipline in disciplines:
                print("ID: " + str(discipline.getId()) + " Name: " + str(discipline.getName()))

    def studentsEnrolledAlphaUI(self):
        id = input("> Discipline Id: ")
        toSort = []
        enrolledList = self._grade_controller.enrolledStudents(id)
        if enrolledList == False:
            print("\n>>> There is no student enrolled at this discipline. ")
        else:
            for studentID in enrolledList:
                name = self._student_controller.getStudentNameById(studentID)
                toSort.append([studentID, name])
            toSort.sort(key = itemgetter(1))
            for student in toSort:
                print("ID: " + str(student[0]) + " /  Name: " + str(student[1]))

    def studentsEnrolledAvgUI(self):
        id = input("> Discipline Id: ")
        toSort = []
        enrolledList = self._grade_controller.enrolledStudents(id)
        if enrolledList == False:
            print("\n>>> There is no student enrolled to this discipline. ")
        else:
            for studentID in enrolledList:
                name = self._student_controller.getStudentNameById(studentID)
                avg = self._grade_controller.averageGradeDiscipline(studentID, id)
                toSort.append([studentID, name, avg])
            toSort.sort(key = itemgetter(2), reverse = True)
            for student in toSort:
                print("ID: " + str(student[0]) + " / Name: " + str(student[1]) + " / Average at given discipline: " + str(student[2]))

    def studentsFailingUI(self):
        failingList = []
        students = self._student_controller.getAllStudents()
        disciplines = self._discipline_controller.getAllDisciplines()
        for student in students:
            for discipline in disciplines:
                avg = self._grade_controller.averageGradeDiscipline(student.getId(), discipline.getId())
                if avg is not False and int(avg < 5):
                    failingList.append([student.getId(), student.getName(), discipline.getName(), avg])
        if len(failingList) == 0:
            print("\n>>> No failing students. ")
        else:
            for fail in failingList:
                print("ID: " + str(fail[0]) + " / Name: " + str(fail[1]) +" / Discipline: " + str(fail[2]) + " / Avg: " + str(fail[3]))

    def studentsBestStatsUI(self):
        toSort = []
        students = self._student_controller.getAllStudents()
        for student in students:
            avg = self._grade_controller.aggregatedAverage(student.getId())
            if avg is not False:
                toSort.append([student.getId(), student.getName(), avg])
        toSort.sort(key = itemgetter(2), reverse=True)
        for student in toSort:
            print("ID: " + str(student[0]) + " / Name: " + str(student[1]) + " / Average: " + str(student[2]))

    def disciplinesAvgUI(self):
        toSort = []
        disciplines = self._discipline_controller.getAllDisciplines()
        for discipline in disciplines:
            avg = self._grade_controller.averageGradeDisciplineAll(discipline.getId())
            if avg is not False:
                name = self._discipline_controller.getDisciplineNameById(discipline.getId())
                toSort.append([discipline.getId(), name, avg])
        toSort.sort(key = itemgetter(2), reverse = True)
        for discipline in toSort:
            print("ID: " + str(discipline[0]) + " / Name: " + str(discipline[1]) + " / Average: " + str(discipline[2]))

