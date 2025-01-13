class Player:
    def __init__(self, name, score):
        self.name = name
        self.darts_thrown = 0
        self.score = score

class Game:
    def __init__(self, players, number):
        self.players = []
        for player in players:
            self.players.append(Player(player, number))
        self.current_player = 0
        self.start_num = number
        self.num_of_darts = 0

    def switch_player(self):
        self.num_of_darts = 0
        self.current_player = (self.current_player + 1) % len(self.players)

    def turn(self, points, multiplier):
        if self.num_of_darts == 3:
            self.switch_player()
            self.num_of_darts = 0
            return True, None  # Turn over, no winner

        score_to_deduct = points * multiplier
        current_player = self.players[self.current_player]

        if (current_player.score - score_to_deduct == 0) and (multiplier == 2):
            print(f"{current_player.name} wins the game!")
            return True, current_player  # Turn over, current player is the winner
        elif current_player.score - score_to_deduct <= 1:
            print(f"{current_player.name} busts!")
            self.switch_player()
            return True, None  # Turn over, no winner
        else:
            current_player.score -= score_to_deduct
            self.num_of_darts += 1
            return False, None  # Turn not over, no winner

    def calculate_finishes(self, target_score):
        finishes = []
        darts = [(1, ''), (2, 'D'), (3, 'T')]  # Single, Double, Treble

        def find_combinations(score, darts_thrown):
            if score == 0 and len(darts_thrown) <= 3:
                if darts_thrown and (darts_thrown[-1].startswith('D') or darts_thrown[-1] == '50'):
                    finishes.append(darts_thrown)
                return
            if len(darts_thrown) >= 3 or score < 0:
                return

            for multiplier, prefix in darts:
                for i in range(1, 21):
                    find_combinations(score - i * multiplier, darts_thrown + [f"{prefix}{i}"])
                if multiplier == 1:  # Add bullseye and outer bullseye
                    find_combinations(score - 25, darts_thrown + [f"{prefix}25"])
                    find_combinations(score - 50, darts_thrown + [f"{prefix}50"])

        find_combinations(target_score, [])
        return finishes

# Example usage
game = Game(["Player1", "Player2"], 501)
possible_finishes = game.calculate_finishes(42)
for finish in possible_finishes:
    print(finish)