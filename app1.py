from flask import Flask
import time
from random import randint

# Create the Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello_world():
    print("Waiting 7 seconds")
    time.sleep(7)
    return 'Hello, World 1!'

# Run the app if this file is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
