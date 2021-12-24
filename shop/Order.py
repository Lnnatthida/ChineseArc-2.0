class Order:
    count_id = 0

    def __init__(self, name, total, status,date):
        Order.count_id += 1
        self.__order_id = Order.count_id
        self.__name = name
        self.__total = total
        self.__status = status
        self.__date = date
        
    def get_order_id(self):
        return self.__order_id

    def get_name(self):
        return self.__name

    def get_total(self):
        return self.__total

    def get_status(self):
        return self.__status

    def get_date(self):
        return self.__date

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def set_name(self, name):
        self.__name = name

    def set_total(self, total):
        self.__total = total

    def set_status(self,status):
        self.__status = status

    def set_date(self,date):
        self.__date = date

