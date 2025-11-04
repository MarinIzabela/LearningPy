from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, vehicle_id, distance_traveled, fuel_level=100, engine_status=True):
        self._vehicle_id = vehicle_id
        self._distance_traveled = distance_traveled
        self.__fuel_level = fuel_level
        self.__engine_status = engine_status

    @property
    def vehicle_id(self):
        return self._vehicle_id

    @property
    def distance_traveled(self):
        return self._distance_traveled

    @distance_traveled.setter
    def distance_traveled(self, km):
        self._distance_traveled = km

    @property
    def fuel_level(self):
        return self.__fuel_level

    @fuel_level.setter
    def fuel_level(self, val):
        self.__fuel_level = val

    @property
    def engine_status(self):
        return self.__engine_status

    @engine_status.setter
    def engine_status(self, ok):
        self.__engine_status = bool(ok)

    @abstractmethod
    def check_maintenance(self):
        pass


class Truck(Vehicle):
    SERVICE_KM = 5000

    def check_maintenance(self) -> str:
        if (self.fuel_level < 10) or (not self.engine_status):
            return f"Alert: {self.vehicle_id} - Critical maintenance needed!"
        if self.distance_traveled >= self.SERVICE_KM:
            return f"Truck {self.vehicle_id} needs service."
        return f"Truck {self.vehicle_id} is fine."


class Bike(Vehicle):
    SERVICE_KM = 500

    def check_maintenance(self) -> str:
        if (self.fuel_level < 10) or (not self.engine_status):
            return f"Alert: {self.vehicle_id} - Critical maintenance needed!"
        if self.distance_traveled >= self.SERVICE_KM:
            return f"Bike {self.vehicle_id} needs service."
        return f"Bike {self.vehicle_id} is fine."


class Drone(Vehicle):
    SERVICE_KM = 500

    def check_maintenance(self) -> str:
        if (self.fuel_level < 10) or (not self.engine_status):
            return f"Alert: {self.vehicle_id} - Critical maintenance needed!"
        if self.distance_traveled >= self.SERVICE_KM:
            return f"Drone {self.vehicle_id} needs service."
        return f"Drone {self.vehicle_id} is fine."


fleet = [Truck("T1", distance_traveled=12000, fuel_level=60, engine_status=True),
         Truck("T2", distance_traveled=12000, fuel_level=60, engine_status=True),
         Bike("B1", distance_traveled=1500, fuel_level=80, engine_status=True),
         Drone("D1", distance_traveled=400, fuel_level=5, engine_status=False),
         Drone("D2", distance_traveled=900, fuel_level=70, engine_status=True)]

for vehicle in fleet:
    msg = vehicle.check_maintenance()
    print(msg)
    if (vehicle.fuel_level < 10) or (not vehicle.engine_status):
        break





