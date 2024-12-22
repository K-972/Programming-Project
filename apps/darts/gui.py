import customtkinter as ctk

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

        if len(players) < 2:
            self.result_label.configure(text="Please add at least 2 players.")
        else:
            self.result_label.configure(text=f"Game Started: {game_type}, {sets} Sets, {legs} Legs with {players}")
            self.root.destroy()
            new_root = ctk.CTk()
            app = ThreeOOne(new_root)
            new_root.mainloop()

    def go_back(self):
        self.root.destroy()
        self.game_type_label.configure(fg_color="blue")
        self.sets_label.configure(fg_color="blue")
        self.legs_label.configure(fg_color="blue")
        # Here you can reopen the previous window or perform any other action
        # For example:
        # previous_root = ctk.CTk()
        # app = PreviousWindow(previous_root)
        # previous_root.mainloop()
        # Since PreviousWindow is not defined, we'll just exit
        exit()

class ThreeOOne:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("301")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c2f31")
        self.root.attributes("-fullscreen", True)

        self.create_widgets()

    def create_widgets(self):
        # Example content for the 301 game screen
        label = ctk.CTkLabel(
            self.root, 
            text="Welcome to 301 Game!", 
            fg_color="#2c2f31", 
            text_color="white", 
            font=("Arial", 24, "bold")
        )
        label.pack(pady=20)

        # Add more widgets and functionality as needed

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Optional: set appearance mode to dark
    ctk.set_default_color_theme("blue")  # Optional: set default color theme

    root = ctk.CTk()
    app = DartsGameSetup(root)
    root.mainloop()