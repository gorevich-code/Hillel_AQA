from sqlalchemy import Column, INTEGER, TEXT
from sqlalchemy.orm import relationship
from .models_base import Base


class CustomersModel(Base):
    __tablename__ = 'Customers'
    Name = Column(TEXT(100))
    SecondName = Column(TEXT(100))
    Phone = Column(TEXT(100))
    Address = Column(TEXT(100))
    CustomerID = Column(INTEGER, primary_key=True)
    Orders = relationship("OrdersModel", back_populates="order", lazy='dynamic')
