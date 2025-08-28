def format_names(dic: dict[str, str]) -> list[str]:
    """Format the dic in list names
    :dic: Dictionary
    :returns: A list with the full names
    """
    list = []
    for key, value in dic.items():
        list.append(key.capitalize() + " " + value.capitalize())
    return list
