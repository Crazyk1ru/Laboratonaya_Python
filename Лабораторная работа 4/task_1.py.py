# TODO импортировать необходимые молули
# импортируем библиотеки csv и json
import csv
import json
#задаем имена входного и выходного файлов
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
#открываем csv файл для чтения с использованием csv.DictReader, который автоматом создает словари

def task() -> None:
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)  # TODO считать содержимое csv файла
        #преобразуем строки CSV в список словарей
        data = [row for row in csv_reader]
    #Сераилизуем данные в JSON и записываем в файл с отступами
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)# TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    #сампроверка
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
