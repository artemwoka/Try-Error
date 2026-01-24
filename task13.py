"""
Створити систему управління бібліотекою з можливістю
видачі та повернення книг з обробкою різних виняткових ситуацій.
"""


class LibraryError(Exception):
    """Базовий клас для помилок бібліотеки."""
    pass


class BookNotFoundError(LibraryError):
    """Виняток: книга не знайдена в каталозі."""
    pass


class BookNotAvailableError(LibraryError):
    """Виняток: всі примірники книги видані."""
    pass


class BookAlreadyReturnedError(LibraryError):
    """Виняток: книга вже повернута або не була видана."""
    pass


class InvalidQuantityError(LibraryError):
    """Виняток: некоректна кількість книг."""
    pass


class Library:
    """Клас для управління бібліотекою."""
    
    def __init__(self):
        """Ініціалізація бібліотеки.
        
        Структура каталогу:
        {
            "назва_книги": {
                "total": загальна_кількість,
                "available": доступна_кількість,
                "borrowed_by": [список_користувачів]
            }
        }
        """
        self.catalog = {}
    
    def add_book(self, title, quantity=1):
        """Додати книгу до каталогу.
        
        Параметри:
            - title (str): назва книги.
            - quantity (int): кількість примірників.
        
        Винятки:
            - InvalidQuantityError: якщо quantity <= 0.
        """
        if quantity <= 0:
            raise InvalidQuantityError("Кількість книг повинна бути більшою за нуль.")
        if title in self.catalog:
            self.catalog[title]["total"] += quantity
            self.catalog[title]["available"] += quantity
        else:
            self.catalog[title] = {
                "total": quantity,
                "available": quantity,
                "borrowed_by": []
            }
    
    def borrow_book(self, title, user):
        """Видати книгу користувачу.
        
        Параметри:
            - title (str): назва книги.
            - user (str): ім'я користувача.
        
        Винятки:
            - BookNotFoundError: книга відсутня в каталозі.
            - BookNotAvailableError: всі примірники видані.
        """
        if title not in self.catalog:
            raise BookNotFoundError(f"Книга '{title}' відсутня в каталозі.")
        if self.catalog[title]["available"] == 0:
            raise BookNotAvailableError(f"Всі примірники книги '{title}' видані.")
        self.catalog[title]["available"] -= 1
        self.catalog[title]["borrowed_by"].append(user)
    
    def return_book(self, title, user):
        """Прийняти повернення книги.
        
        Параметри:
            - title (str): назва книги.
            - user (str): ім'я користувача.
        
        Винятки:
            - BookNotFoundError: книга відсутня в каталозі.
            - BookAlreadyReturnedError: користувач не брав цю книгу.
        """
        if title not in self.catalog:
            raise BookNotFoundError(f"Книга '{title}' відсутня в каталозі.")
        if user not in self.catalog[title]["borrowed_by"]:
            raise BookAlreadyReturnedError(f"Користувач '{user}' не брав книгу '{title}'.")
        self.catalog[title]["available"] += 1
        self.catalog[title]["borrowed_by"].remove(user)
    
    def show_catalog(self):
        """Показати весь каталог."""
        print("Каталог бібліотеки:")
        for title, info in self.catalog.items():
            print(f"'{title}': Всього: {info['total']}, Доступно: {info['available']}")


if __name__ == "__main__":
    library = Library()
    
    # Приклад використання
    print("=== Система управління бібліотекою ===\n")
    
    # Додайте обробку винятків для наступних операцій:
    # 1. Додати книги до каталогу
    # 2. Видати книгу користувачу
    # 3. Повернути книгу
    # 4. Показати каталог

    try:
        library.add_book("1984", 1)
        library.add_book("To Kill a Mockingbird", 2)
        library.show_catalog()
        print()

        library.borrow_book("Harry Potter", "Alice")
        library.borrow_book("1984", "Bob")
        library.show_catalog()
        print()

        library.return_book("1984", "Alice")
        library.show_catalog()
    except InvalidQuantityError as iqe:
        print(f"Помилка: {iqe}")
    except BookNotFoundError as bnfe:
        print(f"Помилка: {bnfe}")
    except BookNotAvailableError as bnae:
        print(f"Помилка: {bnae}")
    except BookAlreadyReturnedError as barre:
        print(f"Помилка: {barre}")
    except Exception as e:
        print(f"Сталася помилка: {e}")