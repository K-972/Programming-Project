class Player:
    def __init__(self, name, score):
        self.name = name
        self.darts_thrown = 0
        self.score = score
        self.legs_won = 0

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
            # print(f"Debug: Switched player to {self.players[self.current_player].name

        score_to_deduct = points * multiplier
        current_player = self.players[self.current_player]
        # print(f"Debug: Current Player: {current_player.name}, Points: {points}, Multiplier: {multiplier}, Score to Deduct: {score_to_deduct}, Current Score: {current_player.score}")
        
        if (current_player.score - score_to_deduct == 0) and (multiplier == 2):
            print(f"{current_player.name} wins the leg!")
            current_player.legs_won += 1
            # self.reset_scores()
            # print(f"Debug: {current_player.name} wins the leg! Legs Won: {current_player.legs_won}")
            
        elif current_player.score - score_to_deduct <= 1:
            print(f"{current_player.name} busts!")
            self.switch_player()
            # print(f"Debug: {current_player.name} busts with score {current_player.score} and score to deduct {score_to_deduct}")
            
        else:
            current_player.score -= score_to_deduct
            # print(f"Debug: {current_player.name}'s new score: {current_player.score}")
        
        self.num_of_darts += 1
        # print(f"Debug: Number of darts thrown: {num_of_darts}")
        
        

    

    def reset_scores(self):
        for player in self.players:
            player.score = self.start_num
            # print(f"Debug: Reset score for {player.name} to {self.start_num}")
