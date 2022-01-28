import os
import json

while True:
    c = open('C:\\Users\\Admin\\PycharmProjects\\grading\\password.txt', 'r')
    v = c.read()
    c.close()

    username = open('C:\\Users\\Admin\\PycharmProjects\\grading\\username.txt')
    ss = username.read()
    username.close()

    print('enter username')
    t = input()
    if t == ss:
        print('enter password')
        x = (input())
        if x == v:
            print('ایا نمره ها پاک شود [y|n]')
            is_deleting = input()
            if is_deleting == 'y':
                os.remove('dic.txt')
                exit()
            print("به چه تعداد نام و نمره و اسم درس وارد میکنید")
            h = int(input())
            i = 0
            if os.path.exists('dic.txt'):
                f = open('dic.txt', 'r')
                d = json.loads(f.read())
                f.close()
            else:
                d = {}
            while i < h:
                print('enter name lesson student')
                l = str(input())
                print('enter name student')
                n = str(input())
                print('enter student score ')
                s = int(input())
                i = i + 1
                if n in d.keys():
                    d[n][l] = s
                else:
                    d[n] = {l:s}
            print('کار معلم تمام است! نمره ثبت شد!')
            w = open('dic.txt', 'w')
            w.write(json.dumps(d))
            w.close()
        else:
            print('error password')
    else:
        print('error username')
