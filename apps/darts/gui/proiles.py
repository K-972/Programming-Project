import json
import math

class Profiles:
    def __init__(self, filename="profiles.json"):
        self.filename = filename
        self.profiles = self.load_profiles()

    def load_profiles(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def change_profile_name(self, old_name, new_name):
        for profile in self.profiles:
            if profile["name"] == old_name:
                profile["name"] = new_name
                self.save_profiles()
                return True
        return False

    def delete_profile(self, profile_name):
        for profile in self.profiles:
            if profile["name"] == profile_name:
                self.profiles.remove(profile)
                self.save_profiles()
                return True
        return False

    def save_profiles(self):
        with open(self.filename, 'w') as file:
            json.dump(self.profiles, file, indent=4)

    def create_profile(self, profile_data):
        self.profiles.append(profile_data)
        self.save_profiles()

    def profile_template(self):
        return {
            "name": "",
            "elo": 0,
            "lifetime_dart_stats": {
                "games_played": 0,
                "wins": 0,
                "losses": 0,
                "highest_3_dart_score": 0,
                "single_dart_avg": 0,
                "three_dart_avg": 0,
                "standard_deviation": 0,
                "checkout_percentage": 0,
                "darts_thrown": []
            },
            "achievements": []
        }

    def record_dart_throw(self, profile_name, score, multiplier, bust=False, win=False):
        for profile in self.profiles:
            if profile["name"] == profile_name:
                if bust:
                    # Handle bust: reset the current set of 3 darts
                    if profile["lifetime_dart_stats"]["darts_thrown"] and len(profile["lifetime_dart_stats"]["darts_thrown"][-1]) < 3:
                        profile["lifetime_dart_stats"]["darts_thrown"].pop()
                else:
                    if not profile["lifetime_dart_stats"]["darts_thrown"] or len(profile["lifetime_dart_stats"]["darts_thrown"][-1]) >= 3:
                        profile["lifetime_dart_stats"]["darts_thrown"].append([])  # Start a new set of 3 darts
                    profile["lifetime_dart_stats"]["darts_thrown"][-1].append(score * multiplier)

                if win:
                    profile["lifetime_dart_stats"]["wins"] += 1
                    profile["lifetime_dart_stats"]["games_played"] += 1
                    # Fill the remaining turns up to 3 darts with None
                    while len(profile["lifetime_dart_stats"]["darts_thrown"][-1]) < 3:
                        profile["lifetime_dart_stats"]["darts_thrown"][-1].append(None)
                elif bust:
                    # Do not increment losses here, handle it when the game ends
                    pass

                self.update_stats(profile)
                self.save_profiles()
                break

    def update_stats(self, profile):
        darts = [score for set_of_darts in profile["lifetime_dart_stats"]["darts_thrown"] for score in set_of_darts if score is not None]
        if darts:
            profile["lifetime_dart_stats"]["single_dart_avg"] = round(sum(darts) / len(darts), 2)
            profile["lifetime_dart_stats"]["three_dart_avg"] = round(sum(darts) / (len(darts) / 3), 2)
            profile["lifetime_dart_stats"]["highest_3_dart_score"] = round(max([sum(darts[i:i+3]) for i in range(0, len(darts), 3)]), 2)
            profile["lifetime_dart_stats"]["standard_deviation"] = round(self.calculate_standard_deviation(darts), 2)
            # Add more stats calculations as needed

    def calculate_standard_deviation(self, darts):
        mean = sum(darts) / len(darts)
        variance = sum((x - mean) ** 2 for x in darts) / len(darts)
        return round(math.sqrt(variance), 2)

    def update_profile_stats(self, profile_name, game_result):
        for profile in self.profiles:
            if profile["name"] == profile_name:
                stats = profile["lifetime_dart_stats"]
                stats["games_played"] += 1
                if game_result == "win":
                    stats["wins"] += 1
                elif game_result == "loss":
                    stats["losses"] += 1
                self.update_stats(profile)
                self.save_profiles()
                break

    def test_create_profile(self):
        new_profile = self.profile_template()
        new_profile["name"] = "Roman"
        self.create_profile(new_profile)
        print(f"Profile created: {new_profile}")

if __name__ == "__main__":
    profiles = Profiles()
    profiles.test_create_profile()
