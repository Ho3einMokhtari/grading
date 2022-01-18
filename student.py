import json

y = open('C:\\Users\\Admin\\PycharmProjects\\grading\\dic.txt', 'r')
tt = json.load(y)
print('enter name student')
a = input()
print(tt[a])
if a not in tt:
    print("دانش اموز شما در لیست معلم وجود ندارد ")
