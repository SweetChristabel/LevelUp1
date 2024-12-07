# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []

    def add(self, person: Person):
        self.people.append(person)
    
    def is_empty(self):
        return self.people == []
    
    def print_contents(self):
        #see if this can be done without doing the same for loop twice
        totalheight = 0
        for person in self.people:
            totalheight += person.height
        print(f"There are {len(self.people)} persons in the room, and their combined height is {totalheight} cm")
        for person in self.people:
            print (f"{person.name} ({person.height} cm)")
        
    def shortest(self):
        if len(self.people) is not 0:
            shortest = self.people[0].height
            for person in self.people:
                if person.height <= shortest:
                    shortest = person.height
                    winner = person
            return winner
        return None
    
    def remove_shortest(self):
        if len(self.people) is not 0:    
            shortest = self.people.index(self.shortest())
            return self.people.pop(shortest)
        return None

            



if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()