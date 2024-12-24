import customtkinter as ctk
from tkinter import messagebox



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

        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        main_frame = ctk.CTkFrame(self.root, fg_color="#2c2f31")
        main_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

        # Top Frame for Back Button
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
            width=100,  # Increased width
            height=50,  # Increased height
            font=("Arial", 16)  # Larger font
        )
        back_button.pack(side=ctk.LEFT)

        # Game Type Selection
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
                fg_color="#3a3d40",  # Background color of the radio button
                text_color="white",
                hover_color="#3a3d40"
            )
            rb.pack(side=ctk.LEFT, padx=10)

        # Sets Selection
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

        # Legs Selection
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

        # Players Section
        players_label = ctk.CTkLabel(
            main_frame, 
            text="Players", 
            fg_color="#2c2f31", 
            text_color="white", 
            font=("Arial", 16, "bold")
        )
        players_label.pack(pady=(20, 10))

        # Button Frame for Add/Remove Player Buttons
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

        # Scrollable Frame for Player Entries
        scrollable_frame = ctk.CTkScrollableFrame(main_frame, fg_color="#2c2f31")
        scrollable_frame.pack(fill=ctk.BOTH, expand=True, pady=10)

        self.players_frame = scrollable_frame

        self.add_player_slot()
        self.add_player_slot()

        # Start Button
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

        # Result Label
        self.result_label = ctk.CTkLabel(
            main_frame, 
            text="", 
            fg_color="#2c2f31", 
            text_color="white", 
            font=("Arial", 14, "bold")
        )
        self.result_label.pack(pady=5)

    def add_player_slot(self):
        player_var = ctk.StringVar()
        player_entry = ctk.CTkEntry(self.players_frame, textvariable=player_var, width=300, fg_color="#3a3d40", text_color="white")
        player_entry.pack(pady=5)
        self.player_entries.append(player_var)

    def remove_player_slot(self):
        if self.player_entries:
            self.player_entries.pop()
            if self.players_frame.winfo_children():
                self.players_frame.winfo_children()[-1].destroy()

    def start_game(self):
        game_type = self.game_type_var.get()
        if game_type == "ATC":
            game_type = "Around The Clock"
        sets = self.sets_var.get()
        legs = self.legs_var.get()
        players = [player.get() for player in self.player_entries if player.get()]

        if len(players) >= 2:
            game_options = [game_type, sets, legs, players]
            match game_options[0]:
                case "301":
                    self.root.destroy()
                    new_root = ctk.CTk()
                    app = ThreeOOne(new_root, game_options)
                    new_root.mainloop()
                case "501":
                    self.root.destroy()
                    new_root = ctk.CTk()
                    app = FiveOOne(new_root)
                    new_root.mainloop()
                case "Around The Clock":
                    self.root.destroy()
                    new_root = ctk.CTk()
                    app = AroundTheClock(new_root)
                    new_root.mainloop()
                case "KILLER":
                    self.root.destroy()
                    new_root = ctk.CTk()
                    app = Killer(new_root)
                    new_root.mainloop()
                case "PRACTICE":
                    self.root.destroy()
                    new_root = ctk.CTk()
                    app = Practice(new_root)
                    new_root.mainloop()

        else:
            messagebox.showerror("Need at least 2 players to start the game.")

    def go_back(self):
        self.root.destroy()
        self.menu = MainMenu()
        print("menu opened")
        self.menu.mainloop()

class ThreeOOne:
    def __init__(self, root, game_options) -> None:
        self.root = root
        self.root.title("301")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c2f31")
        self.root.attributes("-fullscreen", True)

        self.players = game_options[3]
        self.game_options = game_options
        self.scores = {player: 301 for player in self.players}
        self.current_player_index = 0
        self.current_dart = 1
        self.multiplier = 1  # Default multiplier
        self.last_hit_multiplier = 1  # To track the last hit multiplier
        self.previous_score = 301  # To store the score before the current dart

        # Initialize stats
        self.darts_thrown = {player: 0 for player in self.players}
        self.avg_score = {player: 0.0 for player in self.players}
        self.highest_score = {player: 0 for player in self.players}

        self.create_widgets()

    def create_widgets(self):
        num_of_players = len(self.players)
        if num_of_players == 2:
            self.player_frames = []

            # Left Frame for Player 1
            left_frame = ctk.CTkFrame(self.root, width=200, fg_color="#2c2f31")
            left_frame.pack(side="left", fill="y", padx=10, pady=20)

            # Player 1 Name Label
            player_name_label = ctk.CTkLabel(
                left_frame, 
                text="Player Name:", 
                text_color="white", 
                font=("Arial", 20, "bold")
            )
            player_name_label.pack(pady=(0, 5))
            self.player_name = ctk.CTkLabel(
                left_frame, 
                text=self.players[self.current_player_index], 
                font=("Arial", 16)
            )
            self.player_name.pack(pady=(0, 10))

            # Finish Label for Player 1
            finish_label = ctk.CTkLabel(
                left_frame, 
                text="Finish:", 
                text_color="white", 
                font=("Arial", 20, "bold")
            )
            finish_label.pack(pady=(0, 5))
            self.finish = ctk.CTkLabel(
                left_frame, 
                text="0", 
                font=("Arial", 16)
            )
            self.finish.pack(pady=(0, 10))

            # Current Score Label for Player 1
            current_score_label = ctk.CTkLabel(
                left_frame, 
                text="Current Score:", 
                text_color="white", 
                font=("Arial", 20, "bold")
            )
            current_score_label.pack(pady=(0, 5))
            self.current_score = ctk.CTkLabel(
                left_frame, 
                text=str(self.scores[self.players[self.current_player_index]]), 
                font=("Arial", 16)
            )
            self.current_score.pack(pady=(0, 10))

            # Darts Thrown Label for Player 1
            darts_thrown_label = ctk.CTkLabel(
                left_frame, 
                text="Darts Thrown:", 
                text_color="white", 
                font=("Arial", 20, "bold")
            )
            darts_thrown_label.pack(pady=(0, 5))
            self.darts_thrown_label = ctk.CTkLabel(
                left_frame, 
                text=str(self.darts_thrown[self.players[self.current_player_index]]), 
                font=("Arial", 16)
            )
            self.darts_thrown_label.pack(pady=(0, 10))

            # Average Score per Dart Label for Player 1
            avg_score_label = ctk.CTkLabel(
                left_frame, 
                text="Avg Score/Dart:", 
                text_color="white", 
                font=("Arial", 20, "bold")
            )
            avg_score_label.pack(pady=(0, 5))
            self.avg_score_label = ctk.CTkLabel(
                left_frame, 
                text=str(self.avg_score[self.players[self.current_player_index]]), 
                font=("Arial", 16)
            )
            self.avg_score_label.pack(pady=(0, 10))

            # Highest Score in a Turn Label for Player 1
            highest_score_label = ctk.CTkLabel(
                left_frame, 
                text="Highest Score:", 
                text_color="white", 
                font=("Arial", 20, "bold")
            )
            highest_score_label.pack(pady=(0, 5))
            self.highest_score_label = ctk.CTkLabel(
                left_frame, 
                text=str(self.highest_score[self.players[self.current_player_index]]), 
                font=("Arial", 16)
            )
            self.highest_score_label.pack(pady=(0, 10))

            # Right Frame for Player 2
            right_frame = ctk.CTkFrame(self.root, width=200, fg_color="#2c2f31")
            right_frame.pack(side="right", fill="y", padx=10, pady=20)

            # Player 2 Name Label
            player2_name_label = ctk.CTkLabel(
                right_frame, 
                text="Player Name:", 
                text_color="white", 
                font=("Arial", 20, "bold")
            )
            player2_name_label.pack(pady=(0, 5))
            self.player2_name = ctk.CTkLabel(
                right_frame, 
                text=self.players[1], 
                font=("Arial", 16)
            )
            self.player2_name.pack(pady=(0, 10))

            # Finish Label for Player 2
            finish2_label = ctk.CTkLabel(
                right_frame, 
                text="Finish:", 
                text_color="white", 
                font=("Arial", 20, "bold")
            )
            finish2_label.pack(pady=(0, 5))
            self.finish2 = ctk.CTkLabel(
                right_frame, 
                text="0", 
                font=("Arial", 16)
            )
            self.finish2.pack(pady=(0, 10))

            # Current Score Label for Player 2
            current_score2_label = ctk.CTkLabel(
                right_frame, 
                text="Current Score:", 
                text_color="white", 
                font=("Arial", 20, "bold")
            )
            current_score2_label.pack(pady=(0, 5))
            self.current_score2 = ctk.CTkLabel(
                right_frame, 
                text=str(self.scores[self.players[1]]), 
                font=("Arial", 16)
            )
            self.current_score2.pack(pady=(0, 10))

            # Darts Thrown Label for Player 2
            darts_thrown2_label = ctk.CTkLabel(
                right_frame, 
                text="Darts Thrown:", 
                text_color="white", 
                font=("Arial", 20, "bold")
            )
            darts_thrown2_label.pack(pady=(0, 5))
            self.darts_thrown2_label = ctk.CTkLabel(
                right_frame, 
                text=str(self.darts_thrown[self.players[1]]), 
                font=("Arial", 16)
            )
            self.darts_thrown2_label.pack(pady=(0, 10))

            # Average Score per Dart Label for Player 2
            avg_score2_label = ctk.CTkLabel(
                right_frame, 
                text="Avg Score/Dart:", 
                text_color="white", 
                font=("Arial", 20, "bold")
            )
            avg_score2_label.pack(pady=(0, 5))
            self.avg_score2_label = ctk.CTkLabel(
                right_frame, 
                text=str(self.avg_score[self.players[1]]), 
                font=("Arial", 16)
            )
            self.avg_score2_label.pack(pady=(0, 10))

            # Highest Score in a Turn Label for Player 2
            highest_score2_label = ctk.CTkLabel(
                right_frame, 
                text="Highest Score:", 
                text_color="white", 
                font=("Arial", 20, "bold")
            )
            highest_score2_label.pack(pady=(0, 5))
            self.highest_score2_label = ctk.CTkLabel(
                right_frame, 
                text=str(self.highest_score[self.players[1]]), 
                font=("Arial", 16)
            )
            self.highest_score2_label.pack(pady=(0, 10))

            


            label = ctk.CTkLabel(
            self.root, 
            text="Welcome to 301 Game!", 
            fg_color="#2c2f31", 
            text_color="white", 
            font=("Arial", 24, "bold")
        )
            label.pack(pady=20)

            # Current Player Label
            self.current_player_label = ctk.CTkLabel(
                self.root, 
                text=f"Current Player: {self.players[self.current_player_index]}", 
                font=("Helvetica", 18)
            )
            self.current_player_label.pack(pady=10)

            # Current Score Label
            self.current_score_label = ctk.CTkLabel(
                self.root, 
                text=f"Score: {self.scores[self.players[self.current_player_index]]}", 
                font=("Helvetica", 16)
            )
            self.current_score_label.pack(pady=5)

            # Current Dart Label
            self.current_dart_label = ctk.CTkLabel(
                self.root, 
                text=f"Dart: {self.current_dart}/3", 
                font=("Helvetica", 16, "bold")
            )
            self.current_dart_label.pack(pady=5)

            # Number Pad Frame
            keypad_frame = ctk.CTkFrame(self.root, fg_color="#2c2f31")
            keypad_frame.pack(pady=10)

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
                    command=lambda num=number: self.append_score(num)
                )
                button.grid(row=row, column=col, padx=5, pady=5)

        # Special Buttons Frame
        special_frame = ctk.CTkFrame(self.root, fg_color="#2c2f31")
        special_frame.pack(pady=10)

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
            command=lambda: self.append_score(25)
        )
        twenty_five_button.grid(row=1, column=0, padx=5, pady=5)

        # 50 Button
        fifty_button = ctk.CTkButton(
            special_frame, 
            text="50", 
            width=100, 
            height=60, 
            command=lambda: self.append_score(50)
        )
        fifty_button.grid(row=1, column=1, padx=5, pady=5)

        # Scores Display
        self.scores_display = ctk.CTkLabel(
            self.root, 
            text=self.get_scores_text(), 
            font=("Helvetica", 14)
        )
        self.scores_display.pack(pady=20)


    def append_score(self, value):
        current_player = self.players[self.current_player_index]
        current_score = self.scores[current_player]

        # Store previous score in case of a bust
        self.previous_score = current_score

        # Check for Treble on 25 or 50
        if (self.multiplier == 3 or self.multiplier == 2) and value in [25, 50]:
            messagebox.showerror("Invalid Action", "Cannot apply Treble to 25 or 50.")
            self.multiplier = 1  # Reset multiplier
            return

        # Calculate the score with multiplier
        if self.multiplier > 1:
            score = value * self.multiplier
            self.last_hit_multiplier = self.multiplier
            self.multiplier = 1  # Reset multiplier after use
        else:
            score = value
            self.last_hit_multiplier = 1

        # Validate score
        if score > current_score:
            messagebox.showerror("Invalid Score", "Score cannot exceed current score.")
            return
        elif score == current_score:
            if self.last_hit_multiplier == 2:
                messagebox.showinfo("Game Over", f"{current_player} wins!")
                self.root.destroy()
                return
            else:
                messagebox.showerror("Invalid Finish", "The game must end on a Double.")
                return

        # Apply the score
        self.scores[current_player] -= score
        self.update_display()
        self.next_dart()

    def submit_score(self):
        try:
            score = int(self.score_input.get())
            player = self.players[self.current_player_index]
            self.update_stats(player, score)
            self.switch_player()
            self.score_input.delete(0, 'end')
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid score.")

    def update_stats(self, player, score):
        self.darts_thrown[player] += 1
        self.scores[player] -= score
        self.avg_score[player] = (301 - self.scores[player]) / self.darts_thrown[player]
        if score > self.highest_score[player]:
            self.highest_score[player] = score

        # Update the labels
        if player == self.players[0]:
            self.current_score.config(text=str(self.scores[player]))
            self.darts_thrown_label.config(text=str(self.darts_thrown[player]))
            self.avg_score_label.config(text=str(round(self.avg_score[player], 2)))
            self.highest_score_label.config(text=str(self.highest_score[player]))
        else:
            self.current_score2.config(text=str(self.scores[player]))
            self.darts_thrown2_label.config(text=str(self.darts_thrown[player]))
            self.avg_score2_label.config(text=str(round(self.avg_score[player], 2)))
            self.highest_score2_label.config(text=str(self.highest_score[player]))

    def switch_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.update_player_labels()

    def update_player_labels(self):
        self.player_name.config(text=self.players[self.current_player_index])
        self.current_score.config(text=str(self.scores[self.players[self.current_player_index]]))
        self.darts_thrown_label.config(text=str(self.darts_thrown[self.players[self.current_player_index]]))
        self.avg_score_label.config(text=str(round(self.avg_score[self.players[self.current_player_index]], 2)))
        self.highest_score_label.config(text=str(self.highest_score[self.players[self.current_player_index]]))

        self.player2_name.config(text=self.players[1])
        self.current_score2.config(text=str(self.scores[self.players[1]]))
        self.darts_thrown2_label.config(text=str(self.darts_thrown[self.players[1]]))
        self.avg_score2_label.config(text=str(round(self.avg_score[self.players[1]], 2)))
        self.highest_score2_label.config(text=str(self.highest_score[self.players[1]]))

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

        stats_button = ctk.CTkButton(
            main_menu_frame,
            text="Stats",
            command=self.show_stats,
            fg_color="#3a3d40",
            text_color="white",
            hover_color="#4a4d50",
            width=200,
            height=40
        )
        stats_button.pack(pady=10)

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

    def show_stats(self):
        # Implement stats screen
        pass

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
        # Implement actual volume control logic here
        print(f"Theme set to {selected_theme}, Volume set to {volume}")

        window.destroy()

    def quit_application(self):
        self.destroy()

# Example navigation function to go back to MainMenu
def go_back_to_main_menu(self):
    self.destroy()  # Destroy the current window
    main_menu = MainMenu()
    # Remove the following line to prevent multiple mainloops
    main_menu.mainloop()

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Optional: set appearance mode to dark
    ctk.set_default_color_theme("blue")  # Optional: set default color theme

    app = MainMenu()
    app.mainloop()