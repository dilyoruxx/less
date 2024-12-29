# инкапсуляция       Инкапсуляция — это когда доступ к данным и методам контролируется с помощью механизмов ограничения видимости
class Person:
    def __init__(self, name, age ,height):
        self.name = name    # публичный
        self._age = age  # Зашишенный
        self.__height = height    # приватный

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,new_height):
        self.height = new_height

    def info(self):
        print(f'Имя-{self.name}, возраст- {self._age}, рост-{self.__height}')
        self._security()
        self.__privat_method()

    def _security(self):
        print('Зашишенная информация')
    
    def __privat_method(self):
        print('приватная информация')

   
human = Person('dilyor', 14, 182)
human.info()
human._security()



 