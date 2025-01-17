import json

class Profiles:
    def __init__(self, filename="profiles.json"):
        self.filename = filename
        self.profiles = self.load_profiles()

    def load_profiles(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

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

    def record_dart_throw(self, profile_name, score, multiplier):
        for profile in self.profiles:
            if profile["name"] == profile_name:
                profile["lifetime_dart_stats"]["darts_thrown"].append(score)
                self.update_stats(profile)
                self.save_profiles()
                break

    def update_stats(self, profile):
        darts = profile["lifetime_dart_stats"]["darts_thrown"]
        if darts:
            profile["lifetime_dart_stats"]["single_dart_avg"] = sum(darts) / len(darts)
            profile["lifetime_dart_stats"]["three_dart_avg"] = sum(darts) / (len(darts) / 3)
            profile["lifetime_dart_stats"]["highest_3_dart_score"] = max([sum(darts[i:i+3]) for i in range(0, len(darts), 3)])
            # Add more stats calculations as needed

    def test_create_profile(self):
        new_profile = self.profile_template()
        new_profile["name"] = "Roman"
        self.create_profile(new_profile)
        print(f"Profile created: {new_profile}")

if __name__ == "__main__":
    profiles = Profiles()
    profiles.test_create_profile()
