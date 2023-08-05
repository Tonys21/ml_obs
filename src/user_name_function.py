# user_name_functions.py
def get_user_name_from_input():
    """ Not empty string. No spaces. """
    user_name = input("Write down your user name here: ")

    if user_name == "" or " " not in user_name:
        return user_name
    else:
        print('User name is not valid.')
