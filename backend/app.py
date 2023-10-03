from flask import Flask

# Create a Flask web server
app = Flask(__name__)

# Define a route and a function to handle the request
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
