def checkPasswordStrength(password):

    length = len(password) >= 8
    uppercasePresent= any(c.isupper() for c in password)
    lowercasePresent = any(c.islower() for c in password)
    digitPresent = any(c.isdigit() for c in password)
    specialCharPresent = any(c in "!@#$%^&*()_-" for c in password)

    if length and uppercasePresent and lowercasePresent and digitPresent and specialCharPresent:
        return "Strong"
    elif length and (uppercasePresent or lowercasePresent) and digitPresent:
        return "Moderate"
    else:
        return "Weak"

if __name__ == '__main__':
    while True:
        password = input("Enter a password to assess its strength (press Q to exit): ")
        
        if password == 'Q':
            print("Exiting the program .....")
            break
        
        strength = checkPasswordStrength(password)
        print(f"Your password strength is: {strength}")
        
