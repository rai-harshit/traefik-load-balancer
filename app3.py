from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello_world():
    return 'Hello, World 3!'

# Run the app if this file is executed
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
