import requests




class weather:
    def __init__(self) -> None:
        self.apikey = None
        self.temperature = None
        self.pressure = None
        self.humidity = None
        self.descriptio = None

    def __str__(self) -> str:
        return 'This class grabs the weathera and is not the gui of the main loop'
    
    def ReadApiKey(self): # does it pull from the directory of the class
        with open()