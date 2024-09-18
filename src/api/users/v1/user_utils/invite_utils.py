import random


def create_invite_code():
    invite_code = random.randint(1000, 9999)
    return invite_code


def validate_invite_code(code):
    str_code = str(code)
    if not str_code.isdigit() or len(str_code) != 4:
        return False
    return True
