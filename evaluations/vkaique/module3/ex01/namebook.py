def format_names(names: dict[str, str]) -> list[str]:
    """
    Função que recebe um dicionário e retorna
    uma lista com capitalize da primeira letra
    """
    return [f"{first.capitalize()} {last.capitalize()}" for first, last in names.items()]

print(format_names({"bruno":'fernandes'}))
