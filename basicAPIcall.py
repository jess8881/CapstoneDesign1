import openai
import os


openai.api_key = "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"
#개인키 나중에 따로 파일로 빼기 - 보안 이슈

prompt = "I'm writing a job resume for an IT company as a JAVA developer. Recommend me some good sentences."

response = openai.Completion.create(
        model = "text-davinci-003",
        prompt=prompt + " ",
        temperature = 0.6,      #1에 가까워질 수록 randomness 커짐
        max_tokens = 1000,      #답변 길이 제한
)

print(response.choices[0].text.strip())
#print(response.choices[0].text.strip())
#response 안의 choices 안의 0번째 텍스트만 가져옴

#print(response)
#git commit test