from flask import Flask, render_template, request, redirect, url_for
import openai
import os
from dotenv import load_dotenv


# .env 파일 로드
load_dotenv()

#api 키 가져 오기
openai.api_key= os.getenv('OPEN_API_KEY')

app = Flask(__name__)
app.secret_key =os.getenv('MY_SECRET_KEY')

@app.route("/", methods=["GET", "POST"])
def home():
    text = ""
    corrected_text = ""

    if request.method == "POST":
        text = request.form["text"]
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Correct this to standard English.: '{text}'",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7,
        )
        corrected_text = response.choices[0].text.strip().replace('"', '')
        #쌍따옴표 삭제

    return render_template("sample.html", text=text, corrected_text=corrected_text)


if __name__ == '__main__':
    app.run(debug=True)