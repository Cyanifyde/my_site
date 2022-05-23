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

app.run(host='0.0.0.0', port=8080)
