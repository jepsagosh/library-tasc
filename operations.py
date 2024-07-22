import books.books as b
import json
import random
def data_input():  # функция ввода данных книги
    uni = [input("Название:"), input("Автор:"), int(input("Год выпуска")),
           int(input("Статус(1- да, 0-нет):"))]  # массив операций ввода данных
    if uni[3] == 1:
        uni[3] = True
    if uni[3] == 0:
        uni[3] = False
    book_example = b.book(random.randint(0,9999999), uni[0], uni[1], uni[2], uni[3])
    if book_example.check_info() == False:
        print("Ошибка ввода данных")
        return False
    else:
        return book_example.create_dict()


def json_saver(data,file):
    json.dump({data[0]:data},open(file,"w"),indent= 5, ensure_ascii=False,sort_keys=True)
    file.write(',\n')
    return True

def json_reader(file):
    reading_file = open(file,"r")
    return json.loads(reading_file)

a = data_input()
print(json_saver(a,"books/booksdata.json"))
print(json_reader("books/booksdata.json"))