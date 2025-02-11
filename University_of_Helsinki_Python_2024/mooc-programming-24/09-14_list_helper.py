# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def uniques(cls, my_list: list):
        uniques = []
        for i in my_list:
            if i not in uniques:
                uniques.append(i)
        return uniques


    @classmethod
    def greatest_frequency(cls, my_list: list):
        uniques = cls.uniques(my_list)
        winfreq = 0
        for i in uniques:
            if winfreq < my_list.count(i):
                winner = i
                winfreq = my_list.count(i)
        return winner

    @classmethod
    def doubles(cls, my_list: list):
        uniques = cls.uniques(my_list)
        losers = []
        for i in uniques:
            if my_list.count(i) < 2:
                losers.append(i)
        for i in losers:
            uniques.remove(i)
        print(uniques)
        return len(uniques)
    

if __name__ == "__main__":
    numbers = [3, 2, 3, 2, 2, 3, 1, 2, 4, 5, 5, 6]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))