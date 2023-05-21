from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# api 키 가져 오기
openai.api_key = os.getenv('OPEN_API_KEY')

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    # textarea에 들어갈 내용 저장
    input_text = ""
    output_text = ""

    if request.method == "POST":
        input_text = request.form["input_text"]
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Correct this to standard English.: '{input_text}'",
            max_tokens=200,
            n=1,
            stop=None,
            temperature=0.7,
        )
        output_text = response.choices[0].text.strip().replace('"', '')
        # 쌍따옴표 삭제

    return render_template("sample.html", input_text=input_text, output_text=output_text)

if __name__ == '__main__':
    app.run(debug=True)