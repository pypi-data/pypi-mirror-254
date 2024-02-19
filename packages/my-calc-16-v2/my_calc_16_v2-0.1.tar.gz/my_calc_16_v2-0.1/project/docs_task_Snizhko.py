
class Claculator():
    """
    Скрипт повертає результат однієї з чотирьох арифметичних дій над двома числами
    
    :param first_number: Перше число
    :type first_number: float
    :param second_number: друге число
    :type second_number: float
    :param operator: оператор
    :type operator: str
    """
    def __init__(self,
                 first_number:float=0.0,
                 second_number:float=0.0,
                 operator:str=""):
        self.first_number = float(input("Enter first nummber:"))
        self.second_number = float(input("Enter second number:"))
        self.operator = input("Choose action(+,-,/,*):")

    def action(self):
        """
        Метод обчислювання дій
        
        :return: Повертає обчислювання та виводить помилку якщо щось не так 
        :rtype: float
        """
        if self.operator == "+":
            return (self.first_number + self.second_number)
        elif self.operator == "-":
            return (self.first_number - self.second_number)
        elif self.operator == "*":
            return (self.first_number * self.second_number)
        elif self.operator == "/":
            return (self.first_number / self.second_number)
        else:
            return ("Помилка вводу")

calc = Claculator()
print(calc.action())