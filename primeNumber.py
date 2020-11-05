def Prime(number):
    """check if the number is prime or not 
       @param: number: user input value
        
       @return: bool: True if number is prime else false
    """

    if type(number) != int:
        return False
    elif number == 0:
        return False
    elif number < 0 or number == None:
        return False
    elif number > 1:
        for i in range (2, number):
            if (number % i == 0):
                return False
            else:
                return True