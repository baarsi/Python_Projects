import random

# Initialize card suits and ranks for deck creation
suits = ["♥", "♦", "♣", "♠"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = []

# Function to create a deck of cards and shuffle it
def create_deck():
    for suit in suits:
        for rank in ranks:
            deck.append((suit, rank))
    
    random.shuffle(deck)  # Shuffle the deck
    return deck

# Function to draw a specific number of cards from the deck
def draw_card(deck, card_n):
    hand = []
    for i in range(card_n):
        if deck:
            hand.append(deck.pop())  # Remove and return cards
    return hand, deck

# Function to display a card in a stylized way
def show_card(card):
    space = " "
    if len(card[1]) == 2:  # Adjust spacing for two-digit ranks
        space = ""
    print (f"""
+-------+
|{card[1]}     {space}|
|       |
|   {card[0]}   |
|       |
|{space}     {card[1]}|
+-------+
""")

# Start the card drawing game
deck = create_deck()

while len(deck) > 0:
    num_cards = int(input("How many cards do you want to draw? "))
    hand, deck = draw_card(deck, num_cards)
    for card in hand:
        show_card(card)

print("We are out of cards")
