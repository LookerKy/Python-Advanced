# Section01-03
# 클래스 메소드, 인스턴스 메소드 , static 메소드

# 기본 인스턴스 메소드
class Student:
    """
    Student Class
    Author: Lee
    Date: 2021.03.30
    Description: Class, Static, Instance Method
    """
    # 클래스 변수
    tuition_per = 1.0

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        # 인스턴스 변수
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method
    def full_name(self):
        return '{} {}'.format(self._first_name, self._last_name)

    # Instance Method
    def student_detail(self):
        return 'Student Detail Info: {},{},{},{},{},{}'.format(self._id, self.full_name(), self._email, self._grade,
                                                               self._tuition, self._gpa)

    def get_fee(self):
        return 'Before Tuition => id  {}, fee: {}'.format(self._id, self._tuition)

    def get_fee_calc(self):
        return 'After tuition => id: {}, fee: {}'.format(self._id, self._tuition * Student.tuition_per)

    def __str__(self):
        return 'Student Info -> name: {}, grade: {}, email: {}'.format(self.full_name(), self._grade, self._email)

    # Class Method
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.tuition_per = per
        print('Succed! tuition change')

    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa)

    @staticmethod
    def is_scholaship_static(inst):
        if float(inst._gpa) >= 4.3:
            return '{} is a scholarship recipient'.format(inst.full_name())
        return 'Sorry'


student1 = Student(1, 'Kim', 'SaRang', 'student1@naver.com', '1', 400, 3.5)
student2 = Student(1, 'Lee', 'SaRang', 'student1@naver.com', '2', 500, 4.3)

print(student1.__dict__)
print(student2.__dict__)
print(student1)
print(student2)

print()

# 전체정보
print(student1.student_detail())
print(student2.student_detail())

print()

# 학비정보
print(student1.get_fee())
print(student2.get_fee())

print()

# 학비 인상
# Student .tuition_per = 1.2
Student.raise_fee(1.5)
print(student1.get_fee_calc())
print(student2.get_fee_calc())

# 클래스 메소드 인스턴스 생성 실습
student3 = Student.student_const(3, 'Park', "min ji", 'student3@gmail.com', '3', 550, '4.5')
student4 = Student.student_const(4, 'Cho', "Sunghan", 'student4@gmail.com', '4', 600, '4.1')

print(student3.student_detail())
print(student4.student_detail())

print(student3._tuition)
print(student4._tuition)


def is_scholarship(inst):
    if float(inst._gpa) >= 4.3:
        return '{} is a scholarship recipient'.format(inst.full_name())
    return 'Sorry'


print(is_scholarship(student1))
print(is_scholarship(student2))
print(is_scholarship(student3))
print(is_scholarship(student4))
