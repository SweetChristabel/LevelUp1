# Write your solution here
import urllib.request
import json
def retrieve_all():
#so we 1) retrieve
#then we 2) read
#then we 3) json load
    request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    content = request.read()
    courses = json.loads(content)
    courselist = []
    for course in courses:
        if course["enabled"] == False:
            continue
        else:
            fullname = course["fullName"]
            name = course["name"]
            year = course["year"]
            exercisesum = sum(course["exercises"])
            course = fullname, name, year, exercisesum
            courselist.append(course)
    return courselist

def retrieve_course(course_name: str):
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses/"+course_name+"/stats"
    request = urllib.request.urlopen(url)
    request = request.read()
    request = json.loads(request)
    courseinfo = {}
    weeks = 0
    maxstudents = 0
    hours = 0
    exercises = 0
    for key, dict in request.items():
        weeks +=1
        if dict['students'] > maxstudents:
            maxstudents = dict['students']
        hours += dict['hour_total']
        exercises += dict['exercise_total']
    courseinfo['weeks'] = weeks
    courseinfo['students'] = maxstudents
    courseinfo['hours'] = hours
    courseinfo['hours_average'] = int(hours/maxstudents)
    courseinfo['exercises'] = exercises
    courseinfo['exercises_average'] = int(exercises/maxstudents)
    return courseinfo
        


if __name__ == "__main__":
    print(retrieve_course("docker2019"))