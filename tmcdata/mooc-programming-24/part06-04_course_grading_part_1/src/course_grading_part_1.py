# write your solution here
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")


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
            
for id, name in names.items():
    if id in exercises:
        sumofexercises = sum(exercises[id])
        print(f"{name} {sumofexercises}")