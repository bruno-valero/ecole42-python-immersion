def format_names(names: dict[str, str]) -> list[str]:
    """get a dict and transform to a list"""
    lt = []
    for i in names:
        lt.append(i.capitalize() + " " + names[i].capitalize())
    return lt
