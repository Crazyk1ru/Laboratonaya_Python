# TODO решите задачу
#импортируем библиотеку json
import json
INPUT_FILENAME = "data.json"

def task() -> float:
    total_sum = 0.0

    # читаем данные из JSON файла
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        # проходим по каждому словарю в списке
        for item in data:
            score = item.get("score", 0)  # получаем значение score, иначе 0
            weight = item.get("weight", 0)  # получаем значение weight, инчае 0

            # вычисляем произведение и добавляем к общей сумме
            total_sum += score * weight

    # возвращаем сумму, округленную до 3 знаков после запятой
    return round(total_sum, 3)


if __name__ == '__main__':
    print(task())