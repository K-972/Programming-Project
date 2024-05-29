import requests


class weather():
    def __init__(self) -> None:
        self.apikey = None
        self.temperature = None
        self.pressure = None
        self.humidity = None
        self.description = None

    def __str__(self) -> str:
        return 'This class grabs the weathera and is not the gui of the main loop'
    
    def ReadApiKey(self): # does it pull from the directory of the class file or the main file?
        with open("apikey.txt", 'r', encoding='utf-8') as f:
            self.apikey = f.read()
            
    def GetWeather(self):
        
        city_name = "Nuneaton"

        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        complete_url = base_url + "appid=" + self.apikey + "&q=" + city_name

        response = requests.get(complete_url)

        x = response.json()

        if x["cod"] != "404":

            y = x["main"]

            self.temperature = y["temp"]

            self.pressure = y["pressure"]

            self.humidity = y["humidity"]

            z = x["weather"]
            
            self.description = z[0]["description"]

            print(" Temperature (in celsius unit) = " +
                str(self.temperature - 273.15) +
                "\n Atmospheric pressure (in hPa unit) = " +
                str(self.pressure) +
                "\n Humidity (in percentage) = " +
                str(self.humidity) +
                "\n Description = " +
                str(self.description))
        else:
            print(" City Not Found ")
            
            
            
            


            
    