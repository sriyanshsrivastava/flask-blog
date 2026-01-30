from flask import Flask

# flask application and Configuration
app = Flask(__name__)

# Routes
@app.route("/")
@app.route("/home")
def index():
    return "<h1>Home Page</h1>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"


# Code Entrypoint
if __name__=="__main__":
    app.run(debug=True)
