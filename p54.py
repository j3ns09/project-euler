from enum import Enum

# --- Kinds ---
# Clubs : Trèfle
# Hearts : Coeur
# Spades : Pique
# Diamonds : Carreau

spe = {
    "T" : 10,
    "J" : 11,
    "Q" : 12,
    "K" : 13,
    "A" : 14
}
aliases = {
    11 : "Jack",
    12 : "Queen",
    13 : "King",
    14 : "Ace"
}

class Card:
    def __init__(self, val, kind):
        self.val = val
        self.kind = kind
        if self.val > 10:
            self.alias = aliases[self.val]
        else:
            self.alias = None

    def __eq__(self, other):
        if isinstance(other, Card): return self.val == other.val
        raise TypeError("Incorrect type for comparison")

    def __gt__(self, other):
        if isinstance(other, Card):
            return self.val > other.val

    def __lt__(self, other):
        if isinstance(other, Card): return not self.__gt__(other)


    def __repr__(self): return f"Card({self.alias if self.alias else self.val} of {self.kind})"

class Hand(Enum):
    HighCard = 1
    OnePair = 2
    TwoPairs = 3
    ThreeOfAKind = 4
    Straight = 5
    Flush = 6
    FullHouse = 7
    FourOfAKind = 8
    StraightFlush = 9
    RoyalFlush = 10

class Player:
    def __init__(self):
        self.cards : list[Card] = []

    def threeOfAKind(self):
        for i in range(2, len(self.cards)):
            if self.cards[i].val == self.cards[i-1].val + 1 == self.cards[i-2].val + 2:
                return True
        return False

    def fourOfAKind(self):
        for i in range(3, len(self.cards)):
            if self.cards[i].val == self.cards[i-1].val == self.cards[i-2].val == self.cards[i-3].val:
                return True
        return False

    def straight(self):
        count = 0
        for i in range(1, len(self.cards)):
            if self.cards[i].val == self.cards[i-1].val:
                count += 1
        return count == 5

    def _all_suit(self):
        for i in range(1, len(self.cards)):
            if self.cards[i].kind != self.cards[i-1].kind:
                return False
        return True


    def receive_cards(self, deck: list[str]):
        for i, card in enumerate(deck):
            val, kind = card
            if not val.isdigit():
                val = spe[val]
            else:
                val = int(val)

            self.cards.append(Card(val, kind))
        self.cards.sort(key=lambda x: x.val)

    def eval_hand(self):
        properties = {
            "High Card" : max(self.cards),

        }

class GameManager:
    def __init__(self, player1, player2):
        self.cards = {}
        self.player1 = player1
        self.player2 = player2

    def fetch(self):
        with open("poker.txt", 'r') as file:
            cards = file.readlines()
        for i, line in enumerate(cards):
            line = line.split()
            self.cards[i] = {1 : line[:5], 2 : line[5:]}

    def give_cards(self, turn):
        self.player1.receive_cards(self.cards[turn][1])
        self.player2.receive_cards(self.cards[turn][2])

    def play(self):
        return 1 if self.player1.eval_cards() > self.player2.eval_cards() else 2

game = GameManager(Player(), Player())
game.fetch()
game.give_cards(10)

player1 = game.player1
fullHouse = False
threeK = player1.threeOfAKind()
tPairs = False
print("Deck:", player1.cards)
print("High Card:", max(player1.cards))

dict_types = {card.val : [] for card in player1.cards}
for card in player1.cards:
    dict_types[card.val].append(card)

for val in dict_types.values():
    if len(val) == 1:
        print("One Pair:", val)
    elif len(val) == 2:
        tPairs = True
        print("Two Pair:", val)

if tPairs and threeK:
   fullHouse = True

print("Three of a Kind:", "Not a ToaK" if (not threeK) else dict_types)
print("Straight:", "Not all cards are consecutive values" if (not player1.straight()) else player1.cards)
print("Flush:", "Not all cards of same suit" if (not player1._all_suit()) else player1.cards)
print("Full House:", "Not a Full House" if (not fullHouse) else player1.cards)
print("Four of a Kind:", "Not a FoaK" if (not player1.fourOfAKind()) else dict_types)
print("Straight Flush:", "Not all cards of same suit or consecutive values" if (not player1._all_suit() or not player1.straight()) else player1.cards)
print("Royal Flush:", "Not a RF" if sum(card.val for card in player1.cards) != 10+11+12+13+14 else player1.cards)

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

# kinds = {}
# for i in range(5):
#     card = player1.cards[i]

#     try:
#         kinds[card.kind].append(card)
#     except KeyError:
#         kinds[card.kind] = [card]

# print(kinds)
