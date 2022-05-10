import requests  # 서버에 요청, 응답받기
from bs4 import BeautifulSoup  # 크롤링
from datetime import datetime  # 현재 시간
import pandas as pd  # 판다스 사용


print(datetime.today().strftime("%Y년 %m월 %d일의 멜론차트 순위입니다.")) #날짜

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://www.melon.com/chart/day/index.htm"
response = requests.get(url, headers=headers)  # 사람임을 알려주고(헤더) 요청보내기

# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')  # bs통에 넣어주기

results = soup.findAll('tr', 'lst50')
infoset = soup.findAll('div', {"class": "ellipsis"})
rank = 1  # 순위
i = 0  # 3개씩 values리스트에 묶어서 저장하기위한 변수
values = []  # [순위, 노래 제목, 가수, 앨범] 원소를 가진 2차원 리스트
temp = []  # values 안에 넣을 리스트
for info in infoset:
    if(i == 0):  # 처음엔 순위
        temp.append(rank)
    temp.append(info.get_text())
    # print(t.get_text())
    i += 1
    if(i == 3):  # 마지막엔 초기화
        values.append(temp)
        i = 0
        temp = []  # 초기화
        rank += 1  # 순위 증가
print(values)

df = pd.DataFrame(values, columns=["순위", "노래제목", "가수", "앨범"])  # 데이터프레임 생성
df.to_csv("2022-05-10 TOP 100.csv", encoding='utf-8-sig') #한글 깨지지 않도록 인코딩해주기
