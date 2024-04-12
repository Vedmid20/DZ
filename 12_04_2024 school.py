from colorama import Fore, init, Style
import random
init(autoreset=True)


class SchoolMember:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def tell(self):
        return self.name


class Teacher(SchoolMember):
    def __init__(self, name, lastname, surname, salary):
        super().__init__(name, lastname)
        self.surname = surname
        self.salary = salary

    def tell(self):
        return f'Вчитель {super().tell()} {self.surname}, зарплата:  {self.salary}'


class Student(SchoolMember):
    def __init__(self, name, lastname, mark1, mark2, mark3):
        super().__init__(name, lastname)
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        self.lstMarks = [mark1, mark2, mark3]

    def tell(self):
        return f'Студент {super().tell()}, бали: {self.mark1}, {self.mark2}, {self.mark3}, середній бал: {(self.mark1 + self.mark2 + self.mark3) / len(self.lstMarks)}'


lst = []

print(Fore.LIGHTGREEN_EX + f"{'-' * 5} Вид заповнення {'-' * 5}")
print('1.Введення зарплати власноруч\n2.Введення зарплати через рандом')
choiceT = int(input('Введіть тип заповнення зарплати вчителя: '))
print('1.Введення балів власноруч\n2.Введення балів через рандом')
choiceS = int(input('Введіть тип заповнення балів студента: '))

if choiceT == 1:
    for i in range(2):
        print(Fore.LIGHTGREEN_EX + f"{'-' * 5} Дані про вчителя {'-' * 5}")
        lst.append(Teacher(name=str(input('Введіть імя вчителя: ')), lastname=str(input('Введіть прізвище вчителя: ')),
                           surname=str(input('Введіть по батькові вчителя: ')), salary=int(input('Введіть зарплату вчителя: '))))
elif choiceT == 2:
    for i in range(2):
        print(Fore.LIGHTGREEN_EX + f"{'-' * 5} Дані про вчителя {'-' * 5}")
        lst.append(Teacher(name=str(input('Введіть імя вчителя: ')), lastname=str(input('Введіть прізвище вчителя: ')),
                           surname=str(input('Введіть по батькові вчителя: ')), salary=random.randint(8000, 15000)))
else:
    print(Fore.LIGHTRED_EX + 'Помилка: ', 'Ви допустили помилку в виборі операції')

if choiceS == 1:
    for i in range(2):
        print(Fore.LIGHTGREEN_EX + f"{'-' * 5} Дані про студента {'-' * 5}")
        lst.append(Student(name=str(input('Введіть імя студента: ')), lastname=str(input('Введіть прізвище студента: ')),
                           mark1=int(input('Введіть перший бал: ')), mark2=int(input('Введіть другий бал: ')), mark3=int(input('Введіть третій бал: ')),))

elif choiceS == 2:
    for i in range(2):
        print(Fore.LIGHTGREEN_EX + f"{'-' * 5} Дані про студента {'-' * 5}")
        lst.append(Student(name=str(input('Введіть імя студента: ')), lastname=str(input('Введіть прізвище студента: ')),
                           mark1=random.randint(1, 12), mark2=random.randint(1, 12), mark3=random.randint(1, 12),))
else:
    print(Fore.LIGHTRED_EX + 'Помилка: ', 'Ви допустили помилку в виборі операції')

print(Fore.LIGHTGREEN_EX + f'{"-"*5} Загальні дані {"-"*5}')
for i in lst:
    print(Fore.LIGHTYELLOW_EX + '- '*13)
    print(i.tell())
