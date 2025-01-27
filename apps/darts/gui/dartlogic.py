import math



class Player:
    def __init__(self, name, score):
        self.name = name
        self.darts_thrown = 0
        self.score = score
        
        # stats
        self.avg_score_per_dart = 0
        self.three_dart_average = 0
        self.highest_3_dart_score = 0
        self.most_spot_hit = 0
        self.standard_deviation = 0
        self.scores = []  # To keep track of all scores for standard deviation calculation
        self.turn_scores = []  # To keep track of scores per turn
        self.spots_hit = {}  # To track all spots hit on the board
        self.history = []  # To keep track of history for undo

    def update_stats(self):
        if self.darts_thrown > 0:
            self.avg_score_per_dart = sum(self.scores) / self.darts_thrown
        if self.turn_scores:
            self.three_dart_average = sum(self.turn_scores) / len(self.turn_scores)
            self.highest_3_dart_score = max(self.highest_3_dart_score, max(self.turn_scores))
        if self.scores:
            mean = sum(self.scores) / len(self.scores)
            variance = sum((x - mean) ** 2 for x in self.scores) / len(self.scores)
            self.standard_deviation = math.sqrt(variance)
        if self.spots_hit:
            self.most_spot_hit = max(self.spots_hit, key=self.spots_hit.get)

    def add_score(self, score, spot):
        self.scores.append(score)
        self.darts_thrown += 1
        self.history.append((score, spot))
        if len(self.scores) % 3 == 0:
            self.turn_scores.append(sum(self.scores[-3:]))
        if spot in self.spots_hit:
            self.spots_hit[spot] += 1
        else:
            self.spots_hit[spot] = 1
        self.update_stats()

    def undo_last_score(self):
        if self.history:
            last_score, last_spot = self.history.pop()
            self.scores.remove(last_score)
            self.darts_thrown -= 1
            if last_spot in self.spots_hit:
                self.spots_hit[last_spot] -= 1
                if self.spots_hit[last_spot] == 0:
                    del self.spots_hit[last_spot]
            if len(self.scores) % 3 == 0 and self.turn_scores:
                self.turn_scores.pop()
            self.update_stats()


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

    def undo_last_turn(self):
        current_player = self.players[self.current_player]
        if current_player.history:
            last_score, last_spot = current_player.history[-1]
            current_player.score += last_score
            current_player.undo_last_score()
            self.num_of_darts -= 1

    def turn(self, score, multiplier): # THIS LOGIC DOES NOT FUCKING WORK !!!!!!!!!
        current_player = self.players[self.current_player]
        current_player.score -= score * multiplier
        spot = self.calculate_spot(score, multiplier)
        current_player.add_score(score * multiplier, spot)
        # Add logic to determine if the turn is over, if there's a winner, or if there's a bust
        turn_over = False
        winner = None
        bust = False
        # Example logic for determining winner or bust
        if current_player.score == 0 and multiplier == 2:
            winner = current_player
        elif current_player.score <= 1:
            bust = True
            current_player.score += score * multiplier  # Revert the score change
        return turn_over, winner, bust

    def calculate_spot(self, score, multiplier):
        if score == 25 or score == 50:
            return str(score)
        elif multiplier == 2:
            return f"D{score}"
        elif multiplier == 3:
            return f"T{score}"
        else:
            return str(score)

    def return_set_finishes(self, target_score):
        dart_finish = {
            170: ["T20", "T20", "D25"],
            167: ["T20", "T19", "D25"],
            164: ["T20", "T18", "D25"],
            161: ["T20", "T17", "D25"],
            160: ["T20", "T20", "D20"],
            158: ["T20", "T20", "D19"],
            157: ["T20", "T19", "D20"],
            156: ["T20", "T20", "D18"],
            155: ["T20", "T19", "D19"],
            154: ["T20", "T18", "D20"],
            153: ["T20", "T19", "D18"],
            152: ["T20", "T20", "D16"],
            151: ["T20", "T17", "D20"],
            150: ["T20", "T18", "D18"],
            149: ["T20", "T19", "D16"],
            148: ["T20", "T16", "D20"],
            147: ["T20", "T17", "D18"],
            146: ["T20", "T18", "D16"],
            145: ["T20", "T15", "D20"],
            144: ["T20", "T20", "D12"],
            143: ["T20", "T17", "D16"],
            142: ["T20", "T14", "D20"],
            141: ["T20", "T19", "D12"],
            140: ["T20", "T20", "D10"],
            139: ["T20", "T13", "D20"],
            138: ["T20", "T18", "D12"],
            137: ["T20", "T15", "D16"],
            136: ["T20", "T20", "D8"],
            135: ["T20", "T15", "D15"],
            134: ["T20", "T14", "D16"],
            133: ["T20", "T19", "D8"],
            132: ["T20", "T16", "D12"],
            131: ["T20", "T13", "D16"],
            130: ["T20", "T20", "D5"],
            129: ["T19", "T16", "D12"],
            128: ["T18", "T14", "D16"],
            127: ["T20", "T17", "D8"],
            126: ["T19", "T19", "D6"],
            125: ["T20", "T15", "D10"],
            124: ["T20", "T16", "D8"],
            123: ["T19", "T16", "D9"],
            122: ["T18", "T20", "D4"],
            121: ["T20", "T11", "D14"],
            120: ["T20", "20", "D20"],
            119: ["T19", "T12", "D13"],
            118: ["T20", "18", "D20"],
            117: ["T20", "17", "D20"],
            116: ["T20", "16", "D20"],
            115: ["T20", "15", "D20"],
            114: ["T20", "14", "D20"],
            113: ["T20", "13", "D20"],
            112: ["T20", "12", "D20"],
            111: ["T20", "11", "D20"],
            110: ["T20", "10", "D20"],
            109: ["T20", "9", "D20"],
            108: ["T20", "8", "D20"],
            107: ["T19", "10", "D20"],
            106: ["T20", "6", "D20"],
            105: ["T20", "5", "D20"],
            104: ["T18", "10", "D20"],
            103: ["T19", "6", "D20"],
            102: ["T20", "10", "D16"],
            101: ["T17", "10", "D20"],
            100: ["T20", "D20"],
            99: ["T19", "10", "D16"],
            98: ["T20", "D19"],
            97: ["T19", "D20"],
            96: ["T20", "D18"],
            95: ["T19", "D19"],
            94: ["T18", "D20"],
            93: ["T19", "D18"],
            92: ["T20", "D16"],
            91: ["T17", "D20"],
            90: ["T18", "D18"],
            89: ["T19", "D16"],
            88: ["T16", "D20"],
            87: ["T17", "D18"],
            86: ["T18", "D16"],
            85: ["T15", "D20"],
            84: ["T20", "D12"],
            83: ["T17", "D16"],
            82: ["T14", "D20"],
            81: ["T19", "D12"],
            80: ["T20", "D10"],
            79: ["T13", "D20"],
            78: ["T18", "D12"],
            77: ["T15", "D16"],
            76: ["T20", "D8"],
            75: ["T17", "D12"],
            74: ["T14", "D16"],
            73: ["T19", "D8"],
            72: ["T16", "D12"],
            71: ["T13", "D16"],
            70: ["T18", "D8"],
            69: ["T19", "D6"],
            68: ["T16", "D10"],
            67: ["T17", "D8"],
            66: ["T10", "D18"],
            65: ["T19", "D4"],
            64: ["T16", "D8"],
            63: ["T13", "D12"],
            62: ["T10", "D16"],
            61: ["T15", "D8"],
            60: ["20", "D20"],
            59: ["19", "D20"],
            58: ["18", "D20"],
            57: ["17", "D20"],
            56: ["16", "D20"],
            55: ["15", "D20"],
            54: ["14", "D20"],
            53: ["13", "D20"],
            52: ["20", "D16"],
            51: ["19", "D16"],
            50: ["18", "D16"],
            49: ["17", "D16"],
            48: ["16", "D16"],
            47: ["15", "D16"],
            46: ["14", "D16"],
            45: ["13", "D16"],
            44: ["12", "D16"],
            43: ["11", "D16"],
            42: ["10", "D16"],
            41: ["9", "D16"],
            40: ["8", "D16"],
            39: ["7", "D16"],
            38: ["6", "D16"],
            37: ["5", "D16"],
            36: ["4", "D16"],
            35: ["3", "D16"],
            34: ["2", "D16"],
            33: ["1", "D16"],
            32: ["D16"],
            31: ["15", "D8"],
            30: ["D15"],
            29: ["13", "D8"],
            28: ["D14"],
            27: ["11", "D8"],
            26: ["D13"],
            25: ["9", "D8"],
            24: ["D12"],
            23: ["7", "D8"],
            22: ["D11"],
            21: ["5", "D8"],
            20: ["D10"],
            19: ["3", "D8"],
            18: ["D9"],
            17: ["1", "D8"],
            16: ["D8"],
            15: ["7", "D4"],
            14: ["D7"],
            13: ["5", "D4"],
            12: ["D6"],
            11: ["3", "D4"],
            10: ["D5"],
            9: ["1", "D4"],
            8: ["D4"],
            7: ["3", "D2"],
            6: ["D3"],
            5: ["1", "D2"],
            4: ["D2"],
            3: ["1", "D1"],
            2: ["D1"],
            1: ["Not finishable"]
        }
        if target_score in dart_finish:
            return dart_finish[target_score]
        else:
            return None

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

