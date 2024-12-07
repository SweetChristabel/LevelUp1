# Write your solution here
import csv
from datetime import datetime, timedelta
def cheaters():
    cheaters = []
    studentstarttimes = {}
    threehours = timedelta(hours= 3)
    with open ("start_times.csv") as startimefile:
        for line in csv.reader(startimefile, delimiter= ";"):
            startime = line[1].split(":")
            startime = datetime(2000, 1, 1, int(startime[0]), int(startime[1]))
            studentstarttimes[line[0]] = []
            studentstarttimes[line[0]].append(startime)

    with open ("submissions.csv") as submissionfile:
        for line in csv.reader(submissionfile, delimiter= ";"):
            student = line[0]
            #exercise = int(line[1])
            #if exercise in studentstarttimes[student]:
            #    continue
            #else:
            #    studentstarttimes[student].append(exercise)
            submissiontime = line[-1].split(":")
            submissiontime = datetime(2000, 1, 1, int(submissiontime[0]), int(submissiontime[1]))
            if submissiontime > studentstarttimes[student][0] + threehours:
                if student not in cheaters:
                    cheaters.append(student)
    return cheaters
        

if __name__ == "__main__":
    print(cheaters())