"""
Наследование позволяет создавать новый класс на основе уже существующего класса.

Ключевыми понятия: подкласс и суперкласс.
Подкласс наследует от суперкласса все публичные атрибуты и методы.
Суперкласс еще называется базовым (base class) или родительским (parent class),
а подкласс - производным (derived class) или дочерним (child class).
"""

"""
Написать иерархию классов для системы "Транспорт" (Vehicle → Car, Truck) с наследованием, миксинами
"""

"""
Mixin — это класс, предоставляющий реализации методов для повторного использования дочерними классами.
Миксин = маленький класс с одной конкретной задачей
"""


class Vehicle:
    """Транспортное средство"""

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.signal = False  # сигнал есть, но не сигналит

    def __str__(self):  # получаем при print()
        return f"Автомобиль {self.brand} {self.model} создан"

    def start_engine(self):
        return f"Двигатель {self.brand} {self.model} заведен"

    def stop_engine(self):
        return f"Двигатель {self.brand} {self.model} заглушен"

    def signal_start(self):
        if self.signal:
            return "FAAAAA"
        else:
            return f"Сигнал не нажат"


class Car(Vehicle):
    """Легковой авто"""

    def __init__(self, brand, model, doors):
        super().__init__(brand, model)  # наследуем базу от родителя
        self.doors = doors  # у легковых есть двери
        self.trunk_open = False  # у легковых есть багажник, который закрыт

    def open_trunk(self):
        if self.trunk_open:
            return f"Багажник у {self.brand} {self.model} закрыт"
        else:
            return f"Багажник у {self.brand} {self.model} открыт"


class Truck(Vehicle):
    """Грузовой авто"""

    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)  # наследуем базу от родителя
        # СВОИ особенности грузовика:
        self.capacity = capacity  # Грузоподъемность
        self.loaded = False  # Загружен ли

    def load_cargo(self):
        """Загрузить груз - есть ТОЛЬКО у грузовиков"""
        return f"{self.brand} {self.model}: Груз загружен"


class MediaMixin:
    """Миксин для установки медиа"""

    def upgrade_media(self, brand):
        return f"Установлено медиа {brand}"


class ConderMixin:
    """Миксин для установки кондиционера"""

    def upgrade_сonder(self):
        return f"Установлен кондиционер"


class CarWithMedia(Car, MediaMixin):
    pass


class CarWithConder(Car, ConderMixin):
    pass


class CarWithConderandMedia(Car, ConderMixin, MediaMixin):
    pass


vehicle = Vehicle("toyota", "camry")
print(vehicle)
print(vehicle.start_engine())
print(vehicle.stop_engine())
print("___")
car = Car("toyota", "corolla", 5)
print(car)
print(car.start_engine())
print(car.open_trunk())
car.trunk_open = True
print(car.open_trunk())
print("___")
truck = Truck("KAMAZ", "35100", 5000)
print(truck)
print(truck.capacity)
print(truck.load_cargo())
print(truck.signal_start())
truck.signal = True
print(truck.signal_start())
print("___")

luxCar = CarWithMedia("lexus", "lx", 5)
print(luxCar)
print(luxCar.upgrade_media("sony"))


superCar = CarWithConderandMedia("mersedes", "cla", 3)
print(superCar)
print(superCar.upgrade_media("sony"))
print(superCar.upgrade_сonder())
print(superCar.brand)
print(superCar.signal_start())
superCar.signal = True
print(superCar.signal_start())