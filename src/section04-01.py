# section04 -1
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화 가능
# 2. 변수 등에 할당 가능
# 3. 함수 인수 전달 가능
# 4. 함수 결과로 반환 가능 return function

def factorial(n):
    '''
    Factorial Function : n:int
    '''
    if n == 1:
        return 1
    return n * factorial(n - 1)


class A:
    pass


print(factorial(5))
print(type(A))
print(type(factorial))
print(dir(A), dir(factorial))
print(set(sorted(dir(factorial))) - set(sorted(dir(A))))
print(factorial.__name__)
print(factorial.__code__)

print()
print()

# 변수 할당
var_func = factorial

print(var_func(5))
print(var_func)
print(list(map(var_func, range(1, 6))))

# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher Order Function)
print(list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print([var_func(i) for i in range(1, 6) if i % 2])

# reduce()

from functools import reduce
from operator import add

print(reduce(add, range(1, 11)))  # 누산기
print(sum(range(1, 11)))

# 익명함수 lambda

print(reduce(lambda x, t: x + t, range(1, 11)))
print()
print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 후출 가능한지 확인

import random


# 로또 추첨 클래스
class LottoGame:
    def __init__(self):
        self._balls = [n for n in range(1, 46)]

    def pick(self):
        random.shuffle(self._balls)
        return sorted([random.choice(self._balls) for n in range(6)])

    def __call__(self, *args, **kwargs):
        return self.pick()


#
game = LottoGame()

print(callable(str), callable(list), callable(factorial), callable(3.14), callable(game))
print(game.pick())
print(game())
print(callable(game))

print()
print()


# 다향한 매개변수 입력 (* **)
def arg_test(name, *args, point=None, **kwargs):
    return '<args_test> -> ({})({})({})({})'.format(name, args, point, kwargs)


print(arg_test('test1'))
print(arg_test('test1', 'test2'))
print(arg_test('test1', 'test2', 'test3', id='admin', point=7))
print(arg_test('test1', 'test2', 'test3', 'test4', id='admin', point=7, password=1234))
print(arg_test('test1', 'test2', 'test3', 'test4', id='admin', point=7, password=1234))
print()
print()
print()

# 함수 Signatures
from inspect import signature

sg = signature(arg_test)

print(sg)
print(sg.parameters)

print()
print()
print()

# 모든 정보 출력
for name, params in sg.parameters.items():
    print(name, params.kind, params.default)
print()
print()
print()
print()

# partial 사용법 : 인수고정 -> 주로 특정 인수 고정 후 콜백 함수에 사용
# 하나 이상의 인수가 이미 할당된 함수의 새 버전 반환
# 함수의 새 객체 타입은 이전 함수의 자체를 기술하고 있다.

from operator import mul
from functools import partial

print(mul(10, 100))
# 인수 고정
five = partial(mul, 5)

# 고정 추가
six = partial(five, 6)

print(five(100))
print(six())
print([five(i) for i in range(1, 10)])
print(list(map(five, range(1, 10))))
