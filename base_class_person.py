class Person:
    """Создаем человека"""
    count_class = 0

    def __init__(self, name, age, height):
        """Инициализация атрибутов человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100
        Person.count_class += 1

    def description_person(self):
        """Получение описания человека"""
        description = f"Меня зовут {self.name}, мне {self.age}, мой рост {self.height} и мой вес {self.weight}"
        print(description)

    def get_weight(self):
        """Запросить вес человека"""
        print(f'Мой вес {self.weight}')

    def change_weight(self, weight):
        """Изменить вес человека"""
        self.weight = weight
        print('Вес изменен')