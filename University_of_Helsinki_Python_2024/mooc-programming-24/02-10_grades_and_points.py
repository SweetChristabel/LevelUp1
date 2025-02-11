# Write your solution here
points= int(input("How many points [0-100]:"))
if points < 0 or points > 100:
    grade = "impossible!"
elif points >= 0 and points < 50:
    grade = "fail"
elif points >= 50 and points < 60:
    grade = 1
elif points >= 60 and points < 70:
    grade = 2
elif points >= 70 and points < 80:
    grade = 3
elif points >= 80 and points < 90:
    grade = 4
elif points >= 90 and points <= 100:
    grade = 5

print("Grade:", grade)