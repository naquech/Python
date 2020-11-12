VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'


import random


# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self, init_name):
        self.name = init_name
        self.prizeMoney = 0
        self.prizes = []

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self):
        return '{} (${})'.format(self.name, self.prizeMoney)


# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):

    """
    Asks the user to enter a move and return whatever string was entered.
    The user can enter 'exit' to exit the game, 'pass' to skip their turn,
    a single character to guess that letter, or a complete phrase (a
    multi-character phrase other than 'exit' or 'pas') to guess that phrase.
    """
    def getMove(self, category, obscuredPhrase, guessed):
        print('{} has ${}'.format(self.name, self.prizeMoney))
        print('Category: ', category)
        print('Phrase: ', obscuredPhrase)
        print('Guessed: ', guessed)

        user_input = input("Guess a letter, phrase, or type 'exit' or 'pass':")
        return user_input


# Write the WOFComputerPlayer class definition (part C) here
class WOFComputerPlayer(WOFPlayer):

    #a list of English characters sorted from least frequent
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
        self.prizeMoney = 0
        self.prizes = []

    """
    Decide semi-randomly whether to make a 'good' or 'bad' move.
    A higher difficulty is more likely to make a 'good' move.
    """
    def smartCoinFlip(self):
        randNum = random.randint(1, 10)
        if randNum > self.difficulty:
            return True
        else:
            return False

    """
    Returns a list of letters that can be guessed.
    - Should be characters that are in LETTERS but not in the
    guessed parameter.
    - If the player doesn't have enough prize money to guess a
    vowel, then vowels should not be included
    """
    def getPossibleLetters(self, guessed):
        letters_available = []
        for l in LETTERS:
            if l not in guessed:
                #letters_available.append(l)
                if self.prizeMoney > VOWEL_COST:
                    letters_available.append(l)
            else:
                return letters_available

    """
    Returns a valid move.
    If ther aren't any letters that can be guessed, return 'pass'
    Flip the coin to get a move: if good return the most frequent
    character, if bad return a random character from the set of
    possible characters
    """
    def getMove(self, category, obscuredPhrase, guessed):
        letters_available = self.getPossibleLetters(guessed)
        if letters_available == []:
            return 'pass'
        else:
            coin_flip = self.smartCoinFlip()
            if coin_flip == True:
                letters_available[0]
            if coin_flip == False:
                random_char = random.choice(letters_available)
                return random_char


