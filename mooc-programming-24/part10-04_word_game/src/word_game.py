# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            return None
        
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels = ["a", "e", "i", "o", "u"]
        play1w = 0
        play2w = 0
        for vowel in vowels:
            play1w += player1_word.count(vowel)
            play2w += player2_word.count(vowel)
        if play1w > play2w:
            return 1
        elif play2w > play1w:
            return 2
        else:
            return None

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if self.valid(player1_word) and self.valid(player2_word):
            if player1_word == player2_word:
                return None
            if player1_word == "rock":
                if player2_word == "paper":
                    return 2
                elif player2_word == "scissors":
                    return 1
            if player1_word == "paper":
                if player2_word == "scissors":
                    return 2
                elif player2_word == "rock":
                    return 1
            if player1_word == "scissors":
                if player2_word == "rock":
                    return 2
                if player2_word == "paper":
                    return 1
        elif self.valid(player1_word):
            return 1
        elif self.valid(player2_word):
            return 2
        else:
            return None

    def valid(self, input: str):
        validinputs = ("rock", "paper", "scissors")
        return input in validinputs


if __name__ == "__main__":
    p = RockPaperScissors(4)
    p.play()