"""Tic-Tac-Toe game by Christi Johnson"""

positions = [1,2,3,4,5,6,7,8,9]
player = "o"

def main():
    draw_board()
    play_game()


def draw_board():
    global positions
    print()
    print(f"{positions[0]} | {positions[1]} | {positions[2]}")
    print("---------")
    print(f"{positions[3]} | {positions[4]} | {positions[5]}")
    print("---------")
    print(f"{positions[6]} | {positions[7]} | {positions[8]}")
    print()

def play_game():
    global player
     
    turn_count = 0
    while turn_count < 9:
        if player == "o":
            player = "x"
        else:
            player = "o"
        selection = int(input(f"Player {player}'s turn, choose an available square (1-9): "))
        positions[selection - 1] = player
        draw_board()
        turn_count += 1

        if (positions[0] == positions[1] == positions[2]  or
            positions[3] == positions[4] == positions[5]  or
            positions[6] == positions[7] == positions[8]  or
            positions[0] == positions[3] == positions[6]  or
            positions[1] == positions[4] == positions[7]  or
            positions[2] == positions[5] == positions[8]  or
            positions[0] == positions[4] == positions[8]  or
            positions[2] == positions[4] == positions[6]):
            print(f"Good game!  Player {player} is the winner!! Thanks for playing Tic-Tac-Toe.")
            turn_count = 9
        elif turn_count == 9:
            print("No winner, the game is a draw, you should play again!")

if __name__ == "__main__":  
    main()