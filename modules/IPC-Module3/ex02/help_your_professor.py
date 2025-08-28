def average(class_data: dict[str, float]) -> float:
    """Return the average of the values in the given dictionary."""
    if not class_data or not isinstance(class_data, dict):
        return float(0)
    return sum(class_data.values()) / len(class_data) if len(class_data) else 0
