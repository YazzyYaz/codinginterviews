import random


class Deck(object):
    def __init__(self, special_cards=False):
        self.cards = self.generate_cards()

    def get_cards(self):
        return self.cards

    def generate_cards(self):
        return self.__generate_cards()            
            
    def __generate_cards(self):
        suit_list = ["Clubs", "Spades", "Hearts", "Diamonds"]
        deck_of_suits = []
        for suit_type in suit_list:
            suit_set = Suit(suit_type)
            deck_of_suits += list(suit_set.get_suit())
        if special_cards:
            special_list = []
            for i in range(2):
                card = Card("None", "Joker")
                special_list.append(card)
            deck_of_suits += special_list
        return deck_of_suits
        

class Suit(object):
    def __init__(self, suit_type):
        self.suit_type = suit_type
        self.suit = self.generate_suit() 

    def get_suit(self):
        return self.suit

    def generate_suit(self):
        return self.__generate_suit()
    
    def __generate_suit(self):
        card_set = set(["Ace", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"])
        suit_set = set()
        for suit_value in card_set:
            card_value = Card(self.suit_type, suit_value)
            suit_set.add(card_value)
        return suit_set


class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_card_value(self):
        return "Card Suit: {}, Card Value: {}".format(self.suit, self.value)

special_cards = True
deck_of_cards = Deck(special_cards)
full_deck = deck_of_cards.get_cards()
card = random.choice(full_deck)
print(card.suit)
print(card.value)
