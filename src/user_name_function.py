# user_name_functions.py
def get_user_name_from_input():
    """ Not empty string. No spaces. """
    user_name = input("Write down your user name here: ")

    if not user_name or " " in user_name:
        print('User name is not valid.')
    else:
        return user_name
