# ООП - объектно ориентиованная программа

# Snake key -змеиней регистр
# name_first = 'Ergashov'

# Camel key - верблюжей регистр
#MyCar

class Car:  # шаблон, чертеж
    # атрибути класса (вне класса переменные)
    marka = 'mersedes'
    model = 'cls'
    color  = 'red'
    def __init__(self, marka, model, color):   # ссылка на текущий объект сам объект. конструктор
        self.marka = marka
        self.model = model
        self.color  = color

    def info(self): # функцию назвали методом
        print(f'марка машины- {self.marka}, модель машины- {self.model}, цвет машины- {self.color}')

# mers1 = Car()
# print(mers1.marka)

mers1 = Car('mersedes', 'cls', 'black')
mers1.info()


bmw1 = Car('bmw', 'X5', 'red')
bmw1.info()



    

    
