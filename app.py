from flask import Flask, render_template, request
import openai
import os

#시스템 환경변수에 저장한 api key 불러오기
openai.api_key = os.environ['OPENAI_API_KEY']
#openai.api_key = "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"
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("sample.html")

@app.route("/", methods=["POST"])
def correct_grammar():
    text = request.form["text"]
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = f"Correct this to standard English.: '{text}'",
        max_tokens = 100,
        n = 1,
        stop = None,
        temperature = 0.7,
    )
    corrected_text = response.choices[0].text.strip()
    return render_template("sample.html", corrected_text = corrected_text)

if __name__ == '__main__':
    app.run(debug=True)