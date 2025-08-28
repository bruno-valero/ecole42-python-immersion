def average(dic: dict[str, int]) -> float:
    """ Calculate the average of the grades """
    sum = 0
    for grade in list(dic.values()):
        sum = sum + grade
    try:
        return sum / len(dic)
    except ZeroDivisionError:
        print("Error: division by zero")
        # return float(0)
