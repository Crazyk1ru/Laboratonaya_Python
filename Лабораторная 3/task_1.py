class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга '{self.name}'. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()}. Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, (float, int)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self._duration = float(value)

    def __str__(self):
        return f"{super().__str__()}. Продолжительность: {self.duration} ч."


# Примеры использования
paper_book = PaperBook("Война и мир", "Лев Толстой", 1225)
audio_book = AudioBook("1984", "Джордж Оруэлл", 11.5)

print(paper_book)  # Книга 'Война и мир'. Автор Лев Толстой. Количество страниц: 1225
print(repr(paper_book))  # PaperBook(name='Война и мир', author='Лев Толстой')

print(audio_book)  # Книга '1984'. Автор Джордж Оруэлл. Продолжительность: 11.5 ч.
print(repr(audio_book))  # AudioBook(name='1984', author='Джордж Оруэлл')
