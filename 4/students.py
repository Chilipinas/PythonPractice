#4.	Создать классы студент, аспирант. Студент содержит свойства: номер группы, средний балл. Аспирант отличается от студента наличием научной работы (название работы в виде строки). Реализовать в классах следующие методы:
#•	вывести информацию (фио, возраст)
#•	вывести размер стипендии. Если средняя оценка равна 5, то стипендия 8000р для аспиранта и 6000р для студента, если меньше 5, то стипендия для аспиранта 6000р, для студента 4000р, в других случаях стипендия 0р
#•	Сравнение размера стипендии с другим студентом/аспирантом (больше или меньше)


class Student:
    def __init__(self, name, age, group_number, average_grade):
        self.name = name
        self.age = age
        self.group_number = group_number
        self.average_grade = average_grade

    def get_info(self):
        print("Name: {}, Age: {}".format(self.name, self.age))

    def get_scholarship(self):
        if self.average_grade == 5:
            return 6000
        elif self.average_grade < 5:
            return 4000
        else:
            return 0

    def compare_scholarship(self, other_student):
        if self.get_scholarship() > other_student.get_scholarship():
            return "{}'s scholarship is bigger".format(self.name)
        elif self.get_scholarship() < other_student.get_scholarship():
            return "{}'s scholarship is smaller".format(self.name)
        else:
            return "{}'s scholarship is the same as {}".format(self.name, other_student.name)


class Aspirant(Student):
    def __init__(self, name, age, group_number, average_grade, research_title):
        super().__init__(name, age, group_number, average_grade)
        self.research_title = research_title

    def get_info(self):
        super().get_info()
        print("Research Title: {}".format(self.research_title))

    def get_scholarship(self):
        if self.average_grade == 5:
            return 8000
        elif self.average_grade < 5:
            return 6000
        else:
            return 0


# example usage
student1 = Student("Jack Yar", 20, "31245", 5)
student2 = Student("Will Smith", 21, "31245", 4.5)
aspirant1 = Aspirant("Ryan Gosling", 26, "52315", 5, "Development of a gesture classifier using a webcam.")

student1.get_info()
aspirant1.get_info()

print(student1.get_scholarship())
print(aspirant1.get_scholarship())

print(student1.compare_scholarship(aspirant1))