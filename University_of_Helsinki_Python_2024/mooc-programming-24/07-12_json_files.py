# Write your solution here
def print_persons(filename:str ):
    import json
    with open(filename) as file:
        data = file.read()
        people = json.loads(data)
    for person in people:
        hobbystr = "("
        for hobby in person['hobbies']:
            hobbystr += hobby+", "
        if len(hobbystr)>1:
            hobbystr = hobbystr [:-2]+")"
        else:
            hobbystr += ")"
        print(f"{person['name']} {person['age']} years {hobbystr}")


if __name__ == "__main__":
    print_persons("file1.json")