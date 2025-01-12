# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, delimiter='|'):
    # Разделяем строки на списки участников
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    # Находим общих участников и сортируем их в алфавитном порядке
    common_participants = sorted(participants1.intersection(participants2))

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group))  # Ожидается: ['Петров', 'Сидоров']

participants_first_group_comma = "Иванов,Петров,Сидоров"

participants_second_group_comma = "Петров,Сидоров,Смирнов"

print(find_common_participants(participants_first_group_comma, participants_second_group_comma, delimiter=','))
