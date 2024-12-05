import json
import os
from datetime import datetime

class DartDatabase:
    def __init__(self, filename='dart_database.json'):
        self.filename = filename
        # Check if the file exists; if not, create an empty file
        if not os.path.isfile(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)

    def add_throw(self, game_id, player_id, x, y):
        # Read the existing data
        with open(self.filename, 'r') as f:
            data = json.load(f)

        # Create a new throw record
        new_throw = {
            'throw_id': len(data) + 1,
            'game_id': game_id,
            'player_id': player_id,
            'x_coord': x,
            'y_coord': y,
            'timestamp': datetime.now().isoformat()
        }
        
        # Append the new throw
        data.append(new_throw)
        
        # Write data back to the file
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        print("Throw added:", new_throw)

    def get_throws_by_game(self, game_id):
        with open(self.filename, 'r') as f:
            data = json.load(f)
        # Filter throws by game ID
        return [throw for throw in data if throw['game_id'] == game_id]

    def get_all_throws(self):
        with open(self.filename, 'r') as f:
            return json.load(f)
