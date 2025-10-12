data = [
    {'name': 'Raj', 'score': 85, 'age': 21},
    {'name': 'Anu', 'score': 90, 'age': 20},
    {'name': 'Ravi', 'score': 85, 'age': 22}
]

sorted_list = sorted(data, key= lambda x: (-x['score'], x['age']))

for d in sorted_list:
    print(d)
