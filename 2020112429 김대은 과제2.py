project = int(input("과제 점수를 입렵하세요 : "))
MIDtest = int(input("중간고사 점수를 입력하세요 : "))
LASTtest = int(input("기말고사 점수를 입력하세요 : "))


score = (project + MIDtest + LASTtest) /3
print("과제 :",project)
print("중간 :",MIDtest)
print("기말 :",LASTtest)
print("평균 :",score)

if score >= 90:
    print("A학점 입니다")
elif score >= 80:
    print("B학점 입니다")
elif score >= 70:
    print("C학점 입니다")
elif score >= 60:
    print("D학점 입니다")
else:
    print("F학점 입니다")








