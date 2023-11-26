from base_class_person import Person

class Warrior(Person):
    """Создаем класс война"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Запросить вес человека"""
        print(f'Заряд ярости = {self.rage}')

    def description_person(self):
        """Переопределение метода родителя"""
        description = f"Меня зовут {self.name}, мне {self.age}, ярость {self.rage}"
        print(description)