"""This program is to initialize deck of cards having suit ("Clubs",
"Diamonds", "Hearts", "Spades") & Rank ("2", "3", "4", "5", "6", "7",
"8", "9", "10", "Jack", "Queen", "King", "Ace"). Shuffle the cards
using Random method and then distribute 9 Cards to 4 Players and Print
the Cards the received by the 4 Players using 2D Array...

@author Amit Kumar
@version 1.0
@since 15/01/2019
"""
# importing important modules
import itertools
import random

# declaring card deck with the values of cards
carddeck = list(itertools.product(["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"],
                                  ["Clubs", "Diamonds", "Hearts", "Spades"]))

random.shuffle(carddeck)  # shuffling the cards of deck present in 'carddeck' in the form of 2D array


# this function choose an element of first sub-list and an element from second sub-list of 'carddeck' list having
# @param number of cards you want to distribute to first player
def player1(n):
    print("Player 1 gets:-\n")
    for i in range(n):
        print(carddeck[i][0], carddeck[i][1])  # printing an element from 1st sub-list and an element from 2nd sub-list
        carddeck.remove(carddeck[i])  # deleting the selected card from the list to avoid the repetition of card


# this function choose an element of first sub-list and an element from second sub-list of 'carddeck' list having
# @param number of cards you want to distribute to second player
def player2(n):
    print("\nPlayer 2 gets:-\n")
    for j in range(n):
        print(carddeck[j][0], carddeck[j][1])  # printing an element from 1st sub-list and an element from 2nd sub-list
        carddeck.remove(carddeck[j])  # deleting the selected card from the list to avoid the repetition of card


# this function choose an element of first sub-list and an element from second sub-list of 'carddeck' list having
# @param number of cards you want to distribute to third player
def player3(n):
    print("\nPlayer 3 gets:-\n")
    for k in range(n):
        print(carddeck[k][0], carddeck[k][1])  # printing an element from 1st sub-list and an element from 2nd sub-list
        carddeck.remove(carddeck[k])  # deleting the selected card from the list to avoid the repetition of card


# this function choose an element of first sub-list and an element from second sub-list of 'carddeck' list having
# @param number of cards you want to distribute to fourth player
def player4(n):
    print("\nPlayer 4 gets:-\n")
    for l in range(n):
        print(carddeck[l][0], carddeck[l][1])  # printing an element from 1st sub-list and an element from 2nd sub-list
        carddeck.remove(carddeck[l])  # deleting the selected card from the list to avoid the repetition of card


# from this python file only program will compile not from the imported file(s)
if __name__ == '__main__':
    # calling all the function to to distribute the cards randomly
    player1(9)
    player2(9)
    player3(9)
    player4(9)
