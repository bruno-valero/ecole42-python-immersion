def average(grades : dict[str, int]) -> float:
        """Calculates the average of the integer values in a dictionary."""
        if not grades or not isinstance(grades, dict):
                return 0.0
        value = grades.values()
        total = sum(value)
        res = total / len(value)
        return res