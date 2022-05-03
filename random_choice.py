import random
import time

lunch=[]

while True:
    print("lunch =",lunch)
    item = input("lunch 입력해주세요(나가려면 q) : ")
    if (item == "q"):
        break
    else:
        lunch.append(item)
print(lunch)
set_lunch=set(lunch) #set으로 바꿈(중복제거)
while True:
    print(set_lunch)
    item = input("lunch 제거할 것 입력해주세요(나가려면 q) : ")
    if (item=="q"):
        break
    else:    
        set_lunch = set_lunch - set([item])
print(set_lunch, "중에서 선택합니다")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print(random.choice(list(set_lunch)))