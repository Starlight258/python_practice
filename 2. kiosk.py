order={"Num":"101", "Burger":"치즈버거", "Beverage":"콜라"}
for i,j in order.items():
    print(i,":", j);
order["Burger"]="치즈버거"
order["Side"]="치킨너겟"
print(order)
order.clear() #모두 지우기
print(order)
order=[]
order.append({"Num":"102", "Burger":"불고기버거세트", "Beverage":"바닐라쉐이크"})
order.append({"Num":"103", "Burger":"치킨버거", "Beverage":"딸기칠러", "사이드":"치즈스틱"})
print(order)
