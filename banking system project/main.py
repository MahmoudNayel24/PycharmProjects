class Person:
    def __init__(self, name, age, gender, job):
        self.name = str(name)
        self.age = int(age)
        self.gender = str(gender)
        self.job = str(job)

    def introduce(self):
        print("name: ", self.name, "\n age: ", self.age, "\ngender: ", self.gender, "\n job: ", self.job, "\n")


class Student(Person):
    def __init__(self, name, age, gender, job, major):
        super().__init__(name, age, gender, job)
        self.major = str(major)

    def introduce(self):
        print("name: ", self.name, "\n age: ", self.age, "\ngender: ", self.gender, "\n job: ", self.job, "\n major: ", self.major, "\n")
class Teacher(Person):
    def __init__(self, name, age, gender, job, subject):
        super().__init__(name, age, gender, job)
        self.subject = str(subject)
    def introduce(self):
        print("name: ", self.name, "\n age: ", self.age, "\ngender: ", self.gender, "\n job: ", self.job, "\n subject: ",self.subject, "\n")


