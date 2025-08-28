def average(grades: dict[str, float]) -> float:
    """
    Recebe um dicionário com nomes e notas e retorna a média da turma.
    Se não houver notas, retorna 0.
    """
    if not grades:  # se o dicionário estiver vazio
        return 0
    return sum(grades.values()) / len(grades)

print(average({"vipach": 9.5, "rafael": 8.3}))