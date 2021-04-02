# Section05-02
# 파이선 클래스 특별 메소드 심화 활용 및 상속
# Class ABC

# class 선언
class VectorP(object):
    def __init__(self, x, y):
        if y < 30:
            raise ValueError('NOOOO')
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y))

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = float(x)

    @y.setter
    def y(self, y):
        if y < 30:
            raise ValueError('no')
        self.__y = float(y)


# 객체 선언

v = VectorP(20, 40)

# print('Ex1-1 ', v.__x, v.__y)  접근불가

# Getter, Setter
print(dir(v), v.__dict__)
print(v.x, v.y)

for val in v:
    print(val)


# __slot__
# 파이썬 인터프리터에게 통보
# 해당 클래스가 가지는 속성을 제한
# __dict__ 속성 최적화 -> 다수 객체 생성시 -> 메모리 사용 공간 대폭 감소
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 Set 형태를 사용

class TestA(object):
    __slots__ = ('a',)


class TestB():
    pass


use_slot = TestA()
no_slot = TestB()

print(use_slot)
# print(use_slot.__dict__) # dict 자체가 없음
print(no_slot)
print(no_slot.__dict__)

# 메모리 사용량 비교
import timeit


# 측정을 위한 함수
def repeat_outer(obj):
    def repeat_inner():
        obj.a = 'TEST'
        del obj.a

    return repeat_inner


print(min(timeit.repeat(repeat_outer(use_slot), number=1)))
print(min(timeit.repeat(repeat_outer(no_slot), number=1)))

print()
print()


# 객체 슬라이싱
class ObjectS:
    def __init__(self):
        self._numbers = [n for n in range(1, 10000, 3)]

    def __len__(self):
        return len(self._numbers)

    def __getitem__(self, item):
        return self._numbers[item]


s = ObjectS()
# print(s.__dict__)
print(len(s))
print(s[-1])
print(s[::10])
print()
print()
print()
print()
print()


# 파이썬 추상 클래스
# 참조 https://docs.python.org/3/library/collections.abc.html

# 자체적으로 객체 생성 불가
# 상속을 통해 자식 클래스에서 인스턴스를 생성해야 함
# 추상클래스를 사용하는 이유 -> 개발과 관련된 공통된 내용(필드, 메소드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것

# 폰 -> 걸다 끊다, 배터리 충전

# Sequence 상속 받지 않았지만, 자동으로 기능 작동 (__iter__, __contain__)
# 객체 전체를 자동으로 조사 -> 시퀀스 프로토콜

class IterTestA(object):
    def __getitem__(self, item):
        return range(1, 50, 2)[item]


i1 = IterTestA()

print(i1[4])
print(i1[4:10])
print(3 in i1[1:10])
# print([i for i in i1])
print()
print()
print()

# Sequence 상속
# 요구사항인 추상 메소드를 모두 구현해야 동작
# from collections.abc import Sequence
#
#
# class IterTestB(Sequence):
#     def __getitem__(self, item):
#         return range(1, 50, 2)[item]
#
#     def __len__(self, item):
#         return len(range(1, 50, 2)[item])
#
#
# i2 = IterTestB()
# print(i2[4])
# print(i2[4:10])
# print(3 in i2[1:10])

# abc 활용 예제
import abc


class RandomMachine(abc.ABC):
    # 추상 메소드
    @abc.abstractmethod
    def load(self, iterobj):
        '''
        :param iterobj: Iterable 항목 추가
        :return:
        '''

    @abc.abstractmethod
    def pick(self):
        """
        무작위 항목 뽑기
        :return:
        """

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
            return tuple(sorted(items))


import random


class CraneMachine(RandomMachine):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, iterobj):
        self._items.extend(iterobj)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Empty Crane Box')

    def __call__(self, *args, **kwargs):
        return self.pick()


print(issubclass(CraneMachine, RandomMachine))

print(CraneMachine.__mro__)

cm = CraneMachine(range(1, 100))

print(cm._items)
print(cm())
print(cm.pick())
print(cm.inspect())
