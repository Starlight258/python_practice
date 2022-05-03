total_list = []

while True:
    question = input("질문 입력 (나가려면 q) : ")
    if question == "q":
        break
    else:
        total_list.append({"질문": question, "답변" : ""})

for i in total_list:
    print(i["질문"])
    answer = input("답변 입력 : ")
    i["답변"]=answer 
print(total_list)
