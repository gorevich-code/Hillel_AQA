from pony.orm import db_session, select
from models import Customers, Orders
import pickle




class CustomersRepo:
    def __init__(self):
        self.model = Customers

    @db_session
    def get_by_id(self, id):
        query = select(customer for customer in Customers if customer.CustomerID == id)
        data = query.get()
        orders = f'No Orders from {data.Name} {data.SecondName}'
        if data.Orders:
            orders = [x.to_dict() for x in data.Orders]

        return Customers.ObjectModel(
            name=data.Name,
            secondname=data.SecondName,
            phone = data.Phone,
            address = data.Address,
            customerid = data.CustomerID,
            orders = orders
        )



cr = CustomersRepo()
second = cr.get_by_id(4)
print(second)

