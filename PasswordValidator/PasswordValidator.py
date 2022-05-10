def validate(password, args=[], lower=1, upper=float('inf')):
    
    if(not(all(regex.match(password) for regex in args))):
        return False

    if(lower <= 0):
        return False, "Lower limit cannot be less than 1"

    if(upper < lower):
        return False, "Invalid Upper Bound"

    if(len(password) < lower):
        return False

    if(len(password) > upper):
        return False

    return True, "Password is acceptable"

def main():
    print("Welcome to Password Validation Program!!")
    

if __name__ == "__main__":
    main()