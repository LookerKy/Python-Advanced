# Section01-02

class Student:
    """
    Student Class
    Author: Lee
    Date: 2021.03.30
    """
    # 클래스 변수
    student_count = 0

    def __init__(self, name, number, grade, details, email=None):
        # 인스턴스 변수
        self._name = name
        self._grade = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1

    def __str__(self):
        return 'str : {}'.format(self._name)

    def __repr__(self):
        return 'repr : {}'.format(self._name)

    def detail_info(self):
        print('Current Id: {}'.format(id(self)))
        print('Student Detail Info: {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_count -= 1


# Self 의미
student1 = Student('Cho', 2, 3, {'Gender': 'Male', 'score1': 44, 'score2': 66})
student2 = Student('kim', 2, 3, {'Gender': 'Male', 'score1': 85, 'score2': 74}, email="test@gmail.com")

# ID 확인
print(id(student1))
print(id(student2))

print(id(student1) == id(student2))
print(student1 is student2)

# dir & dict 확인
print(dir(student1))
print(dir(student2))
print()
print(student1.__dict__)
print(student2.__dict__)

# Docstring
print(Student.__doc__)
print()

# 실행
student1.detail_info()
student2.detail_info()

# 에러
# Student.detail_info()
print()

Student.detail_info(student1)
Student.detail_info(student2)
print()

# 비교
print(student1.__class__, student2.__class__)
print(id(student1.__class__) == id(student2.__class__))

# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장 X)
# student1._name = "hello"

print(student1._name)
print()
print()

# 클래스 변수

# 접근 - 누구나 접근 가능
print(Student.student_count)
print()
print()

# 공유 확인
print(Student.__dict__)
print(student1.__dict__)
print(student2.__dict__)

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))

del student2
print(student1.student_count)
print(Student.student_count)



