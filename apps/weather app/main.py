import sys
import os
import eel


sys.path.append(os.path.join(os.path.dirname(__file__), '_classes')) # go into calssed dir

from classes import weather # imports the calsses




# reset dir to script location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)







eel.init('_web') # initialize    



##########################################
############ CORE FUNCTIONS ##############
##########################################

@eel.expose 
def HelloWorld():
    print('Hello World!')


@eel.expose  
def close_window():
    eel.close_page()

eel.start('index.html', size=(200,200))









def development_close():
    close = input("press enter to close")
    if close == "":
        close_window()
    else:
        close_window()





# Updates the weather stats
@eel.expose
def GrabWeather():
    object = weather()
    object.ReadApiKey()
    object.GetWeather()



