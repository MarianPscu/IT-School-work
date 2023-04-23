from typing import Self
import random

s1 = "♠"
s2 = "♥"
s3 = "♦"
s4 = "♣"

CARD_SYMBOLS = ["♠", "♥","♦","♣" ]

CARD_VALUE_MAP = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "A": 11,
    "J": 12,
    "Q": 13,
    "K": 14
    
}



class Card:

    def __init__(self, number: int, symbol: str) -> None:
        if number not in CARD_VALUE_MAP:
            raise ValueError("Invalid card number.")

        if symbol not in CARD_SYMBOLS:
            raise ValueError("Invalid card symbol.")

        self.__symbol = symbol
        self.__number = number

    def __str__(self) -> str:
        # trebuie sa returneze string
        return f"<Card {self.__number}{self.__symbol}>"

    def __repr__(self) -> str:
        return self.__str__()

    def get_number(self) -> int:
        return CARD_VALUE_MAP[self.__number]

    def get_symbol(self):
        return self.__symbol

    def __eq__(self, other):
        # operator overloading
        # returneaza boolean
        # if self.number == other.number:
        #   return False
        return self.__number == other.get_number()

    def __lt__(self, other):
        return self.get_number() < other.get_number()

    def __le__(self, other):
        return self.get_number() <= other.get_number()

    def __gt__(self, other):
        return self.get_number() > other.get_number()

    def __ge__(self, other):
        return self.get_number() >= other.get_number()

    def __add__(self, other: Self) -> int:
        return self.get_number() + other.get_number()
    
    def __radd__(self, other: int):
        return other + self.get_number()

class Deck:
    """
    When calling len() on this you will get the number of cards remained in deck.
    """

    def __init__(self) -> None:
        self.__cards = []
        for symbol in CARD_SYMBOLS:
            for number in CARD_VALUE_MAP:
                self.__cards.append(Card(number, symbol))

    def __len__(self):
        # trebuie sa returneze int sau float
        return len(self.__cards)

    def get_cards(self, n):

        """Returns n cards"""

        empty_bin = []

        if n > len(self.__cards):
            raise ValueError("There are not enough cards in the deck")

        for i in range(n):
            empty_bin.append(self.__cards.pop())

        return empty_bin

        #return self.__cards.pop()

    def shuffle(self):
        random.shuffle(self.__cards)

    def run_game(self):
        player_hand = self.get_cards(2)
        dealer_hand = self.get_cards(2)
        while True:
            
            

            if sum(player_hand) == 21:
                print("You win!")
                break

            elif sum(player_hand) < 21:
                try:
                    while sum(player_hand) < 21:
                        print(f" Valoarea mainii tale este {sum(player_hand)}")
                        response = str(input("Do you want another card?"))
                        if response not in ["yes", "no"]:
                            raise ValueError("You must only use yes or no answers")
                        if response == "yes":
                            player_hand = player_hand + self.get_cards(1)
                        else:
                            if sum(player_hand) > sum(dealer_hand):
                                print(f"You win {sum(player_hand)}")
                                break
                            elif sum(player_hand) == sum(dealer_hand):
                                print(f"Draw! {sum(player_hand)}")
                                break
                            else:
                                print(f"You lose {sum(player_hand)}" )
                                break
                except ValueError:
                    print("You must respond with yes or no")
                    response = str(input("Do you want another card?"))

                break

            else:
                print("You lose")
                break

d1 = Deck()

c1 = Card("2", CARD_SYMBOLS[0])
c2 = Card("3", CARD_SYMBOLS[1])

#print(c1 == c2)
# c1.__eq__(c2)

# print(f"Exception happened for object: {c1}")
#print(f"Carti in pachet: {len(d1)}")

#print(d1.get_cards(5))

#print(f"Carti in pachet: {len(d1)}")
# print(c1.__str__())

# c1_str = str(c1)
# c1_str = c1.__str__()

#c = c1 + c2
# c1.__add__(c2)
d1.shuffle()
d1.run_game()
