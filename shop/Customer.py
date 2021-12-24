class Customer:
    count_id = 0

    def __init__(self, firstName, lastName, email, city, address, password):
        Customer.count_id +=1
        self.__customerID = Customer.count_id
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__city = city
        self.__address = address
        self.__password = password

    def get_customerID(self):
        return self.__customerID
    def get_firstName(self):
        return self.__firstName
    def get_lastName(self):
        return self.__lastName
    def get_email(self):
        return self.__email
    def get_city(self):
        return self.__city
    def get_address(self):
        return self.__address
    def get_password(self):
        return self.__password

    def set_customerID(self,customerID):
        self.__customerID = customerID
    def set_firstName(self,firstName):
        self.__firstName = firstName
    def set_lastName(self,lastName):
        self.__lastName = lastName
    def set_email(self,email):
        self.__email = email
    def set_city(self,city):
        self.__city = city
    def set_address(self,address):
        self.__address = address
    def set_password(self,password):
        self.__password = password
