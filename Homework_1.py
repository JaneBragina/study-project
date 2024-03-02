from solution import LittleBell

def lab_1():
    treuNum = 0
    while(treuNum == 0):
        num = float(input("Введите температуру в Цельсиях (Чтобы выйти из программы введите 777): "))
        if(num == 777):
            treuNum = 1
            return

        if (num < 15.5):
            print("Холодно")
        elif(num > 15.5 and num < 28):
            print("Нормально")
        else:
            print("Жарко")


def lab_2():
    num = int(input("Введите сколько строк: "))
    miy = False

    for i in range(num):
        string = input(f"Строка {i}: ")
        if ("кот" in string):
            miy = True

    if(miy):
        print("МЯУ")
    else:
        print("Нет")

def lab_3():
    booling = False
    string = []

    while(booling == False):
        word = input()
        if (word == 'стоп' or word == 'Стоп'):
            booling = True
        else:
            string.append(word)

    max_word = max(string, key=len)
    min_word = min(string, key=len)
    
    print(max_word, min_word)

    for elem in min_word:
        if(elem not in max_word):
            print("Нет")
            return
        
    print('Да')


def lab_4():
    booling = int(input("Введите кол-во покупочек: "))
    string = []

    for _ in range(booling):
        string.append(input())

    for i in range(booling):
        print(string[i])

def lab_5():
    word = input("Оденься... ")
    string = ''
    for elem in word:
        string += elem + elem

    print(string)

def gret():
    firstname = input("Ваше имя: ")
    secondname = input("Ваша фамилия: ")

    return firstname, secondname

def lab_6():
    firstname, secondname = gret()
    print(f"Здравствуйте, {firstname} {secondname}.")


def lab_7():
    bell = LittleBell()
    
    bell.sound()
    bell.sound()
    bell.sound()


def main():
    # lab_1()
    # lab_2()
    # lab_3()
    # lab_4()
    # lab_5()
    # lab_6()
    lab_7()

if __name__ == "__main__":
    main()