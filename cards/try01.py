#!/user/bin/env python3
#Creates a deck of cards and returns two random cards to the screen
#import random package
import random

#Card design
print("Lets play some cards")
card_draw = ["A", "K", "Q", "J", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
card_symbol = ["Heart", "Diamond", "Club", "Spade"]

#Random draw 1
random_draw1 = random.choice(card_draw)
random_symbol1 = random.choice(card_symbol)

#Random draw 2
random_draw2 = random.choice(card_draw)
random_symbol2 = random.choice(card_symbol)

#Random cards 1 & 2
random_card1 = random_draw1,random_symbol1
random_card2 = random_draw2,random_symbol2

#Print two random cards
print(random_card1)
print(random_card2)
