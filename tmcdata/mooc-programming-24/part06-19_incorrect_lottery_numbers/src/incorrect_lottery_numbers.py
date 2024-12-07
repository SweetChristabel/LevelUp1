# Write your solution here
def filter_incorrect():
    with open("lottery_numbers.csv") as lotterynumbers:
        hitlist = []
        for line in lotterynumbers:
            parts = line.split(";")
            weeknr = parts[0][5:]
            try:
                weeknr = int(weeknr)
                nrslist = parts[1].strip().split(",")
                if len(nrslist) != 7:
                    raise ValueError
                unique = []
                for nr in nrslist:
                    nr = int(nr)
                    if nr < 1 or nr > 39:
                        raise ValueError
                    if nr not in unique:
                        unique.append(nr)
                if len(unique) != len(nrslist):
                    raise ValueError
            except ValueError:
                continue
            hitlist.append(line)
    
    with open("correct_numbers.csv","w") as correctlines:
        for line in hitlist:
            correctlines.write(line)

if __name__ == "__main__":
    filter_incorrect()