import time
import random
from Player import Player

# format the card user input to support case insensitive
def cardFormatter(cardName):
    cardName = cardName.lower()
    strList = list(cardName)
    strList[0] = strList[0].upper()
    for i in range(len(strList)):
        if strList[i] == " ":
            strList[i+1] = strList[i+1].upper()
    cardName = "".join(strList)
    return cardName

# deal the 10 cards and return that dictionary of 10 cards
def dealCards(allCards):
    dealtCards = dict()
    # get a random card type to deal
    cardList = list(allCards.keys())
    numCardsDealt = 0
    # deal 10 cards
    while numCardsDealt < 10:
        randomCard = random.choice(cardList)
        # deal the card if there's 1 or more cards of the type left
        # select another card to deal if there's no more of that card in the stack
        while allCards[randomCard] < 1:
           randomCard = random.choice(cardList)

        # add card to dealt card pile
        if randomCard in dealtCards.keys():
            dealtCards[randomCard] += 1
        else:
            dealtCards[randomCard] = 1
        allCards[randomCard] -= 1
        numCardsDealt += 1
    # playerCards = Player(dealtCards)
    return dealtCards

# put the rest of the cards into the draw pile
# def setDrawPile(allCards):
#     drawPile = allCards
#     return drawPile

# # play the rounds
# def playRounds():

# print out cards in the pile user has in hand
def printHandPile(player):
    handPile = player.getHandPile()
    print("Here are the cards in your hand: ")
    for card in handPile.items():
        print(card[0] + ": " + str(card[1]))
    print("-----")

# print out cards user have face-up
def printFaceUp(player):
    faceUpCards = player.getFaceUp()
    if faceUpCards:
        print("Here are the cards that you have put down: ")
        for card in faceUpCards.items():
            print(card[0] + ": " + str(card[1]))
        print("-----")
    else:
        print("\nYou haven't put down any card yet.")
        print("-----")

# print out cards computer have face-up
def printCompFaceUp(compPlayer):
    faceUpCards = compPlayer.getFaceUp()
    if faceUpCards:
        print("Here are the cards the other player has put down: ")
        for card in faceUpCards.items():
            print(card[0] + ": " + str(card[1]))
        print("")
    else:
        print("\nThe other player hasn't put down any card yet.\n")

# take in user input to add to face-up cards pile. verified
def userChooseCard(compPlayer, userPlayer):
    allCards = ["Tempura", "Sashimi", "Dumplings", "Two Maki Rolls", "Three Maki Rolls", "One Maki Roll",
                "Salmon Nigiri", "Squid Nigiri", "Egg Nigiri", "Pudding", "Wasabi", "Chopsticks"]
    printHandPile(userPlayer)
    # printCompFaceUp(compPlayer)
    # check if the user has chopsticks and ask if they want to use
    # print("line 165", checkChopsticks(userPlayer))
    if checkChopsticks(userPlayer):
        useChopsticks = input("You currently have a chopsticks card available to use. Would you want to use it? ")
        useChopsticks = useChopsticks.strip().lower()
        while not useChopsticks == "yes" and not useChopsticks == "no":
            print("Please enter yes or no.")
            useChopsticks = input("You currently have a chopsticks card available to use. Would you want to use it? ")
            useChopsticks = useChopsticks.strip().lower()
        if useChopsticks == "yes":   # draw 2 cards if player wants to use chopsticks
            for i in range(2):
                handPile = userPlayer.getHandPile()
                cardName = input("Which card would you like to put down? ")
                cardName = cardName.strip()
                cardName = cardFormatter(cardName)
                # print(cardName)
                # check if card is valid and tell user to enter the cards exactly as it is named
                while not cardName in allCards or not cardName in handPile:
                    if not cardName in allCards:
                        print("The card you chose is invalid.")
                        cardName = input("Choose again: ")
                        cardName = cardName.strip()
                        cardName = cardFormatter(cardName)
                    else:
                        print("You don't have the card you have selected in your hand.")
                        cardName = input("Choose again: ")
                        cardName = cardName.strip()
                        cardName = cardFormatter(cardName)
                userPlayer.addFaceUp(cardName)
                userPlayer.withdrawHandPile(cardName)
                print("You have put down " + cardName + ".")
                print("-----")
            # take away the chopsticks from the face-up pile
            faceUpPile = userPlayer.getFaceUp()
            if faceUpPile["Chopsticks"] > 1:
                faceUpPile["Chopsticks"] -= 1
            else:
                del faceUpPile["Chopsticks"]
            userPlayer.switchFaceUpPile(faceUpPile)

            # put chopsticks back to the pile to be passed on once drew 2 cards
            userPlayer.putCardBack("Chopsticks")

        else:  # only draw 1 card if user don't want to use chopsticks
            handPile = userPlayer.getHandPile()
            cardName = input("Which card would you like to put down? ")
            cardName = cardName.strip()
            cardName = cardFormatter(cardName)
            while not cardName in allCards or not cardName in handPile:
                if not cardName in allCards:
                    print("The card you chose is invalid.")
                    cardName = input("Choose again: ")
                    cardName = cardName.strip()
                    cardName = cardFormatter(cardName)
                else:
                    print("You don't have the card you have selected in your hand.")
                    cardName = input("Choose again: ")
                    cardName = cardName.strip()
                    cardName = cardFormatter(cardName)
            userPlayer.addFaceUp(cardName)
            userPlayer.withdrawHandPile(cardName)
            print("You have put down " + cardName + ".")
            print("-----")
    else:  # if doesn't have chopsticks
        handPile = userPlayer.getHandPile()
        cardName = input("Which card would you like to put down? ")
        cardName = cardName.strip()
        cardName = cardFormatter(cardName)
        # print("220", allCards)
        # print("222", cardName)
        while not cardName in allCards or not cardName in handPile:
            if not cardName in allCards:
                print("The card you chose is invalid.")
                cardName = input("Choose again: ")
                cardName = cardName.strip()
                cardName = cardFormatter(cardName)
            else:
                print("You don't have the card you have selected in your hand.")
                cardName = input("Choose again: ")
                cardName = cardName.strip()
                cardName = cardFormatter(cardName)
        userPlayer.addFaceUp(cardName)
        userPlayer.withdrawHandPile(cardName)
        # print("238", userPlayer.cardsFaceUp)
        # printFaceUp(userPlayer)
        print("You have put down " + cardName + ".")
        print("-----")

# choose card to add to face-up pile for computer. verified
def compChooseCard(compPlayer):
    handPile = compPlayer.getHandPile()
    # draw 2 cards if have chopsticks and then put that chopstick card back to hand to pass on
    if checkChopsticks(compPlayer):
        # choose 2 random card for computer to withdraw and add to face-up pile
        for i in range(2):
            cardName = random.choice(list(handPile))
            compPlayer.addFaceUp(cardName)
            compPlayer.withdrawHandPile(cardName)
        # get the computer's current face-up pile
        faceUpPile = compPlayer.getFaceUp()
        # add chopstick back and delete chopstick or subtract 1 from the face up pile
        compPlayer.putCardBack("Chopsticks")
        if faceUpPile["Chopsticks"] > 1:
            faceUpPile["Chopsticks"] -= 1
        else:
            del faceUpPile["Chopsticks"]
        compPlayer.switchFaceUpPile(faceUpPile)
    else:
        # choose a random card for computer to withdraw and add to face-up pile
        cardName = random.choice(list(handPile))
        compPlayer.addFaceUp(cardName)
        compPlayer.withdrawHandPile(cardName)
    # print what the computer has faced up
    # printCompFaceUp(compPlayer)

# check if computer has chopstick. verified
def checkChopsticks(player):
    faceUpPile = player.getFaceUp()
    chopsticks = "Chopsticks"
    if chopsticks in faceUpPile.keys():
        return True
    else:
        return False

# switch hand pile with each other. verified
def switchPile(compPlayer, userPlayer):
    compPile = compPlayer.getHandPile()
    userPile = userPlayer.getHandPile()
    compPlayer.switchHandPile(userPile)
    userPlayer.switchHandPile(compPile)

# add up score of Maki Rolls
def scoreMaki(compPlayer, userPlayer):
    allCards = {"Tempura": 14, "Sashimi": 14, "Dumplings": 14, "Two Maki Rolls": 12, "Three Maki Rolls": 8,
                "One Maki Roll": 6, "Salmon Nigiri": 10, "Squid Nigiri": 5, "Egg Nigiri": 5, "Pudding": 10, "Wasabi": 6,
                "Chopsticks": 4}
    compFaceUp = compPlayer.getFaceUp()
    userFaceUp = userPlayer.getFaceUp()
    compNumMakis = 0
    userNumMakis = 0
    # add up the number of makis for each player
    if "One Maki Roll" in compFaceUp.keys():
        compNumMakis += compFaceUp["One Maki Roll"]
    if "Two Maki Rolls" in compFaceUp.keys():
        compNumMakis += (compFaceUp["Two Maki Rolls"] * 2)
    if "Three Maki Rolls" in compFaceUp.keys():
        compNumMakis += (compFaceUp["Three Maki Rolls"] * 3)
    if "One Maki Roll" in userFaceUp.keys():
        userNumMakis += userFaceUp["One Maki Roll"]
    if "Two Maki Rolls" in userFaceUp.keys():
        userNumMakis += (userFaceUp["Two Maki Rolls"] * 2)
    if "Three Maki Rolls" in userFaceUp.keys():
        userNumMakis += (userFaceUp["Three Maki Rolls"] * 3)

    # if one player doesn't have Maki then the other one gets 6 points
    if compNumMakis == 0 and userNumMakis > 0:
        userPlayer.addScore(6)
    elif userNumMakis == 0 and compNumMakis > 0:
        compPlayer.addScore(6)
    elif compNumMakis > userNumMakis:  # computer has more maki cards
        userPlayer.addScore(3)
        compPlayer.addScore(6)
    elif compNumMakis < userNumMakis:  # user has more maki cards
        userPlayer.addScore(6)
        compPlayer.addScore(3)
    elif compNumMakis == userNumMakis and compNumMakis > 0 and userNumMakis > 0:  # if both tie
        userPlayer.addScore(3)
        compPlayer.addScore(3)
    # print("compNumMakis", compNumMakis)
    # print("userNumMakis", userNumMakis)
    # print("Makis user", compPlayer.totalScore)
    # print("Makis user", userPlayer.totalScore)

# add up score of Tempura
def scoreTempura(compPlayer, userPlayer):
    compFaceUp = compPlayer.getFaceUp()
    userFaceUp = userPlayer.getFaceUp()
    if "Tempura" in compFaceUp.keys():
        compTempura = compFaceUp["Tempura"]
        if compTempura % 2 == 1:  # if computer have uneven number of tempura cards
            compTempura = int(compTempura // 2)
            compScore = compTempura * 5  # only want to add score for every set of 2 tempura
            compPlayer.addScore(compScore)
        else:  # if computer have even number of tempura cards
            compTempura = int(compTempura / 2)
            compScore = compTempura * 5
            compPlayer.addScore(compScore)
    if "Tempura" in userFaceUp.keys():
        userTempura = userFaceUp["Tempura"]
        if userTempura % 2 == 1:  # if user have uneven number of tempura cards
            userTempura = int(userTempura // 2)
            userScore = userTempura * 5
            userPlayer.addScore(userScore)
        else:  # if user have even number of tempura cards
            userTempura = int(userTempura / 2)
            userScore = userTempura * 5
            userPlayer.addScore(userScore)
    # print("Tempura comp", compPlayer.totalScore)
    # print("Tempura user", userPlayer.totalScore)

# cout score for sashimi
def scoreSashimi(compPlayer, userPlayer):
    compFaceUp = compPlayer.getFaceUp()
    userFaceUp = userPlayer.getFaceUp()
    if "Sashimi" in compFaceUp.keys():
        compSashimi = compFaceUp["Sashimi"]
        # add score for computer
        if compSashimi % 3 != 0 and compSashimi > 3:
            compSashimi = int(compSashimi // 3)
            compScore = compSashimi * 10
            compPlayer.addScore(compScore)
        elif compSashimi == 3:
            compScore = 10
            compPlayer.addScore(compScore)
    if "Sashimi" in userFaceUp.keys():
        userSashimi = userFaceUp["Sashimi"]
        # add score for user
        if userSashimi % 3 != 0 and userSashimi > 3:
            userSashimi = int(userSashimi // 3)
            userScore = userSashimi * 10
            userPlayer.addScore(userScore)
        elif userSashimi == 3:
            userScore = 10
            userPlayer.addScore(userScore)
    # print("Sashimi comp", compPlayer.totalScore)
    # print("Sashimi user", userPlayer.totalScore)

# add up score for dumplings
def scoreDumplings(compPlayer, userPlayer):
    compFaceUp = compPlayer.getFaceUp()
    userFaceUp = userPlayer.getFaceUp()
    prevScore = 0
    if "Dumplings" in compFaceUp.keys():
        compDumplings = compFaceUp["Dumplings"]
        # add score for computer
        if compDumplings > 4:  # 5 or more dumplings will score 15 points
            compPlayer.addScore(15)
        else:
            for i in range(1, 5):
                if compDumplings == i:
                    compScore = prevScore + i
                    break
                prevScore += i
                compScore = prevScore
            compPlayer.addScore(compScore)
    prevScore = 0
    if "Dumplings" in userFaceUp.keys():
        userDumplings = userFaceUp["Dumplings"]
        # add score for user
        if userDumplings > 4:
            userPlayer.addScore(15)
        else:
            for i in range(1, 5):
                if userDumplings == i:
                    userScore = prevScore + i
                    break
                prevScore += i
                userScore = prevScore
            userPlayer.addScore(userScore)
    # print("Dumplings comp", compPlayer.totalScore)
    # print("Dumplings user", userPlayer.totalScore)

# add up score for squid nigiri and wasabi
def scoreSquidNigiri(compPlayer, userPlayer):
    compFaceUp = compPlayer.getFaceUp()
    userFaceUp = userPlayer.getFaceUp()
    wasabiUsedSquidComp = 0
    wasabiUsedSquidUser = 0
    # add score for computer
    if "Squid Nigiri" in compFaceUp.keys() and "Wasabi" in compFaceUp.keys():
        compSquid = compFaceUp["Squid Nigiri"]
        compWasabi = compFaceUp["Wasabi"]
        # add score for computer
        if compSquid == compWasabi or compSquid < compWasabi:  # if each squid nigiri is on top of a wasabi
            compScore = compSquid * 9
            wasabiUsedSquidComp += compSquid
            compPlayer.addScore(compScore)
        else:  # if not every squid is on wasabi
            squidNoWasabi = compSquid - compWasabi
            squidWasabi = compSquid - squidNoWasabi
            wasabiUsedSquidComp += squidWasabi
            compScore = (squidWasabi * 9) + (squidNoWasabi * 3)
            compPlayer.addScore(compScore)
    elif "Squid Nigiri" in compFaceUp.keys():  # if computer only has nigiri but no wasabi
        compSquid = compFaceUp["Squid Nigiri"]
        compScore = compSquid * 3
        compPlayer.addScore(compScore)

    # add score for user
    if "Squid Nigiri" in userFaceUp.keys() and "Wasabi" in userFaceUp.keys():
        userSquid = userFaceUp["Squid Nigiri"]
        userWasabi = userFaceUp["Wasabi"]
        # add score for user
        if userSquid == userWasabi or userSquid < userWasabi:  # if each squid nigiri is on top of a wasabi
            userScore = userSquid * 9
            wasabiUsedSquidUser += userSquid
            userPlayer.addScore(userScore)
        else:  # if not every squid is on wasabi
            squidNoWasabi = userSquid - userWasabi
            squidWasabi = userSquid - squidNoWasabi
            wasabiUsedSquidUser += squidWasabi
            userScore = (squidWasabi * 9) + (squidNoWasabi * 3)
            userPlayer.addScore(userScore)
    elif "Squid Nigiri" in userFaceUp.keys():
        userSquid = userFaceUp["Squid Nigiri"]
        userScore = userSquid * 3
        userPlayer.addScore(userScore)
    # print("Squid user", compPlayer.totalScore)
    # print("Squid user", userPlayer.totalScore)
    return wasabiUsedSquidComp, wasabiUsedSquidUser

# add up score for salmon nigiri and wasabi
def scoreSalmonNigiri(compPlayer, userPlayer, wasabiUsedSquidComp, wasabiUsedSquidUser):
    compFaceUp = compPlayer.getFaceUp()
    userFaceUp = userPlayer.getFaceUp()
    wasabiUsedSalmonComp = 0
    wasabiUsedSalmonUser = 0
    # add score for computer
    if "Salmon Nigiri" in compFaceUp.keys() and "Wasabi" in compFaceUp.keys():
        compSalmon = compFaceUp["Salmon Nigiri"]
        compWasabi = compFaceUp["Wasabi"]
        wasabiLeftSalmonComp = compWasabi - wasabiUsedSquidComp
        if wasabiLeftSalmonComp > 0:  # use the wasabi that's left for salmon
            if compSalmon == compWasabi or compSalmon < compWasabi:  # if each salmon nigiri is on top of a wasabi
                compScore = compSalmon * 6
                wasabiUsedSalmonComp = compSalmon
                compPlayer.addScore(compScore)
            else:  # if not every salmon is on wasabi
                salmonNoWasabi = compSalmon - compWasabi
                salmonWasabi = compSalmon - salmonNoWasabi
                wasabiUsedSalmonComp = salmonWasabi
                compScore = (salmonWasabi * 6) + (salmonNoWasabi * 2)
                compPlayer.addScore(compScore)
        else:  # no wasabi left to use so just sum up the salmon nigiri score alone
            compSalmon = compFaceUp["Salmon Nigiri"]
            compScore = compSalmon * 2
            compPlayer.addScore(compScore)
    elif "Salmon Nigiri" in compFaceUp.keys():
        compSalmon = compFaceUp["Salmon Nigiri"]
        compScore = compSalmon * 2
        compPlayer.addScore(compScore)
    # add score for user
    if "Salmon Nigiri" in userFaceUp.keys() and "Wasabi" in userFaceUp.keys():
        userSalmon = userFaceUp["Salmon Nigiri"]
        userWasabi = userFaceUp["Wasabi"]
        wasabiLeftSalmonUser = userWasabi - wasabiUsedSquidUser
        if wasabiLeftSalmonUser > 0:
            if userSalmon == userWasabi or userSalmon < userWasabi:  # if each salmon nigiri is on top of a wasabi
                userScore = userSalmon * 6
                wasabiUsedSalmonUser += userSalmon
                userPlayer.addScore(userScore)
            else:  # if not every squid is on wasabi
                salmonNoWasabi = userSalmon - userWasabi
                salmonWasabi = userSalmon - salmonNoWasabi
                wasabiUsedSalmonUser += salmonWasabi
                userScore = (salmonWasabi * 6) + (salmonNoWasabi * 2)
                userPlayer.addScore(userScore)
        else:
            userSalmon = userFaceUp["Salmon Nigiri"]
            userScore = userSalmon * 2
            userPlayer.addScore(userScore)
    elif "Salmon Nigiri" in userFaceUp.keys():
        userSalmon = userFaceUp["Salmon Nigiri"]
        userScore = userSalmon * 2
        userPlayer.addScore(userScore)
    # print("Salmon user", compPlayer.totalScore)
    # print("Salmon comp", userPlayer.totalScore)
    return wasabiUsedSalmonComp, wasabiUsedSalmonUser

# add up score for egg nigiri and wasabi
def scoreEggNigiri(compPlayer, userPlayer, wasabiUsedSquidComp, wasabiUsedSalmonComp, wasabiUsedSquidUser,
                   wasabiUsedSalmonUser):
    compFaceUp = compPlayer.getFaceUp()
    userFaceUp = userPlayer.getFaceUp()
    # add score for computer
    if "Egg Nigiri" in compFaceUp.keys() and "Wasabi" in compFaceUp.keys():
        compEgg = compFaceUp["Egg Nigiri"]
        compWasabi = compFaceUp["Wasabi"]
        wasabiLeftEgg = compWasabi - wasabiUsedSquidComp - wasabiUsedSalmonComp
        if wasabiLeftEgg > 0:  # use the wasabi that's left for egg
            if compEgg == compWasabi or compEgg < compWasabi:  # if each egg nigiri is on top of a wasabi
                compScore = compEgg * 3
                compPlayer.addScore(compScore)
            else:  # if not every salmon is on wasabi
                eggNoWasabi = compEgg - compWasabi
                eggWasabi = compEgg - eggNoWasabi
                compScore = (eggWasabi * 3) + (eggNoWasabi)
                compPlayer.addScore(compScore)
        else:  # no wasabi left for egg
            compEgg = compFaceUp["Egg Nigiri"]
            compPlayer.addScore(compEgg)
    elif "Egg Nigiri" in compFaceUp.keys():
        compEgg = compFaceUp["Egg Nigiri"]
        compPlayer.addScore(compEgg)
    # add score for user
    if "Egg Nigiri" in userFaceUp.keys() and "Wasabi" in userFaceUp.keys():
        userEgg = userFaceUp["Egg Nigiri"]
        userWasabi = userFaceUp["Wasabi"]
        wasabiLeftEgg = userWasabi - wasabiUsedSquidUser - wasabiUsedSalmonUser
        if wasabiLeftEgg > 0:
            if userEgg == userWasabi or userEgg < userWasabi:  # if each egg nigiri is on top of a wasabi
                userScore = userEgg * 3
                userPlayer.addScore(userScore)
            else:  # if not every squid is on wasabi
                eggNoWasabi = userEgg - userWasabi
                eggWasabi = userEgg - eggNoWasabi
                userScore = (eggWasabi * 3) + (eggNoWasabi)
                userPlayer.addScore(userScore)
        else:
            userEgg = userFaceUp["Egg Nigiri"]
            userPlayer.addScore(userEgg)
    elif "Egg Nigiri" in userFaceUp.keys():
        userEgg = userFaceUp["Egg Nigiri"]
        userPlayer.addScore(userEgg)
    # print("Egg user", compPlayer.totalScore)
    # print("Egg comp", userPlayer.totalScore)

# add score without pudding
def totalScoreNoPudding(compPlayer, userPlayer):
    compFaceUp = compPlayer.getFaceUp()
    userFaceUp = userPlayer.getFaceUp()
    scoreMaki(compPlayer, userPlayer)
    scoreTempura(compPlayer, userPlayer)
    scoreSashimi(compPlayer, userPlayer)
    scoreDumplings(compPlayer, userPlayer)
    wasabiUsedSquid = scoreSquidNigiri(compPlayer, userPlayer)
    wasabiUsedSalmon = scoreSalmonNigiri(compPlayer, userPlayer, wasabiUsedSquid[0], wasabiUsedSquid[1])
    scoreEggNigiri(compPlayer, userPlayer, wasabiUsedSquid[0], wasabiUsedSalmon[0], wasabiUsedSquid[1],
                   wasabiUsedSalmon[1])

# add score with pudding (maybe just pass in the player and the number of puddings they have and calculate after calling scoreNoPudding?
def scorePudding(compPlayer, userPlayer):
    compFaceUp = compPlayer.getFaceUp()
    userFaceUp = userPlayer.getFaceUp()
    compPudding = 0
    userPudding = 0
    if "Pudding" in compFaceUp.keys():
        compPudding = compFaceUp["Pudding"]
    if "Pudding" in userFaceUp.keys():
        userPudding = userFaceUp["Pudding"]
    if compPudding < userPudding:
        userPlayer.addScore(6)
    elif compPudding > userPudding:
        compPlayer.addScore(6)
    else:
        userPlayer.addScore(3)
        compPlayer.addScore(3)


# announce current score
def announceScore(compPlayer, userPlayer):
    print("Your current score is", userPlayer.getScore(), "points.")
    print("Your opponent's current score is", compPlayer.getScore(), "points.")
    print("-----")

# announce winner
def announceWinner(compPlayer, userPlayer):
    compScore = compPlayer.getScore()
    userScore = userPlayer.getScore()
    compFaceUp = compPlayer.getFaceUp()
    userFaceUp = userPlayer.getFaceUp()
    compPudding = 0
    userPudding = 0
    if "Pudding" in compFaceUp.keys():
        compPudding = compFaceUp["Pudding"]
    if "Pudding" in userFaceUp.keys():
        userPudding = userFaceUp["Pudding"]
    if compScore > userScore:
        print("Unfortunately, you have lost. Good luck next time!")
    elif compScore < userScore:
        print("You won!")
    else:  # if there's a tie
        # whoever has the most pudding cards win
        if compPudding > userPudding:
            print("Unfortunately, you have lost. Good luck next time!")
        elif compPudding < userPudding:
            print("You won!")
        else:
            print("You tied!")

# discard face-up cards after each round but keep pudding cards
def discardFaceUp(compPlayer, userPlayer):
    compFaceUp = compPlayer.getFaceUp()
    userFaceUp = userPlayer.getFaceUp()
    if "Pudding" in compFaceUp.keys():
        compPudding = compFaceUp["Pudding"]
        compFaceUp = {"Pudding": compPudding}
    else:
        compFaceUp = {}
    if "Pudding" in userFaceUp.keys():
        userPudding = userFaceUp["Pudding"]
        userFaceUp = {"Pudding": userPudding}
    else:
        userFaceUp = {}
    # print("557 compPlayer Pudding is", compFaceUp)
    # print("558 userPlayer Pudding is", userFaceUp)
    compPlayer.switchFaceUpPile(compFaceUp)
    userPlayer.switchFaceUpPile(userFaceUp)

def playRounds():
    allCards = {"Tempura": 14, "Sashimi": 14, "Dumplings": 14, "Two Maki Rolls": 12, "Three Maki Rolls": 8,
                "One Maki Roll": 6, "Salmon Nigiri": 10, "Squid Nigiri": 5, "Egg Nigiri": 5, "Pudding": 10, "Wasabi": 6,
                "Chopsticks": 4}
    # drawPile = dict()
    print("Let's begin our game of Sushi Go!\n")
    # print("572 all cards left are", allCards)
    computerPlayer = Player(dealCards(allCards))
    userPlayer = Player(dealCards(allCards))
    # play 3 rounds
    for i in range(1, 4):
        print("Round", i)
        print("-----")
        print("Dealing cards...")
        # deal cards to players
        # print("577 all cards left are", allCards)
        time.sleep(1)
        print("Finished dealing.")
        print("-----")
        for i in range(10):  # there will be 10 cards so will pass around 10 times
            if i < 9:
                # computer choose card to put down
                print("The other player is choosing their card to place down...")
                compChooseCard(computerPlayer)
                time.sleep(1)

                # player choose card to put down
                userChooseCard(computerPlayer, userPlayer)

                # both reveal their cards
                print("Let's reveal both sides' chosen cards...")
                time.sleep(1)
                printCompFaceUp(computerPlayer)
                printFaceUp(userPlayer)

                #pass the hand pile to the other player
                switchPile(computerPlayer, userPlayer)
            else:
                # computer places the last card
                print("The other player is placing the last card down...")
                compHandPile = computerPlayer.getHandPile()
                lastCard = str(list(compHandPile.keys())[0])
                computerPlayer.addFaceUp(lastCard)
                time.sleep(1)

                # player places the last card
                print("Placing your last card down...")
                userHandPile = userPlayer.getHandPile()
                lastCard = str(list(userHandPile.keys())[0])
                userPlayer.addFaceUp(lastCard)
                time.sleep(1)

                # both reveal their cards
                print("Let's reveal both sides' last cards...")
                time.sleep(1)
                printCompFaceUp(computerPlayer)
                printFaceUp(userPlayer)
        # add up score for the round
        totalScoreNoPudding(computerPlayer, userPlayer)
        announceScore(computerPlayer, userPlayer)
        # discard the face up piles except pudding
        discardFaceUp(computerPlayer, userPlayer)
        # reset stuff for next round
        userFaceUp = userPlayer.getFaceUp()
        compFaceUp = computerPlayer.getFaceUp()
        # print("627 userFaceUp is", userFaceUp)
        # print("628 compFaceUp is", compFaceUp)
        dealtCards = dealCards(allCards)
        userPlayer.reset(dealtCards, userFaceUp)
        dealtCards = dealCards(allCards)
        computerPlayer.reset(dealtCards, compFaceUp)
    # add up puddings and announce winner
    print("Time for desserts! We will now add the puddings onto the total score.")
    scorePudding(computerPlayer, userPlayer)
    announceScore(computerPlayer, userPlayer)
    print("-----")
    announceWinner(computerPlayer, userPlayer)

def main():
    playRounds()

main()

