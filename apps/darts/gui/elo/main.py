import random
import math

class Player:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.rating = 1000
        self.games_played = 0

    def update_rating(self, score, expected_score):
        if self.rating < 2000:
            k_factor = 25
        elif self.rating < 2200:
            k_factor = 20
        else:
            k_factor = 10
        self.rating += k_factor * (score - expected_score)

def expected_score(player_rating, opponent_rating):
    return 1 / (1 + math.pow(10, (opponent_rating - player_rating) / 400))

def update_ratings(players, scores):
    for i, player in enumerate(players):
        expected_scores = [expected_score(player.rating, opponent.rating) for j, opponent in enumerate(players) if i != j]
        expected_score_avg = sum(expected_scores) / len(expected_scores)
        old_rating = player.rating
        player.update_rating(scores[i], expected_score_avg)
        new_rating = player.rating
        write_game_outcome(player.name, old_rating, new_rating, scores[i])

def write_game_outcome(player_name, old_rating, new_rating, score):
    with open("game_outcomes.txt", "a") as file:
        file.write(f"Player: {player_name}, Old Rating: {old_rating}, New Rating: {new_rating}, Score: {score}\n")

# Create players with specific skill levels
players = [
    Player("Alice", 1500),
    Player("Bob", 1600),
    Player("Charlie", 1700)
]

# Example scores for a game
scores = [1, 0, 0.5]

# Update ratings based on the scores
update_ratings(players, scores)