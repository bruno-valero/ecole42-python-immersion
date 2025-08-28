def format_names(names: dict[str, str]) -> list[str]:
   """Formats full names from a dictionary of first and last names."""
   if not names or not isinstance(names, dict):
      return []
   return [f"{name} {last}" for name, last in names.items()]

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}

print(format_names([46546]))