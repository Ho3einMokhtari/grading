import json

print('Grading System')

grades = {
    'ali': 18,
    'amin': 20,
    'reza': 11,
    'hossein': 20
}

f = open('stu.txt', 'w')
f.write(json.dumps(grades))
