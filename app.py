from flask import Flask, render_template, request
from sentiment.watson_analyzer import analyze_with_watson

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result_watson = None

    if request.method == "POST":
        user_input = request.form["text"]
        result_watson = analyze_with_watson(user_input)

    return render_template("index.html", result_watson=result_watson, result_openai=None)

if __name__ == "__main__":
    app.run(debug=True)
