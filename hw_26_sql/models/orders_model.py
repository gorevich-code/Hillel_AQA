from sqlalchemy import Column, INTEGER, ForeignKey, TEXT
from sqlalchemy.orm import relationship
from .models_base import Base


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
            'Goods': self.Goods}

        return result.__str__()