from flask import Flask, render_template, request
import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

app = Flask(__name__)


#html 파일 가져옴
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    purpose = request.form['purpose']
    return user_input + ' ' + purpose


def grammar_correction(text):
    model_engine = "text-davinci-003"
    prompt = "Please correct my grammar: " + text
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text.strip()
    return message

def generate_recommendation(text, purpose):
    model_engine = "text-davinci-003"
    prompt = "Generate a recommendation for a " + purpose + " based on this text: " + text
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = completions.choices[0].text.strip()
    return message


if __name__ == "__main__":
    app.run(debug = True)