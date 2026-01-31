import string
import random
from password.new_password import generate_password

def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
    for char in password:
        assert char in valid_characters

def test_password_length():
    """ Test that length of the generated password is equal to the specified value """
    length = random.randint(10, 100)
    password = generate_password(length=length)
    assert len(password) == length