from flask import Blueprint, render_template, request
from get_final_result import get_final_result
app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        result = get_final_result(text)
        return "This text's author is: " + result[1]
    return render_template("index.html")#, data=data)

@app_blueprint.route('/about')
def index_about():
    return '<h1>about</h1>' 
