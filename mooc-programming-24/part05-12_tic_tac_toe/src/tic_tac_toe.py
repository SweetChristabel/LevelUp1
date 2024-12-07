# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    acceptableinputs = [0, 1, 2]
    if x in acceptableinputs and y in acceptableinputs:
        if game_board[y][x] == "":
            game_board[y][x] = piece
            return True
        else:
            return False    
    else:
        return False



if __name__ == "__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)