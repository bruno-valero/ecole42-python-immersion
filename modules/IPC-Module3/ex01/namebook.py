def format_names(persons: dict[str, str]) -> list[str]:
    if not persons or not isinstance(persons, dict):
        return []
    """Return a list of full names in the format 'first last' from a dict of names."""
    return [f"{item[0]} {item[1]}".title() for item in persons.items()]
