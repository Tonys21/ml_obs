# user_functions.py
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Write down your email: ")

    if "@" not in email or "." not in email:
        print('Email is not valid.')
    else:
        return email


if __name__ == '__main__':
    get_email_from_input
