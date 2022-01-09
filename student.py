import json
j = open('C:\\Users\\Admin\\PycharmProjects\\grading\\user stu.txt','r')
x = j.read()
g = open('C:\\Users\\Admin\\PycharmProjects\\grading\\password student.txt','r')
n = g.read()
print('enter password student')
p = input()
if p == n:
    print('enter username student')
    u = input()

    if u == x :
         y = open('C:\\Users\\Admin\\PycharmProjects\\grading\\dic.txt', 'r')
         tt=json.load(y)
         print('enter name student')
         a = input()
         print(tt[a])
         if a not in tt:
            print("دانش اموز شما در لیست معلم وجود ندارد ")
    else:
        print('error username')

else:
    print('error password')
