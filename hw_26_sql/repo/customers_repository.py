from Hillel_AQA_homeworks.hw_26_sql.models import CustomersModel
from Hillel_AQA_homeworks.hw_26_sql.session import session
import pprint

class CustomersRepository:
    def __init__(self):
        self.__session = session
        self.__model = CustomersModel

    def get_all(self):
        return self.__session.query(self.__model).all()

    def print_all(self):
        print(self.get_all())

    def get_by_id(self, customer_id: int) -> CustomersModel:
        customer: CustomersModel | None = self.__session.get(self.__model, {'CustomerID': customer_id})
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


def __init__():
    cr = CustomersRepository()

    second = cr.get_by_id(2)
    print(second)


if __name__ == '__main__':
    __init__()
