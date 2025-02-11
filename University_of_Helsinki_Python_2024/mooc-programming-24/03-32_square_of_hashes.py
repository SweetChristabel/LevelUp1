# Write your solution here
def hash_square(x):
    rep = 1
    while rep <= x:
        print("#"*x)
        rep += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)
    hash_square(10)