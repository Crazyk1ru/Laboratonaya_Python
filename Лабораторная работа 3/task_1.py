# TODO Напишите функцию для поиска индекса товара
def find_item_index(items, item_to_find): #создаем функцию
    try:  #начинает блок для обработки исключенний
        return items.index(item_to_find) #используем метод index в списке items что бы найти индекс первого вхождения элемента
    except ValueError: # определяет если возникнет исключение
        return None #возвращаем значение None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан'] # спсиок

for find_item in ['банан', 'груша', 'персик']: # перебирает каждый элемент в списке
    index_item = find_item_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None: # проверяет, не равен ли index_item значению None. Если он не равен None, это означает, что товар был найден.
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
