# Section04 -2

# Decorator & Closure

def func_v1(a):
    print(a)
    print(b)


# func_v1(5)

b = 10


def func_v2(a):
    print(a)
    print(b)


func_v2(2)


def func_v3(a):
    print(a)
    print(b)
    b = 5  # 지역 변수 있을 시 전역변수 참조 x


# func_v3(5)  # error

from dis import dis

print(dis(func_v3))
print()
print()
print()
print()
print()

# Closure
# 반환되는 내부 함수에 대해서 선언 된 연결을 가지고 참조하는 방식
# 반환 당시 함수 유효범위를 벗어난 변수 또는 메소드에 직접 접근이 가능하다.

a = 10

print(a + 10)
print(a + 100)

# 결과를 누적 할 수 있을 까?
print(sum(range(1, 51)))
print(sum(range(51, 101)))


# 클래스 이용

class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v, *args, **kwargs):
        self._series.append(v)
        print('class >>>> {} / {} '.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)


avg_cls = Averager()

print(avg_cls(15))
print(avg_cls(40))
print(avg_cls(35))


# 클로저로 생성
# 전역 변수 사용 감소
# 디자인 패턴 적용

def avgs():
    # Free variable
    seriese = []

    # 클로저 영역
    def averager(v):
        # seriese = []  # check
        seriese.append(v)
        print('class >>>> {} / {} '.format(seriese, len(seriese)))
        return sum(seriese) / len(seriese)

    return averager


avg_closure1 = avgs()
print(avg_closure1(10))
print(avg_closure1(15))
print(avg_closure1(1234))
print(avg_closure1(14329234))

print()
print()

print(dir(avg_closure1))
print()
print(avg_closure1.__code__)
print()
print(avg_closure1.__code__.co_freevars)
print()
print(dir(avg_closure1.__closure__[0]))
print()
print(avg_closure1.__closure__[0].cell_contents)

print()
print()
print()
print()


# 클로저 오사용

def closure_avg2():
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return averager


avg_closure2 = closure_avg2()
print(avg_closure2(10))
print(avg_closure2(20))
print(avg_closure2(30))

# 데코레이터 실습
# 1. 중복 제거, 코드 간결
# 2. 클로저 보다 문법 간결
# 3. 조합해서 사용 용이

# 단점
# 디버깅이 어려움
# 에러의 모호함
import time


def perf_time(func):
    def pref_clocked(*args):
        st = time.perf_counter()
        result = func(*args)
        et = time.perf_counter() - st
        name = func.__name__
        arg_str = ','.join(repr(arg) for arg in args)
        print('[%0.5fs] %s(%s) -> %r ' % (et, name, arg_str, result))
        return result

    return pref_clocked


@perf_time
def time_func(second):
    time.sleep(second)


@perf_time
def sum_func(*numbers):
    return sum(numbers)


@perf_time
def fact_func(n):
    return 1 if n < 2 else n * fact_func(n - 1)


# 데코레이터 미사용
non_deco1 = perf_time(time_func)
non_deco2 = perf_time(sum_func)
non_deco3 = perf_time(fact_func)

print(non_deco1, non_deco1.__code__.co_freevars)
print(non_deco2, non_deco2.__code__.co_freevars)
print(non_deco3, non_deco3.__code__.co_freevars)

print('*' * 40, 'Called Non Deco -> time_func')
print()
print()
print()
non_deco1(2)
non_deco2(100, 200, 300, 500)
non_deco3(100)
print()
print()
print()
print()

print('*' * 40, 'Called Deco -> func')

time_func(2)
sum_func(100, 200, 300, 400, 500)
# fact_func(100)