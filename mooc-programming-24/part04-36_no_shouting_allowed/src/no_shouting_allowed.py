# Write your solution here
def no_shouting(listastrings: list):
    prunedlist = []
    for i in listastrings:
        if not i.isupper():
            prunedlist.append(i)
    return prunedlist        

if __name__ == "__main__":
    listastrings = ["whodis", "WHO DIS", "Who Dis", "who", "DIS"]
    print(no_shouting(listastrings))