
def user_validator(username):
    """     User validator name

        This validator only checks that the length of the 
        username is at least 6 characters

    Args:
        username (str): string with the name to verify

    Returns:
        boolean: return if the verification has passed
    """
    if len(username)>=6:
        return True
    else:
        return False

def password_validator(password):
    """     Password velidator

        Use lower, upper, and digits as auxiliary variables 
        to determine password requirements
        Al least one lower case, one upper case, one digit
        and at least 8 characters

    Args:
        password (str): String with the password to verify

    Returns:
        boolean: Return if the verification has passed
    """
    lower, upper, digit = 0, 0, 0
    if len(password) >=8 :
        for char in password:
            if char.islower():
                lower += 1
            if char.isupper():
                upper += 1
            if char.isdigit():
                digit += 1
    if lower >= 1 and upper >= 1 and digit >= 1 :
        return True
    else:
        return False

