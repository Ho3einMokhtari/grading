import json
c = open('C:\\Users\\Admin\\PycharmProjects\\grading\\password.txt','r')
v = c.read()

username = open('C:\\Users\\Admin\\PycharmProjects\\grading\\username.txt')
ss = username.read()





print('enter password')
x =(input())
if x == v  :
    print('enter username')
    t = input()
    if t == ss:
        print('yes')
        print("به چه تعداد نام و نمره وارد میکنید")
        h = int(input())
        i = 0
        while i < h :
            print('enter name student')
            n = str(input())
            print('enter student score ')
            s = int(input())
            d = {
                n:s,
            }
            w = open('dic.txt', 'w')
            w.write(json.dumps(d))
            i = i + 1
    else:
       print('error username')
else:
    print('error password')



