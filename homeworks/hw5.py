class Person:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def to_string(self):
        return f"Имя: {self.full_name}, Возраст: {self.age}"

    def __str__(self):
        return f"Имя: {self.full_name}, Возраст: {self.age}"


class Driver(Person):
    def __init__(self, full_name, age, experience):
        super().__init__(full_name, age)
        self.experience = experience

    def to_string(self):
        return f"Водитель: {super().to_string()}, Стаж вождения: {self.experience}"

    def __str__(self):
        return f"Водитель: {super().to_string()}, Стаж вождения: {self.experience}"


class Engine:
    def __init__(self, power, company):
        self.power = power
        self.company = company

    def to_string(self):
        return f"Мощность: {self.power}, Производитель: {self.company}"

    def __str__(self):
        return f"Мощность: {self.power}, Производитель: {self.company}"


class Car:
    def __init__(self, marka, car_class, driver: Driver, engine: Engine):
        self.marka = marka
        self.car_class = car_class
        self.driver = driver
        self.engine = engine

    def start(self):
        print("Поехали")

    def stop(self):
        print("Останавливаемся")

    def turn_right(self):
        print("Поворот направо")

    def turn_left(self):
        print("Поворот налево")

    def to_string(self):
        return f"Марка: {self.marka}, Класс: {self.car_class}, {self.driver.to_string()}, {self.engine.to_string()}"

    def __str__(self):
        return f"Марка: {self.marka}, Класс: {self.car_class}, {self.driver.to_string()}, {self.engine.to_string()}"


class Lorry(Car):
    def __init__(self, marka, car_class, driver, engine, carrying):
        super().__init__(marka, car_class, driver, engine)
        self.carrying = carrying

    def to_string(self):
        return f"{super().to_string()}, Грузоподъемность: {self.carrying}"

    def __str__(self):
        return f"{super().to_string()}, Грузоподъемность: {self.carrying}"


class SportCar(Car):
    def __init__(self, marka, car_class, driver, engine, speed):
        super().__init__(marka, car_class, driver, engine)
        self.speed = speed

    def to_string(self):
        return f"{super().to_string()}, Максимальная скорость: {self.speed}"

    def __str__(self):
        return f"{super().to_string()}, Максимальная скорость: {self.speed}"


driver1 = Driver("Иван Иванов", 35, 5)
engine1 = Engine(200, "Toyota")
car1 = Car("Toyota Camry", "Седан", driver1, engine1)

driver2 = Driver("Петр Петров", 48, 10)
engine2 = Engine(300, "Volvo")
lorry1 = Lorry("Volvo FH", "Грузовик", driver2, engine2, 5000)

driver3 = Driver("Анна Сидорова", 27, 3)
engine3 = Engine(400, "Ferrari")
sport_car1 = SportCar("Ferrari 488", "Спорткар", driver3, engine3, 300)

print(car1)
print(lorry1)
print(sport_car1)
