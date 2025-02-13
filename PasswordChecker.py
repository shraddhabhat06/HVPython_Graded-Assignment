
import re

def password_checker(pwd):
    """
    Checks the strength of a given password based on the following criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character (!@#$%^&*(),.?)

    Args:
        pwd (str): The password to check.

    Returns:
        tuple: (bool, str) - A boolean indicating whether the password is strong,
               and a message providing feedback on the password strength.
    """
    error = []
    
    if len(pwd) < 8:
        error.append("pass must be at least 8 characters long.")
    if not re.search(r"[A-Z]", pwd):
        error.append("Password must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", pwd):
        error.append("Password must contain at least one lowercase letter.")
    if not re.search(r"\d", pwd):
        error.append("Password must contain at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?", pwd):
        error.append("Password must contain at least one special character.")

    
    if error:
        # If there are any errors, return False along with the error messages
        return False, "\n".join(error)
    # If all conditions are met, return True with a success message
    return True, "Strong password."

# Taking input from user
pwd = input("Enter your password: ")
is_strong, message = password_checker(pwd)
print(message)
