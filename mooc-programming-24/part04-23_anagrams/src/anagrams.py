# Write your solution here
def anagrams(stringone, stringtwo) -> str:
    if sorted(stringone) == sorted(stringtwo):
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagrams("ireen mitmann", "trenni minema"))