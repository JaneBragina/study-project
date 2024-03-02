# Класс Accountant должен уметь одинаково успешно работать и с экземплярами
# класса Pupa и с экземплярами класса Lupa. У класса Accountant должен быть
# метод give_salary(worker). Который, получая на вход экземпляр классов Pupa или
# Lupa, вызывает у них метод take_salary(int). Необходимо придумать как
# реализовать такое поведение. Метод take_salary инкрементирует внутренний
# счётчик у каждого экземпляра класса на переданное ему значение.
# При этом Pupa и Lupa два датасайнтиста и должны работать с числами. У них
# есть метод do_work (spisok1, spisok2). Pupa считывают из обоих переданных ему
# списков числа и поэлементно их суммируют. Lupa считывают из обоих
# переданных ему списков числа и поэлементно их вычитают. Работники обоих
# типов выводят результат своих трудов на экран.
# Класс Accountant реализует логику начисления ЗП на ваше
# усмотрение, но будьте внимательны чтобы не получилось так, что
# Lupa получит за Pupa, а Pupa ничего не получит.

class Accountant:
    def give_salary(self, worker):
        worker.take_salary(1000)

class Pupa:
    def __init__(self):
        self.salary = 0

    def take_salary(self, amount):
        self.salary += amount

    def do_work(self, list1, list2):
        result = [x + y for x, y in zip(list1, list2)]
        print("Пупа:", result)

class Lupa:
    def __init__(self):
        self.salary = 0

    def take_salary(self, amount):
        self.salary += amount

    def do_work(self, list1, list2):
        result = [x - y for x, y in zip(list1, list2)]
        print("Лупа:", result)


def main():
    pupa = Pupa()
    lupa = Lupa()
    accountant = Accountant()

    pupa_list = [1, 2, 3]
    lupa_list = [3, 2, 1]

    pupa.do_work(pupa_list, pupa_list)
    lupa.do_work(lupa_list, lupa_list)

    accountant.give_salary(pupa)
    accountant.give_salary(lupa)

    print("Пупа:", pupa.salary)
    print("Лупа:", lupa.salary)


if __name__ == "__main__":
    main()