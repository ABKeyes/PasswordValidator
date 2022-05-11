import re


# Password Validator Function
# Allows user to pass a password string and a list of requirements that the password must adhere to.
# The method will then test each requirement and return True if all requirements are met
def validate(password, args=None, lower=1, upper=float('inf')):
    
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
    args = ['\d+', '[A-Z]', '[?!@#$%^&*]']
    failmessage = {
                0: "Password does not contain number",
                1: "Password does not contain uppercase letter",
                2: "Password does not contain special characters: ?!@#$%^&*"}
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