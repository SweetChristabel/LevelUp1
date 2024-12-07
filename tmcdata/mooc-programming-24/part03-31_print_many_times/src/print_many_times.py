# Write your solution here
def print_many_times(text, times):
    rep = 1
    while rep <= times:
         print(text)
         rep +=1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)
    print_many_times("we go up", 10)