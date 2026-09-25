# 🔐 Password Generator

Простой и удобный генератор случайных паролей на Python!

## 📋 Описание

Это приложение генерирует безопасные случайные пароли заданной длины, используя комбинацию букв, цифр и специальных символов.

## ✨ Возможности

- 🎲 Генерация полностью случайных паролей
- 📏 Настраиваемая длина пароля
- 🔤 Использование букв (прописные и строчные)
- 🔢 Использование цифр
- 🔣 Использование специальных символов
- ⚡ Быстрая работа
- 💻 Кроссплатформенность

## 🚀 Использование

### Установка

Просто скопируйте файл `generate_password.py` в ваш проект.

### Быстрый старт

```python
import random
import string

def generate_password(length=12):
    """Генерация случайного пароля заданной длины."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(characters)
    return password

# Пример использования
password_length = 12
print("Ваш новый пароль:", generate_password(password_length))
#no