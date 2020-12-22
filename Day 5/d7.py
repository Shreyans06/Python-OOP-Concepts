class OverdrawException(Exception):
    pass


class LimitReachedException(Exception):
    pass


class Account:
    def __init__(self, account_type, balance, min_balance):
        self.__account_type = account_type
        self.__balance = balance
        self.__min_balance = min_balance

    def get_account_type(self):
        return self.__account_type

    def get_balance(self):
        return self.__balance

    def get_min_balance(self):
        return self.__min_balance

    def set_balance(self, balance):
        self.__balance = balance


class Customer:
    def __init__(self, customer_id, customer_name, age, account):
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__age = age
        self.__account = account

    def get_customer_id(self):
        return self.__customer_id

    def get_customer_name(self):
        return self.__customer_name

    def get_age(self):
        return self.__age

    def get_account(self):
        return self.__account

    def take_card(self):
        print("Take card out from the ATM")

    def withdraw(self, amount):
        if amount > self.__account.get_balance():
            self.take_card()
            raise OverdrawException("OverdrawException")
        elif self.__account.get_balance() - amount < self.__account.get_min_balance():
            self.take_card()
            raise LimitReachedException("LimitReachedException")
        else:
            self.__account.set_balance(self.__account.get_balance()-amount)


class PrivilegedCustomer(Customer):
    def __init__(self, customer_id, customer_name, age, account, bonus_points):
        super(PrivilegedCustomer, self).__init__(customer_id, customer_name, age, account)
        self.__bonus_points = bonus_points

    def get_bonus_points(self):
        return self.__bonus_points

    def __increase_bonus(self):
        if self.get_account().get_balance() > 1000:
            self.__bonus_points += 10
        else:
            self.__bonus_points += 2

    def withdraw(self, amount):
        super(PrivilegedCustomer, self).withdraw(amount)
        self.__increase_bonus()


account = Account("Savings", 1000, 500)
priv_customer = PrivilegedCustomer(100, "Gopal", 43, account, 100)
try:
    priv_customer.withdraw(200)
    print(priv_customer.get_bonus_points())
    print(priv_customer.get_account().get_balance())
except OverdrawException as e:
    print(e)
except LimitReachedException as e:
    print(e)

