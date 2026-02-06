import string
from password.new_password import generate_password


def test_password_characters():
    """Тест, что при генерации используются только допустимые символы"""
    valid_characters = string.ascii_letters + string.digits + string.punctuation
    password = generate_password(100)  # длинный пароль для надёжной проверки

    for char in password:
        assert char in valid_characters


def test_password_length():
    """Тест, что длина пароля соответствует заданной"""
    length = 20
    password = generate_password(length)

    assert len(password) == length


def test_passwords_are_different():
    """Тест, что два сгенерированных подряд пароля различаются"""
    password1 = generate_password(16)
    password2 = generate_password(16)

    assert password1 != password2
