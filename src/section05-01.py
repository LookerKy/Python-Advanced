# Section05-01
# 객체 참조 특징
# python object reference

print(dir())

# id vs __eq__
x = {'name': 'kime', 'age': 33, 'city': 'seoul'}
y = x
print(id(x), id(y))
print(x == y)
print(x is y)
print(x, y)

x['class'] = 10
print(x, y)

print()
print()

z = {'name': 'kime', 'age': 33, 'city': 'seoul', 'class': 10}

print(z, x)
print(x is z)  # 같은 객체
print(x is not z)
print(x == z)  # 값이 같다

# 객체 생성 후 완전 불변 -> 즉, id는 객체 주소 비교, ==(__eq__)는 값을 비교

print()
print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print(id(tuple1), id(tuple2))
print(tuple2 is tuple1)
print(tuple2 == tuple1)
print(tuple1.__eq__(tuple2))

print()
print()

# copy, Deep Copy

# Copy
tl1 = [10, [100, 105], (5, 10, 15), 75]
tl2 = tl1
tl3 = list(tl1)

print(tl1 == tl2)
print(tl1 is tl2)
print(tl1 == tl3)
print(tl1 is tl3)
print(id(tl1), id(tl2), id(tl3))
print(tl1)
print(tl2)
print(tl3)
print(id(tl1[1]), id(tl3[1]))
print(id(tl1[0]), id(tl3[0]))
print(id(tl1[2]), id(tl3[2]))
print(id(tl1[3]), id(tl3[3]))

# 증명
tl1.append(1000)
tl1[1].remove(105)

print(tl1)
print(tl2)
print(tl3)

print()

print(id(tl1[2]))
tl1[1] += [110, 120]
tl1[2] += (110, 120)
print(id(tl1[2]))

print(tl1)
print(tl2)  # 튜플 재 할당(객체 새로 생성)
print(tl3)

print()
print()
print()


# Deep copy

# 장바구니
class Basket:
    def __init__(self, product=None):
        if product is None:
            self._product = []
        else:
            self._product = list(product)

    def put_prod(self, prod_name):
        self._product.append(prod_name)

    def del_prod(self, prod_name):
        self._product.remove(prod_name)


import copy

basket1 = Basket(['Apple', 'Bag', 'Tv', 'Snack', 'Water'])
basket2 = copy.copy(basket1)
basket3 = copy.deepcopy(basket1)

print(id(basket1), id(basket2), id(basket3))
print(id(basket1._product), id(basket2._product), id(basket3._product))

print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')

print(basket1._product)
print(basket2._product)
print(basket3._product)


# 함수 매개변수 전달 사용법
def mul(x, y):
    x += y
    return x


x = 10
y = 5

print(mul(x, y), x, y)

a = [10, 100]
b = [5, 10]

print(mul(a, b), a, b)  # 가변형 일 때는 원본 데이터 변경됨

c = (10, 100)
d = (5, 10)

print(mul(c, d), c, d)  # 불변형 c -> 원본 데이터 변경 안됨

# 파이썬 불변 예외 -> 값이 같은 변수를 2개 생성해도 참조가 같음
# str, bytes, frozenset, tuple : 사본 생성 x => 참조 반환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print(tt1 is tt2, id(tt1), id(tt2))
print(tt1 is tt3, id(tt1), id(tt3))

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print(tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print(ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))

