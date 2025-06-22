#PlAYER 1 and 2 BLINDING SETUP
from getpass import getpass as input

#Game Counter
counter1 = 0 
counter2 = 0
print()

#PLAYER INPUTS
print("\033[33m", "EPIC ROCK PAPER SCISSORS BATTLE", "\033[0m")
print()
while True:
    player1 = input("Player 1 - What is your move?:  ").strip().lower()
    print()
    player2 = input("Player 2 - What is your move?:  ").strip().lower()
    print()

#rps formulae

#ROCK/ROCK
    if player1 == ("rock") and player2 == ("rock"):
        print("\033[32m", "We have a pebble party with zero winners 😕, both players choose 🪨", "\033[0m")
        print()
        print("The score remains Player 1:", "\033[35m", counter1, "\033[0m", "Player 2:", "\033[35m", counter2, "\033[0m")

#ROCK/PAPER
    elif player1 == ("rock") and player2 == ("paper"):
        counter2 += 5
        print("\033[32m", "Bedtime for boulders! Player 2 wins with 📃 over 🪨 +5 pts!", "\033[0m")
        print()
        print("The score is now Player 1:", "\033[35m", counter1, "\033[0m", "Player 2:", "\033[35m", counter2,"\033[0m" )

#ROCK/SCISSORS
    elif player1 == ("rock") and player2 == ("scissors"):
        counter1 += 5
        print("\033[32m", "Granite over guillotine! Player 1 wins with 🪨 over ✂️ +5 pts!", "\033[0m")
        print()
        print(" The score is now Player 1:","\033[35m", counter1,"\033[0m", "Player 2:", "\033[35m", counter2, "\033[0m")

#PAPER/ROCK
    elif player1 == ("paper") and player2 == ("rock"):
        counter1 +=5
        print("\033[32m", "One swipe of paper and the rock is history! Player 1 wins with 📃 over 🪨 +5 pts!", "\033[0m")
        print()
        print(" The score is now Player 1:","\033[35m", counter1, "\033[0m", "Player 2:", "\033[35m", counter2, "\033[0m")

#PAPER/SCISSORS
    elif player1 == ("paper") and player2 == ("scissors"):
        counter2 += 5
        print("\033[32m", "Snip snip! Player 2 wins with ✂️ over 📃 +5 pts!", "\033[0m")
        print()
        print(" The score is now Player 1:", "\033[35m", counter1, "\033[0m", "Player 2:", "\033[35m", counter2, "\033[0m")

#PAPER/PAPER
    elif player1 == ("paper") and player2 == ("paper"):
        print("\033[32m", "Page on page, call it a standstill 😕. Both players choose 📃", "\033[0m")
        print()
        print("The score remains Player 1:","\033[35m", counter1, "\033[0m", "Player 2:", "\033[35m",counter2, "\033[0m")

#PAPER/ROCK
    elif player1 == ("scissors") and player2 == ("rock"):
        counter2 += 5
        print("\033[32m", "Cliff vs Cutlery - CLIFF WINS. Player 2 wins with 🪨 over ✂️ +5pts", "\033[0m")
        print()
        print(" The score is now Player 1:", "\033[35m", counter1, "\033[0m", "Player 2:", "\033[35m", counter2, "\033[0m")

#SCISSORS/PAPER        
    elif player1 == ("scissors") and player2 == ("paper"):
        counter1+= 5
        print("\033[32m", "Blade beats blank page! Player 1 wins with ✂️ over 📃 +5pts!", "\033[0m")
        print()
        print(" The score is now Player 1:", "\033[35m", counter1, "\033[0m", "Player 2:", "\033[35m", counter2, "\033[0m")

 #SCISSORS/SCISSORS  
    elif player1 == ("scissors") and player2 == ("scissors"):
        print("\033[32m", "Iron sharpens iron. Total stalemate 😕. Both players chose ✂️", "\033[0m")
        print()
        print("The score remains Player 1:", "\033[35m", counter1, "\033[0m", "Player 2:", "\033[35m", counter2, "\033[0m")
    
    else:
        print("\033[31m", "Invalid user input, must be [rock], [paper] or [scissors]", "\033[0m")
    print()

#GAME SCORE CALCULATIONS
    playAgain = input("Play Again (yes/no)?:  ").strip().lower()
    print()
    if playAgain != "yes":
        print("GAME OVER! Final Score - Player 1:", "\033[35m", counter1, "\033[0m", "Player 2:",  "\033[35m", counter2, "\033[0m")
        if counter1 > counter2:
            print("\033[32m"," PLAYER 1 WINS!", "\033[0m")
        elif counter1 < counter2:
            print("\033[32m", "PLAYER 2 WINS!", "\033[0m")
        else:
            print("\033[32m", "TOTAL STALEMATE 😕", "\033[0m")
        break
