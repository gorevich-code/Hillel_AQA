from Hillel_AQA_homeworks.hw_26_sql.models.customer_model import CustomersModel
from Hillel_AQA_homeworks.hw_26_sql.models.orders_model import OrdersModel
from Hillel_AQA_homeworks.hw_26_sql.session import session


class CustomersRepository:
    def __init__(self):
        self.__session = session
        self.__model = CustomersModel
        self.customer: CustomersModel

    def get_all(self):
        return self.__session.query(self.__model).all()

    def print_all(self):
        print(self.get_all())

    def get_by_id(self, customer_id: int, return_dict: bool = True):
        customer: CustomersModel | None = self.__session.get(self.__model, {'CustomerID': customer_id})
        if return_dict:
            cstmr = {
                'Customer_id':  customer.CustomerID,
                'Name':  customer.Name,
                'SecondName':  customer.SecondName,
                'Phone':  customer.Phone,
                'Address':  customer.Address,
                'Orders':  customer.Orders.filter(OrdersModel.CustomerID == customer.CustomerID).all()
                }
            return cstmr
        return customer

    def create_new(self, name: str, second_name: str, phone: str, address: str) -> bool:
        new_customer = CustomersModel()
        new_customer.CustomerID = None
        new_customer.Name = name
        new_customer.SecondName = second_name
        new_customer.Phone = phone
        new_customer.Address = address
        try:

            self.__session.add(new_customer)
            return True

        except:
            return False

    def delete(self, customer_id: int) -> bool:
        try:
            customer = self.get_by_id(customer_id)
            self.__session.delete(customer)
            return True

        except:
            return False

    def __repr__(self: CustomersModel):
        return {
            'Customer_id': self.CustomerID,
            'Name': self.Name,
            'SecondName': self.SecondName,
            'Phone': self.Phone,
            'Address': self.Address,
            'Orders': self.Orders
        }


def __init__():
    cr = CustomersRepository()

    second = cr.get_by_id(2)
    print(second)


if __name__ == '__main__':
    __init__()
