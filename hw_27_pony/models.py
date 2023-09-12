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

    class ObjectModel:
        def __init__(self, name, secondname, phone, address, customerid, orders):
            self.Name = name
            self.SecondName =
            self.Phone



class Orders(db.Entity):
    _table_ = "Orders"
    OrderID = PrimaryKey(int, auto=True, column='OrderID')
    Goods = Required(str, column='Goods')
    CustomerID = Required("Customers", column='CustomerID')


db.generate_mapping(check_tables=True)
set_sql_debug(True)