# Write your solution here
import csv
from datetime import datetime, timedelta
def get_student_startimes():
    students = {}
    with open ("start_times.csv") as startimefile:
        for line in csv.reader(startimefile, delimiter= ";"):
            startime = line[1].split(":")
            startime = datetime(2000, 1, 1, int(startime[0]), int(startime[1]))
            students[line[0]] = {}
            students[line[0]]["start"] = startime
    return students

def final_points():
    threehours = timedelta(hours= 3)
    students = get_student_startimes()
    with open ("submissions.csv") as submissionfile:
        for line in csv.reader(submissionfile, delimiter= ";"):
            student = line[0]
            task = line[1]
            points = line[2]
            submissiontime = line[-1].split(":")
            submissiontime = datetime(2000, 1, 1, int(submissiontime[0]), int(submissiontime[1]))
            if submissiontime > students[student]["start"] + threehours:
                continue
            print(students[student])
            if task in students[student]:
                if students[student][task] < points:
                    students[student][task] = points
            else:
                students[student][task] = points
    trimmedstudents = {}
    for stdnt, stats in students.items():
        del stats["start"]
        stdntstatlist = []
        for exercise, points in stats.items():
            stdntstatlist.append(int(points))
        trimmedstudents[stdnt] = sum(stdntstatlist)
    return trimmedstudents

if __name__ == "__main__":
    print(final_points())

