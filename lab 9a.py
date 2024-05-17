#Cecilia(Yixian) Zhang
# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']
beats = {'rock':'scissors', 'paper':'rock','scissors':'paper'}
p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)

class RockPaperScissorsGame:
    def __init__(self, num_players=1):
        self.num_players = num_players
        self.wins = {"Player 1": 0, "Player 2": 0, "Tie": 0}

    def determine_winner(self, p1, p2):
        if p1 == p2:
            return "Tie"
        elif beats[p1] == p2:
            return "Player 1 wins"
        else:
            return "Player 2 wins"
        
    def get_human_choice(self):
        while True:
            choice = input('Player 1, pick one of rock, paper, or scissors: ').lower()
            if choice in choices:
                return choice
            else:
                print("Invalid choice, please try again.")
    
    def get_choice(self, player_number):
        if player_number == 1:
            if self.num_players >= 1:
                return self.get_human_choice()
            else:
                return random.choice(choices)
        else:
            return random.choice(choices)
    
    def play_once(self):
        p1 = self.get_choice(1)
        p2 = self.get_choice(2)
        print(f'Player 1: {p1}\nPlayer 2: {p2}')
        
        winner = self.determine_winner(p1, p2)
        print(f"The winner is: {winner}")
        self.update_wins(winner)
        
    def play_in_loop(self, num_games):
        for _ in range(num_games):
            self.play_once()
        print(f"Results after {num_games} games: {self.wins}")
    
    def update_wins(self, winner):
        if winner == "Tie":
            self.wins["Tie"] += 1
        elif winner == "Player 1 wins":
            self.wins["Player 1"] += 1
        else:
            self.wins["Player 2"] += 1

def main():
    num_players = int(input("Enter the number of human players (0 or 1): "))
    game = RockPaperScissorsGame(num_players=num_players)
    game.play_once()
    
    num_games = int(input("How many games would you like to play in a loop? "))
    game.play_in_loop(num_games)

if __name__ == "__main__":
    main()
