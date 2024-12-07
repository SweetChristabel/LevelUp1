# Write your solution here
def gather_data(): #gather user inputs
    listofinputs = []
    while True:
        studentresult = input("Exam points and exercises completed:")
        if studentresult =="":
            break
        else: listofinputs.append(studentresult)
    return listofinputs

def transform_data(listofinputs: list): #splits user inputs, turns them into integers and sorts them into lists for exam points and exercises
    exampoints = []
    exercises = []
    for i in listofinputs:
        templist = i.split()
        exampoints.append(int(templist[0]))
        exercises.append(int(templist[1]))
    return exampoints, exercises

def convert_points(exercises: list): #converts number of exercises into points
    exercisepoints = []    
    for i in exercises:
        exercisepoints.append(int(i/10))
    return exercisepoints

def sum_and_grade(exampoints: list, exercisepoints: list): #sums points per student, assigns grade, fails if exam is less than 10
    summedpoints = []
    grades = []
    for i in range(0,len(exampoints)):
        totalpoints = exercisepoints[i] + exampoints[i]
        summedpoints.append(totalpoints)
        if exampoints[i] < 10:
            grades.append(0)
        elif totalpoints < 15:
            grades.append(0)
        elif totalpoints < 18:
            grades.append(1)
        elif totalpoints < 21:
            grades.append(2)
        elif totalpoints < 24:
            grades.append(3)
        elif totalpoints < 28:
            grades.append(4)
        else:
            grades.append(5)
    return grades, summedpoints


def print_stats(grades: list, summedpoints: list): #makes statistics and prints them out
    avg = sum(summedpoints)/len(summedpoints)
    prcnt = (len(grades) - grades.count(0))/len(grades) * 100
    print("Statistics:")
    print(f"Points average: {round(avg, 1)}")
    print(f"Pass percentage: {round(prcnt, 1)}")
    print("Grade distribution:")
    print("5: "+grades.count(5)*"*")
    print("4: "+grades.count(4)*"*")
    print("3: "+grades.count(3)*"*")
    print("2: "+grades.count(2)*"*")
    print("1: "+grades.count(1)*"*")
    print("0: "+grades.count(0)*"*")



listofinputs = gather_data()
exampoints, exercises = transform_data(listofinputs)
exercisepoints = convert_points(exercises)
grades, summedpoints = sum_and_grade(exampoints, exercisepoints)
print_stats(grades, summedpoints)
