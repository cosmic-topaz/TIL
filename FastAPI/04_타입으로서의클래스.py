## 변수의 타입으로 클래스 선언하기

class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name


