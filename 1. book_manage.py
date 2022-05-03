import random
import time

book_list=[]

def register(): #책 등록
    title = input("제목 : ")
    author = input("저자 : ")
    pubCom = input("출판사 : ")
    date = input("입고일 : ")
    book_list.append({"제목":title, "저자": author, "출판사":pubCom, "입고일":date})
    print("등록이 완료되었습니다!")
    print(book_list)

def delete(): #책 삭제
    for i in book_list:
        print(i["제목"])
    title= input("삭제할 책 제목 : ")
    c=0
    for i in book_list:
        if i["제목"]==title:
            book_list.remove(i)
            print(book_list)
            c=1
            break
    if c==0:
        print("삭제할 책이 리스트에 없습니다!!")
    else:
        print("정상적으로 삭제되었습니다!")

def choice(): #책 추천
    for i in book_list:
        print(i["제목"])
    print("중에서 하나를 추천합니다")
    print(5)
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    rec = random.choice(book_list)
    print("추천 책 : ", rec)

#반복 과정
while True:
    print("----------------------------------------------------------------------")
    print("1. 책 등록")
    print("2. 책 삭제")
    print("3. 책 목록")
    print("4. 책 추천")
    print("5. 종료")
    num = int(input("메뉴 선택(숫자) : ")) #input은 문자열 반환하므로 int로 형변환
    print("----------------------------------------------------------------------")
    if num == 1:
        register()
    elif num == 2:
        delete()
    elif num == 3:
        print(book_list)
    elif num == 4:
        choice()
    elif num == 5:
        break
    else:
        print("숫자를 다시 입력해주세요!!")