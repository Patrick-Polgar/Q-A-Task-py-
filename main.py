#here we are import in the moduls
from flask import Flask,jsonify, render_template , request

#here we create a object from Flask class
staffbase_app = Flask(__name__)

Q_and_A = {"What is a meaning of life?":[]}
question = Q_and_A.keys()

#this is allocate the place in a webpage
@staffbase_app.route("/", methods = ["POST","GET"])
def this_is_my_function():
    if request.method == "POST":
        Q_and_A["What is a meaning of life?"].append(request.form["my_text"])
        from_usr = Q_and_A["What is a meaning of life?"]

        return render_template("index.html", content = question, answers = from_usr)
    if request.method == "GET":
        from_usr = Q_and_A["What is a meaning of life?"]
        return render_template("index.html", content = question, answers = from_usr)

#this is a new webpage with the answers
@staffbase_app.route("/tellme/")
def display_the_answer():
    from_usr = Q_and_A["What is a meaning of life?"]
    return render_template("tellme.html", content = from_usr)

staffbase_app.run(port=8080,debug=True)