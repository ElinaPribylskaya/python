# Kласс House: id, Номер квартиры, Площадь, Этаж, Количество комнат, Улица, Тип здания, Срок эксплуатации.
# Функции-члены реализуют запись и считывание полей (проверка корректности), расчета возраста задания (необходимость в кап. ремонте).
# Создать список объектов. Вывести:
# a)	список квартир, имеющих заданное число комнат;
# б) список квартир, имеющих заданное число комнат и расположенных на этаже, который находится в заданном промежутке;

import datetime


class Flat:
    __id=0



    def __init__(self,number_init,square_init,floor_init,rooms_init,street_init,buildtype_init,year_init):
        self.__id = Flat.__id+1
        Flat.__id=Flat.__id + 1
        self.__number = number_init
        self.__square = square_init
        self.__floor = floor_init
        self.__rooms = rooms_init
        self.__street = street_init
        self.__buildtype = buildtype_init
        self.__year = year_init

    # чтение инкапсулированной массы
    def get_id(self):
        return self.__id
    def get_number(self):
        return self.__number
    def get_square(self):
        return self.__square
    def get_floor(self):
        return self.__floor
    def get_rooms(self):
        return self.__rooms
    def get_street(self):
        return self.__street
    def get_buildtype(self):
        return self.__buildtype
    def get_year(self):
        return self.__year

    def set_number(self,number):
        return self.__number==number
    def set_square(self,square):
        return self.__square==square
    def set_floor(self,floor):
        return self.__floor==floor
    def set_rooms(self,rooms):
        return self.__rooms==rooms
    def set_street(self,street):
        return self.__street==street
    def set_buildtype(self,buildtype):
        return self.__buildtype==buildtype
    def set_year(self,year):
        return self.__year==year

    def age(self):
        ages = 0
        current_year = datetime.date.today().year
        return current_year-self.get_year()

    @classmethod
    def curent_id(cls):
        return cls.__id

    @staticmethod
    def term_age(age):
        if age>50:
            print("Building must be reconstruct")
        else:
            print("Building must not be reconstruct")





house = []
number = 56
square = 72.5
floor = 6
rooms =  2
street = "Amuratorskaya"
buildtype = "blooks"
year=1954
flat = Flat(number,square,floor,rooms,street,buildtype,year)
house.append(flat)

number = 45
square = 172.5
floor = 5
rooms =  5
street = "Kolasa"
buildtype = "blooks"
year=1948
flat = Flat(number,square,floor,rooms,street,buildtype,year)
house.append(flat)

number = 12
square = 42.5
floor = 2
rooms =  1
street = "Gikalo"
buildtype = "blooks"
year=2011
flat = Flat(number,square,floor,rooms,street,buildtype,year)
house.append(flat)

print(Flat.curent_id())
Flat.term_age(45)
Flat.term_age(65)
# print("Enter information about the first automobile:")
# end = 'next'
# while end != "end":
#     brand = str(input("Enter the brand of the car: "))
#     model = str(input("Enter the model of the car: "))
#     production_year = str(input("Enter the year of production of car: "))
#     color = str(input("Enter the color of the car: "))
#     price = int(input("Enter the price of the car: "))
#     number = str(input("Enter the number of the car: "))
#     car = Car(brand, model, production_year, color, price, number)
#     end = str(input("Enter 'end' if it was the last car!, else write 'next'"))
#     autosalon.append(car)



number_rooms=int(input("Enter the number of rooms: "))

for i in range(len(house)):
    if house[i].get_rooms() == number_rooms:
        print(str(house[i].get_id())+" "+str(house[i].get_street())+" "+str(house[i].get_number())+" "+str(house[i].age()))

number_rooms=int(input("Enter the number of rooms: "))
floor_min=int(input("Enter the minimal floor: "))
floor_max=int(input("Enter the maximal floor: "))
for i in range(len(house)):
    if house[i].get_rooms() == number_rooms:
        if house[i].get_floor()>floor_min and house[i].get_floor()<=floor_max:
            print(str(house[i].get_id()) + " " + str(house[i].get_street()) + " " + str(house[i].get_number()))
