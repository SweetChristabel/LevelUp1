# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def __str__(self):
        if self.minutes < 10:
            min = "0" + str(self.minutes)
        else:
            min = str(self.minutes)
        if self.seconds < 10:
            sec = "0" + str(self.seconds)
        else:
            sec = str(self.seconds)
        return f"{min}:{sec}"
    
    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.minutes = 0

if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(3602):   
        print(watch)
        watch.tick()