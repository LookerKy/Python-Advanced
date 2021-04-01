# Section03-02
# 파이썬 심화
# 시퀀스형
# 해시테이블 -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 x
# Dict 및 Set 심화

import csv
from types import MappingProxyType

# Dict 구조
print('Ex1-1 - ')
print(__builtins__.__dict__)

print()
print()

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])  # immutable in mutable
print('Ex1-2 ', hash(t1))
# print('Ex1-3 ', hash(t2))

print()
print()

# 지능형 딕셔너리 (Comprehending Dict)
with open('resource/test1.csv', 'r', encoding='utf-8') as f:
    temp = csv.reader(f)
    z = 0
    # Header skip
    next(temp)
    # 변환
    NA_CODES = [tuple(x) for x in temp]
    print(NA_CODES)

a = iter(NA_CODES)
print(next(a))
print(next(a))
print(next(a))

n_code1 = {country: code for country, code in NA_CODES}
n_code2 = {country.upper(): code for country, code in NA_CODES}
print()
print()

print(n_code1)

print()
print()

print(n_code2)

# Dict Setdefault
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val1'),
          ('k2', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'),
          )

new_dict1 = {}
new_dict2 = {}

for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# use setDefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

print()
print()


# 사용자 정의 dict 상속
class UserDict(dict):
    def __missing__(self, key):
        print('Called: __missing__')
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        print('Called: __getItem__')
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        print('Called __contains__')
        return item in self.keys() or str(item) in self.keys()


user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({'one': 1, 'two': 2})
user_dict3 = UserDict([('one', 1), ('two', 2)])
a = {1: 2, 2: 3}

print('Ex4-1 ', user_dict1, user_dict2, user_dict3)
print('Ex4-2 ', user_dict2.get('two'))
print('Ex4-3 ', 'one' in user_dict3)
print('Ex4-2 ', user_dict3['one'])
# print('Ex4-2 ', user_dict3['three'])
print('Ex4-2 ', 'three' in user_dict3)

# immutable Dict

d = {'key1': 'TEST!'}
d_frozen = MappingProxyType(d)

print('5-1 -', d, id(d))
print('5-1 -', d_frozen, id(d_frozen))
print('5-1 -', d is d_frozen, d == d_frozen)

# d_frozen['key1'] = 'TEST@'

d['key2'] = 'TEST@'

print('EX5-4', d)
print()
print()

# Set 구조 (FrozenSet)
s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# 추가
s1.add('Melon')

# 추가 불가
# s5.add('Melon')

print('Ex6-1 -', s1, type(s1))
print('Ex6-1 -', s2, type(s2))
print('Ex6-1 -', s3, type(s3))
print('Ex6-1 -', s4, type(s4))

# 선언 최적화
# from dis import dis -> 인터프리터 빌드 과정 출력

# 지능형 집합(Comprehending Set)
from unicodedata import name

print()
print('Ex 7-1 ')

print({name(chr(i), '') for i in range(0, 256)})

