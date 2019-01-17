"""This program is the extension of Problem 9 having ability to Sort by
Rank and maintain the cards in a Queue implemented using Linked List.

@author Amit Kumar
@version 1.0
@since 16/01/2019
"""
# importing important modules
import re
import random
from utility.Utility import *


class DeckOfCards:

    def __init__(self):
        pass

    def shuffle(self):
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        Rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        list_cards = []
        card_suits = ''

        while len(list_cards) < 36:
            for i in range(0, 9):

                cards_rank = ''

                random_no = random.randint(1, 13)

                cards_rank = Rank[random_no - 1]

                random_no_suits = random.randint(0, 3)
                cards_rank = cards_rank + ' ' + suits[random_no_suits]

                if list_cards.__contains__(cards_rank) is False:

                    if len(list_cards) is not 36:
                        list_cards.append(cards_rank)

        row = 4
        column = 9
        two_d_array = [[0 for j in range(column)] for i in range(row)]
        index = 0
        for i in range(row):

            for j in range(column):
                two_d_array[i][j] = list_cards[index]
                index += 1

        return list_cards, two_d_array


card = DeckOfCards()
card.shuffle()


class Player:

    def __init__(self, list_cards, utility_obj, queue):
        self.list_cards = list_cards
        self.utility_obj = utility_obj
        self.queue = queue

    def replacing(self):
        i = 0
        while i < len(self.list_cards):

            if bool(re.search('Ace', self.list_cards[i])):
                self.list_cards[i] = re.sub('Ace', '14', self.list_cards[i], 1)

            if bool(re.search('Jack', self.list_cards[i])):
                self.list_cards[i] = re.sub('Jack', '11', self.list_cards[i], 1)

            if bool(re.search('Queen', self.list_cards[i])):
                self.list_cards[i] = re.sub('Queen', '12', self.list_cards[i], 1)

            if bool(re.search('King', self.list_cards[i])):
                self.list_cards[i] = re.sub('King', '13', self.list_cards[i], 1)

            i += 1

        ranks = []
        number = []
        i = 0
        while i < len(self.list_cards):
            ranks.append(self.list_cards[i].split(" "))

            number.append(int(ranks[i][0]))
            i += 1

        number = bubble_sort(number)
        i = 0
        sorted_card = []
        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

        while i < 36:

            string = ''
            random_no = random.randint(0, 3)
            string = suits[random_no]
            string = str(number[i]) + " " + string

            while sorted_card.__contains__(string) is True:
                random_no = random.randint(0, 3)
                string = suits[random_no]
                string = str(number[i]) + ' ' + string

            if sorted_card.__contains__(string) is False:
                sorted_card.append(string)

            i += 1

            i = 0
            while i < len(sorted_card):

                if bool(re.search('14', sorted_card[i])):
                    sorted_card[i] = re.sub('14', 'Ace', sorted_card[i], 1)

                if bool(re.search('11', sorted_card[i])):
                    sorted_card[i] = re.sub('11', 'Jack', sorted_card[i], 1)

                if bool(re.search('12', sorted_card[i])):
                    sorted_card[i] = re.sub('12', 'Queen', sorted_card[i], 1)

                if bool(re.search('13', sorted_card[i])):
                    sorted_card[i] = re.sub('13', 'King', sorted_card[i], 1)

                i += 1

        player_objs = []
        limit = 0
        index = 9
        for i in range(0, 4):
            # player_objs.append(Player(card.shuffle(), Utility(), Queue()))

            for sorted_cards in sorted_card:
                if limit < index:
                    player_objs[i].queue.enqueue(sorted_card[limit])

                    limit += 1
            index += 9

        for i in range(0, 4):
            print('Player', i + 1, '\n', '----------')
            print(player_objs[i].queue.show())
            print('\n')


d1 = DeckOfCards()
