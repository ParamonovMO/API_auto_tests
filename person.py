class Person():
    """Модель человека"""

    def __init__(self, name, age):
        """Инициализаия атрибутов человека - имя, возраст"""
        self.name = name
        self.age = age
        print('Человек создан')

    def sing(self):
        """Просим человека спеть"""
        print(self.name, 'Человек поет')

    def dance(self):
        """Просим человека станцевать"""
        print(self.name, 'Человек танцует')


man = Person('Maxim', 32)
wooman = Person('Ksenia', 30)

man.dance()
wooman.sing()

print(man.name)
print(wooman.age)
