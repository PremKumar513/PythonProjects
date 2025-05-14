#Password Checker
#conditions for strong password 
#(password must be minimum 8 character and maximum 12 characters, must contain lower char, 
# must contain upper char, must contain numeric values, must contain special characters)

import re

def check_password_strenght(password):
    if len(password) < 8:
        return "Weak: Password must be between 8 and 12 characters long."
    if len(password) > 12:
        return "Weak: Password must be 12 max characters long."
    if not any(char.isdigit() for char in password):
        return("weak: Password must contain Numberic Value")
    if not any(char.islower() for char in password):
        return("weak: Password must contain lower char")
    if not any(char.isupper() for char in password):
        return("weak: Password must contain Upper char")
    if not re.search(r'[!@#$%^&*()]' , password):
        return("weak: Password must contain special Character")
    return "YOU have Strong password"
def password_checker():
    print("Welcome to Password Checker System")

    while True:
        password=input("\n Enter your password (or type 'exit' for quit:)")
        if password=="exit":
            print("Thank you Coming hope your day is Good")
        result=check_password_strenght(password)
        print(result)

#to run the password_checker
if __name__=="__main__":
    password_checker()