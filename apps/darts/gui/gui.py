from operator import ne
import customtkinter as ctk
from tkinter import messagebox
from dartlogic import Game
from proiles import Profiles

class MainGame:
    def __init__(self, root, game_options, start_number) -> None:
        self.root = root
        self.root.title(start_number)
        self.root.geometry("1280x720")
        self.root.configure(bg="#2c2f31")
        self.root.attributes("-fullscreen", True)
        self.start_number = start_number

        self.players = game_options[3]
        self.game_options = game_options

        self.game = Game(self.players, start_number)
        self.current_dart_scores = []  # Track scores for the current turn
        self.multiplier = 1  # Initialize multiplier with default value

        self.profiles = Profiles()  # Initialize Profiles instance

        self.create_widgets()

        print(self.game.players[self.game.current_player].score)

    def set_multiplier(self, multiplier_type):
        if multiplier_type == 'Treble':
            self.multiplier = 3
        elif multiplier_type == 'Double':
            self.multiplier = 2
        else:
            self.multiplier = 1

    def miss(self):
        self.turn(0, 1)

    def undo(self):
        # Handle undo action
        if self.current_dart_scores:
            last_score = self.current_dart_scores.pop()
            self.game.undo_last_turn()
            self.update_ui()
            print("Undo last action")

    def confirm_score(self):
        # Handle confirm score action
        print("Score confirmed")
        self.next_turn()

    def turn(self, score, multiplier):
        if len(self.current_dart_scores) >= 3:
            messagebox.showinfo("Turn Over", "Please press the Confirm button to proceed to the next turn.")
            return

        self.current_dart_scores.append((score, multiplier))
        turn_over, winner, Bust = self.game.turn(score, multiplier)
        self.update_ui()
        self.multiplier = 1  # Reset multiplier after every throw
        if winner:
            self.show_winner_popup(winner)
        elif Bust:
            self.show_bust_popup()
        elif turn_over:
            self.show_confirm_button()
        elif len(self.current_dart_scores) == 3:
            self.show_confirm_button()

    def show_confirm_button(self):
        print("Showing confirm button")  # Debugging line
        self.confirm_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10)
        self.root.update_idletasks()  # Force the GUI to update

    def next_turn(self):
        self.confirm_button.grid_forget()
        self.current_dart_scores = []  # Reset dart scores for the next turn
        self.game.switch_player()
        self.update_ui()

    def update_ui(self):
        current_player = self.game.players[self.game.current_player]
        self.current_player_label.configure(text=f"Current Player: {current_player.name}")
        self.current_score_label.configure(text=f"Score: {current_player.score}")

        # Calculate and update finish
        finishes = self.game.return_set_finishes(current_player.score)
        if finishes:
            finish_text = ", ".join(["-".join(finish) for finish in finishes[:3]])  # Show up to 3 finishes
        else:
            finish_text = "N/A"
        self.finish_label.configure(text=f"Finish: {finish_text}")

        # Update dart scores
        dart_scores = [f"Dart {i+1}: {score * multiplier}" for i, (score, multiplier) in enumerate(self.current_dart_scores)]
        self.dart1_label.configure(text=dart_scores[0] if len(dart_scores) > 0 else "Dart 1: 0")
        self.dart2_label.configure(text=dart_scores[1] if len(dart_scores) > 1 else "Dart 2: 0")
        self.dart3_label.configure(text=dart_scores[2] if len(dart_scores) > 2 else "Dart 3: 0")

        # Update player frames
        for i, player in enumerate(self.game.players):
            self.player_frames[i]['current_score_value'].configure(text=str(player.score))
            self.player_frames[i]['darts_thrown_value'].configure(text=str(player.darts_thrown))
            self.player_frames[i]['avg_score_per_dart_value'].configure(text=f"{player.avg_score_per_dart:.2f}")
            self.player_frames[i]['highest_score_value'].configure(text=str(player.highest_3_dart_score))
            self.player_frames[i]['lowest_score_value'].configure(text=f"{player.standard_deviation:.2f}")
            self.player_frames[i]['most_hit_value'].configure(text=str(player.most_spot_hit))
            self.player_frames[i]['standard_deviation_value'].configure(text=f"{player.standard_deviation:.2f}")

    def create_widgets(self):
        num_of_players = len(self.players)
        self.player_frames = []

        # Adjust font size based on the number of players
        label_font_size = 16
        value_font_size = 18
        if num_of_players > 6:
            label_font_size = 14
            value_font_size = 16
        if num_of_players > 10:
            label_font_size = 12
            value_font_size = 14

        # Configure grid weights for dynamic resizing
        for i in range(2):  # Assuming a maximum of 2 rows
            self.root.grid_rowconfigure(i, weight=1)
        for i in range((num_of_players + 1) // 2):  # Number of columns needed
            self.root.grid_columnconfigure(i, weight=1)

        # Player frames on the left
        for i in range(num_of_players):
            player_frame = ctk.CTkFrame(self.root, fg_color="#2c2f31")
            player_frame.grid(row=i % 2, column=i // 2, padx=10, pady=20, sticky="nsew")

            player_frame.grid_rowconfigure(0, weight=1)
            player_frame.grid_rowconfigure(1, weight=1)
            player_frame.grid_rowconfigure(2, weight=1)
            player_frame.grid_rowconfigure(3, weight=1)
            player_frame.grid_rowconfigure(4, weight=1)
            player_frame.grid_rowconfigure(5, weight=1)
            player_frame.grid_rowconfigure(6, weight=1)
            player_frame.grid_rowconfigure(7, weight=1)
            player_frame.grid_rowconfigure(8, weight=1)
            player_frame.grid_rowconfigure(9, weight=1)
            player_frame.grid_columnconfigure(0, weight=1)
            player_frame.grid_columnconfigure(1, weight=1)

            def create_label_value_pair(row, label_text, value_text):
                label = ctk.CTkLabel(
                    player_frame, 
                    text=label_text, 
                    text_color="white", 
                    font=("Arial", label_font_size, "bold")
                )
                label.grid(row=row, column=0, pady=(0, 5), sticky="w")
                value = ctk.CTkLabel(
                    player_frame, 
                    text=value_text, 
                    font=("Arial", value_font_size)
                )
                value.grid(row=row, column=1, pady=(0, 5), sticky="w")
                return label, value

            player = self.game.players[i]
            player_name_label, player_name_value = create_label_value_pair(0, "Player Name:", player.name)
            finish_label, finish_value = create_label_value_pair(1, "Finish:", "0")
            current_score_label, current_score_value = create_label_value_pair(2, "Current Score:", str(player.score))
            darts_thrown_label, darts_thrown_value = create_label_value_pair(3, "Darts Thrown:", str(player.darts_thrown))
            avg_score_per_dart_label, avg_score_per_dart_value = create_label_value_pair(4, "Avg Score /dart:", f"{player.avg_score_per_dart:.2f}")
            lowest_score_label, lowest_score_value = create_label_value_pair(6, "Avg Score 3 dart:", f"{player.most_spot_hit:.2f}%")
            highest_score_label, highest_score_value = create_label_value_pair(5, "Highest Score:", str(player.highest_3_dart_score))
            most_hit_label, most_hit_value = create_label_value_pair(7, "Most Hit:", str(player.most_spot_hit))
            standard_deviation_label, standard_deviation_value = create_label_value_pair(8, "Standard dev:", f"{player.standard_deviation:.2f}")

            self.player_frames.append({
                'frame': player_frame,
                'player_name_label': player_name_label,
                'player_name_value': player_name_value,
                'finish_label': finish_label,
                'finish_value': finish_value,
                'current_score_label': current_score_label,
                'current_score_value': current_score_value,
                'darts_thrown_label': darts_thrown_label,
                'darts_thrown_value': darts_thrown_value,
                'avg_score_per_dart_label': avg_score_per_dart_label,
                'avg_score_per_dart_value': avg_score_per_dart_value,
                'highest_score_label': highest_score_label,
                'highest_score_value': highest_score_value,
                'lowest_score_label': lowest_score_label,
                'lowest_score_value': lowest_score_value,
                'most_hit_label': most_hit_label,
                'most_hit_value': most_hit_value,
                'standard_deviation_label': standard_deviation_label,
                'standard_deviation_value': standard_deviation_value
            })

        # Scoring system on the right
        scoring_frame = ctk.CTkFrame(self.root, fg_color="#2c2f31")
        scoring_frame.grid(row=0, column=(num_of_players + 1) // 2, rowspan=2, padx=10, pady=20, sticky="nsew")

        label = ctk.CTkLabel(
            scoring_frame, 
            text=f"Welcome to {self.start_number} Game!", 
            fg_color="#2c2f31", 
            text_color="white", 
            font=("Arial", 24, "bold")
        )
        label.grid(row=0, column=0, columnspan=2, pady=20)

        # Current Player Label
        self.current_player_label = ctk.CTkLabel(
            scoring_frame, 
            text=f"Current Player: {self.game.players[self.game.current_player].name}", 
            font=("Helvetica", 18)
        )
        self.current_player_label.grid(row=1, column=0, columnspan=2, pady=10)

        # Current Score Label
        self.current_score_label = ctk.CTkLabel(
            scoring_frame, 
            text=f"Score: {self.game.players[self.game.current_player].score}", 
            font=("Helvetica", 16)
        )
        self.current_score_label.grid(row=2, column=0, columnspan=2, pady=5)

        # Finish Label
        self.finish_label = ctk.CTkLabel(
            scoring_frame, 
            text="Finish: 0", 
            font=("Helvetica", 16)
        )
        self.finish_label.grid(row=3, column=0, columnspan=2, pady=5)

        # Dart Scores Labels
        self.dart1_label = ctk.CTkLabel(
            scoring_frame, 
            text="Dart 1: 0", 
            font=("Helvetica", 16)
        )
        self.dart1_label.grid(row=4, column=0, columnspan=2, pady=5)

        self.dart2_label = ctk.CTkLabel(
            scoring_frame, 
            text="Dart 2: 0", 
            font=("Helvetica", 16)
        )
        self.dart2_label.grid(row=5, column=0, columnspan=2, pady=5)

        self.dart3_label = ctk.CTkLabel(
            scoring_frame, 
            text="Dart 3: 0", 
            font=("Helvetica", 16)
        )
        self.dart3_label.grid(row=6, column=0, columnspan=2, pady=5)

        # Buttons Frame
        buttons_frame = ctk.CTkFrame(scoring_frame, fg_color="#2c2f31")
        buttons_frame.grid(row=7, column=0, columnspan=2, pady=10)

        # Miss Button
        miss_button = ctk.CTkButton(
            buttons_frame, 
            text="Miss", 
            width=80, 
            height=40, 
            command=self.miss
        )
        miss_button.grid(row=0, column=0, padx=5, pady=5)

        # Undo Button
        undo_button = ctk.CTkButton(
            buttons_frame, 
            text="Undo", 
            width=80, 
            height=40, 
            command=self.undo
        )
        undo_button.grid(row=0, column=1, padx=5, pady=5)

        # Confirm Score Button
        self.confirm_button = ctk.CTkButton(
            buttons_frame, 
            text="Confirm", 
            width=80, 
            height=40, 
            command=self.confirm_score
        )
        self.confirm_button.grid(row=0, column=2, padx=5, pady=5)
        self.confirm_button.grid_forget()  # Hide the confirm button initially

        # Number Pad Frame
        keypad_frame = ctk.CTkFrame(scoring_frame, fg_color="#2c2f31")
        keypad_frame.grid(row=8, column=0, columnspan=2, pady=10)

        # Number Buttons 1-20
        numbers = list(range(1, 21))
        rows = 4
        cols = 5
        for index, number in enumerate(numbers):
            row = index // cols
            col = index % cols
            button = ctk.CTkButton(
                keypad_frame, 
                text=str(number), 
                width=60, 
                height=60, 
                command=lambda num=number: self.turn(num, self.multiplier)
            )
            button.grid(row=row, column=col, padx=5, pady=5)

        # Special Buttons Frame
        special_frame = ctk.CTkFrame(scoring_frame, fg_color="#2c2f31")
        special_frame.grid(row=9, column=0, columnspan=2, pady=10)

        # Treble Button
        treble_button = ctk.CTkButton(
            special_frame, 
            text="Treble", 
            width=100, 
            height=60, 
            command=lambda: self.set_multiplier('Treble')
        )
        treble_button.grid(row=0, column=0, padx=5, pady=5)

        # Double Button
        double_button = ctk.CTkButton(
            special_frame, 
            text="Double", 
            width=100, 
            height=60, 
            command=lambda: self.set_multiplier('Double')
        )
        double_button.grid(row=0, column=1, padx=5, pady=5)

        # 25 Button
        twenty_five_button = ctk.CTkButton(
            special_frame, 
            text="25", 
            width=100, 
            height=60, 
            command=lambda: self.turn(25, 1)
        )
        twenty_five_button.grid(row=1, column=0, padx=5, pady=5)

        # 50 Button
        fifty_button = ctk.CTkButton(
            special_frame, 
            text="50", 
            width=100, 
            height=60, 
            command=lambda: self.turn(50, 1)
        )
        fifty_button.grid(row=1, column=1, padx=5, pady=5)

    def show_bust_popup(self):
        messagebox.showinfo("Bust!", "You have busted! Next player's turn.")

    def show_winner_popup(self, winner):
        result = messagebox.askquestion("Winner!", f"{winner.name} wins the game! Do you want to replay or go back to the main menu?", icon='info', type='yesnocancel', default='yes', detail='Yes: Replay\nNo: Main Menu\nCancel: Exit')
        if result == 'yes':
            self.replay_game()
        elif result == 'no':
            self.go_back_to_main_menu()
        else:
            self.root.quit()

    def replay_game(self):
        # Logic to reset the game state and start a new game
        self.game = Game(self.players, self.start_number)
        self.current_dart_scores = []
        self.update_ui()

    def go_back_to_main_menu(self):
        # Logic to go back to the main menu
        self.root.quit()
        # You can add logic here to show the main menu if you have one

class Settings:
    def __init__(self, root):
        self.root = root
        self.root.title("Settings")
        self.root.geometry("800x600")  # Adjusted size for better fullscreen handling
        self.root.configure(bg="#2c2f31")
        self.root.attributes("-fullscreen", True)  # Open in fullscreen

        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        main_frame = ctk.CTkFrame(self.root, fg_color="#2c2f31")
        main_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        # Back Button
        back_button = ctk.CTkButton(
            main_frame,
            text="Back",
            command=self.go_back,
            fg_color="gray",  # Changed from default blue to gray
            font=("Helvetica", 24),  # Increased font size
            hover_color="#3a3d40",  # Darker hover color
            width=100,  # Increased width
            height=40  # Increased height
        )
        back_button.pack(anchor="nw", pady=(0, 10))

        # Settings Label
        settings_label = ctk.CTkLabel(main_frame, text="Settings", font=("Helvetica", 16))
        settings_label.pack(pady=10)

        # Audio Settings
        audio_label = ctk.CTkLabel(main_frame, text="Audio Settings", font=("Helvetica", 14))
        audio_label.pack(pady=(20, 10))

        # Volume Slider
        volume_label = ctk.CTkLabel(main_frame, text="Volume:")
        volume_label.pack(pady=(10, 0))
        self.volume_slider = ctk.CTkSlider(main_frame, from_=0, to=100, number_of_steps=100)
        self.volume_slider.set(50)
        self.volume_slider.pack(pady=5)

        # Mute Checkbox
        self.mute_var = ctk.BooleanVar()
        mute_checkbox = ctk.CTkCheckBox(main_frame, text="Mute", variable=self.mute_var)
        mute_checkbox.pack(pady=5)

        visual_label = ctk.CTkLabel(main_frame, text="Visual Settings", font=("Helvetica", 14))
        visual_label.pack(pady=(20, 10))

        # Light Mode Checkbox
        self.light_mode_var = ctk.BooleanVar()
        light_mode_checkbox = ctk.CTkCheckBox(main_frame, text="Light Mode", variable=self.light_mode_var)
        light_mode_checkbox.pack(pady=5)

        # Save Button
        save_button = ctk.CTkButton(main_frame, text="Save", command=self.save_settings)
        save_button.pack(pady=20)

    def go_back(self):
        self.root.destroy()
        self.menu = MainMenu()

    def save_settings(self):
        volume = self.volume_slider.get()
        mute = self.mute_var.get()
        light_mode = self.light_mode_var.get()
        # Add logic to save settings
        print(f"Settings saved - Volume: {volume}, Mute: {mute}, Light Mode: {light_mode}")




class DartsGameSetup:
    def __init__(self, root):
        self.root = root
        self.root.title("Darts Game Setup")
        self.root.geometry("800x600")  # Adjusted size for better fullscreen handling
        self.root.configure(bg="#2c2f31")
        self.root.attributes("-fullscreen", True)  # Open in fullscreen

        self.game_type_var = ctk.StringVar(value="501")
        self.sets_var = ctk.StringVar(value="1")
        self.legs_var = ctk.StringVar(value="1")
        self.player_entries = []

        self.profiles = Profiles()  # Load profiles
        self.profile_names = [profile["name"] for profile in self.profiles.profiles]  # Extract profile names

        self.create_widgets()

    def create_widgets(self):
        main_frame = ctk.CTkFrame(self.root, fg_color="#2c2f31")
        main_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        top_frame = ctk.CTkFrame(main_frame, fg_color="#2c2f31")
        top_frame.pack(fill=ctk.X, pady=(0, 10))

        back_button = ctk.CTkButton(
            top_frame, 
            text="Back", 
            command=self.go_back, 
            fg_color="#2c2f31", 
            text_color="white",
            hover_color="#3a3d40",
            border_width=0,
            width=100,
            height=50,
            font=("Arial", 16)
        )
        back_button.pack(side=ctk.LEFT)

        game_type_label = ctk.CTkLabel(
            main_frame, 
            text="Game Type", 
            fg_color="#2c2f31", 
            text_color="white", 
            font=("Arial", 16, "bold")
        )
        game_type_label.pack(pady=(10, 5))

        game_types = ["301", "501", "ATC", "KILLER", "PRACTICE"]
        game_type_frame = ctk.CTkFrame(main_frame, fg_color="#2c2f31")
        game_type_frame.pack(pady=5)

        for game in game_types:
            rb = ctk.CTkRadioButton(
                master=game_type_frame, 
                text=game, 
                variable=self.game_type_var, 
                value=game, 
                fg_color="#3a3d40",
                text_color="white",
                hover_color="#3a3d40"
            )
            rb.pack(side=ctk.LEFT, padx=10)

        sets_label = ctk.CTkLabel(
            main_frame, 
            text="Sets", 
            fg_color="#2c2f31", 
            text_color="white", 
            font=("Arial", 16, "bold")
        )
        sets_label.pack(pady=(20, 5))

        sets_entry = ctk.CTkEntry(main_frame, textvariable=self.sets_var, width=200, fg_color="#3a3d40", text_color="white")
        sets_entry.pack(pady=5)

        legs_label = ctk.CTkLabel(
            main_frame, 
            text="Legs", 
            fg_color="#2c2f31", 
            text_color="white", 
            font=("Arial", 16, "bold")
        )
        legs_label.pack(pady=(20, 5))

        legs_entry = ctk.CTkEntry(main_frame, textvariable=self.legs_var, width=200, fg_color="#3a3d40", text_color="white")
        legs_entry.pack(pady=5)

        players_label = ctk.CTkLabel(
            main_frame, 
            text="Players", 
            fg_color="#2c2f31", 
            text_color="white", 
            font=("Arial", 16, "bold")
        )
        players_label.pack(pady=(20, 10))

        button_frame = ctk.CTkFrame(main_frame, fg_color="#2c2f31")
        button_frame.pack(pady=(0, 10))

        add_player_button = ctk.CTkButton(
            button_frame, 
            text="Add Player", 
            command=self.add_player_slot, 
            fg_color="#2c2f31", 
            text_color="white",
            hover_color="#3a3d40",
            border_width=0
        )
        add_player_button.pack(side=ctk.LEFT, padx=10)

        remove_player_button = ctk.CTkButton(
            button_frame, 
            text="Remove Player", 
            command=self.remove_player_slot, 
            fg_color="#2c2f31", 
            text_color="white",
            hover_color="#3a3d40",
            border_width=0
        )
        remove_player_button.pack(side=ctk.LEFT, padx=10)

        scrollable_frame = ctk.CTkScrollableFrame(main_frame, fg_color="#2c2f31")
        scrollable_frame.pack(fill=ctk.BOTH, expand=True, pady=10)

        self.players_frame = scrollable_frame

        self.add_player_slot()
        self.add_player_slot()

        start_button = ctk.CTkButton(
            main_frame, 
            text="Start Game", 
            command=self.start_game, 
            fg_color="#2c2f31", 
            text_color="white",
            hover_color="#3a3d40",
            border_width=0
        )
        start_button.pack(pady=20)

        self.result_label = ctk.CTkLabel(
            main_frame, 
            text="", 
            fg_color="#2c2f31", 
            text_color="white", 
            font=("Arial", 14, "bold")
        )
        self.result_label.pack(pady=5)

    def add_player_slot(self):
        if len(self.player_entries) >= 12:
            messagebox.showerror("Error", "Maximum number of players is 12.")
            return

        # Add a dropdown to select a profile
        profile_dropdown = ctk.CTkComboBox(self.players_frame, values=self.profile_names, width=300, fg_color="#3a3d40", text_color="white")
        profile_dropdown.pack(pady=5)
        self.player_entries.append(profile_dropdown)

    def remove_player_slot(self):
        if self.player_entries:
            self.player_entries.pop()
            if self.players_frame.winfo_children():
                self.players_frame.winfo_children()[-1].destroy()

    def start_game(self):
        for player in self.player_entries:
            if isinstance(player, ctk.StringVar) and len(player.get()) > 15:
                messagebox.showerror("Error", "Player names must be 15 characters or less.")
                return
        game_type = self.game_type_var.get()
        if game_type == "ATC":
            game_type = "Around The Clock"
        sets = self.sets_var.get()
        legs = self.legs_var.get()
        players = [player.get() if isinstance(player, ctk.StringVar) else player.get() for player in self.player_entries if player.get()]

        if len(players) >= 2:
            game_options = [game_type, sets, legs, players]
            print(f"Starting game with options: {game_options}")  # Debug print
            match game_options[0]:
                case "301":
                    self.root.destroy()
                    new_root = ctk.CTk()
                    print("Initializing MainGame for 301")  # Debug print
                    app = MainGame(new_root, game_options, 301)
                    new_root.mainloop()
                case "501":
                    self.root.destroy()
                    new_root = ctk.CTk()
                    print("Initializing MainGame for 501")  # Debug print
                    app = MainGame(new_root, game_options, 501)
                    new_root.mainloop()
                case "Around The Clock":
                    self.root.destroy()
                    new_root = ctk.CTk()
                    print("Initializing AroundTheClock")  # Debug print
                    app = AroundTheClock(new_root)
                    new_root.mainloop()
                case "KILLER":
                    self.root.destroy()
                    new_root = ctk.CTk()
                    print("Initializing Killer")  # Debug print
                    app = Killer(new_root)
                    new_root.mainloop()
                case "PRACTICE":
                    self.root.destroy()
                    new_root = ctk.CTk()
                    print("Initializing Practice")  # Debug print
                    app = Practice(new_root)
                    new_root.mainloop()
        else:
            messagebox.showerror("Need at least 2 players to start the game.")

    def go_back(self):
        self.root.destroy()
        self.menu = MainMenu()
        print("menu opened")
        self.menu.mainloop()

class profile_screen:
    def __init__(self, root):
        self.root = root
        self.root.title("Profiles")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c2f31")
        self.root.attributes("-fullscreen", True)

        self.profiles = Profiles()
        self.profile_names = [profile["name"] for profile in self.profiles.profiles]

        self.create_widgets()
        self.display_profiles()

    def create_widgets(self):
        # Back Button
        self.back_button = ctk.CTkButton(self.root, text="Back", command=self.go_back)
        self.back_button.pack(fill=ctk.X, padx=10, pady=10)

        # Create Profile Button
        self.create_profile_button = ctk.CTkButton(self.root, text="Create Profile", command=self.create_profile)
        self.create_profile_button.pack(fill=ctk.X, padx=10, pady=10)

        # Container for player profiles
        self.profiles_frame = ctk.CTkFrame(self.root)
        self.profiles_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

    def go_back(self):
        self.root.destroy()
        main_menu = MainMenu()
        main_menu.mainloop()

    def create_profile(self):
        new_profile = self.profiles.profile_template()
        new_profile["name"] = "New Player"  # You can add a dialog to get the name from the user
        self.profiles.create_profile(new_profile)
        self.refresh_profiles()

    def display_profiles(self):
        for profile in self.profiles.profiles:
            self.add_player_profile(profile)

    def add_player_profile(self, profile):
        player_frame = ctk.CTkFrame(self.profiles_frame, height=100)  # Increase the height of the frame
        player_frame.pack(fill=ctk.X, pady=5)

        name_label = ctk.CTkLabel(player_frame, text=profile["name"])
        name_label.pack(side=ctk.LEFT, padx=5)

        button_frame = ctk.CTkFrame(player_frame)  # Create a frame for the buttons
        button_frame.pack(side=ctk.RIGHT, padx=5)

        edit_button = ctk.CTkButton(button_frame, text="Edit", command=lambda p=profile: self.edit_profile(p))
        edit_button.pack(side=ctk.LEFT, padx=5)

        view_button = ctk.CTkButton(button_frame, text="View", command=lambda p=profile: self.view_profile(p))
        view_button.pack(side=ctk.LEFT, padx=5)

    def edit_profile(self, profile):
        # Logic to edit the profile
        pass

    def view_profile(self, profile):
        # Logic to view the profile
        pass

    def refresh_profiles(self):
        for widget in self.profiles_frame.winfo_children():
            widget.destroy()
        self.display_profiles()




class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Menu")
        self.geometry("400x400")
        self.configure(fg_color="#2c2f31")
        self.attributes("-fullscreen", True)
        self.create_main_menu()

    def create_main_menu(self):
        main_menu_frame = ctk.CTkFrame(self, fg_color="#2c2f31")
        main_menu_frame.pack(expand=True, pady=50)

        title_label = ctk.CTkLabel(
            main_menu_frame,
            text="Ethan's Darts App",
            fg_color="#2c2f31",
            text_color="white",
            font=("Arial", 34, "bold")
        )
        title_label.pack(pady=(0, 30))

        play_button = ctk.CTkButton(
            main_menu_frame,
            text="Play",
            command=self.play_game,
            fg_color="#3a3d40",
            text_color="white",
            hover_color="#4a4d50",
            width=200,
            height=40
        )
        play_button.pack(pady=10)

        profiles_button = ctk.CTkButton(
            main_menu_frame,
            text="Profiles",
            command=self.show_profiles,
            fg_color="#3a3d40",
            text_color="white",
            hover_color="#4a4d50",
            width=200,
            height=40
        )
        profiles_button.pack(pady=10)

        settings_button = ctk.CTkButton(
            main_menu_frame,
            text="Settings",
            command=self.open_settings,
            fg_color="#3a3d40",
            text_color="white",
            hover_color="#4a4d50",
            width=200,
            height=40
        )
        settings_button.pack(pady=10)

        quit_button = ctk.CTkButton(
            main_menu_frame,
            text="Quit",
            command=self.quit_application,
            fg_color="#3a3d40",
            text_color="white",
            hover_color="#4a4d50",
            width=200,
            height=40
        )
        quit_button.pack(pady=10)

    def play_game(self):
        self.destroy()
        play_game_root = ctk.CTk()
        app = DartsGameSetup(play_game_root)
        print("Game Setup Window Opened")
        play_game_root.mainloop()



    def show_profiles(self):
        self.destroy()
        profiles_root = ctk.CTk()
        app = profile_screen(profiles_root)
        print("Profiles Window Opened")
        profiles_root.mainloop()

    def open_settings(self):
        self.destroy()
        settings_root = ctk.CTk()
        app = Settings(settings_root)
        print("Settings Window Opened")
        settings_root.mainloop()

    def save_settings(self, window):
        selected_theme = self.theme_var.get()
        ctk.set_appearance_mode(selected_theme)
        
        volume = self.volume_slider.get()
        print(f"Theme set to {selected_theme}, Volume set to {volume}")

        window.destroy()

    def quit_application(self):
        self.destroy()

    def go_back_to_main_menu(self):
        self.destroy()
        main_menu = MainMenu()
        main_menu.mainloop()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = MainMenu()
    app.mainloop()