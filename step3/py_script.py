

class Animal:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def shout(self):
        print(f'{self.name}在叫')

    def run(self):
        print(f'{self.name}在跑')


class Cat(Animal):
    def __init__(self, name, color, age, gender, hair):
        super().__init__(name, color, age, gender)
        self.hair = hair

    def catch_mouse(self):
        print('抓老鼠')

    def shout(self):
        print(f'{self.name}喵喵叫')

if __name__ == '__main__':
    a = Animal('dog', 'black', 2, 'male')
    c = Cat('jack', 'yellow', 3, 'male', '短毛')

    print(c.hair)
    c.catch_mouse()
    a.shout()
    c.shout()






























