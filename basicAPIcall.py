import openai
import os       #key 보관을 위한 os 모듈


api_key = os.environ['OPENAI_API_KEY']
#시스템 환경 변수에 OPENAI_API_KEY 등록 후 사용


prompt = "Correct this sentence grammatically. 'My life would sucks without your.'"

response = openai.Completion.create(
        model = "text-davinci-003",
        prompt=prompt + " ",
        temperature = 0.6,      #1에 가까워질 수록 randomness 커짐
        max_tokens = 1000,      #답변 길이 제한
)

print(response.choices[0].text.strip())
#response 안의 choices 안의 0번째 텍스트만 가져옴
#print(response)
