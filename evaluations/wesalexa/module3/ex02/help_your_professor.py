def average(dic: dict[str, int]) -> float:
    """get a dict with names: numbers and return an average of the grades"""
    try:
        result = 0.0
        x = 0
        for i in dic:
            result += dic[i]
            x += 1
        return result / x
    except TypeError:
        return (0)
