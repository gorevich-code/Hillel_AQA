from sqlalchemy import Column, INTEGER, ForeignKey, TEXT
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class OrdersModel(Base):
    __tablename__ = "Orders"
    OrderID = Column(INTEGER, primary_key=True)
    Goods = Column(TEXT(100))
    CustomerID = Column(INTEGER, ForeignKey("Customers.CustomerID"), nullable=False)
    order = relationship('CustomersModel', back_populates='Orders')

    def __repr__(self):
        result = {
            'OrderID': self.OrderID,
            'CustomerID': self.CustomerID,
            'Goods': self.Goods,
            'Customer': self.Customer}

        return result


class CustomersModel(Base):
    __tablename__ = 'Customers'
    Name = Column(TEXT(100))
    SecondName = Column(TEXT(100))
    Phone = Column(TEXT(100))
    Address = Column(TEXT(100))
    CustomerID = Column(INTEGER, primary_key=True)
    Orders = relationship("OrdersModel", back_populates="order", lazy='dynamic')


    def __repr__(self):
        print(self.Orders)
        result = {
            'Customer_id': self.CustomerID,
            'Name': self.Name,
            'SecondName': self.SecondName,
            'Phone': self.Phone,
            'Address': self.Address,
            'Orders': self.Orders
        }

        return result.__str__()






