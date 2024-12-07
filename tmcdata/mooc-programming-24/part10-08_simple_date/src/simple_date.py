# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __gt__(self, another):
        if self.year == another.year:
            if self.month == another.month:
                return self.day > another.day
            else:
                return self.month > another.month
        else:
            return self.year > another.year

    def __lt__(self, another):
        return not self.__eq__(another) and not self.__gt__(another)

    def __eq__(self, another):
        return self.year == another.year and self.month == another.month and self.day == another.day

    def __ne__(self, another):
        return not self.__eq__(another)
    
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
    def __add__(self, days):
        newday = self.day + days
        newmonth = self.month
        newyear = self.year
        if newday > 30:
            newmonth += newday // 30
            newday %= 30
            if newmonth > 12:
                newyear += newmonth // 12
                newmonth %= 12
        return SimpleDate(newday, newmonth, newyear)
        
    def __sub__(self, another):
        if self.__gt__(another):
            later = self
            earlier = another
        else:
            later = another
            earlier = self    
        days = later.day - earlier.day
        months = later.month - earlier.month
        years = later.year - earlier.year
        if days < 0:
            months -= 1
            days += 30
        if months < 0:
            years -= 1
            months += 12
        days += months * 30
        days += years * 360
        return days

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)