# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f'{self.name} barks!')

    def sit(self):
        print(f'{self.name} sits!')

    def roll_over(self):
        print(f'{self.name} rolled over!')
