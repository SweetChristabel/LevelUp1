# Write your solution here
def controlchar(identifier: int):
    chars = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    i = identifier % 31
    return chars[i]


def is_it_valid(pic: str):
    if len(pic) != 11:
        return False    
    from datetime import datetime
    date = pic[:6]
    day = int(date[:2].strip("0"))
    month = int(date[2:4].strip("0"))
    if pic[6] == "+":
        year = "18"
    elif pic[6] == "-":
        year = "19"
    elif pic[6] == "A":
        year = "20"
    else:
        return False
    year += date[4:]
    year = int(year)
    try:
        datetime(year, month, day)
        identifier = int(date+pic[7:10])
    
    except:
        return False

    if pic[-1] != controlchar(identifier):
        return False
    return True





if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))
                      