class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 0
        self.happiness = 5

    def feed(self):
        self.hunger -= 1
        self.happiness += 1
        print(f"{self.name} is fed and happy!")

    def play(self):
        if self.hunger >= 3:
            print(f"{self.name} is too hungry to play!")
        else:
            self.happiness += 2
            print(f"{self.name} is playing and having fun!")

    def sleep(self):
        self.hunger += 1
        self.happiness += 1
        print(f"{self.name} is sleeping and gaining energy.")

    def check_status(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Hunger: {self.hunger}")
        print(f"Happiness: {self.happiness}")


# Приклад використання класу Cat
my_cat = Cat("Whiskers", 3)
my_cat.check_status()  # Виведе поточний стан котика

my_cat.feed()  # Годуємо котика
my_cat.play()  # Граємо з котиком
my_cat.sleep()  # Котик спить

my_cat.check_status()  # Виведе оновлений стан котика
