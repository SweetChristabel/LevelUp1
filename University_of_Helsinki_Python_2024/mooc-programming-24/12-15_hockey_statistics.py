# Write your solution here
import json
import heapq
class FileHandler():
    def __init__(self, filename):
        self.__filename = filename
    
    def load_file(self):
        with open(self.__filename) as file:
            stats = json.loads(file.read())
        return stats


class HockeyStats():
    def __init__(self):
        self.__stats = []

    def fetch_stats(self, filename):
        self.__stats = FileHandler(filename).load_file()

    def amountofplayers(self):
        return len(self.__stats)

    def getscore(self, player):
        return player["goals"]+player["assists"]
    
    def getgoals(self, player):
        return player["goals"]
    
    def getgames(self, player):
        return player["games"]

    def search(self, searchterm):
        for i in self.__stats:
            if i["name"] == searchterm:
                return i
        return None
            
    def sumteams(self):
        return sorted(set([i["team"] for i in self.__stats]))
        
    def sumcountries(self):
        return sorted(set([i["nationality"] for i in self.__stats]))
    
    def teamlist(self, team):
        return sorted(filter(lambda i: i["team"] == team, self.__stats), key= self.getscore, reverse= True)
    
    def countrylist(self, country):
        return sorted(filter(lambda i: i["nationality"] == country, self.__stats), key= self.getscore, reverse= True)

    def printplayer(self, player):
        return f"{player["name"]:21}{player["team"]}{player["goals"]:4} + {player["assists"]:2} = {self.getscore(player):3}"
    
#    def listbypoints(self, n):
#        iter = 0
#        while iter < n:
#            yield sorted(self.__stats, key = self.getscore, reverse = True)[iter]
#            iter += 1
#LET ME TRY SOMETHING NEW HERE
    def listbypoints(self, n):
        return heapq.nlargest(n, self.__stats, key=lambda player: (self.getscore(player), self.getgoals(player)))
    
    def listbygoals(self, n):
        return heapq.nlargest(n, self.__stats, key=lambda player: (self.getgoals(player), -self.getgames(player)))

#NOTICE THE MINUS IN FRONT OF GETGAMES. THAT'S FOR REVERSE SORTING. FUCKING GENIUS SHIT I TELL YA

    def __str__(self):
        return str(self.__stats)
    


class HockeyStatApplication():
    def __init__(self):
        self.__hockeystats = HockeyStats()

    def help(self):
        print("""
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals
        """)

    def execute(self):
        filename = input("file name:")
        self.__hockeystats.fetch_stats(filename)
        print(f"read the data of {self.__hockeystats.amountofplayers()} players")
        self.help()
        while True:
            command = int(input("command: "))
            if command == 0:
                break
            if command == 1:
                hit = self.__hockeystats.search(input("name: "))
                if hit == None:
                    print("Player not found")
                else:
                    print(self.__hockeystats.printplayer(hit))
            if command == 2:
                for i in self.__hockeystats.sumteams():
                    print(i)
            if command == 3:
                for i in self.__hockeystats.sumcountries():
                    print(i)
            if command == 4:
                hit = self.__hockeystats.teamlist(input("team: "))
                for i in hit:
                    print(self.__hockeystats.printplayer(i))
            if command == 5:
                hit = self.__hockeystats.countrylist(input("country: "))
                for i in hit:
                    print(self.__hockeystats.printplayer(i))
            if command == 6:
                for i in self.__hockeystats.listbypoints(int(input("how many: "))):
                    print(self.__hockeystats.printplayer(i))
            
            if command == 7:
                for i in self.__hockeystats.listbygoals(int(input("how many: "))):
                    print(self.__hockeystats.printplayer(i))


app = HockeyStatApplication()
app.execute()

