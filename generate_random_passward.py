import random
import string

def generate_random_passward(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    passward = ''.join(random.choice(characters) for _ in range(length))
    return passward
passward_length = 12
random_number = generate_random_passward(passward_length)
print(random_number)