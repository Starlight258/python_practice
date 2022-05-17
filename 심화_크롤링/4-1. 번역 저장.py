from googletrans import Translator

def translate(file):
    translator=Translator() #번역기 생성

    print("=============================")
    print("한국어: ko 영어: en 프랑스어:fr 아랍어:ar")
    print("베트남어: vi 독일어: de 스페인어:es 몽골어:mn")
    print("중국어(간체): zh-CN 힌디어: hi")
    print("=============================")
    dest = input("번역하고 싶은 언어를 입력하세요 : ")

    detected=translator.detect(file) #입력 언어 감지
    result=translator.translate(file, dest) #번역하기

    print("=========입 력 문 장=========")
    print(detected.lang, ":", file) #입력 언어 : 입력 파일
    print("=========번 역 결 과=========")
    print(dest, ":", result.text) #번역할 언어 : 번역 결과
    print("=============================")
    with open("result.txt", "w") as result_txt: #번역결과 result.txt에 저장
        result_txt.write(result.text)

#입력으로 파일 만들기
with open("input.txt", "w") as txt: 
    story=input("번역하고 싶은 글을 입력하세요 : ")
    txt_file=txt.write(story)
    print("파일을 생성하였습니다")
    
#파일 읽고 번역하기, 번역한 것은 파일에 저장
with open("input.txt", "r") as txt:
    txt_file=txt.read()
    result = translate(txt_file) #번역하고 파일에 저장

