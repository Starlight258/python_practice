import smtplib #smtp 라이브러리
from email.message import EmailMessage #MIME 형식 메세지 생성 모듈
import imghdr #이미지 확장자 파악
import re #정규표현식 사용
#!! 그 전에 gmail - IMAP 설정 허용, 계정-보안설정-보안수준 낮은 앱 허용하기 !!

SMTP_SERVER="smtp.gmail.com" #gmail 서버
SMTP_PORT=465 #포트 번호(gmail에서 할당한 포트, 우리가 바꿀수 없음, 누구나 이 포트 이용)

#보낼 주소, 제목, 내용 입력받기
# login = input("내 구글 id : ") -> 이 기능은 꼭 필요하지 않아 생략
# pw = input("내 구글 비밀번호 : ")
addr = input("이메일 보낼 주소 : ")
subject = input("이메일 제목 : ")
content = input("이메일 내용 : ")

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
message.set_content(content) #통에 넣을 메세지

#헤더 값 설정=제목, 송신자, 수신자
message["Subject"]=subject # 메일 제목
message["From"]="수신자 메일" #수신자
message["To"]=addr #송신자

#보낼 이미지 첨부하기
with open("img.png", "rb") as image: #rb 모드로 읽은 이미지를 image 변수 
    image_file=image.read() #읽은 내용 image_file 변수로 설정
    
image_type = imghdr.what('img', image_file) #binary 이미지가 어떤 유형인지 파악해줌(png, jpg...)
message.add_attachment(image_file, maintype='image', subtype=image_type) #이미지 첨부

smtp=smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) #서버
print(smtp.login("내 계정", "비번")) #계정, 비밀번호-서버에 로그인하기

sendEmail(message["To"]) #유효한 이메일 주소이면 메일 보내기

smtp.quit() #smtp 연결 나가기
