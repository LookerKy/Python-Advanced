# Section02-01
# Python Advanced
# 데이터 모델
# 참조 : https://docs.python.org/3/reference/datamodel.html
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크(data type) -> 시퀀스(Sequence) 반복(Iterator) 함수(Function) 클래스(Class)

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id 와 type 을 가지고있음
# 일급 객체

# 일반적인 튜플 사용
from math import sqrt
from collections import namedtuple

pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

line_len1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)

print('Ex 1-1', line_len1)

# namedtuple 사용
Point = namedtuple('Point', 'x y')

pt1 = Point(1.0, 5.0)
pt2 = Point(2.5, 1.5)

line_len2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)
print('Ex 1-2', line_len2)

# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True)  # 같은 변수나 예약어가 들어왔을 때 임의로 변수네이밍을 해줌

print('EX2-1', Point1, Point2, Point3, Point4)
temp_dict = {'x': 75, 'y': 35}
# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)  # Dict to Unpacking
print('EX2-2 -', p1, p2, p3, p4, p5)

# 사용
print('EX3-1', p1[0] + p2[1])
print('EX3-1', p1.x + p2.y)  # 클래스의 변수 접근 방식

# Unpacking
x, y = p3

print('EX3-3', x + y)

# Rename 테스트
print('Ex3-4', p4)

# namedtuple method
temp = [52, 38]

# _make() : 새로운 객체 생성
p4 = Point1._make(temp)

print('Ex4-1 -', p4)

# _fields : 필드 네임 확인
print('Ex4-2 - ', p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환

print('Ex4-3 -', p1._asdict(), p4._asdict())

# _replace() : 수정된 새로운 객체 반환
print('Ex4-4', p2._replace(y=100))

# 실 사용 실습
# 학생 전체 그룹생성
# 반20명 , 4개의 반 -> (A,B,C,D) 번호
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]
print(len(students))
print(students[4].rank)

students2 = [Classes(rank, number) for rank in 'A B C D'.split() for number in [str(n) for n in range(1, 21)]]

# 출력

for s in students:
    print()
