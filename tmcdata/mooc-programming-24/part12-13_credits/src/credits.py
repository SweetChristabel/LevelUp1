from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(attempts: list):
    return reduce(lambda reduced_sum, item: reduced_sum + item.credits, attempts, 0)

#Function (lambda) takes the item as an argument, and then parts of the item can be accessed within the function. 

def sum_of_passed_credits(attempts:list):
    return reduce(lambda reduced_sum, item: reduced_sum + item.credits, filter(lambda a: a.grade > 0, attempts), 0)

def average(attempts: list):
    passed = list(filter(lambda i: i.grade >= 1, attempts))
    return reduce(lambda reduced_avg, item: reduced_avg + item.grade/len(passed), passed, 0)


if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)