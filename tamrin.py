while True:
    import os
    import json

    c = open('C:\\Users\\Admin\\PycharmProjects\\grading\\password.txt', 'r')
    v = c.read()
    c.close()

    username = open('C:\\Users\\Admin\\PycharmProjects\\grading\\username.txt')
    ss = username.read()
    username.close()

    print('enter username')
    d = {}
    t = input()
    if t == ss:
        print('enter password')
        x = (input())
        if x == v:
            print('ایا نمرات پاک شود[y|n]')
            b = str(input())
            if b == 'n':
                print('yes')
                print("به چه تعداد نام و نمره و اسم درس وارد میکنید")
                h = int(input())
                i = 0
                while i < h:
                    print('enter name lesson student')
                    l = str(input())
                    print('enter name student')
                    n = str(input())
                    print('enter student score ')
                    s = int(input())
                    i = i + 1
                    d[n]= {l:s}
                    print('کار معلم تمام است! نمره ثبت شد!')
                    w = open('dic.txt', 'w')
                    w.write(json.dumps(d))
                    w.close()
            if os.path.exists('dic.txt'):
                r = open('dic.txt', 'w')
                r.write(json.dumps(d))
                r.close()
            elif b == 'y':
                print('yes')
                print("به چه تعداد نام و نمره و اسم درس وارد میکنید")
                h = int(input())
                i = 0
                while i < h:
                    print('enter name lesson student')
                    l = str(input())
                    print('enter name student')
                    n = str(input())
                    print('enter student score ')
                    s = int(input())
                    i = i + 1
                    d[n]= {l:s}
                    print('کار معلم تمام است! نمره ثبت شد!')
                    w = open('dic.txt', 'w')
                    w.write(json.dumps(d))
                    w.close()
        else:
            print('error password')
    else:
        print('error username')
