import books.books as b
import json
import random
def data_input():  # функция ввода данных книги
    try:
        uni = [input("Название: "), input("Автор: "), int(input("Год выпуска: ")),
               int(input("Статус(1- да, 0-нет): "))]  # массив операций ввода данных
    except (ValueError or (uni[3] != (1 or 0))):
        return False
    else:
        if uni[3] != (1 or 0):
            return False
        if uni[3] == 1:
            uni[3] = True
        if uni[3] == 0:
            uni[3] = False
        book_example = b.book(random.randint(0, 9999999), uni[0], uni[1], uni[2], uni[3])
        return book_example.create_dict()



def json_create():
    file_pat = input("Перед началом работы введите путь существующего или нового .json файла - ")
    try:
        f = open(file_pat)
    except IOError:
        f = open(file_pat,"a")
        f = open(file_pat,"w")
        f.write(json.dumps({}))
    return file_pat

def json_saver(data,file_path):
    file = open(file_path,"r")
    text = file.read()
    file.close()
    text_dict = json.loads(text)
    text_dict.update({len(text_dict):data})
    json_text = json.dumps(text_dict)
    file = open(file_path, "w")
    file.write(json_text)
    file.close()

def show_all_books(file):
    db = open(file,"r")
    books = json.loads(db.read())
    for i in range(len(books)):
        number = str(i)
        book = books[number]
        book_info = b.book(book["Id"],book["Название"],book["Автор"],book["Год"],book["Статус"])
        book_info.print_info()
def delete_book(file,value):
    db = open(file, "r")
    books = json.loads(db.read())
    for i in range(len(books)):
        number = str(i)
        book = books[number]
        if book["Id"] == value:
            del books[number]
    json_data = json.dumps(books)
    file = open(file, "w")
    file.write(json_data)
    file.close()




