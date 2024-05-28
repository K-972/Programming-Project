import sys
import os
import eel


sys.path.append(os.path.join(os.path.dirname(__file__), '_classes')) # go into calssed dir

from classes import weather # imports the calsses




# reset dir to script location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)







eel.init('_web') # initialize    

@eel.expose 
def HelloWorld():
    print('Hello World!')

eel.start('index.html', size=(800, 600))














# Updates the weather stats
def GrabWeather():
    object = weather()
    object.ReadApiKey()
    object.GetWeather()
    


