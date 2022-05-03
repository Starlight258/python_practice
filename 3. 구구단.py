print("   # 9단 #      # 8단 #       # 7단 #      # 6단 #      # 5단 #      # 4단 #      # 3단 #      # 2단 #      # 1단 #")
for i in range(9,0,-1):
    for j in range(9,0,-1):
        print("{0:<2} * {1:<2} = {2:<2}".format(j,i, i*j), end=" ")
    print("\n")

