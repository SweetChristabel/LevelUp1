# Write your solution here
def everything_reversed(my_list: list):
    tsil_ym = []
    i = len(my_list) - 1
    while i >= 0:
        word = my_list[i]
        drow = word[::-1]
        tsil_ym.append(drow)
        i -= 1
    return tsil_ym



if __name__ == "__main__":
    listicle = ["Simona", "Daniel", "Tor", "Kjell"]
    print(everything_reversed(listicle))
    