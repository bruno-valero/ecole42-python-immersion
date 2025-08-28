def format_cents(cents: int) -> str:
    value = cents * -1 if cents < 0 else cents
    brl = value / 100
    str_cents: str = (
        f"[{'+' if cents >= 0 else '-'}] R$ {brl:,.2f}".replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )
    return str_cents
