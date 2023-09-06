import random
import emoji

def rpsls():
    playagain = True
    playerScore = 0
    computerscore = 0
    while playagain:
        validChoice = False
        possibleChoices = ["r","p","c","l","s"]
        choice = {"r":"Rock", "p":"Paper", "c":"Scissors","l":"Lizard","s":"Spock"}
        emojis = {"r":emoji.emojize("::moai::"), "p":emoji.emojize("::page_facing_up::"), "c":emoji.emojize(":scissors:"),"l":emoji.emojize(":lizard::"),"s":emoji.emojize(":vulcan_salute:")}
        while not validChoice:
            playerChoice = input(f"Enter your Choice - (R)ock{emojis['r']}, (P)aper{emojis['p']}, S(c)issors{emojis['c']}, (L)izard{emojis['l']}, (S)pock{emojis['s']}: ")
            playerChoice=playerChoice.lower()
            if playerChoice in possibleChoices:
                validChoice = True
        computerChoice = possibleChoices[random.randint(0,4)]
        print("Player chose: " + str(choice.get(playerChoice)))
        print("Opponet chose: " + str(choice.get(computerChoice)))
        if playerChoice == computerChoice:
            print("It's a tie. You must try again")
        elif playerChoice== "c":
            if computerChoice == "p":
                print(f"Scissors{emojis['c']} cut Paper{emojis['p']}. You Win")
                playerScore += 1
            elif computerChoice == "l":
                print(f"Scissors{emojis['c']} decapitates Lizard{emojis['l']}. You win")
                playerScore += 1
            elif computerChoice == "r":
                print(f"Rock{emojis['r']} breaks Scissors{emojis['c']}. You lose")
                computerscore += 1
            else:
                print(f"Spock{emojis['s']} smashes Scissors{emojis['c']}. You lose")
                computerscore += 1
        elif playerChoice == "s":
            if computerChoice == "c":
                print(f"Spock{emojis['s']} smashes Scissors{emojis['c']}. You Win")
                playerScore += 1
            elif computerChoice == "r":
                print(f"Spock{emojis['s']} vaporizes Rock{emojis['r']}. You win")
                playerScore += 1
            elif computerChoice == "l":
                print(f"Lizard{emojis['l']} poisons Spock{emojis['s']}. You lose")
                computerscore += 1
            else:
                print(f"Paper{emojis['p']} disproves Spock{emojis['s']}. You lose")
                computerscore += 1
        elif playerChoice == "l":
            if computerChoice == "s":
                print(f"Lizard{emojis['l']} poisons Spock{emojis['s']}. You win")
                playerScore += 1
            elif computerChoice == "p":
                print(f"Lizard{emojis['l']} eats Paper{emojis['p']}. You win")
                playerScore += 1
            elif computerChoice == "r":
                print(f"Rock{emojis['r']} crushes Lizard{emojis['l']}. You lose")
                computerscore += 1
            else:
                print(f"Scissors{emojis['c']} decapitates Lizard{emojis['l']}. You lose")
                computerscore += 1
        elif playerChoice == "r":
            if computerChoice == "c":
                print(f"Rock{emojis['r']} breaks Scissors{emojis['c']}. You win")
                playerScore += 1
            elif computerChoice == "l":
                print(f"Rock{emojis['r']} crushes Lizard{emojis['l']}. You win")
                playerScore += 1
            elif computerChoice == "s":
                print(f"Spock{emojis['s']} vaporizes Rock{emojis['r']}. You lose")
                computerscore += 1
            else:
                print(f"Paper{emojis['p']} wraps Rock{emojis['r']}. You lose")
                computerscore += 1
        else:
            if computerChoice == "r":
                print(f"Paper{emojis['p']} wraps Rock{emojis['r']}. You win")
                playerScore += 1
            elif computerChoice == "s":
                print(f"Paper{emojis['p']} disproves Spock{emojis['s']}. You win")
                playerScore += 1
            elif computerChoice == "l":
                print(f"Lizard{emojis['l']} eats Paper{emojis['p']}. You lose")
                computerscore += 1
            else:
                print("Scisors cut Paper{emojis['p']}. You lose")
                computerscore += 1
        print("The current score is:\nPlayer: " + str(playerScore) + "\nComputer: " + str(computerscore))
        newgame = input("Would you like to go again? y/n - ")
        newgame=newgame.lower()
        if newgame == "n":
            if playerScore > computerscore:
                print("The final score is:\nPlayer: " + str(playerScore) + " and Computer: " + str(computerscore) + ". You Win!")
            elif computerscore > playerScore:
                print("The final score is:\nPlayer: " + str(playerScore) + " and Computer: " + str(computerscore) + ". You Lose!")
            else:
                print("The final score is:\nPlayer: " + str(playerScore) + " and Computer: " + str(computerscore) + ". You Tie!")
            playagain= False

rpsls()
