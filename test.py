import json

a = int(input())
if a == 1:
    pass
elif a == 2:
    print('yes')
else:
    print('no')

print('Grading System')

grades = {
    'ali': 18,
    'amin': 20,
    'reza': 11,
    'hossein': 20
}

f = open('stu.txt', 'w')
f.write(json.dumps(grades))
f.close()

g = open('stu.txt', 'r')
s = g.read()
g.close()

print(s)
print(hash(s))