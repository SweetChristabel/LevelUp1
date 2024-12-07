# Write your solution here
def fractionate(amount: int):
    from fractions import Fraction
    frac = []
    for i in range(amount):
        frac.append(Fraction(1, amount))
    return frac



if __name__ == "__main__":
    print(fractionate(5))
    for p in fractionate(3):
        print(p)
