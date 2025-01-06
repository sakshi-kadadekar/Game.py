import sys
import random

class Game:
    def __init__(self, name):
        self.attempts = 5
        self.total_attempts = 5
        self.wins = 0
        self.losses = 0
        self.colors = ["red", "yellow", "blue", "green", "black"]
        self.name = name

    def display(self):
        print(f"Welcome to the game, {self.name}!")

    def Gamming(self):
        self.attempts = self.total_attempts  # Reset attempts for a new game
        machine_color = random.choice(self.colors)
        while self.attempts > 0:
            result = input("1>Start \n2>Exit \nEnter your choice: ").strip()
            if result == '1':
                color = input("Please enter the color: ").lower().strip()
                if color not in self.colors:
                    print("Invalid color. Your guess was wrong.")
                elif color == machine_color:
                    print("You won the game!")
                    self.wins += 1
                    print(f"Attempts taken: {self.total_attempts - self.attempts + 1}")
                    print(f"Total number of attempts: {self.total_attempts}")
                    break  # Exit the game loop on win
                else:
                    print("Your guess was wrong. Please try again.")
                self.attempts -= 1
                print(f"Attempts left: {self.attempts}")
            elif result == '2':
                print("Exiting the game.")
                sys.exit(0)
            else:
                print("Invalid input. Please choose 1 or 2.")

        if self.attempts == 0:  # All attempts used (loss condition)
            print("Game over! You have used all your attempts.")
            print(f"Machine-generated color was: {machine_color}")
            self.losses += 1  # Increment losses if all attempts are used

    def show_scoreboard(self):
        print(f"Number of games won: {self.wins}")
        print(f"Number of games lost: {self.losses}")
        print(f"Player's name: {self.name}")



name = input("Enter name for scoreboard: ").strip()
obj = Game(name)
obj.display()

while True:
    obj.Gamming()
    userinput = input("1>See scoreboard \n2>Play again \n3>Exit \nEnter your choice: ").strip()
    if userinput == '1':
        obj.show_scoreboard()
    elif userinput == '2':
        continue
    elif userinput == '3':
        print("Thank you for playing!")
        sys.exit(0)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
