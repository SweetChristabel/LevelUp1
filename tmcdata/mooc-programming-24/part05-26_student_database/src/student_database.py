# Write your solution here
def add_student(database: dict, name: str):
        database[name] = []


def print_student(database: dict, name: str):
    if name in database:
        if database[name] == []:
            print(f"{name}: \n no completed courses")
        else:
            print(name+":")
            for nm, crs in database.items():
                if nm == name:
                    print(f" {len(crs)} completed courses: ")
                    gradesum = 0
                    for i in crs:
                        print(f"  {i[0]} {i[1]}")
                        gradesum += i[1]
                    print(f" average grade {gradesum/len(crs)}")                
    else:
        print(f"{name}: no such person in the database")

def add_course(database: dict, name: str, coursegrade: tuple):
    if not coursegrade[1] == 0:
        if database[name] == []:
            database[name].append(coursegrade)
        else:
            rep = False
            for i in range(len(database[name])):
                if coursegrade[0] in database[name][i]:
                    winner = max(database[name][i][1], coursegrade[1])
                    database[name].remove(database[name][i])
                    database[name].append((coursegrade[0], winner))
                    rep = True
            if rep == False:    
                database[name].append(coursegrade)    

def summary(database:dict):
    print(f"students {len(database)}")
    crswinner = 0
    avgwinner = 0
    
    for name, coursegrade in database.items():
        if len(coursegrade) > crswinner:
            crswinnername = name
            crswinner = len(coursegrade)
        sum = 0
        for i in range(len(coursegrade)):
            sum += coursegrade[i][1]
        avg = sum/len(coursegrade)
        if avg > avgwinner:
            avgwinner = avg
            avgwinnername = name
    print(f"most courses completed {crswinner} {crswinnername}")
    print(f"best average grade {avgwinner} {avgwinnername}")

        


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 3))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)