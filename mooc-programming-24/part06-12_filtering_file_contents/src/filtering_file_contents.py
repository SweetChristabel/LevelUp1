#Write your solution here
def filter_solutions():
    solutionsprocessed = []
    with open("solutions.csv") as ogsolutions:
        for line in ogsolutions:
            solutions = line.split(";")
            calc = solutions[1]
            if "+" in calc:
                i = calc.index("+")
                solutions[1] = int(calc[:i]), int(calc[i:])

            if "-" in calc:
                i = calc.index("-")
                solutions[1] = int(calc[:i]), int(calc[i:])

            solutions[2] = int(solutions[2].strip())
            solutionsprocessed.append(solutions)
    open("correct.csv", 'w').close()
    open("incorrect.csv", 'w').close()
    for i in solutionsprocessed:
        sol = sum(i[1])
        if i[1][1] > 0:
            i[1] = f"{i[1][0]}+{i[1][1]}"
        else:
            i[1] = f"{i[1][0]}{i[1][1]}"

        if sol == i[2]:
            with open("correct.csv", "a") as correctfile:
                correctfile.write(f"{i[0]};{str(i[1])};{i[2]}\n")
        else:
            with open("incorrect.csv", "a") as incorrectfile:
                incorrectfile.write(f"{i[0]};{str(i[1])};{i[2]}\n")
            



if __name__ == "__main__":                                
    filter_solutions()