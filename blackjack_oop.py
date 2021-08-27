import random
import pygame 

#  CONSTANTS
SUITS = {"S":"\u2664", "H":"\u2661", "C": "\u2667", "D": "\u2662"}
RANKS = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

BLACK = (0,0,0)
WHITE = (255, 255, 255)
# Card
class Card:
    def __init__(self, rank, suit):
        #  Member variables
        self.rank = rank
        self.suit = suit

    def print(self):
        print(self.rank + ' ' + self.suit)

    def display(self, x, y):
        pass


# Deck
class Deck:
    def __init__(self):
        # member variable 
        self.cards = [Card(value, suit) for value in RANKS for suit in SUITS]

    def print(self):
        for card in self.cards:
            card.print()

    def deal(self):
        random.shuffle(self.cards)
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self._value = 0
        self.card_images = []

    def add_card(self, card):
        self.cards += [card]
        self._value += RANKS[card.rank]
        self.card_images += ['img/' + card.rank + card.suit + '.png']

    def print(self):
        for card in self.cards:
            card.print()

    def print_paths(self):
        for card in self.card_images:
            print(card)

    def display(self, canvas, position):
        x, y = position
        for card in self.card_images:
            img = pygame.image.load(card).convert()
            canvas.blit(img, (x, y))
            x += 50
    
    def _val(self):
        return self._value
    # by making it a property, we don't allow other classes to change it. we 'protect' it
    value = property(_val)

    # a print method that doesnt print the last card, to use for the CPU

    # value
    # return sum of the values of all the cards in the hand

# player and cpu classes, that inherit from Hand
class Player(Hand):
    def __init__(self):
        super().__init__() 


class Dealer(Hand):
    def __init__(self):
        super().__init__()

    def print(self):
        for i in range(len(self.cards)):
            if i != 0:
                print('\u2753')
            else:
                self.cards[i].print()

    def display(self, canvas, position):
        x, y = position

        #  first card, show card
        card = 'img/' + self.cards[0].rank + self.cards[0].suit + '.png'

        img = pygame.image.load(card).convert()
        canvas.blit(img, (x, y))
        x += 50
        # rest of our cards, show the back
        for _ in self.card_images[1:]:
            card = 'img/back.png'
            img = pygame.image.load(card).convert()
            canvas.blit(img, (x, y))
            x += 50


# Game
class Game:
    # Write an init function
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.state = False
        self.cpu_state = False
    
    # deal 2 cards each
    def deal(self):
        for _ in range(2):
            self.player.add_card(self.deck.deal())
            self.dealer.add_card(self.deck.deal()) 
        
        

    # print_current_hands -> use the methods we have for printing the hands to print the current state of the game
    def print(self):
        print('Player cards: ')
        self.player.print() 

        print('Dealer cards: ')
        self.dealer.print()

    #  a function to decide who wins
    def check_blackjack(self):
      if self.player.value == 21 and self.dealer.value == 21:
        print('Tie.')
      if self.player.value == 21:
        print('Blackjack! You win!')
      if self.dealer.value == 21:
         print('You lost.')
      if self.player.value > 21:
         print('You lost.')
      if self.dealer.value > 21:
         print('You win!')
    
    def play(self):
      
      s_or_m = input('Type "s" to stand or type "m" to move.')
      if s_or_m == 'm':
        self.player.add_card(self.deck.deal())
      
      self.dealer.add_card(self.deck.deal())
    
    def hit(self):
        self.player.add_card(self.deck.deal())
            
    

# Define a class 'Button'
class Button:
    # needs to show some text
    # needs to do something when we click it
    # where to show it (surface + x, y coordinates, position)
    # how big (dimensions) 

# '0', False, None, '' -> we call them 'falsey' values

    def __init__(self, text, position, dimensions, action=None):
        # For setting the text
        self.font = pygame.font.SysFont('Courier', 25, True, False)
        self.text = self.font.render(text, True, BLACK)
        self.rect = self.text.get_rect()

        # We want this as a tuple (x, y)
        self.position = position
        self.dimensions = dimensions

        self.action = action

    def draw(self, surface):
        x, y = self.position
        w, h = self.dimensions

        self.rect.center = ((x + (w*0.5)), (y + (h*0.5))) 
        pygame.draw.rect(surface, WHITE, (x, y, w, h))
        surface.blit(self.text, self.rect)

    def isOver(self):
        x, y = self.position
        w, h = self.dimensions
        mouse = pygame.mouse.get_pos()
        if x < mouse[0] < x + w and y < mouse[1] < y + h:
            return True
        else:
            return False


#  Needs draw itself,
#  check if the mouse is over it
#  set its message

# DRY Principle
# Don't
# Repeat
# Yourself

#  Opposed to what some people WET
# Write 
# Everything
# Thrice

    #   We want to write DRY code, not WET

    # Abstraction



# game = Game()
# game.deal()
# # game.print()
# game.check_blackjack()
