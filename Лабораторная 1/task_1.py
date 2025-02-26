# TODO Написать 3 класса с документацией и аннотацией типов
from abc import ABC, abstractmethod

class Furniture(ABC):
    def __init__(self, material: str, height: float, width: float):
        if height <= 0 or width <= 0:
            raise ValueError("Высота и ширина должны быть положительными числами.")
        self.material = material
        self.height = height
        self.width = width

    @abstractmethod
    def use(self) -> str:
        """
        Использовать мебель.

        :return: Описание использования мебели.

        >>> chair = Chair("дерево", 1.0, 0.5)
        >>> chair.use()
        'Сидеть на стуле.'
        """
class Chair(Furniture):
    def use(self) -> str:
        return "Сидеть на стуле."

class Tree(ABC):
    """
    Абстрактный класс для деревьев.
    """

    def __init__(self, species: str, age: int):
        """
        Конструктор класса Tree.

        :param species: Вид дерева (должен быть строкой).
        :param age: Возраст дерева (должен быть неотрицательным целым числом).

        :raises ValueError: Если age отрицательный.
        """
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")

        self.species = species
        self.age = age

    @abstractmethod
    def grow(self) -> str:
        """
        Дерево растет.

        :return: Описание роста дерева.

        >>> oak = Oak("дуб", 10)
        >>> oak.grow()
        'Дуб растет.'
        """


class Oak(Tree):
    def grow(self) -> str:
        return "Дуб растет."


class SocialNetwork(ABC):
    """
    Абстрактный класс для социальных сетей.
    """

    def __init__(self, name: str, users_count: int):
        """
        Конструктор класса SocialNetwork.

        :param name: Название социальной сети (должно быть строкой).
        :param users_count: Количество пользователей (должно быть неотрицательным целым числом).

        :raises ValueError: Если users_count отрицательный.
        """
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")

        self.name = name
        self.users_count = users_count

    @abstractmethod
    def connect(self) -> str:
        """
        Соединить пользователей.

        :return: Описание соединения пользователей.

        >>> facebook = Facebook("Facebook", 2000000000)
        >>> facebook.connect()
        'Пользователи Facebook соединяются.'
        """
        ...


class Facebook(SocialNetwork):
    def connect(self) -> str:
        return "Пользователи Facebook соединяются."



if __name__ == "__main__":
    import doctest# TODO работоспособность экземпляров класса проверить с помощью doctest
    chair = Chair("дерево", 1.0 , 0.5)
    print(chair.use())
    oak = Oak("дуб",10)
    print(oak.grow())
    facebook = Facebook("Facebook", 2000000000)
    print(facebook.connect())
