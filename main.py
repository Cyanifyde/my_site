from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


@app.route('/')
def home():
    app.route('/')
    return render_template("frontpage.html")
    
@app.route('/about/')
def about():
    return render_template("about.html")
    
@app.route('/buy/')
def buy():
    return render_template("buy.html")
    
@app.route('/projects/')
def projects():
    return render_template("projects.html")
@app.route('/timer/')
def timer():
    return render_template("timer.html")
@app.route('/extra/')
def extra():
    return render_template("extra.html")
@app.route('/snakegame/')
def snakegame():
    return render_template("snake_game/snakegame.html")
app.run(host='0.0.0.0', port=8080)
