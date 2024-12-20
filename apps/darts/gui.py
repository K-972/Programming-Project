import tkinter as tk
from tkinter import ttk
import time


class DartsGameSetup:
    def __init__(self, root):
        self.root = root
        self.root.title("Darts Game Setup")
        self.root.geometry("400x500")
        self.root.configure(bg="#2c2f31")

        self.game_type_var = tk.StringVar(value="501")
        self.sets_var = tk.StringVar(value="1")
        self.legs_var = tk.StringVar(value="1")
        self.player_entries = []

        self.create_widgets()

    def create_widgets(self):
        game_type_label = tk.Label(self.root, text="Game Type", bg="#2c2f31", font=("Arial", 12, "bold"))
        game_type_label.pack(pady=5)

        game_types = ["301", "501", "ATC", "KILLER", "PRACTICE"]
        game_type_frame = tk.Frame(self.root, bg="#2c2f31")
        game_type_frame.pack()

        for game in game_types:
            rb = tk.Radiobutton(game_type_frame, text=game, variable=self.game_type_var, value=game, bg="#2c2f31", fg="white")
            rb.pack(side=tk.LEFT, padx=5)

        sets_label = tk.Label(self.root, text="Sets", bg="#2c2f31", font=("Arial", 12, "bold"))
        sets_label.pack(pady=5)
        sets_entry = tk.Entry(self.root, textvariable=self.sets_var)
        sets_entry.pack(pady=5)

        legs_label = tk.Label(self.root, text="Legs", bg="#2c2f31", font=("Arial", 12, "bold"))
        legs_label.pack(pady=5)
        legs_entry = tk.Entry(self.root, textvariable=self.legs_var)
        legs_entry.pack(pady=5)

        players_label = tk.Label(self.root, text="Players", bg="#2c2f31", font=("Arial", 12, "bold"))
        players_label.pack(pady=5)

        for i in range(4):
            player_var = tk.StringVar()
            player_entry = tk.Entry(self.root, textvariable=player_var)
            player_entry.pack(pady=5)
            self.player_entries.append(player_var)

        start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        start_button.pack(pady=20)

        self.result_label = tk.Label(self.root, text="", bg="#2c2f31", fg="white", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=5)

    def start_game(self):
        game_type = self.game_type_var.get()
        if game_type == "ATC":
            game_type = "Around The Clock"
        sets = self.sets_var.get()
        legs = self.legs_var.get()
        players = [player.get() for player in self.player_entries if player.get()]

        if len(players) <= 2:
            self.result_label.config(text=f"Game Started: {game_type}, {sets}, {legs} with {players}")
            time.sleep(5)
            self.root.destroy()
            new_root = tk.Tk()
            app = three_0_1(new_root)
            new_root.mainloop()
        else:
            self.result_label.config(text=f"Game Started: {game_type}, {sets}, {legs} with {players}")

class three_0_1:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title(f"301")
        self.root.geometry("400x500")
        self.root.configure(bg="#2c2f31")
        self.root.attributes("-fullscreen", True)

if __name__ == "__main__":
    root = tk.Tk()
    app = DartsGameSetup(root)
    root.mainloop()



