import secrets
import string


def generate_random_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    print(alphabet)
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password


random_password = generate_random_password(16)
print(random_password)
