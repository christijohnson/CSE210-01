"""Tic-Tac-Toe game by Christi Johnson"""

positions = [1,2,3,4,5,6,7,8,9]
player = "o"

def main():
    draw_board()
    play_game()


def draw_board():
    global positions
    print(f"{positions[0]} | {positions[1]} | {positions[2]}")
    print("---------")
    print(f"{positions[3]} | {positions[4]} | {positions[5]}")
    print("---------")
    print(f"{positions[6]} | {positions[7]} | {positions[8]}")

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

if __name__ == "__main__":  
    main()