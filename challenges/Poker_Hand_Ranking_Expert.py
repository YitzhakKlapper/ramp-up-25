
# added functinality in the input to accept cards. as opposed to just taking a list
def consecutive(deck):
    # deck is a list of tuples: [(number, suit), ...]
    values = [num for num, suit in deck]
    values.sort()
    return all(values[i] + 1 == values[i+1] for i in range(len(values)-1))

def Straight(deck):
    numbers = [num for num, suit in deck]
    return all(numbers[i] + 1 == numbers[i+1] for i in range(len(numbers) - 1))

def flush(deck):
    suits = [suit for num, suit in deck]
    return len(set(suits)) == 1

def amount(deck):
    a = []
    values = [num for num, suit in deck]
    deckSet = set(values)
    for card in deckSet:
        a.append(int(values.count(card)))
    if a.count(2) == 1 and a.count(3) == 1:
        return "Full House"
    elif a.count(2) == 1:
        return "Pair"
    elif a.count(3) == 1:
        return "Three of a Kind"
    elif a.count(4) == 1:
        return "Four of a Kind"
    elif a.count(2) == 2:
        return "Two Pair"
    else:
        return False
        
def deckSort(deck):
    face_map = {'K': 13, 'Q': 12, 'J': 11, 'A': 14}

    sortedDeck = [(int(card[:-1]) if card[:-1].isdigit() else face_map[card[:-1]], card[-1]) for card in deck]
    return sorted(sortedDeck, key=lambda x: (x[0], x[1]))

def getCards():
    deck = []
    for i in range(5):
        print("Enter card", i + 1, "(e.g., 'Kh' for King of hearts):")
        card = input().upper().strip()
        deck.append(card)
    return deckSort(deck)

def getHandType(deck):
    if Straight(deck) and flush(deck):
        values = [num for num, suit in deck]
        values.sort()
        if values == [10, 11, 12, 13, 14]:
            return("Royal Flush")
        else:
            return("Straight Flush")
    elif amount(deck) == "Four of a Kind":
        return("Four of a Kind")
    elif amount(deck) == "Full House":
        return("Full House")
    elif flush(deck):
        return("Flush")
    elif Straight(deck):
        return("Straight")
    elif amount(deck) == "Three of a Kind":
        return("Three of a Kind")
    elif amount(deck) == "Two Pair":
        return("Two Pair")
    elif amount(deck) == "Pair":
        return("Pair")
    else:
        return("High Card")
def main():
    deck = getCards()
    print("Your hand:", deck)
    hand_type = getHandType(deck)
    print()
    print("Hand type:", hand_type)


    
    
if __name__ == "__main__":
    main()      