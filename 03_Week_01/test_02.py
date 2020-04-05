
"""
import requests


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.json()['origin'], r.text)

# to make frequency dictionary
zen_map = dict()

for word in zen.split():
    cleaned_word = word.strip('.,!-*').lower()
    if cleaned_word not in zen_map:
        zen_map[cleaned_word] = 0

    zen_map[cleaned_word] += 1

print(zen_map)


# S.isdigit()


# Data sorting by 2 levels:
age_num = [(26, 8), (20, 1), (42, 6), (40, 2), (19, 1), (21, 6)]
age_num.sort(key=lambda x: (-x[1], x[0]))
print(age_num)

# Age calculation
import datetime

# bd = {}
# bd = {"bdate":"6.6"}
bd = {"bdate":"25.8.1993"}

if bd:
    dd = bd["bdate"].split(".")
    if len(dd) == 3:
        ddd = datetime.datetime.now().year - int(dd[-1])
        print(ddd)
"""


