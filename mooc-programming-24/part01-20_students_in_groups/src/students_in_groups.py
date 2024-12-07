# Write your solution here
amtofstudents = int(input("How many students on the course?"))
groupsize = int(input("Desired group size?"))
amtofgroups = amtofstudents // groupsize
if amtofstudents % groupsize > 0:
    amtofgroups += 1
print("Number of groups formed:", amtofgroups)