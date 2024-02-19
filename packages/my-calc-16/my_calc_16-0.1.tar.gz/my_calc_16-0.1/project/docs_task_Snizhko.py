
while True:
    """
    Скрипт повертає результат однієї з чотирьох арифметичних дій над двома числами
    
    :param first_number: Перше число
    :type first_number: float
    :param second_number: друге число
    :type second_number: float
    :param operator: оператор
    :type operator: str
    """
    first_number = float(input("Enter first nummber:"))
    second_number = float(input("Enter second number:"))
    operator = input("Choose action(+,-,/,*,q - exit):")
    if operator == "+":
        print(first_number+second_number)
    elif operator == "-":
        print(first_number-second_number)
    elif operator == "/":
        print(first_number / second_number)
    elif operator == "*":
        print(first_number*second_number)
    elif operator == "q":
        break
    else:
        print("помилка вводу")
    """
    :return: виводить результат 
    :rtype: float
    """