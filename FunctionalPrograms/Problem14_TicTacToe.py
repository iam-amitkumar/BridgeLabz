""" This TIC-TAC-TOE is same as classic TIC-TAC-TOE game
(in this case game will run on console)in which two players
plays the game and the player wins whose symbol makes co-linear
on the game-board but in this game second player(opponent)
will be computer.
@author Amit Kumar
@version 1.0
@since 01/01/2019
"""
# importing important modules
import random

global player, p_rows, p_columns, player_name

print("TIC TAC TOE GAME\n-----------------\n")
try:
    player = int(input("Choose your number to play (2 - 9): "))
    player_name = input("Please enter your name: ")
except Exception as e:
    print(e)

print("Computer's number = 1\nYour number = ", player)
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


# function to print game-board after each move of each player
def print_board():
    count = 0
    print("     0  1  2")  # print columns head
    for i in board:
        print(" ", count, i)  # print rows head and lists of list
        count += 1
    print()


print_board()
count_turn = 0  # game will considered as draw if count will reach 9 and none of players win
turn = False  # to give chance to each player alternatively(True for computer and False for human)
while count_turn != 9:
    if turn:  # Computer's turn because it's True
        rows = random.randint(0, 2)  # generating random number to determine row number for computer's turn
        columns = random.randint(0, 2)  # generating random number to determine column number for computer's turn
        if board[rows][columns] == 0:  # checking whether randomly chosen cell is already occupied or not
            print("Computer played: \n-----------------")
            board[rows][columns] = 1  # assigning computer's symbol to the chosen unoccupied cell
            print()
            print_board()  # printing board after symbol assignment
            count_turn += 1  # incrementing the value to count the number of turns played by both players
            turn = False  # assigning False to give the chance to other player next time
        if((board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1) or  # checking whether computer won or not
                (board[1][0] == 1 and board[1][1] == 1 and board[1][2] == 1) or  # for each combination
                (board[2][0] == 1 and board[2][1] == 1 and board[2][2] == 1) or
                (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1) or
                (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1) or
                (board[0][0] == 1 and board[0][1] == 1 and board[0][2] == 1) or
                (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1) or
                (board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1) or
                (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1)):
            print(">>> Oops!!! Computer Wins and You Lost <<<")
            break
    if turn is False and count_turn <= 8:  # Player's turn because it's False
        try:
            p_rows = int(input("Enter the row number (0-2): "))
            p_columns = int(input("Enter the column number (0-2): "))
        except Exception as e:
            print(e)

        if board[p_rows][p_columns] == 0:  # checking whether cell chosen by player is already occupied or not
            print(" ", player_name, " played: \n----------------")
            board[p_rows][p_columns] = player  # assigning player's symbol to the chosen unoccupied cell
            print()
            print_board()  # printing board after symbol assignment
            count_turn += 1  # incrementing the value to count the number of turns played by both players
            turn = True  # assigning True to give the chance to computer next time
        if((board[0][0] == player and board[0][1] == player and board[0][2] == player) or  # checking whether computer
                (board[1][0] == player and board[1][1] == player and board[1][2] == player) or  # won or not for each
                (board[2][0] == player and board[2][1] == player and board[2][2] == player) or  # combination
                (board[0][0] == player and board[1][0] == player and board[2][0] == player) or
                (board[0][1] == player and board[1][1] == player and board[2][1] == player) or
                (board[0][0] == player and board[0][1] == player and board[0][2] == player) or
                (board[0][2] == player and board[1][2] == player and board[2][2] == player) or
                (board[0][2] == player and board[1][1] == player and board[2][0] == player) or
                (board[0][0] == player and board[1][1] == player and board[2][2] == player)):
            print(">>> Congrats!!! You won the game <<<")
            exit()


if count_turn == 9:  # declaring game as Draw if the number of turns become 9, i.e., all the cells of
    # board occupied but no one wins the game
    print(">>> No one won <<<\n>>> !!!Game Draw!!! <<<")
