def average(class_notes: dict[str, int]) -> float:
    """Calculates the average score from a dictionary of class notes."""
    if len(class_notes) == 0:
        return 0
    aver: int = 0
    for note in class_notes.values():
        aver += note
    return (aver / len(class_notes))


class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
print(average(class_3B))
