# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if self.__cents < 10:
            return f"{self.__euros}.0{self.__cents} eur"
        return f"{self.__euros}.{self.__cents} eur"

    def __eq__(self, another):
        return self.__euros == another.__euros and self.__cents == another.__cents
    
    def __gt__(self, another):
        if self.__euros == another.__euros:
            return self.__cents > another.__cents
        else:
            return self.__euros > another.__euros

    def __lt__(self, another):
        if self.__euros == another.__euros:
            return self.__cents < another.__cents
        else:
            return self.__euros < another.__euros

    def __ne__(self, another):
        return not self.__eq__(another)
    
    def __add__(self, another):
        euros = self.__euros + another.__euros
        if self.__cents + another.__cents >= 100:
            euros += 1
            cents = self.__cents + another.__cents - 100
        else:
            cents = self.__cents + another.__cents
        return Money(euros, cents)

    def __sub__(self, another):
        if self.__lt__(another):
            raise ValueError("a negative result is not allowed")
        else:
            euros = self.__euros - another.__euros
            if self.__cents < another.__cents:
                euros -= 1
                cents = self.__cents + 100 - another.__cents
            else:
                cents = self.__cents - another.__cents
        return Money(euros, cents)



if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1