from dataclasses import dataclass

@dataclass
class Coordinates:
    lat: float
    long: float



coord1 = Coordinates(40.7128, -74.0060)
coord2 = Coordinates(34.0522, -118.2437)
coord3 = Coordinates(40.7128, -74.0060)
print(coord1)
print(coord2)
print(coord1 == coord2)
print(coord1 == coord3)