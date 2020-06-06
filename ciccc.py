# Group 4: Matheus, Diana, Yusuke

import random
import os
import platform


profilesList = []
accountList = []
loggedInAccount = None


class Account:
    # implements class account here


    def __init__(self, username, password, studentID):

        self._username = username
        self._password = password
        self._studentID = studentID

    def saveAccount(self):

        accountDict = {
            "username": self._username,
            "password": self._password,
            "studentID": self._studentID
        }

        accountList.append(accountDict)

        # print(f"\nAccount List {accountList}\n")

    def searchAccount(username):
        global accountList

        for i in range(len(accountList)):
            tempAccount = accountList[i]

            # If the user exists
            if username == tempAccount['username']:
                return tempAccount
        
        return 404


class Course:
    def __init__(self, name, code, unit):
        self._courseName = name
        self._courseCode = code
        self._courseUnit = unit

    def getCourseName(self):
        return self._courseName

    def getCourseCode(self):
        return self._courseCode

    def getCourseUnit(self):
        return self._courseUnit


class TakenCourse(Course):
    # implements class TakenCourse
    def __init__(self, collegeCourse, semester=0, grade=-1):
        name = collegeCourse.getCourseName()
        code = collegeCourse.getCourseCode()
        unit = collegeCourse.getCourseUnit()
        super().__init__(name, code, unit)

        self._semester = semester
        self._grade = grade
        self._unit = unit

    def printCourse(self):
        if self._semester == Portal.getCurrentSemester():
            print(f"{self._courseCode}: {self._courseName}: {self._grade}",end="[Current Semester]")
        else:
            print(f"{self._courseCode}: {self._courseName}: {self._grade}",end="")

    def printCourseAndGrade(self):
        if self._semester == Portal.getCurrentSemester():
            print(f"{self._courseCode}: {self._courseName}: {self._grade}",end="[Current Semester]")
        else:
            print(f"{self._courseCode}: {self._courseName}: {self._grade}",end="")

    def getCourseGradeAndUnit(self):
        return (self._grade, self._unit)

    def printCurrentSemesterCourses(self):
        if self._semester == Portal.getCurrentSemester():
            print(f"{self._courseCode}: {self._courseName}: {self._grade}",end="[Current Semester]")

    def getCourseSemester(self):
        return self._semester

    def getCourse(self):
        return self


class CollegeCourse(Course):
    # implements and complete class CollegeCourse
    def __init__(self, name, code, unit):
        super().__init__(name, code, unit)
        self._courseUnit = unit

    def printCourse(self):
        print("Course Name: %s | Course Code: %s | Course Unit %d \n" % (self._courseName, self._courseCode, self._courseUnit))

    def printCourseAndGradeAndUnit(self):
        print(f"{self._courseCode}: {self._courseName}: {self._courseUnit}",end="")


class Student:
    # implements class student here
    def __init__(self, studentProfile, admissionYear=2020):
        self._admissionYear = admissionYear
        self._admissionSemester = 1  # Suppose each student starts in semester 1 of the admission year
        self._generalTranscript = GeneralTranscript()
        self._semesterTranscript = CurrentSemesterTranscript()
        self._studentProfile = studentProfile

    def getAdmissionYear(self):
        return self._admissionYear

    def registerCourse(self, collegeCourse, semester, grade=0):

        courseRegistrationYear = semester.getYear()
        courseRegistrationSemester = semester.getSemesterNo()

        course = TakenCourse(collegeCourse, semester, grade)

        if semester.isCurrentSemester():
            self._semesterTranscript.addCourse(course)
            self._generalTranscript.addCourse(course)
        else:
            self._generalTranscript.addCourse(course)

    def getGTranscript(self):
        return self._generalTranscript

    def getSTranscript(self):
        return self._semesterTranscript

    def getStudentProfile(self):
        return self._studentProfile

    def calculateGPA(self, isCurrentSemester = False):
        if isCurrentSemester:
            coursesList = self.getGTranscript().getCurrentSemesterCourses()
        else:
            coursesList = self.getGTranscript().getAllCourses()

        if coursesList == -1:
            return 0

        gradeAndUnitList = []
        unitSum = 0
        tempGPA = 0

        for course in coursesList:
            gradeAndUnit = course.getCourseGradeAndUnit()
            gradeAndUnitDict = {
                "grade": gradeAndUnit[0],
                "unit": gradeAndUnit[1]
            }
            gradeAndUnitList.append(gradeAndUnitDict)
            unitSum += gradeAndUnit[1]

        for i in range(len(gradeAndUnitList)):
            tempDict = gradeAndUnitList[i]
            tempGPA += tempDict['grade'] * tempDict['unit']

        gpa = tempGPA / unitSum
        
        return gpa
            

class StudentProfile:

    usedStudentIDs = set()

    global profilesList

    # implements class student here
    def __init__(self, firstName, lastName, gender, country, age, address, studentId = 0):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.country = country
        self.age = age
        self.address = address
        self.studentId = studentId

    def saveStudentProfile(self):

        if self.studentId == 0:

            studentID = StudentProfile.createStudentID()

            self.studentId = studentID

        profilesList.append(self)

    def createStudentID():

        newStudentID = random.randint(00000000, 99999999)

        while newStudentID in StudentProfile.usedStudentIDs:
            
            newStudentID = randint(00000000, 99999999)
            
        StudentProfile.usedStudentIDs.add(newStudentID)
        return newStudentID

    def searchStudentProfile(studentId):
        global profilesList

        for i in range(len(profilesList)):
            tempProfile = profilesList[i]

            # If the user exists
            if studentId == tempProfile.getStudentID():
                return tempProfile
        
        return 404

    def getFullName(self):

        fullName = self.firstName + " " + self.lastName
        return fullName

    def getGender(self):
        return self.gender

    def getCountry(self):
        return self.country

    def getAge(self):
        return self.age
    
    def getAddress(self):
        return self.address

    def getStudentID(self):
        return self.studentId

    def getStudentTitle(self, isTitle = False):

        if isTitle:
            if self.getGender().upper() == "M":
                return "Sir"
            elif self.getGender().upper() == "F":
                return "Madam"
            else:
                return "Sir/Madam"
        
        if self.getGender().upper() == "M":
            return "Mr."
        elif self.getGender().upper() == "F":
            return "Mrs."
        else:
            return ""

    def showMyCourses(portalManager):
        global loggedInAccount
        loggedInStudent = portalManager._portal.findStudent(loggedInAccount.getStudentID())

        print(f"Hi, {loggedInAccount.getStudentTitle()}", loggedInAccount.getFullName(),end=",\n")
        print("You have taken the following courses so far:")
        coursesList = loggedInStudent.getGTranscript().getAllCourses()
        courseCounter = 0

        for course in coursesList:
            courseCounter += 1
            print(f"{courseCounter}) ",end="")
            course.printCourse()
            print()

        print("\n----------------")
        print("Press any key to return to the main menu")
        input("")

    def showMyProfile(portalManager):
        global loggedInAccount
        loggedInStudent = portalManager._portal.findStudent(loggedInAccount.getStudentID())

        print("Name:", loggedInAccount.getFullName())
        print("StudentID:", loggedInAccount.getStudentID())
        print("Gender:", loggedInAccount.getGender())
        print("Address:", loggedInAccount.getAddress())
        print("Country of Origin:", loggedInAccount.getCountry())
        print("Age:", loggedInAccount.getAge())
        print("Year of Admission:", loggedInStudent.getAdmissionYear())
        print(f"Overall GPA: {loggedInStudent.calculateGPA():.2f}")
        print("Courses Taken:", end=" ")
        loggedInStudent.getGTranscript().printTranscript()
        print("\n----------------")
        print("Press any key to return to the main menu")
        input("")

    def showMyCertificate(portalManager):

        global loggedInAccount
        loggedInStudent = portalManager._portal.findStudent(loggedInAccount.getStudentID())

        qtyTakenCourses = len(loggedInStudent.getGTranscript().getAllCourses())

        currentSemester = Portal.getCurrentSemester()

        manager = Manager.getManager()

        if loggedInAccount.getStudentTitle() == "Mr.":
            genderCall = "he"
        elif loggedInAccount.getStudentTitle() == "Mrs.":
            genderCall = "she"
        elif loggedInAccount.getStudentTitle() == "":
            genderCall = "he/she"

        print(f"Dear {loggedInAccount.getStudentTitle(True)},", end="\n\n")
        print(f"This is to certify that {loggedInAccount.getStudentTitle()} {loggedInAccount.getFullName()} with Student ID {loggedInAccount.getStudentID()} is a student at semester {currentSemester.getSemesterNo()} at CICCC.")
        print(f"{genderCall.capitalize()} was admitted to our college in {loggedInStudent.getAdmissionYear()} and has taken {qtyTakenCourses} course(s) so far.")
        print(f"Currently, {genderCall} resides at {loggedInAccount.getAddress()}.",end="\n\n")
        print("If you have any questions, please don't hesitate to contact us.")
        print("Thanks,")
        print(f"[Manager: {manager.getFullName()}]")
        print("\n----------------")
        print("Press any key to return to the main menu")
        input("")

    def showMyTranscript(portalManager):
        global loggedInAccount
        loggedInStudent = portalManager._portal.findStudent(loggedInAccount.getStudentID())

        print(f"Hi, {loggedInAccount.getStudentTitle()}", loggedInAccount.getFullName(),end=",\n")
        print("Here is your general transcript:")
        coursesList = loggedInStudent.getGTranscript().getAllCourses()
        courseCounter = 0

        for course in coursesList:
            courseCounter += 1
            print(f"{courseCounter}) ",end="")
            course.printCourse()
            print()

        print(f"YOUR GPA IS: {loggedInStudent.calculateGPA():.2f}",end="\n\n")

        print("Here is your current semester transcript:")
        currentSemesterCoursesList = loggedInStudent.getGTranscript().getCurrentSemesterCourses()
        courseCounter = 0

        if currentSemesterCoursesList == -1:
            print("The student does not have courses taken this semester")

        else:
            for course in currentSemesterCoursesList:
                courseCounter += 1
                print(f"{courseCounter}) ",end="")
                course.printCurrentSemesterCourses()
                print()
            
            print(f"YOUR GPA IS: {loggedInStudent.calculateGPA(True):.2f}",end="\n\n")
            
        print("\n----------------")
        print("Press any key to return to the main menu")
        input("")

    def showMyGPA(portalManager):
        global loggedInAccount
        loggedInStudent = portalManager._portal.findStudent(loggedInAccount.getStudentID())

        print(f"Hi, {loggedInAccount.getStudentTitle()}", loggedInAccount.getFullName(),end=",\n")
        print(f"Your overall GPA is: {loggedInStudent.calculateGPA():.2f}",end="\n\n")
        print(f"Your current semester's GPA is: {loggedInStudent.calculateGPA(True):.2f}",end="\n\n")

        print("\n----------------")
        print("Press any key to return to the main menu")
        input("")

    def showGPARank(portalManager):
        global loggedInAccount
        loggedInStudent = portalManager._portal.findStudent(loggedInAccount.getStudentID())

        studentGPA = loggedInStudent.calculateGPA()

        studentsList = portalManager.getAllStudents()

        GPAList = []
        GPAList.append(studentGPA)

        for student in studentsList:
            GPAList.append(student.calculateGPA())

        sortedGPAList = sorted(GPAList, reverse=True)

        rankPosition = sortedGPAList.index(studentGPA) + 1

        print(f"Hi, {loggedInAccount.getStudentTitle()}", loggedInAccount.getFullName(),end=",\n")
        print(f"Your overall GPA is {studentGPA:.2f} and therefore your rank is {rankPosition}")

        print("\n----------------")
        print("Press any key to return to the main menu")
        input("")


class Transcript:
    # implements class transcript here
    def __init__(self):
        self._allTakenCourses = []

    def addCourse(self, takenCourse):
        self._allTakenCourses.append(takenCourse)
        # complete this method

    def printTranscript(self):

        if len(self._allTakenCourses) == 0:
            print("The student does not have any taken courses")
        for c in self._allTakenCourses:
            c.printCourse()
            print(", ", end="")
        print()

    def getAllCourses(self):
        return self._allTakenCourses

    def getAllCourseCodes(self):
        courseCodeList = []

        for course in self._allTakenCourses:
            courseCodeList.append(course.getCourseCode())

        return courseCodeList

    def getCurrentSemesterCourses(self):
        currentSemesterCourses = []
        if len(self._allTakenCourses) == 0:
            print("The student does not have any taken courses")
        for c in self._allTakenCourses:
            if c.getCourseSemester() == Portal.getCurrentSemester():
                currentSemesterCourses.append(c)
        
        if len(currentSemesterCourses) == 0:
            return -1

        return currentSemesterCourses


class GeneralTranscript(Transcript):
    # implements class GeneralTranscript here
    def __init__(self):
        super().__init__()


class CurrentSemesterTranscript(Transcript):
    # implements class CurrentSemesterTranscript here
    def __init__(self):
        super().__init__()


class Manager:
    # implements class Manager here
    managerInfo = None

    def __init__(self, firstName, lastName, title):
        self._firstName = firstName
        self._lastName = lastName
        self._title = title

        Manager.managerInfo = self

    def getManager():
        return Manager.managerInfo

    def getFullName(self):
        return self._firstName + " " + self._lastName


class Semester:
    # implements class Semester here
    def __init__(self, semesterNo, year):
        self._semesterNo = semesterNo
        self._year = year
        self._setIfCurrentSemester()

    def __eq__(self, other):
        return self._year == other._year and self._semesterNo == other._semesterNo

    def getYear(self):
        return self._year

    def getSemesterNo(self):
        return self._semesterNo

    # checks whether the semester object is representing current semester or not. Suppose, current semester is year = 2020, semester = 2
    def _setIfCurrentSemester(self):
        currentSemester = 1
        currentYear = 2020

        if (self._semesterNo == currentSemester) and (self._year == currentYear):
            self._isCurrentSemester = True
        else:
            self._isCurrentSemester = False

    def isCurrentSemester(self):
        return self._isCurrentSemester

    def printSemester(self):
        print("Year: %d Semester%d isCurrent %d" % (self._year, self._semesterNo, self._isCurrentSemester))


class Menu:
    # implements class Menu here
    menuPortalManager = None

    def clearTerminal():

        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def showLoginMenu(portalManager):
        Menu.clearTerminal()
        Menu.menuPortalManager = portalManager
        Menu.lineSeparator()
        print("Please enter your account to login:")
        Menu.lineSeparator()
        print("Username: ")
        print("Password: ", end="\n\n")
        print("-"*16)
        print("Not registered yet? Type “Register” and press enter to start the registration process!")
        Menu.doLogin()

    def showRegisterMenu():
        global loggedInAccount

        Menu.lineSeparator()
        print("Welcome to CICCC College: Please Register")
        Menu.lineSeparator()

        userFirstName = Menu.validateWord("Please enter your first name: ", "first name")
        userLastName = Menu.validateWord("Please enter your last name: ", "last name")
        userGender = Menu.validateGender()
        userCountry = Menu.validateWord("Please enter your country of origin: ", "country of origin")
        userAddress = Menu.validateWord("Please enter your address: ", "address")
        userAdmissionYear = int(Menu.validateNumber("Please enter your year of admission: ", "year of admission"))
        userAge = Menu.validateNumber("Please enter your age: ", "age")

        username = Menu.validateUsername()
        userPassword = Menu.validatePassword()

        # Create the Student Profile
        studentProfile = StudentProfile(userFirstName, userLastName, userGender, userCountry, userAge, userAddress)

        studentProfile.saveStudentProfile()

        # Create the Student Account
        studentAccount = Account(username, userPassword, studentProfile.getStudentID())
        
        studentAccount.saveAccount()

        # Create the Student
        student = Student(studentProfile, userAdmissionYear)
        Menu.menuPortalManager._portal.registerStudent(student)
        Menu.menuPortalManager._portal.addRandomCoursesToStudent(student)

        # Global variable related to the logged user
        loggedInAccount = studentProfile

        print(f"\nThanks, your account and profile has been created successfully. Welcome Aboard, {username}!")

    def showMainMenu():
        
        Menu.printMainMenuOptions()
        userMenuInput = int(input("Enter the number corresponding to each item to proceed: "))

        while userMenuInput != 10:
            if userMenuInput == 1:
                Menu.clearTerminal()
                Menu.lineSeparator()
                print("Enrolment Certificate")
                Menu.lineSeparator()
                StudentProfile.showMyCertificate(Menu.menuPortalManager)

            elif userMenuInput == 2:
                Menu.clearTerminal()
                Menu.lineSeparator()
                print("My Courses")
                Menu.lineSeparator()
                StudentProfile.showMyCourses(Menu.menuPortalManager)

            elif userMenuInput == 3:
                Menu.clearTerminal()
                Menu.lineSeparator()
                print("My Transcript")
                Menu.lineSeparator()
                StudentProfile.showMyTranscript(Menu.menuPortalManager)

            elif userMenuInput == 4:
                Menu.clearTerminal()
                Menu.lineSeparator()
                print("My GPA")
                Menu.lineSeparator()
                StudentProfile.showMyGPA(Menu.menuPortalManager)

            elif userMenuInput == 5:
                Menu.clearTerminal()
                Menu.lineSeparator()
                print("GPA Rank")
                Menu.lineSeparator()
                StudentProfile.showGPARank(Menu.menuPortalManager)

            elif userMenuInput == 6:
                Menu.clearTerminal()
                Menu.lineSeparator()
                print("List of Courses")
                Menu.lineSeparator()
                Menu.menuPortalManager.listAllCourses()

            elif userMenuInput == 7:
                Menu.clearTerminal()
                Menu.lineSeparator()
                print("List of Students")
                Menu.lineSeparator()
                Menu.menuPortalManager.listAllStudents()

            elif userMenuInput == 8:
                Menu.clearTerminal()
                Menu.lineSeparator()
                print("Student's Profile")
                Menu.lineSeparator()
                StudentProfile.showMyProfile(Menu.menuPortalManager)

            elif userMenuInput == 9:
                Menu.clearTerminal()
                Menu.showLoginMenu(Menu.menuPortalManager)

            Menu.printMainMenuOptions()
            userMenuInput = int(input("Enter the number corresponding to each item to proceed: "))

        if userMenuInput == 10:
            Menu.clearTerminal()
            exit()

    def printMainMenuOptions():
        Menu.lineSeparator()
        print("Select from the options: ")
        Menu.lineSeparator()
        print("-[1] Print my enrollment certificate")
        print("-[2] Print my courses")
        print("-[3] Print my transcript")
        print("-[4] Print my GPA")
        print("-[5] Print my ranking among all students in the college")
        print("-[6] List all available courses")
        print("-[7] List all students")
        print("-[8] Show my profile")
        print("-[9] Logout")
        print("-[10] Exit")
        # print("-[11] Bonus")
        Menu.lineSeparator()

    def validateWord(inputText, inputVariable):
        
        userInput = input(inputText)
        
        while (not all(c.isalpha() or c.isspace() for c in userInput)):
            print(f"\nThe {inputVariable} contains digit(s)! Please enter a valid one!\n")
            userInput = input(inputText)

        return userInput

    def validateGender():
        
        genderList = ["M","F","O"]
        
        userGender = input("Please enter your gender[M/F/O]: ")

        while not userGender.upper() in genderList:
            print("\nThe gender is not valid! Please try again.\n")
            userGender = input("Please enter your gender[M/F/O]: ")

        return userGender

    def validateNumber(inputText, inputVariable):

        userInput = input(inputText)

        while not userInput.isdigit():
            print(f"\nThe {inputVariable} contains letter(s)! Please enter a valid one!\n")
            userInput = input(inputText)

        return userInput

    def validateUsername():
        username = input("Please enter a username [At least 6 characters]: ")

        while len(username) < 6 or not username.isalpha():
            print("\nThe username must have at least 6 characters and no digits!\n")
            username = input("Please enter a username [At least 6 characters]: ")
            
        return username

    def validatePassword():
        userPassword = input("Please enter a password [At least 6 characters with at least one digit]: ")

        while len(userPassword) < 6 or not userPassword.isalnum():
            print("\nThe password must have at least 6 characters and one digit!\n")
            userPassword = input("Please enter a password [At least 6 characters with at least one digit]: ")

        return userPassword

    def lineSeparator():
        print("*"*60)

    def doLogin():

        global loggedInAccount

        username = input("")

        if username.lower() == "register":
            Menu.clearTerminal()
            Menu.showRegisterMenu()
            Menu.clearTerminal()
            Menu.showMainMenu()

        else:

            searchResult = Account.searchAccount(username)

            if searchResult == 404:
                Menu.clearTerminal()
                print("This username does not exist. Please register yourself!")
                print("\n----------------")
                print("Press any key to continue")
                input("")
                Menu.clearTerminal()
                Menu.showLoginMenu(Menu.menuPortalManager)
                Menu.clearTerminal()
                Menu.showMainMenu()
            else:
                password = input("")

                while password != searchResult["password"]:
                    print("The password is wrong. Please try again.")
                    password = input("")

                studentProfile = StudentProfile.searchStudentProfile(searchResult['studentID'])

                if studentProfile == 404:
                    Menu.clearTerminal()
                    print("This profile does not exist. Please register yourself!")
                    print("\n----------------")
                    print("Press any key to continue")
                    input("")
                    Menu.clearTerminal()
                    Menu.showLoginMenu(Menu.menuPortalManager)
                
                # Global variable related to the logged user
                loggedInAccount = studentProfile

                Menu.clearTerminal()
                Menu.showMainMenu()


class Portal:

    # _currentSemester = Semester(2020, 1)  # Static/class property. Suppose the current semester is first semester 2020
    def __init__(self):
        self._collegeCourses = []
        self._registeredStudents = []

    # use this method to register a student
    def registerStudent(self, student):
        self._registeredStudents.append(student)

    def findStudent(self, studentID):

        for student in self._registeredStudents:
            studentProfile = student.getStudentProfile()
            if studentID == studentProfile.getStudentID():
                return student

    def addCourse(self, collegeCourse):
        self._collegeCourses.append(collegeCourse)
    # class this method to add some random courses to a student - You don't need to understand how this method works. Just call it and it will add some courses
    # to the student and to different semesters

    def addRandomCoursesToStudent(self, student):
        for course in self._collegeCourses:
            rand = random.uniform(0, 1)
            admissionYear = student.getAdmissionYear()
            currentSemester = Portal.getCurrentSemester()

            if currentSemester.getYear() == admissionYear:
                numberOfSemesterBetweenCurrentSemesterAndAdmission = currentSemester.getSemesterNo()
            else:
                numberOfSemesterBetweenCurrentSemesterAndAdmission = 2 * (currentSemester.getYear() - admissionYear) + currentSemester.getSemesterNo()

            randomSemster = random.randint(1, numberOfSemesterBetweenCurrentSemesterAndAdmission)

            year = randomSemster // 2
            semesterNo = (randomSemster % 2) + 1
            semester = Semester(semesterNo, student.getAdmissionYear() + year)

            randomGrade = random.randint(30, 100)

            if rand <= .5:
                student.registerCourse(course, semester, randomGrade)

    # static/class method
    def getCurrentSemester():
        currentSemester = Semester(1, 2020)  # Static/class property. Suppose the current semester is first semester 2020
        return currentSemester


class PortalManager:
    def __init__(self):
        self._portal = Portal()

    def createATestPortal(self):

        # create all courses offered
        self._createAllCollegeCourses()

        # Create Manager
        Manager("Peter", "Jackson", "Mr.")

        # Student 1
        student1Account = Account("student1","111111",8012321)
        student1Account.saveAccount()

        # create a student 1
        student1Profile = StudentProfile("Peter", "Sand", "M", "Ireland", 21, "Vancouver",8012321)
        student1Profile.saveStudentProfile()
        student1 = Student(student1Profile, 2019)

        # register the student 1
        self._portal.registerStudent(student1)

        # add courses with grades to the student
        student1.registerCourse(CollegeCourse("Phyton", "CSCI101", 3), Semester(1, 2019), 80)
        student1.registerCourse(CollegeCourse("Object-Oriented Programming", "CSCI102", 2), Semester(2, 2019), 76)
        student1.registerCourse(CollegeCourse("Problem Solving", "CSCI201", 1), Semester(1, 2020), 67)
        student1.registerCourse(CollegeCourse("Project Management", "CSCI202", 3), Semester(1, 2019), 82)
        student1.registerCourse(CollegeCourse("Java Programming", "CSCI301", 3), Semester(2, 2019), 73)


        # Student 2
        student2Account = Account("student2","222222",8014525)
        student2Account.saveAccount()

        # create a student 2
        student2Profile = StudentProfile("Sheila", "Rogers", "F", "India", 19, "Surrey",8014525)
        student2Profile.saveStudentProfile()
        student2 = Student(student2Profile, 2018)

        # register the student 2
        self._portal.registerStudent(student2)

        # add courses with grades to the student
        student2.registerCourse(CollegeCourse("Phyton", "CSCI101", 3), Semester(1, 2018), 65)
        student2.registerCourse(CollegeCourse("Object-Oriented Programming", "CSCI102", 2), Semester(2, 2018), 67)
        student2.registerCourse(CollegeCourse("Problem Solving", "CSCI201", 1), Semester(2, 2018), 85)
        student2.registerCourse(CollegeCourse("Project Management", "CSCI202", 3), Semester(1, 2019), 56)
        student2.registerCourse(CollegeCourse("Java Programming", "CSCI301", 3), Semester(1, 2019), 75)
        student2.registerCourse(CollegeCourse("Web Development", "CSCI302", 2), Semester(2, 2019), 76)
        student2.registerCourse(CollegeCourse("Android Programming", "CSCI401", 2), Semester(2, 2019), 80)
        student2.registerCourse(CollegeCourse("iOS Application", "CSCI402", 3), Semester(1, 2020), 74)



        # Student 3
        student3Account = Account("student3","333333",8011111)
        student3Account.saveAccount()

        # create a student 3
        student3Profile = StudentProfile("Edward", "Richards", "M", "China", 20, "Burnaby",8011111)
        student3Profile.saveStudentProfile()
        student3 = Student(student3Profile, 2019)

        # register the student 3
        self._portal.registerStudent(student3)

        # add courses with grades to the student
        student3.registerCourse(CollegeCourse("Problem Solving", "CSCI201", 1), Semester(1, 2019), 78)
        student3.registerCourse(CollegeCourse("Project Management", "CSCI202", 3), Semester(1, 2019), 87)
        student3.registerCourse(CollegeCourse("Web Development", "CSCI302", 2), Semester(1, 2020), 77)


        # Student 4
        student4Account = Account("student4","444444",8033344)
        student4Account.saveAccount()

        # create a student 4
        student4Profile = StudentProfile("Souzan", "Robson", "F", "India", 20, "Surrey",8033344)
        student4Profile.saveStudentProfile()
        student4 = Student(student4Profile, 2019)

        # register the student 4
        self._portal.registerStudent(student4)

        # add courses with grades to the student
        student4.registerCourse(CollegeCourse("Project Management", "CSCI202", 3), Semester(1, 2019), 89)
        student4.registerCourse(CollegeCourse("Java Programming", "CSCI301", 3), Semester(1, 2019), 87)
        student4.registerCourse(CollegeCourse("Web Development", "CSCI302", 2), Semester(2, 2019), 71)
        student4.registerCourse(CollegeCourse("Android Programming", "CSCI401", 2), Semester(2, 2019), 69)
        student4.registerCourse(CollegeCourse("iOS Application", "CSCI402", 3), Semester(1, 2020), 75)



        # Student 5
        student5Account = Account("student5","555555",8012322)
        student5Account.saveAccount()

        # create a student 5
        student5Profile = StudentProfile("Jeff", "Cooper", "M", "England", 21, "Vancouver",8012322)
        student5Profile.saveStudentProfile()
        student5 = Student(student5Profile, 2018)

        # register the student 5
        self._portal.registerStudent(student5)

        # add courses with grades to the student
        student5.registerCourse(CollegeCourse("Web Development", "CSCI302", 2), Semester(1, 2018), 78)
        student5.registerCourse(CollegeCourse("Android Programming", "CSCI401", 2), Semester(2, 2018), 56)
        student5.registerCourse(CollegeCourse("iOS Application", "CSCI402", 3), Semester(2, 2018), 89)
        student5.registerCourse(CollegeCourse("Project Management", "CSCI202", 3), Semester(1, 2019), 66)
        student5.registerCourse(CollegeCourse("Java Programming", "CSCI301", 3), Semester(1, 2019), 77)
        student5.registerCourse(CollegeCourse("Object-Oriented Programming", "CSCI102", 2), Semester(2, 2019), 87)
        student5.registerCourse(CollegeCourse("Problem Solving", "CSCI201", 1), Semester(2, 2019), 67)

    # create college courses
    def _createAllCollegeCourses(self):
        python = CollegeCourse("Python", "CSCI101", 3)
        objectOrientedProgramming = CollegeCourse("Object-Oriented Programming", "CSCI102", 2)
        problemSolving = CollegeCourse("Problem Solving", "CSCI201", 1)
        projectManagement = CollegeCourse("Project Management", "CSCI202", 3)
        javaProgramming = CollegeCourse("Java Programming", "CSCI301", 3)
        webDevelopment = CollegeCourse("Web Development", "CSCI302", 2)
        androidProgramming = CollegeCourse("Android Programming", "CSCI401", 2)
        iOSApplication = CollegeCourse("iOS Application", "CSCI402", 3)

        self._portal.addCourse(python)
        self._portal.addCourse(objectOrientedProgramming)
        self._portal.addCourse(problemSolving)
        self._portal.addCourse(projectManagement)
        self._portal.addCourse(javaProgramming)
        self._portal.addCourse(webDevelopment)
        self._portal.addCourse(androidProgramming)
        self._portal.addCourse(iOSApplication)

    def listAllStudents(self):

        print(f"There are {len(self._portal._registeredStudents)} student(s) in CICCC College as following:")
        studentCounter = 0

        for student in self._portal._registeredStudents:
            studentCounter += 1
            print(f"{studentCounter}) {student.getStudentProfile().getFullName()}: {student.getStudentProfile().getStudentID()}")

        print("\n----------------")
        print("Press any key to return to the main menu")
        input("")

    def listAllCourses(self):

        global loggedInAccount
        loggedInStudent = self._portal.findStudent(loggedInAccount.getStudentID())

        studentCourseListCode = loggedInStudent.getGTranscript().getAllCourseCodes()
        studentCourseList = loggedInStudent.getGTranscript().getAllCourses()


        print("The following courses are offered in CICCC College:", end="\n\n")
        allCourses = self._portal._collegeCourses
        courseCounter = 0

        for course in allCourses:
            courseCounter += 1
            print(f"{courseCounter}) ", end="")
            course.printCourseAndGradeAndUnit()
            if course.getCourseCode() not in studentCourseListCode:
                print(" [Not Taken]")
            else:
                for i in range(len(studentCourseList)):
                    if course.getCourseCode() == studentCourseList[i].getCourseCode():
                        studentAdmissionYear = loggedInStudent.getAdmissionYear()
                        yearNo = studentCourseList[i].getCourseSemester().getYear()
                        semesterNo = studentCourseList[i].getCourseSemester().getSemesterNo()

                        takenAtSemester = (yearNo - studentAdmissionYear) * 2 + semesterNo

                        print(f" [Taken at semester {takenAtSemester}]")

        print("\n----------------")
        print("Press any key to return to the main menu")
        input("")

    def getAllStudents(self):
        return self._portal._registeredStudents


def main():
    print()
    portalManager = PortalManager()
    portalManager.createATestPortal()
    Menu.showLoginMenu(portalManager)

main()