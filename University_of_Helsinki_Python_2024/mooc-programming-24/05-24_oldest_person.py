# Write your solution here
def oldest_person(people: list):
    winner = ("start", 9999)
    for i in people:
        if i[1] < winner[1]:
            winner = i
    return winner[0]   

        




if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))