# TODO Найдите количество книг, которое можно разместить на дискете
a = 100
b = 50
c = 25
d = 4

m = 1.44
q = m * 1024 * 1024

total = a * b * c
book = total * d

number_of_books = q // book
print("Количество книг, помещающихся на дискету:", int(number_of_books))
