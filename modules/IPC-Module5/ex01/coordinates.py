from typing import Any


class Coordinates:
    lat: float
    long: float

    def __init__(self, lat: float, long: float) -> None:
        self.lat = lat
        self.long = long

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, self.__class__):
            lat_eq = self.lat == other.lat
            long_eq = self.long == other.long
            return lat_eq and long_eq
        return False

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(lat={self.lat}, long={self.long})"
