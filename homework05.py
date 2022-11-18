# Задание 1
# Создайте аналог телефонной книги. 
# Каждая запись в книге должна 
# иметь идентификационный номер, имя, фамилия, дату рождения, профессию.
# Напишите для этого класса метод get_information которая будет 
# выдавать информацию об экземпляре этого класса.

# Пример входных данных:

# >>>from datetime import date >>> >>>c = Contact(id=1,   
#     first_name='John',       last_name='Dow',   
#     birth_date=date(day=21, month=4, year=1996),   
#     profession='Python developer')

# Пример выходных данных:

# >>>c.get_information()

# ID - 1
# Full name - John Dow
# Birth Date - 21.04.1996
# Profession - Python developer

from datetime import date

class Contact:

    def __init__(self, id, full_name, birth_date, profession):
        self.id = id
        self.full_name = full_name
        self.birth_date = birth_date
        self.profession = profession

    def get_information(self):
        return f'ID - {self.id}\nFull name - {self.full_name}\nBirth Date - {self.birth_date}\nProfession - {self.profession}'

    
c = Contact(1, "Zhanybekov Adilet", date(2004,1,4),"Programmer")  
      
print(c.get_information())




# Задание 2
# Создайте иерархию классов для описания фауны со следующими требованиями:

# Обязательное присутствие классов птиц, рыбы и млекопитающих. 
# Напишите для них методы и парамметры свойственные для животных этих классов. 
# Так же обязательное присутствие классов хищников и травоядных. 
# У классов хищник и травоядное обязательно должен быть метод eat. 
# Этот метод должен показывать, чем питается животное.

# Создайте классы сокол, пингвин, форель, кит. 
# Наследуйте эти классы от вышеуказанных классов, 
# при наследовании обратите внимание на природные свойства животных этих классов. 
# Если есть необходимость, перепишите методы родителя для того чтобы эти методы 
# соответствовали свойствам животного. 
# Создайте экземпляры классов сокол, пингвин, форель, кит. 
# Вызовите все доступные им методы

# Пример:

# >>>p = Penguin(type='royal', age='1 year')
# >>>p.eat()
# I eat fish
# >>>p.can_swim()
# True
# >>>p.can_fly()
# I cannot fly
          
class birds:
    
    def __init__(self, type, age):
        self.type = type
        self.age = age
    
    def fly(self):
        print(f'{True}')
        
    def swim(self):
        print(f'{False}')
    
    def run(self):
        print(f'{False}') 

class fishes:

    def __init__(self, type, age):
        self.type = type
        self.age = age
    
    def swim(self):
        print(f'{True}')
        
    def fly(self):
        print(f'{False}')
    
    def run(self):
        print(f'{False}')

class mammals:

    def __init__(self, type, age):
        self.type = type
        self.age = age
    
    def run(self):
        print(f'{True}')
        
    def swim(self):
        print(f'{False}')
    
    def fly(self):
        print(f'{False}') 



class predator:
    
    def eat(self):
        print('I hunt and eat meat')
    
class herbivores:

    def eat(self):
        print('I eat only the grasses')


class Falcon(birds, predator):
    pass

class Pengiun(birds, predator):
    def swim(self):
        print(f'{True}')

class Trout(fishes, predator):
    pass

class Whale(mammals, predator):
    def swim(self):
        print(f'{True}')
    pass
    
f = Falcon("newtoni", 2)
f.eat()
f.fly()
f.swim()
f.run()

p = Pengiun("royal", 3)
p.eat()
p.fly()
p.swim()
p.run()

t = Trout("royal", 4)
t.eat()
t.fly()
t.swim()
t.run()

w = Whale("Blue Whale", 20)
w.eat()
w.fly()
w.swim()
w.run()


# Задание 3
# Вам дана функция:

# def show_even_numbers(*args):
#     even_numbers_lst = [] 
#     for i in args:
#         try:
#             if i%2 == 0:
#                 even_numbers_lst.append(i)
#         except TypeError:
#                     continue 
#     return even_numbers_lst
# Напишите декоративную функцию для этой функции чтобы выводить
# каждое чётное число введённое в эту функцию раздельно,
# а так же указывать каким номером вы их получили.

# Пример выходных данных:

# >>>show_even_numbers(3, 8, 'hello', 100, [14, 13, 12], 12)
# 1 - 8
# 2 - 100
# 3 - 12



def show_even_numbers(*args):
    even_numbers_lst = [] 
    for i in args:
        try:
            if i%2 == 0:
                even_numbers_lst.append(i)
        except TypeError:
                    continue 
    return even_numbers_lst

def rewrite_list(func):
    count = 1
    for i in func:
        print(f'{count} - {i}')
        count += 1
    
rewrite_list(show_even_numbers(3, 8, 'hello', 100, [14, 13, 12], 12))

