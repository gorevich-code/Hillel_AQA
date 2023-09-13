from pony.orm import Database, PrimaryKey, Optional, Required, Set, set_sql_debug

db = Database()
db.bind(provider='postgres', user='postgres', host='127.0.0.1', database='HillelDB', password='postgres')


class Customers(db.Entity):
    _table_ = 'Customers'
    Name = Required(str, column='Name')
    SecondName = Required(str, column='SecondName')
    Phone = Required(str, column='Phone')
    Address = Required(str, column='Address')
    CustomerID = PrimaryKey(int, auto=True, column='CustomerID')
    Orders = Set("Orders")

    class CustomerData:
        def __init__(self, Name, SecondName, Phone, Address, CustomerID, orders):
            self.name=Name
            self.secondname=SecondName,
            self.phone=Phone,
            self.address=Address,
            self.customerid=CustomerID,
            self.orders=orders

        def __repr__(self):
            print(
                f'\n\nName : {self.name} '
                f'\nSecond Name : {self.secondname} '
                f'\nPhone : {self.phone} '
                f'\nAddress : {self.address} '
                f'\nCustomerID : {self.customerid} '
                f'\nOrders : {self.orders}\n\n'
            )







class Orders(db.Entity):
    _table_ = "Orders"
    OrderID = PrimaryKey(int, auto=True, column='OrderID')
    Goods = Required(str, column='Goods')
    CustomerID = Required("Customers", column='CustomerID')


db.generate_mapping(check_tables=True)
set_sql_debug(True)