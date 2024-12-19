import tkinter as tk
from tkinter import ttk

# Function to handle game start
def start_game():
    game_type = game_type_var.get()
    if game_type == "ATC":
        game_type = "Around The Clock"
    sets = sets_var.get()
    legs = legs_var.get()
    players = [player.get() for player in player_entries if player.get()]
    
    if len(players) < 2:
        result_label.config(text="Please add at least 2 players.")
    else:
        result_label.config(text=f"Game Started: {game_type}, {sets}, {legs} with {players}")

# GUI Application
root = tk.Tk()
root.title("Darts Game Setup")
root.geometry("400x500")
root.configure(bg="#2c2f31")

# Game Type Selection
game_type_label = tk.Label(root, text="Game Type", bg="#2c2f31", font=("Arial", 12, "bold"))
game_type_label.pack(pady=5)

game_type_var = tk.StringVar(value="501")
game_types = ["301", "501", "ATC", "KILLER", "PRACTICE"]
game_type_frame = tk.Frame(root, bg="#2c2f31")
game_type_frame.pack()

for game in game_types:
    rb = ttk.Radiobutton(game_type_frame, text=game, variable=game_type_var, value=game)
    rb.pack(side="left", padx=5)

# Sets Selection
sets_label = tk.Label(root, text="Sets", bg="#2c2f31", font=("Arial", 12, "bold"))
sets_label.pack(pady=5)

sets_var = tk.StringVar(value="No sets")
sets_dropdown = ttk.Combobox(root, textvariable=sets_var, values=["No sets", "1 set", "2 sets", "3 sets"])
sets_dropdown.pack(pady=5)

# Legs Selection
legs_label = tk.Label(root, text="Legs", bg="#2c2f31", font=("Arial", 12, "bold"))
legs_label.pack(pady=5)

legs_var = tk.StringVar(value="3 legs")
legs_dropdown = ttk.Combobox(root, textvariable=legs_var, values=["1 leg", "3 legs", "5 legs"])
legs_dropdown.pack(pady=5)

# Player Section
players_label = tk.Label(root, text="Players", bg="#2c2f31", font=("Arial", 12, "bold"))
players_label.pack(pady=5)

player_entries = []
player_frame = tk.Frame(root, bg="#2c2f31")
player_frame.pack(pady=5)

def add_player():
    if len(player_entries) < 4:  # Limit to 4 players
        player_var = tk.StringVar()
        entry = ttk.Entry(player_frame, textvariable=player_var, foreground='grey')
        
        # Placeholder functionality
        placeholder = f"Player {len(player_entries) + 1} name"
        player_var.set(placeholder)

        def on_focus_in(event, var=player_var, placeholder_text=placeholder):
            if var.get() == placeholder_text:
                entry.config(foreground='white')
                var.set("")

        def on_focus_out(event, var=player_var, placeholder_text=placeholder):
            if not var.get():
                entry.config(foreground='grey')
                var.set(placeholder_text)

        # Bind focus events for placeholder effect
        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

        entry.pack(pady=2)
        player_entries.append(player_var)

def remove_player():
    if player_entries:
        player_entries.pop().set("")
        player_frame.pack_slaves()[-1].destroy()


# player controller buttons
add_button = tk.Button(player_frame, text="+ Add Player", command=add_player)
add_button.pack(side="left", padx=5)

remove_button = tk.Button(player_frame, text="- Remove Player", command=remove_player)
remove_button.pack(side="left", padx=5)

# Start Button
start_button = tk.Button(root, text="START GAME", command=start_game, bg="#4da8f5", fg="black", font=("Arial", 12, "bold"))
start_button.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", bg="#2c2f31", fg="red", font=("Arial", 10))
result_label.pack(pady=10)

root.mainloop()
