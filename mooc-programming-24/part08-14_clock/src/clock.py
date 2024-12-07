# Write your solution here:
# Write your solution here:
class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def __str__(self):
        if self.minutes < 10:
            min = "0" + str(self.minutes)
        else:
            min = str(self.minutes)
        if self.seconds < 10:
            sec = "0" + str(self.seconds)
        else:
            sec = str(self.seconds)
        if self.hours < 10:
            hr = "0" + str(self.hours)
        else:
            hr = str(self.hours)
        return f"{hr}:{min}:{sec}"
    
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0
        if self.hours == 24:
            self.hours = 0
            self.minutes = 0
            self.seconds = 0

    def set(self, hours: int, minutes: int):
        self.seconds = 0
        self.minutes = minutes
        self.hours = hours

if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)