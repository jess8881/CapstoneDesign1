from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# API 키 가져오기
openai.api_key = os.getenv('OPEN_API_KEY')

app = Flask(__name__)

# 이전 출력 결과를 유지하기 위한 변수 초기화
previous_output_text = ""
previous_recommendations = []


@app.route("/", methods=["GET", "POST"])
def home():
    # textarea에 들어갈 내용 저장
    input_text = ""
    action = ""

    global previous_output_text, previous_recommendations  # previous_output_text와 previous_recommendations를 전역 변수로 선언

    if request.method == "POST":
        input_text = request.form["input_text"]
        action = request.form.get("action", "None") # 기본값을 none으로 설정. 버튼을 안 누를 수도 있으니까

        if action == "correct_grammar":
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Correct this to standard English.: '{input_text}'",
                max_tokens=200,
                n=1,
                stop=None,
                temperature=0.7,
            )
            output_text = response.choices[0].text.strip().replace('"', '')
        else:
            # 'correct grammar' 버튼을 누르지 않은 경우 이전 출력 결과를 유지
            output_text = previous_output_text

        if action == "resume":
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Read my resume and give me three example sentences for my resume: '{input_text}'",
                max_tokens=200,
                n=1,
                stop=None,
                temperature=0.7,
            )
            recommendations = [choice.text.strip().replace('"', '') for choice in response.choices]
        elif action == "report":
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Read my report for University and give me three example sentences for my report: '{input_text}'",
                max_tokens=200,
                n=1,
                stop=None,
                temperature=0.7,
            )
            recommendations = [choice.text.strip().replace('"', '') for choice in response.choices]
        elif action == "blog_post":
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Read my blog post and give me three example sentences for my blog post: '{input_text}'",
                max_tokens=200,
                n=1,
                stop=None,
                temperature=0.7,
            )
            recommendations = [choice.text.strip().replace('"', '') for choice in response.choices]
        else:
            recommendations = []  # 액션이 없는 경우 빈 리스트로 초기화

        # 이전 출력 결과를 업데이트
        previous_output_text = output_text
        previous_recommendations = recommendations

    return render_template("sample.html", input_text=input_text, output_text=previous_output_text, recommendations=previous_recommendations)


if __name__ == '__main__':
    app.run(debug=True)