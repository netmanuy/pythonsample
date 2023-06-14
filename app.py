
import random, string
from datetime import datetime
from flask import Flask

# Define Flask ApP
app = Flask(__name__)

@app.route('/')
def hello_world():

    # List of characters for random generation
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    # Generate current date   
    dt_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Set first_name & last_name as empty
    first_name=''
    last_name=''
    
    # Generate random string from 20 lenght 
    for i in range(0, 20):
        first_name += random.choice(characters)
        last_name += random.choice(characters)
    
    # Return the result
    return "First name: " + first_name + " || Last name: " + last_name + " || Today date: " + dt_string