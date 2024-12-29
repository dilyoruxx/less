"Наследование, абстракция, инкапсуляция и полиморфизм"
" DRY - Don`t Repeat Yourself == не повторяй себя"

# Наследоание
'''
Когда дочерный класс наследует все его свойство
'''
class Car: # Родительский класс и Дочерний класс 
    def __init__(self, marka, model, color):    #__init__.py конструктор
        "Атрибут объекта"
        self.marka = marka
        self.model = model
        self.color = color
        
    def info(self):
        print(f"Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}") 

class Daewoo(Car):
    def __init__(self, marka, model, color, year):
        #super().__init__(marka, model, color)
        Car.__init__(self, marka, model, color)
        self.year = year

    def info(self):
        print(f"Марка машины-{self.marka}, модель-{self.model}, цвет-{self.color}, год выпуска -{self.year}") 

# nexia = Daewoo('Daewoo', 'Nexia', 'green', 1996)
# nexia.info()

# Абстракция
'''
Абстракция: Абстрактный класс с абстрактными методами, 
которые должны быть реализованы в наследуемых классах.
'''

# Полиморфизм
'''
Полиморфизм: Один метод, который работает с объектами разных типов, 
но каждый тип реализует его по-своему.
'''

class Animal:       #- абстрактный класс, 

    def make_sound(self):   #   абс функция не реализуется
        pass

class Cat(Animal):
    def make_sound(self):
        print("MEOW-MEOW")


class Dog(Animal):
    def make_sound(self):
        print("GAF-GAF")


class Cow(Animal):
    def make_sound(self):
        print("Moo-Moo")


# cat = Cat()     #   только создали
# dog = Dog()
# cow = Cow()


# cat.make_sound()
# dog.make_sound()
# cow.make_sound()

#Класс для обработки платежей 
class CreditCardPayment():
    def proccess_payment(self, amount):
        return print(f'Обработка по кредитной карте, на сумму {amount}$')
    
#Класс для обработки платежей 
class PayPalPayment:
    def proccess_payment(self, amount):
        return print(f'Обработка по PayPal, на сумму {amount}$')
    
def make_payment(payment_method, amount):
    payment_method.proccess_payment(amount)
    
credit_card_payment = CreditCardPayment()
paypal = PayPalPayment

# make_payment(credit_card_payment, 100)
# make_payment(paypal, 200)