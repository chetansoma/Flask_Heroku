from flask import Flask
app = Flask(__name__)

@app.router('/', methods = ['GET', 'POST'])
def index():
    return "<h1> you have create the project!!! with Heroku"

if __name__ == '__main__':
    app.run()