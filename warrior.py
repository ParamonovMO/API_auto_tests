from base_class_warrior import Warrior


warrior = Warrior('Conon', 32, 200)
warrior.description_person()
warrior.change_weight(150)
print(warrior.description_person())
warrior.get_rage()