import operations
from platform   import system as system_name
from subprocess import call   as system_call

if __name__ == '__main__':
    command = 'cls' if system_name().lower().startswith('win') else 'clear'
    file_path = operations.json_create()
    system_call(command)
    while True:
        print(file_path)
        chois = input("\nДобро пожаловать в электронную библиотеку.\n1 - создание книги\n2 - удаление книги по Id\n3 - поиск книги по значению\n4 - просмотр всех книг\n5 - смена статуса\n6-Выход\n")
        if chois == "1":#команда создания книги
            system_call(command)
            data = operations.data_input()
            if data != False:
                operations.json_saver(data,file_path)
                system_call(command)
            system_call(command)
        if chois == "2":#команда удаления
            system_call(command)
            Id = int(input("Id книги для удаления - "))
            if Id == "Выход":
                system_call(command)
            else:
                system_call(command)
                operations.delete_book(file_path,Id)
                system_call(command)
        if chois == "3":#команда поиска
            system_call(command)
            val = input("Введите значение для поиска - ")
            print("Для выхода введите 1")
            operations.search_book(file_path,val)
            ex = input()
            if ex == "1":
                system_call(command)

        if chois == "4":#команда показа всех книг
            system_call(command)
            operations.show_all_books(file_path)
            next = input("1-для выхода\n")
            if next == "1":
                system_call(command)
        if chois == "5":#команда для редактирования статуса
            system_call(command)
            Id = int(input("Id книги для редактирования статуса - "))
            operations.change_status(file_path,Id)
            system_call(command)
        if chois == "6":#выход
            break


