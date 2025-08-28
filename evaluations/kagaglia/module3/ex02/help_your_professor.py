def average(grades : dict[str, int]) -> float:
        """Calculates the average of the integer values in a dictionary."""
        value = grades.values()
        if not grades:
                return 0.0
        total = sum(value)
        res = total / len(value)
        return res