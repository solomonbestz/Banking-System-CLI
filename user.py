import string


class BestzError(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self) -> str:
        return self.message


class User:
    def __init__(self, first_name: str, last_name: str, email: str,
                 age: int, gender: str, password: str, confirm_pass: str,
                 phone_num: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.gender = gender
        self.password = password
        self.confirm_pass = confirm_pass
        self.phone_num = phone_num


    def validate_password(self):
        if self.password == self.confirm_pass:
            return self.password
        else:
            raise BestzError("Wrong Password")
    
    def validate_email(self):
        if "@gmail.com" in self.email:
            return self.email
        else:
            raise BestzError("Wrong Gmail")
    
    def validate_phone(self):
        if (len(self.phone_num) == 11) and (string.ascii_letters not in self.phone_num):
            return self.phone_num 
        else:
            raise BestzError("Wrong Phone number")
    
    def validate_gender(self):
        if (len(self.gender) == 1) and ((self.gender.lower() == 'm') or (self.gender.lower() == "f")):
            return self.gender
        else:
            raise BestzError("Wrong Gender, You can't be devil sent")
