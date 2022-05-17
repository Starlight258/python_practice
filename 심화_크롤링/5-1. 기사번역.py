import requests
from bs4 import BeautifulSoup 
from googletrans import Translator
from email.message import EmailMessage
import smtplib
import re

#크롤링하기
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://n.news.naver.com/mnews/article/214/0001196663?sid=104"
response = requests.get(url, headers=headers)  # 사람임을 알려주고(헤더) 요청보내기

soup = BeautifulSoup(response.text, 'html.parser')  # bs통에 넣어주기
title_set = soup.findAll('h2', {"class" : "media_end_head_headline"})
content_set = soup.findAll('div', {"class": "_article_content"})

title = title_set[0].get_text() #기사 제목
for content in content_set: #기사 내용
    content =content.get_text()

#번역하기
translator = Translator()

print("=============================")
print("한국어: ko 영어: en 프랑스어:fr 아랍어:ar")
print("베트남어: vi 독일어: de 스페인어:es 몽골어:mn")
print("중국어(간체): zh-CN 힌디어: hi")
print("=============================")
dest = input("번역하고 싶은 언어를 입력하세요 : ")

detected = translator.detect(content) #입력 문장의 언어 감지
result = translator.translate(content, dest) #번역하기(번역할 문장, 번역할 언어)

print("=========출 력 결 과=========")
print(detected.lang, ":", content)
print(dest, ":", result.text)
print("=============================")

#이메일 보내기
SMTP_SERVER="smtp.gmail.com" #gmail 서버
SMTP_PORT=465 #포트 번호(gmail에서 할당한 포트, 우리가 바꿀수 없음, 누구나 이 포트 이용)
addr = input("이메일 보낼 주소 : ")
subject = input("이메일 제목 : ")

#유효한 이메일 주소이면 메일 보냄, 아니면 메일 안보냄
def sendEmail(addr): 
    reg="^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]{2,3}$" #id@site.com 정규식
    if bool(re.match(reg, addr)):
        smtp.send_message(message) #메일을 보내는 함수
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

#보낼 message
message=EmailMessage() #이메일 통(MIME형태로 바꿔줌)
message.set_content(title+" : "+content+"\n\n"+result.text) #통에 넣을 메세지
#헤더 값 설정=제목, 송신자, 수신자
message["Subject"]=subject # 메일 제목
message["From"]="###.gmail.com" #수신자
message["To"]=addr #송신자

#gmail 서버에 로그인
smtp=smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) #서버연결
print(smtp.login("###.gmail.com", "비밀번호")) #계정, 비밀번호-서버에 로그인하기

sendEmail(message["To"]) #유효한 이메일 주소이면 메일 보내기

smtp.quit() #smtp 연결 나가기