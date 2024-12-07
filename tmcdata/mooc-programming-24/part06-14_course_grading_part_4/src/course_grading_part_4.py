# tee ratkaisu tänne
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points =  input("Exam points: ")
course_info = input("Course information: ")

names = {}
with open(student_info) as studentinfo:
    for line in studentinfo:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        else:
            names[parts[0]] = parts[1].strip() + " " + parts[2].strip()

exercises = {}
with open(exercise_data) as exercisedata:
    for line in exercisedata:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        else:
            exercises[parts[0]] = []
            for i in parts[1:]:
                exercises[parts[0]].append(int(i.strip()))
        
exampoints = {}
with open(exam_points) as examdata:
    for line in examdata:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        else:
            exampoints[parts[0]] = []
            for i in parts[1:]:
                exampoints[parts[0]].append(int(i.strip()))

studentionary = {}
for id, name in names.items():
    fullname = name
    studentionary[fullname] = []
    if id in exercises:
        exercisenr = sum(exercises[id])
        studentionary[fullname].append(exercisenr)
        exercisept = int(exercisenr/40*10)
        studentionary[fullname].append(exercisept)
    if id in exampoints:
        exampt = sum(exampoints[id])
        studentionary[fullname].append(exampt)
    totalpts = exercisept + exampt
    studentionary[fullname].append(totalpts)
    if totalpts < 15:
        grade = 0
    elif totalpts < 18:
        grade = 1
    elif totalpts < 21:
        grade = 2
    elif totalpts < 24:
        grade = 3
    elif totalpts < 28:
        grade = 4
    else:
        grade = 5
    studentionary[fullname].append(grade)
    studentionary[fullname].append(id)


coursestring = ""
gold = []
with open(course_info) as courseinfo:
    for line in courseinfo:
        parts = line.split(":")
        gold.append(parts[1].strip())
coursestring = f"{gold[0]}, {gold[1]} credits\n"

with open("results.txt","w") as resultxt:
    resultxt.write(coursestring)
    resultxt.write((len(coursestring)-1)*"="+"\n")
    resultxt.write(f"name{26 * ' '}exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")
    for name in studentionary:
        resultxt.write(f"{name:30}{studentionary[name][0]:<10}{studentionary[name][1]:<10}{studentionary[name][2]:<10}{studentionary[name][3]:<10}{studentionary[name][4]}\n")

with open("results.csv","w") as resultcsv:
    for name in studentionary:
        resultcsv.write(f"{studentionary[name][5]};{name};{studentionary[name][4]}\n")

print("Results written to files results.txt and results.csv")