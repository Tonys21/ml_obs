# user_password_function.py
def get_password_from_input():
    """ Password needs to be at least 8 characters long with at least one number, one special character and one letter. """
    password = input("Write down your password here: ")
    special_characters = '"!@#$%^&*()-+?_=,<>/'
    numbers = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"

    if (len(password) > 7 and any(c in special_characters for c in password) and any(
            c in numbers for c in password) and any(c in letters for c in password)):
        return password
    else:
        print('password is not valid.')

