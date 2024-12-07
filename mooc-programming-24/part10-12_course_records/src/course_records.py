# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credits: int):
        self.__name = name
        self.__grade = grade
        self.__credits = credits
    
    def __str__(self):
        return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"
    
    def name(self):
        return self.__name

    def grade(self):
        return self.__grade
    
    def fixgrade(self, grade: int):
        if self.__grade < grade:
            self.__grade = grade
    
    def credits(self):
        return self.__credits


class Studies:
    def __init__(self):
        self.__courses = {}

    def addcourse(self, name: str, grade: int, credits: int): 
        if not name in self.__courses:
            self.__courses[name] = Course(name, grade, credits)
        else:
            self.__courses[name].fixgrade(grade)
 
    def getcourse(self, name: str):
        if name in self.__courses:
            return f"{self.__courses[name]}"
        else:
            return None
    
    def printstats(self):
        totalcredits = 0
        grades = {5: 0, 4: 0, 3: 0, 2: 0, 1: 0}
        for course in self.__courses.values():
            totalcredits += course.credits()
            grades[course.grade()] += 1
        print(f"{len(self.__courses)} completed courses, a total of {totalcredits} credits")
        sum = 0
        for grade, amount in grades.items():
            sum += grade * amount
        print(f"mean {round(sum/len(self.__courses),1)}")
        print("grade distribution")
        for grade, amount in grades.items():
            print(str(grade)+": "+(amount*"x"))


class UserInterface:
    def __init__(self):
        self.__studies = Studies()
 
    def guidance(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
 
    def execute(self):
        self.guidance()
        while True:
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                name = input("course: ")
                grade = int(input("grade: "))
                cred = int(input("credits: "))
                self.__studies.addcourse(name, grade, cred)
            elif command == "2":
                course = input("course: ")
                hit = self.__studies.getcourse(course)
                if hit == None:
                    print("no entry for this course")
                else:
                    print(hit)
            elif command == "3":
                self.__studies.printstats()
            else:
                print("unknown command")

application = UserInterface()
application.execute()