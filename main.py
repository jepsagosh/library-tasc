import operations
from platform   import system as system_name
from subprocess import call   as system_call

if __name__ == '__main__':
    command = 'cls' if system_name().lower().startswith('win') else 'clear'
    file_path = operations.json_create()
    system_call(command)
    while True:
        chois = input("Добро пожаловать в электронную библиотеку.\n1 - создание книги\n2-удаление книги по Id\n4 - просмотр всех книг\n5-выход\n")
        if chois == "1":
            system_call(command)
            data = operations.data_input()
            if data != False:
                operations.json_saver(data,file_path)
                system_call(command)
            system_call(command)
        if chois == "2":
            system_call(command)
            Id = int(input("Id книги для удаления - "))
            if Id == "Выход":
                system_call(command)
            else:
                system_call(command)
                operations.delete_book(file_path,Id)
                system_call(command)
        if chois == "4":
            system_call(command)
            operations.show_all_books(file_path)
            next = input("1-для выхода\n")
            if next == "1":
                system_call(command)
        if chois == "5":
            system_call(command)
            break


