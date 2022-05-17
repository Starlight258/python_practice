import requests
from bs4 import BeautifulSoup 
from email.message import EmailMessage
import smtplib
from datetime import datetime #날짜
# import re
#크롤링하기 - 코로나 현황, 오늘 날씨, 핫한 뉴스기사 제목 4개
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

#코로나 현황
url="https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%BD%94%EB%A1%9C%EB%82%9819"
response = requests.get(url, headers=headers)  # 사람임을 알려주고(헤더) 요청보내기

soup = BeautifulSoup(response.text, 'html.parser')  # bs통에 넣어주기

status_1 = soup.find('li', {"class" : "info_01"})
status_2 = soup.find('li', {"class" : "info_02"})
status_3 = soup.find('li', {"class" : "info_03"})
status_4 = soup.find('li', {"class" : "info_04"})

status = status_1.get_text()+status_2.get_text()+status_3.get_text()+status_4.get_text()

#오늘 날씨
url="https://search.naver.com/search.naver?&query=%EB%82%A0%EC%94%A8&oquery=%EC%98%A4%EB%8A%98%EC%9D%98%EB%82%A0%EC%94%A8"
response = requests.get(url, headers=headers)  # 사람임을 알려주고(헤더) 요청보내기

soup = BeautifulSoup(response.text, 'html.parser')  # bs통에 넣어주기

weather_set1 = soup.findAll('div', {"class" : "_today"}) #오늘의 날씨
weather_set2 = soup.findAll('ul', {"class" : "today_chart_list"}) #기타 날씨 정보

weather="" #날씨
for w in weather_set1: 
    weather += w.get_text() #날씨 정보 추가
weather += "\n"+ weather_set2[0].get_text() #기타 날씨 정보도 추가

#핫한 뉴스기사 제목 4개
url="https://news.naver.com/"
response = requests.get(url, headers=headers)  # 사람임을 알려주고(헤더) 요청보내기

soup = BeautifulSoup(response.text, 'html.parser')  # bs통에 넣어주기

article_set = soup.findAll('div', {"class" : "cjs_t"}) #기사제목 태그
article_list=[]
i=0;
for a in article_set: 
    if(i<4): #기사 4개까지만 보내기
        # a = re.sub(r'[\s+\t\r\n]', '', a.text.strip()) #공백 삭제
        article_list.append(a)
        i +=1
    else:
        break;

article=""
for al in article_list:
    article += (al.get_text()+"\n") #텍스트로 묶기

#이메일 보내기
SMTP_SERVER="smtp.gmail.com" #gmail 서버
SMTP_PORT=465 #포트 번호(gmail에서 할당한 포트, 우리가 바꿀수 없음, 누구나 이 포트 이용)
addr = input("이메일 보낼 주소 : ")
subject = datetime.today().strftime("%Y/%m/%d 브리핑")

#유효한 이메일 주소이면 메일 보냄, 아니면 메일 안보냄
def sendEmail(addr): 
    smtp.send_message(message) #메일을 보내는 함수
    print("정상적으로 메일이 발송되었습니다.")

#보낼 message
message=EmailMessage() #이메일 통(MIME형태로 바꿔줌)
content= "<코로나 발생 현황>\n"+ status+"\n<오늘의 날씨>\n" + weather +"\n<언론사별 핫한 뉴스>\n" + article
message.set_content(content) #통에 넣을 메세지
#헤더 값 설정=제목, 송신자, 수신자
message["Subject"]=subject # 메일 제목
message["From"]="보낼사람 메일" #수신자
message["To"]=addr #송신자

#gmail 서버에 로그인
smtp=smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) #서버연결
print(smtp.login("###@gmail.com", "비밀번호")) #계정, 비밀번호-서버에 로그인하기

sendEmail(message["To"]) #유효한 이메일 주소이면 메일 보내기

smtp.quit() #smtp 연결 나가기