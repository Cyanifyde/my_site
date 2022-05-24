from flask import Flask, render_template

app = Flask(__name__, template_folder='template')


app.config["TEMPLATES_AUTO_RELOAD"]=True
app.config["STATIC_AUTO_RELOAD"]=True
@app.route('/')
def home():
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
@app.route('/games/snakegame/')
def snakegame():
    return render_template("snake_game/snakegame.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

app.register_error_handler(404, page_not_found)

app.run(host='0.0.0.0', port=8080)
