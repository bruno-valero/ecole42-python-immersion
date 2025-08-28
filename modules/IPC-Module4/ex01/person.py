class Person:
    name: str
    age: int

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def birthday(self) -> None:
        self.age += 1


#     def __str__(self):
#         return f"{self.__class__.__name__}(name={self.name}, age={self.age})"

# teste = Person("teste", 45)
# teste2 = Person("teste2", 50)
# print(teste)
# print(teste2)
