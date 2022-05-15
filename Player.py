class Player:
    def __init__(self, handPile):
        # a dictionary of the cards in their hands
        self.handPile = handPile
        # a dictionary of the cards facing up (name:number)
        self.cardsFaceUp = dict()
        self.totalScore = 0

    # reset stuff for future rounds
    def reset(self, handPile, cardsFaceUp):
        self.handPile = handPile
        self.cardsFaceUp = cardsFaceUp

    # get the current pile in the user's hand
    def getHandPile(self):
        return self.handPile

    # get the current face-up cards player has
    def getFaceUp(self):
        return self.cardsFaceUp

    # add to the player's total score
    def addScore(self, score):
        self.totalScore += score

    # get the current score
    def getScore(self):
        return self.totalScore

    # when the player choose a card to put down, add that to the face-up pile
    def addFaceUp(self, cardName):
        # check if player already has the card, add to that number of card
        if cardName in self.cardsFaceUp.keys():
            self.cardsFaceUp[cardName] += 1
        else:
            self.cardsFaceUp[cardName] = 1

    # switch hand card pile
    def switchHandPile(self, handPileToSwitch):
        self.handPile = handPileToSwitch

    # switch face-up card pile
    def switchFaceUpPile(self, pileToSwitch):
        self.cardsFaceUp = pileToSwitch

    # withdraw a card from the pile in hand before passing to the next person
    def withdrawHandPile(self, cardDrew):
        if self.handPile[cardDrew] > 1:
            self.handPile[cardDrew] -= 1
        else:
            del self.handPile[cardDrew]

    # put a card back into the pile
    def putCardBack(self, card):
        if card in self.handPile.keys():
            self.handPile[card] += 1
        else:
            self.handPile[card] = 1

