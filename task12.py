"""
Створити систему реєстрації користувача з перевіркою даних.
Використати власні винятки для різних типів помилок.
"""


class ValidationError(Exception):
    """Базовий клас для помилок валідації."""
    pass


class InvalidEmailError(ValidationError):
    """Виняток для невалідної електронної пошти."""
    pass


class WeakPasswordError(ValidationError):
    """Виняток для слабкого пароля."""
    pass


class InvalidAgeError(ValidationError):
    """Виняток для невалідного віку."""
    pass


def validate_email(email):
    """Перевірити формат електронної пошти.
    
    Параметри:
        - email (str): адреса електронної пошти.
    
    Винятки:
        - InvalidEmailError: якщо email не містить '@' або '.':
    """
    if "@" not in email or "." not in email:
        raise InvalidEmailError("Електронна пошта повинна містити '@' та '.'")


def validate_password(password):
    """Перевірити надійність пароля.
    
    Параметри:
        - password (str): пароль користувача.
    
    Винятки:
        - WeakPasswordError: якщо пароль коротший 8 символів
                            або не містить цифр.
    """
    if len(password) < 8:
        raise WeakPasswordError("Пароль повинен бути не менше 8 символів.")
    if not any(char.isdigit() for char in password):
        raise WeakPasswordError("Пароль повинен містити принаймні одну цифру.")


def validate_age(age):
    """Перевірити вік користувача.
    
    Параметри:
        - age (int): вік користувача.
    
    Винятки:
        - InvalidAgeError: якщо вік менше 14 або більше 120.
    """
    if age < 14 or age > 120:
        raise InvalidAgeError("Вік повинен бути в діапазоні від 14 до 120 років.")


def register_user(email, password, age):
    """Зареєструвати користувача після валідації всіх даних.
    
    Параметри:
        - email (str): електронна пошта.
        - password (str): пароль.
        - age (int): вік.
    
    Повертає:
        - dict: дані користувача.
    """
    validate_email(email)
    validate_password(password)
    validate_age(age)

    dict_user = {
        "email": email,
        "password": password,
        "age": age
    }
    return dict_user


if __name__ == "__main__":
    print("=== Реєстрація користувача ===")
    
    email = input("Email: ")
    password = input("Пароль: ")
    try:

        age = int(input("Вік: "))
        user = register_user(email, password, age)
        print("Користувач успішно зареєстрований:", user)
    except ValueError:
        print("Помилка: введено некоректне значення для віку. Будь ласка, введіть число.")
    except InvalidEmailError as iee:
        print(f"Помилка валідації: {iee}")
    except WeakPasswordError as wpe:
        print(f"Помилка валідації: {wpe}")
    except InvalidAgeError as iae:
        print(f"Помилка валідації: {iae}")
    except Exception as e:
        print(f"Сталася помилка: {e}")