# Write your solution here
def longest(strings: list):
    winner = ""
    for string in strings:
        if len(string) > len(winner):
            winner = string
    return winner
if __name__ == "__main__":

    strings = ["hi", "hiya", "howdilydoodily", "hello", "bye"]
    print(longest(strings))