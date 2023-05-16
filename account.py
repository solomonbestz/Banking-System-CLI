
from user import User

class Account(User):

    user_id = 1
    data_base = {
    
    }

    def __init__(self, first_name: str, last_name: str, email: str, age: int, gender: str, password: str, confirm_pass: str, phone_num: str, balance: float = 0) -> None:
        super().__init__(first_name, last_name, email, age, gender, password, confirm_pass, phone_num)

        self.balance = balance

    def generate_account_number(self):
        pass

    def create_account(self):
        Account.data_base[Account.user_id] = {'name': self.first_name + " "+self.last_name, 'email': self.validate_email(),
                                            'gender': self.validate_gender(), 'password': self.validate_password(), 'account-number': None }
        Account.user_id += 1


    def check_balance(self):
        print(self.balance)

    def deposit(self, amount: float):
        self.balance += amount

    def withdrawal(self, amount: float):
        if amount > self.balance:
            print("Thief!!!!!!, How much you get for account")
        else:
            self.balance -= amount

    
    