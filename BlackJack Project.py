import random

suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2 ,'Three':3, 'Four':4, 'Five':5,'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

play=True

class Card:

    def __init__(self,suit,rank):
        #Creates objects for suit and ranks
        self.suit=suit
        self.rank=rank

    def __str__(self):
        #Example display 2 of hearts
        # 2=ranks   hearts=suits
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):
        self.deck=[]
        # starts with hearts then
        # 2nd loops through all possible ranks for hearts
        # first loop diamonds
        # 2nd loops through all possible ranks for diamonds
        # does this for Spades and clubs
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' +card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card= self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0

    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=='Ace':
            self.aces+=1

    def adjust_ace(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1

class Chips:

    def __init__(self):
        self.total=25
        self.bet=0

    def win_bet(self):
        self.total+=self.bet

    def lose_bet(self):
        self.total-=self.bet

def take_bet(chips):

    while True:
        try:
            chips.bet=int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a must be an integer!')
        else:
            if chips.bet>chips.total and chips.bet<chips.total:
                 print("Sorry, your bet is invalid")
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_ace()

def hit_or_stand(deck,hand):
    global play

    while True:
        x=input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower()=='h':
            hit(deck,hand)

        elif x[0].lower()=='s':
            print("Player stands. Dealer is playing.")
            play=False
        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n')
    print("Player's Hand =",player.value)

def player_bust(player,dealer,chips):
    print("Player busts!")

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie!d")


# Now for the game step

def main():
    play=True
    while True:
        print("Welcome to BlackJack! Try to get as close to 21 as possible without going over!\n\ Dealer will hit until they reach 17.")

        deck=Deck()
        deck.shuffle()

        # shuffle the deck, deal two cards to player
        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand=Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        player_chips=Chips()

        take_bet(player_chips)

        show_some(player_hand,dealer_hand)


        while play:
            hit_or_stand(deck,player_hand)

            #shows dealers card wile keeping  the 2nd hidden
            show_some(player_hand,dealer_hand)

            if player_hand.value > 21:
                player_bust(player_hand,dealer_hand,player_chips)
                break

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)

            show_all(player_hand,dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)

            else:
                push(player_hand,dealer_hand)


        print("\n Player's winnings stand at",player_chips.total)

        new_game = input("Would you like to play again? Enter 'y' or 'n' ")

        if new_game[0].lower() == 'y':
            play=True
            continue
        else:
            print("Thanks for playing!")
            break
main()