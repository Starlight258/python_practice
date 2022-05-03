total_dictionary = {}

while True:
    question = input("질문을 입력해주세요(입력 종료는 q) : ")
    if (question=="q"):
        break
    else : 
        total_dictionary[question] = ""

for i in total_dictionary:
    print(i) # key 프린트
    answer = input("답변 : ")
    total_dictionary[i] = answer 

print(total_dictionary)

