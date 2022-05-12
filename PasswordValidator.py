import re
import string

def validate(password, args=None, lower=1, upper=float('inf')):
    """ 
    validate function determines if given password is valid based on passed parameters.
    password: The password user wishes to validate.
    args: List of regular expressions to test against the password.
    lower: Minimum length required for password. Set to 1 by default.
    Upper: Maximum length required for password. Set to infinity by default
    Return: Tuple containing
        Bool valid stating if password is valid by given parameters.
        String message that states why password is invalid. If password is valid, will return 'Password is acceptable'
        List of indexes of failed regular expressions.
    """
    
    valid = True
    message = "Password is acceptable"
    failed = []

    if(args==None):
        args = []

    if(lower <= 0):
        return False, "Lower limit cannot be less than 1", failed
    if(upper < lower):
        return False, "Invalid upper bound", failed

    for i, regex in enumerate(args):
        pattern = re.compile(regex)
        match = pattern.search(password)
        if(match is None):
            failed.append(i)
            valid = False
            message = "Failed regex test"

    if(len(password) < lower):
        valid = False
        message = "Password too short"

    if(len(password) > upper):
        valid = False
        message = "Password too long"

    return valid, message, failed

def validate_wrapper() -> None:
    special = string.punctuation
    args = ['\d+', '[A-Z]', f'[{special}]']
    failmessage = {
                0: "Password does not contain number",
                1: "Password does not contain uppercase letter",
                2: f"Password does not contain special characters: {special}"}
    lower = 8
    upper = 16
    password = input("Input potential password: ")

    result = validate(password, args, lower, upper)

    valid = result[0]
    message = result[1]
    failed = result[2]

    if(valid):
        print(message)
        return

    print(message)
    for idx in failed:
        print(failmessage.get(idx))
        print()

def run() -> None:
    
    print()
    while(True):
        print("===========")
        print("1: Validate")
        print("2: end")
        val = input("Select option: ")
        if(val == '2'):
            print("Ending Execution")
            print("================")
            break;
        if(val == '1'):
            print(  "===============")
            print()
            validate_wrapper()
            continue
        print("Invalid Input")

def main():
    print("Welcome to Password Validation Program!!")
    run()
    
    

if __name__ == "__main__":
    main()