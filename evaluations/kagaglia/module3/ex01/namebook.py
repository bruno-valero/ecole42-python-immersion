def format_names(name_dict : dict[str, str]) -> list[str]:
    """
    Formats the first and last names from a dictionary by capitalizing each one."""
    namess = []
    for name, lastname in name_dict.items():
        names = f"{name.capitalize()} {lastname.capitalize()}"
        namess.append(names)
    return namess