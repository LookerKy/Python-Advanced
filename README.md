# Python Advanced

## 파이썬 심화 과정

## 목차

- Section01 : Class의 변수 및 메소드
- Section02 : Python의 다양한 Data Model 소개

## Section01 : Class

클래스는 기본적으로 python의 상위 객체인 object를 상속한다.

### 클래스의 self 란?

> 자기 자신을 의미하며 다른 프로그래밍 언어에서는 `this` 의 역할을 한다.
> 여기서 자기자신은 instance화 된 객체의 자기 자신을 의미한다.

## Section01 : variable of Class

### 인스턴스 변수

#### 선언

인스턴스 변수는 객체가 인스턴스화 됬을 때 정의 되는 변수로써 생성자인 `__init__` 메소드를 통해 정의 된다.

```python
class Student:
    def __init__(self, name, grade, number):
        self._name = name
        self._grade = grade
        self._number = number
```

### 클래스 변수

클래스 변수는 인스턴스와 상관없이 클래스 자체에 선언되는 변수 로써
객체가 만들어지지 않아도 메모리에 잡히는 변수이다.

```python
class Student:
    student_count = 0  # class 변수

    def __init__(self, name, grade, number):
        self._name = name
        self._grade = grade
        self._number = number

        Student.student_count += 1
```

## Section01 : Method of Class

### 인스턴스 메소드

### 클래스 메소드

### 스태틱 메소드