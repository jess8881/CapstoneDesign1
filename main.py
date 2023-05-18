import nltk
from nltk.tokenize import sent_tokenize
import openai
import os
from dotenv import load_dotenv


#######API key 숨기기#########
# .env 파일 로드
load_dotenv()

# api 키 가져오기
api_key = os.getenv('OPEN_API_KEY')
openai.api_key = api_key
#############################


valid_categories = ['이력서', '블로그', '과제']
category = input(f"텍스트 목적을 선택하세요 ({', '.join(valid_categories)}): ")

#없는 목적을 입력할 경우 에러 메시지 반복
while category not in valid_categories:
    print("셋 중 하나를 선택해주세요.")
    category = input(f"텍스트 목적 셋 중 하나를 선택해주세요 ({', '.join(valid_categories)}): ")

text= input("검사하고 싶은 영어 텍스트를 입력하세요: ")

#이거 없으면 문자열 반복 안 됨
sentences = sent_tokenize(text)

#텍스트 검사
corrected_sentences = []
for sentence in sentences:
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Correct this to standard English: {sentence}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    corrected_sentence = response.choices[0].text.strip()
    corrected_sentences.append(corrected_sentence)

#추천 문장
recommendation = ''
if category == "이력서":
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Read my resume and give me three example sentences for my resume: {sentences}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    recommendation = response.choices[0].text.strip()
elif category == "블로그":
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Read my blog article and give me three example sentences for my blog article: {sentences}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    recommendation = response.choices[0].text.strip()
elif category == "과제":
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"Read my report for University and give me three example sentences for my report: {sentences}",
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    recommendation = response.choices[0].text.strip()

print("교정된 문장:")
for sentence in corrected_sentences:
    print(sentence)

print("추천 문장:")
print(recommendation)