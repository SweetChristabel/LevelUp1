# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

class Suitcase:
    def __init__(self, maxweight: int):
        self.__maxweight = maxweight
        self.__totweight = 0
        self.__items = []

    def add_item(self, item: Item):
        if self.__totweight + item.weight() <= self.__maxweight:
            self.__totweight += item.weight()
            self.__items.append(item)

    def __str__(self):
        if len(self.__items) == 1:
            return f"1 item ({self.__totweight} kg)"
        return f"{len(self.__items)} items ({self.__totweight} kg)"
    
    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return self.__totweight
    
    def heaviest_item(self):
        if self.__items == []:
            return None
        else:
            heaviest = 0
            for item in self.__items:
                if item.weight() > heaviest:
                    heaviest = item.weight()
                    winner = item
            return winner

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__contents = []
        self.__contentweight = 0

    def add_suitcase(self, suitcase: Suitcase):
        if self.__contentweight + suitcase.weight() <= self.__max_weight:
            self.__contents.append(suitcase)
            self.__contentweight += suitcase.weight()

    def __str__(self):
        if len(self.__contents) == 1:
            return f"1 suitcase, space for {self.__max_weight - self.__contentweight} kg"
        return f"{len(self.__contents)} suitcases, space for {self.__max_weight - self.__contentweight} kg"

    def print_items(self):
        for suitcase in self.__contents:
                suitcase.print_items()

if __name__ == "__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()