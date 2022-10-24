import random

""" simple password generator, takes first name, last name and length. It generates password """


def simple_generator(first_name: str, last_name: str, length: int):
    password_base = (list(first_name + last_name + "!@#$%^&*()" + "1234567890"))
    random.shuffle(password_base)
    password = []
    for i in range(length):
        password.append(random.choice(password_base))

    random.shuffle(password)

    return f"password : {''.join(password)}"


print(simple_generator(first_name='Levan', last_name='Gogaladze', length=20))



