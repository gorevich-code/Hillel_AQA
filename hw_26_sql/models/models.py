from sqlalchemy import Column, INTEGER, ForeignKey, TEXT
from sqlalchemy.orm import declarative_base, relationship, backref

Base = declarative_base()


class CustomersModel(Base):
    __tablename__ = 'Customers'
    CustomerID = Column(INTEGER, ForeignKey("Orders.OrderID"), primary_key=True)
    Name = Column(TEXT(100))
    SecondName = Column(TEXT(100))
    Phone = Column(TEXT(100))
    Address = Column(TEXT(100))
    Orders = relationship("OrdersModel", back_populates="Customer")

    def __repr__(self):
        print(self.Orders)
        """result = {
            'Customer_id': self.CustomerID,
            'Name': self.Name,
            'SecondName': self.SecondName,
            'Phone': self.Phone,
            'Address': self.Address,
            'Orders': self.Orders.__str__()
        }"""
        result = (f"'Customer_id': {self.CustomerID}\n"
                  f"'Name': {self.Name}\n"
                  f"'SecondName': {self.SecondName}\n"
                  f"'Phone': {self.Phone}\n"
                  f"'Address': {self.Address}\n"
                  f"'Orders': {self.Orders}\n")
        return result.__str__()


class OrdersModel(Base):
    __tablename__ = "Orders"
    OrderID = Column(INTEGER, primary_key=True)
    Goods = Column(TEXT(100))
    CustomerID = Column(INTEGER, ForeignKey("Customers.CustomerID"))
    Customer = relationship("CustomersModel", back_populates="Orders")

    def __repr__(self):
        """        result = {
            'OrderID': self.OrderID,
            'CustomerID': self.CustomerID,
            'Goods': self.Goods,
            'Customer': self.Customer}"""

        result = (f"'OrderID': {self.OrderID}\n"
                  f"'CustomerID': {self.CustomerID}\n"
                  f"'Goods': {self.Goods}\n"
                  f"'Customer': {self.Customer}\n")
        return result
