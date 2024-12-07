# Write your solution here
def who_won(game_board: list):
    player1 = 0
    player2 = 0
    for row in game_board:
        player1 += row.count(1)
        player2 += row.count(2)
    
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0

if __name__ == "__main__":
    game_board = [[1, 2, 1, 0, 2],[2, 1, 0, 0, 2], [1, 0, 1, 2, 2], [2, 0, 1, 2, 1], [1, 1, 0, 2, 2]]
    print(who_won(game_board))