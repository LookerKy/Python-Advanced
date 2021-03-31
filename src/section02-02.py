# Section02-02

# Magic Method
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 참조 : https://www.tutorialsteacher.com/python/magic-methods-in-python
# 기본형
print(int)

# 모든 속성 및 메소드 출력 -> __로출력되는 모든 것을 매직메소드 라고 한다.
print(dir(int))
print()
print()

# use
n = 100
print('Ex1-1', n + 200)
print('Ex1-2', n.__add__(200))
print('Ex1-3', n.__doc__)
print('Ex1-4', n.__bool__(), bool(n))
print('Ex1-5', n * 100, n.__mul__(100))

print()
print()


# 클래스 예제
class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return 'Student Class Info: {}, {}'.format(self._name, self._height)

    def __ge__(self, other):
        print('Called. >> __ge__ Method')
        if self._height >= other._height:
            return True
        else:
            return False

    def __le__(self, other) -> bool:
        print('Called. >> __le__ Method')
        if self._height <= other._height:
            return True
        else:
            return False

    # 빼기 메소드
    def __sub__(self, other):
        print('Called >> __sub__ Method')
        return self._height - other._height


student1 = Student('James', 181)
student2 = Student('Mie', 165)

# 연산자가 들어오면 ge le 메소드가 실행된다고 생각하면 됨
print('EX2-1 - ', student1 >= student2)
print('EX2-2', student1 - student2)

print()
print()


# 클래스 예제2

# 벡터(Vector)

class Vector:
    def __init__(self, *args):
        '''
        create a vector, example : v = Vector(1,2)
        :param args:
        '''
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        '''
        returns the Vector information
        '''
        return 'Vector(%r, %r)' % (self._x, self._y)

    # 내장함수 오버라이딩
    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        return Vector(self._x * other, self._y * other)

    def __bool__(self):
        return bool(max(self._x, self._y))


v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()

print('Ex3-1 -', Vector.__init__.__doc__)
print('Ex3-2 -', Vector.__repr__.__doc__)
print('Ex3-3 - ', v1, v2, v3)
print('Ex3-4 - ', v1 + v2)
print('Ex3-5 - ', v1 * 4)
print('Ex3-6 -', v2 * 10)
print('Ex3-7 -', bool(v1), bool(v2))
print('Ex3-8 - ', bool(v3))

