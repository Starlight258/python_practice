from googletrans import Translator

translator = Translator()

sentence = input("번역하고 싶은 문장을 입력하세요 : ")
print("=============================")
print("한국어: ko 영어: en 프랑스어:fr 아랍어:ar")
print("베트남어: vi 독일어: de 스페인어:es 몽골어:mn")
print("중국어(간체): zh-CN 힌디어: hi")
print("=============================")
dest = input("번역하고 싶은 언어를 입력하세요 : ")

detected = translator.detect(sentence) #입력 문장의 언어 감지
result = translator.translate(sentence, dest) #번역하기(번역할 문장, 번역할 언어)

print("=========출 력 결 과=========")
print(detected.lang, ":", sentence)
print(dest, ":", result.text)
print("=============================")
