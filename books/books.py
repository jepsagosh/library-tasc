class book:#общий класс книги
    def __init__(self, Id: int, title: str, author: str, year: str, status : bool):
        self.Id = Id
        self.title = title
        self.author = author
        self.year = year
        self.status = status
        self.dic = {}
        if self.status == True:
            self.status_str = "В наличии"
        else:
            self.status_str = "Нет в наличии"


    def create_dict(self):#создания словаря с принятыми значениями
            self.dic["Название"] = self.title
            self.dic["Id"] = self.Id
            self.dic["Автор"] = self.author
            self.dic["Статус"]=self.status
            self.dic["Год"] = self.year
            return self.dic

    def import_dic(self,dic):#прием словаря для инициализации
        self.dic["Название"] = dic["Название"]
        self.dic["Id"] = dic["Id"]
        self.dic["Автор"] = dic["Автор"]
        self.dic["Статус"] = dic["Статус"]
        self.dic["Год"] = dic["Год"]

        self.Id = dic["Id"]
        self.author = dic["Автор"]
        self.year = dic["Год"]
        self.title = dic["Автор"]
        self.status = dic["Статус"]
        return self.dic


    def print_info(self):#вывод информации
        print("Id-",self.Id,",Статус-",self.status_str,"Название-",self.title, "Автор-",self.author,"Год-", self.year)





