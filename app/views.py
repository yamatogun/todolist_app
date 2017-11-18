from . import app

@app.route("/")
def home():
    return render_template("list_of_todos.html")
