from flask import Flask

# flask application and Configuration
app = Flask(__name__)

# Routes
@app.route("/")
def index():
    return "Hello world!"


# Code Entrypoint
if __name__=="__main__":
    app.run(debug=True)
