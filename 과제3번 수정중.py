print("별 찍기\n 1. ☆\n 2. ★ \n 3. #")

a = "☆"
b = "★"
c = "#"

mode = input("모드를 선택하시오 : ")
if mode == "1" :
    print(a)
elif mode == "2" :
    print(b)
elif mode == "3" :
    print(c)


star = 5
for i in range(star):
    print(" " * ((star - 1) - i), end = "")
    print("☆" * (2 * i + 1))