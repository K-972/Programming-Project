import eel
import os



script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

print("Current working directory:", os.getcwd())
print("Contents of 'web' directory:", os.listdir('web'))

# Initialize the eel application
eel.init('web')

# Define a simple Python function
@eel.expose
def say_hello_py(name):
    print(f'Hello from Python, {name}!')

# Start the eel application
eel.start('index.html', size=(800, 600))
