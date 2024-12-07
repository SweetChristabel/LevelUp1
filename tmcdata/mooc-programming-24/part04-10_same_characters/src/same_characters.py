# Write your solution here
def same_chars(word, x, y):
    if len(word)-1 <= x or len(word)-1 <= y:
        return False
    elif word[x] == word[y]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
    print(same_chars("boo-lean", 1, 2))
    print(same_chars("boo", 2, 5))
    print(same_chars("abc", 0, 3))
