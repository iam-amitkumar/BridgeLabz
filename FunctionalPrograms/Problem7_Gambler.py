"""Gambler program prints the Print number of Wins and percentage
of Win and Loss while playing bet. The player place $1 bet each time.
The game stop at three condition: i) when player goes broke
ii) completed the user desired no. of games iii) player won

@author Amit Kumar
@version 1.0
@since 28/12/2018
"""
# importing the important modules
import utility.Utility
import random

global stake, goal, no_of_times

print("\nEnter the value to put on stake ")
try:
    stake = utility.Utility.get_integer()  # taking value of stake from the user
except Exception as e:
    print(e)

print("\nEnter your goal you want to earn ")
try:
    goal = utility.Utility.get_integer()  # taking the value of goal from the user
except Exception as e:
    print(e)

print("\nEnter the times you want to play ")
try:
    no_of_times = utility.Utility.get_integer()  # taking the value of number of games user wants to play
except Exception as e:
    print(e)

win = 0
loss = 0
count = 0

flag = 0
while flag == 0:
    if stake > 0:  # checking whether user still have some money to play the bet further
        if stake < goal:  # checking if the user reached his/her goal or not
            if count != no_of_times:  # checking if user completed his/her number of bets he/she provided
                rand = random.random()
                count += 1  # incrementing the variable "count" to check further in loop that user is not exceeding
                # his/her desired turns of bet
                if rand <= 0.5:
                    win += 1  # incrementing the times of wins when player wins
                    stake += 1  # incrementing the stake when player wins to check if stake reach to player's goal
                else:
                    loss += 1  # incrementing the times of loss when player lost
                    stake -= 1  # # decrementing the stake when player loose to check if player still have some money
                    # to play further
            else:
                print("\n!!! Number of games completed !!!")
                break  # cursor will go out of the loop if number of games get completed
        else:
            print("\n!!! Congrats!!! You reached your goal !!!")
            break  # cursor will go out of the loop if User
    else:
        print("\n!!! You lost all the money !!!")
        break  # cursor will go out of the loop if number of games get completed

print("\nTotal wins: ", win)
win_percent = (win/(win+loss))*100
loss_percent = (loss/(win+loss))*100
print("Percentage of Wins: ", win_percent, "%")
print("Percentage of Loss: ", loss_percent, "%")
