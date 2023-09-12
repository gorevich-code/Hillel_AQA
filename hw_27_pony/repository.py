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
        self.model.orders = [x.to_dict() for x in data.Orders]

        return dict(self.model)



cr = CustomersRepo()
second = cr.get_by_id(2)
print(second)

