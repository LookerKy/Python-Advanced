# Chapter01-1
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 장점: 코드의 재사용, 코드 중복 방지 등
# 클래스 변수, 인스턴스 변수

# 구조 설계 후 재사용 성 증가

class Student:
    def __init__(self, name, number, grade, details):
        self._name = name
        self._grade = number
        self._grade = grade
        self._details = details

    def __str__(self):
        return 'str : {}'.format(self._name)

    def __repr__(self):
        return 'repr : {}'.format(self._name)


student1 = Student('Kim', 1, 1, {'gender': 'Male', 'score1': 95, 'score2': 87})
student2 = Student('Lee', 2, 2, {'gender': 'Male', 'score1': 77, 'score2': 92})
student3 = Student('Park', 3, 4, {'gender': 'Female', 'score1': 99, 'score2': 100})

print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)

# 리스트 선언

student_list = []

student_list.append(student1)
student_list.append(student2)
student_list.append(student3)

print()

print(student_list)

for x in student_list:
    print(repr(x))
    print(x)
