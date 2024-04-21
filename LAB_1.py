from abc import ABC, abstractmethod
from typing import Union

class Animal:
    def __init__(self, name: str, age: int, species: str):
        """
        Абстрактный класс для описания животных.

        :param name: Имя животного
        :param age: Возраст животного, в годах
        :param species: Вид животного

        Примеры:
        >>> lion = Lion("Simba", 3)
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age = age

        if not isinstance(species, str):
            raise TypeError("Вид должен быть строкой")
        self.species = species

    def sound(self) -> None:
        """Издает звук.
        Примеры:
        lion = Lion("Simba", 3, "Lion")
        lion.sound()
        """
        pass

    def move(self) -> None:
        """Двигается.
        Примеры:
        lion = Lion("Simba", 3, "Lion")
        lion.move()
        """
        pass

class Vehicle:
    def __init__(self, brand: str, model: str, year: int):
        """
        Абстрактный класс для описания транспортных средств.

        :param brand: Марка транспортного средства
        :param model: Модель транспортного средства
        :param year: Год выпуска

        Примеры:
        >>> car = Car("Toyota", "Camry", 2020)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка должна быть строкой")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        self.model = model

        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть целым числом")
        if year < 0:
            raise ValueError("Год выпуска не может быть отрицательным")
        self.year = year

    def drive(self) -> None:
        """Двигается.
        Примеры:
        car = Car("Toyota", "Camry", 2020)
        car.drive()
        """
        pass

    def stop(self) -> None:
        """Останавливается.
        Примеры:
        car = Car("Toyota", "Camry", 2020)
        car.stop()"""
        pass

class ElectronicDevice:
    def __init__(self, name: str, power: Union[int, float], weight: Union[int, float]):
        """
        Абстрактный класс для описания электронных устройств.

        :param name: Название устройства
        :param power: Мощность устройства, в ваттах
        :param weight: Вес устройства, в кг

        Примеры:
        >>> smartphone = Smartphone("iPhone", 5, 0.2)
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        self.name = name

        if not isinstance(power, (int, float)):
            raise TypeError("Мощность должна быть числом")
        if power < 0:
            raise ValueError("Мощность не может быть отрицательной")
        self.power = power

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес должен быть числом")
        if weight < 0:
            raise ValueError("Вес не может быть отрицательным")
        self.weight = weight

    def turn_on(self) -> None:
        """Включается.
        Примеры:
        smartphone = Smartphone("iPhone", 5, 0.2)
        smartphone.turn_on()
        """
        pass

    def turn_off(self) -> None:
        """Выключается.
        Примеры:
        smartphone = Smartphone("iPhone", 5, 0.2)
        smartphone.turn_off()
        """
        pass