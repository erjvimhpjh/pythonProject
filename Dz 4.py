import random

class NumberEncryptor:
    def __init__(self):
        self.hidden_number = None

    def encrypt(self, number):
        self.hidden_number = number
        # Виконуємо випадкову математичну операцію над числом
        # Наприклад, додавання випадкового числа від -10 до 10
        random_number = random.randint(-10, 10)
        encrypted_number = self.hidden_number + random_number
        return encrypted_number

    def decrypt(self):
        # Повертаємо зашифроване число
        return self.hidden_number

# Приклад використання
encryptor = NumberEncryptor()
number = 45
encrypted_number = encryptor.encrypt(number)
print("Зашифроване число:", encrypted_number)
decrypted_number = encryptor.decrypt()
print("Розшифроване число:", decrypted_number)
