import os
os.getcwd()

import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("/Users/ethanhumphreys/Documents/GitHub/Programming-Project/lear/classes/emloyee system/employees.db")
cursor = connection.cursor()
