from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__, static_url_path='/static', template_folder="templates")

num1 = None
num2 = None

@app.route("/")
def index():
    global num1, num2
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    return render_template("index.html", num1=num1, num2=num2)

@app.route("/background_process", methods = ['GET','POST'])
def background_process():
    global num1, num2
    guess = int(request.values.get("guess"))
    answer = num1*num2

    if(guess == answer ):
        return jsonify({"result" : "Correct"})
    else:
        return jsonify({"result" : "Incorrect. Please try again!!"})

@app.route("/update", methods = ['GET','POST'])
def update():
    index()
    return jsonify({"num1":num1, "num2":num2})

if __name__=="__main__":
    app.run(debug=True)