for i in range(0,2301):
    a = 7 ** 350 + 7 ** 150 - i
    a1 = ""
    while a > 0:
        a1 = a1 + str(a % 7)
        a = a // 7
    if(a1.count("0") == 200):
        print(i)
