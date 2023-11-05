def to_lowercase_decorator(func):
    def wrapper():
        user_input = input("Введите текст: ")
        lower_case_input = user_input.lower()
        func(lower_case_input)
    return wrapper

# Пример использования декоратора
@to_lowercase_decorator
def process_input(user_input):
    print("Ваш текст в нижнем регистре:", user_input)

process_input()