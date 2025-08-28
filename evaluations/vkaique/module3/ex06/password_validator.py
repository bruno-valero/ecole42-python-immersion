import string

def is_valid_password(password: str) -> bool:
    """
    Valida se a senha atende aos seguintes critérios:
    - mínimo de 8 caracteres
    - máximo de 16 caracteres
    - pelo menos 1 letra maiúscula
    - pelo menos 1 letra minúscula
    - pelo menos 1 dígito
    - pelo menos 1 caractere especial (string.punctuation)
    - não pode conter espaços
    """
    return (
        not any(ch.isspace() for ch in password) and  
        any(ch.islower() for ch in password) and   
        any(ch.isupper() for ch in password) and 
        any(ch.isdigit() for ch in password) and  
        any(ch in string.punctuation for ch in password)
    )
