import random

password_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input("Введите желаемую длину пароля: "))

generated_password = ''.join(random.choice(password_characters) for _ in range(password_length))

print("Сгенерированный пароль:", generated_password)
