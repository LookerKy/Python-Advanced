# section 03-01
# python advanced
# 시퀀스 형
# 컨테이너(Container) : 서로 다른 자료형을 저장  [list, tuple, collections.deque]
# Flat : 한 개의 자료형 [str, bytes, bytearray, array,array, memoryview]
# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, str, btyes

import array

# 지능형 리스트(Conprehending Lists)

# None Comprehending Lists
chars = '!@#!%!$%!@#!@+'
code1 = []
for s in chars:
    code1.append(ord(s))

print('Ex1-1 -', code1)

# Comprehending Lists
codes2 = [ord(s) for s in chars]
print('EX1-2 - ', codes2)
# Comprehending Lists
# 속도 약간 우세

codes3 = [ord(s) for s in chars if ord(s) > 40]
codes4 = list(map(ord, chars))
codes5 = list(filter(lambda x: x > 40, map(ord, chars)))
print('Ex1-3', codes3)
print('Ex1-4', codes4)
print('Ex1-5', codes5)
print('Ex1-6', [chr(s) for s in code1])

print()
print()

# Generator - 한 번에 한 개의 항목을 생성(메모리 유지 x)
tuple_g = (ord(s) for s in chars)

array_g = array.array('I', (ord(s) for s in chars))
print(type(tuple_g))
print('Ex2-1', tuple_g)
print('Ex2-2', next(tuple_g))
print('Ex2-3', next(tuple_g))
print('Ex2-4', next(tuple_g))
print('Ex2-5', array_g)
print('Ex2-6', array_g.tolist())

print()
print()

# generator 예제

print('Ex3-1', ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1, 11)):
    print('Ex3-2 - ', s)

print()
print()

# 리스트 주의 할 점
marks1 = [['~'] * 3 for n in range(3)]
marks2 = [['~'] * 3] * 3

print('Ex4-1', marks1)
print('Ex4-2', marks2)

print()

marks1[0][1] = 'X'
marks2[0][1] = 'X'

print('Ex4-3', marks1)
print('Ex4-4', marks2)

# 증명
print('Ex 4-5 - ', [id(i) for i in marks1])
print('Ex 4-6 - ', [id(i) for i in marks2])

# Tuple

# Packing * unpacking


# unpacking
a, b = divmod(100, 9)
print(a, b)

packed = (500, 2)
print('Ex 5-2 - ', divmod(*packed))
print('Ex 5-3 - ', *(divmod(100, 9)))  # unpacked 에 의해 풀려서 나옴

print()

x, y, *reset = range(10)
print('Ex5-4 -', x, y, reset)
x, y, *reset = range(2)
print('Ex5-4 -', x, y, reset)
x, y, *reset = 1, 2, 3, 4, 5
print('Ex5-4 -', x, y, reset)



print(type(reset))

# Mutable vs Immutable
t = (10, 20, 30)
l = [10, 20, 30]

print('Ex6-1', l, t, id(l), id(t))

# list tuple 깊은 복사
t = t*2
l = l*2
print('Ex6-2', l, t, id(l), id(t))

# list 얕은 복사(주소값 동일), tuple 깊은복사
t *= 2
l *= 2

print('Ex6-3', l, t, id(l), id(t))



