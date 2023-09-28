class Human:
    def __init__(self, name: str, age: int, work: str):
        self.name = name
        self.age = age
        self.work = work

    def __str__(self):
        return f'Это человек по имени {self.name}, ему {self.age} лет, работает в {self.work}'
    
    def greetings(self):
        print(f'Вас приветствует {self.name}')

stone = Human('Кирилл','39','GB')
oleg = Human('Олег','18','Студент')

stone.greetings()
oleg.greetings()

print(stone.__str__())
print(oleg.__str__())

