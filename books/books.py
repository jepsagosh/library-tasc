class book:#общий класс книги
    def __init__(self, Id: int, title: str, author: str, year: int, status : bool):
        self.Id = Id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.dic = {}


    def check_info(self):
        if ((type(self.Id)!= int )or(type(self.title) != str) or type(self.author) != str or type(self.year) != int or type(self.status)!= bool):
            return False
        else:
            return True

    def create_dict(self):
        if book.check_info(self) == True:
            self.dic["Название"] = self.title
            self.dic["Id"] = self.Id
            self.dic["Автор"] = self.author
            self.dic["Статус"]=self.status
            self.dic["Год"] = self.year
            return self.dic
        else:
            return False
    def print_info(self):
        return self.dic





