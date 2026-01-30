from flask import Flask, render_template

# flask application and Configuration
app = Flask(__name__)

# Dummy data
    #posts
posts=[
    {
        "author":"Satish",
        "title":"Blog post 1",
        "content": "first post content",
        "date_posted":"January 30, 2026"
    },
{
        "author":"Ritesh",
        "title":"Blog post 2",
        "content": "Post content from ritesh",
        "date_posted":"January 31, 2026"
    }
]
# Routes
@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")


# Code Entrypoint
if __name__=="__main__":
    app.run(debug=True)
