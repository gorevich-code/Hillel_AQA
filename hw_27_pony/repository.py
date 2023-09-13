from pony.orm import db_session, select
from models import Customers, Orders


class CustomersRepo:
    def __init__(self):
        self.model = Customers

    def _process_data(self, data):
        if not hasattr(data, 'Name'):
            return None
        orders = f'No Orders from {data.Name} {data.SecondName}'
        if data.Orders:
            orders = [x.to_dict() for x in data.Orders]

        self.Customers.ObjectModel(
            name=data.Name,
            secondname=data.SecondName,
            phone=data.Phone,
            address=data.Address,
            customerid=data.CustomerID,
            orders=orders
        )
        return self

    @db_session
    def get_all(self):
        query = select(customer for customer in Customers).order_by("customer.CustomerID")
        data = (self._process_data(cstmr) for cstmr in query[:])
        return list(data)

    @db_session
    def get_by_any_filed(self, field_name, field_value):
        query = select(customer for customer in Customers if getattr(customer, field_name) == field_value)
        data = query.get()
        return self._process_data(data)

    @db_session
    def update_field_by_id(self, id, field_to_change, new_value):
        customer = self.get_by_any_filed(field_name='CustomerID', field_value=id)

        if hasattr(customer, field_to_change):
            setattr(customer, field_to_change, new_value)

        else:
            print('Specified field is not exists !')

    @db_session
    def delete_by_id(self, id):
        customer = self.get_by_any_filed(field_name='CustomerID', field_value=id)
        customer.delete()






cr = CustomersRepo()
second = cr.get_by_any_filed(field_name='CustomerID', field_value=2)
print(second.ObjectModel)
all = cr.get_all()
print(all)

cr.update_field_by_id(id=5, field_to_change='SecondName', new_value='Di Caprioooo')
#cr.delete_by_id(7)