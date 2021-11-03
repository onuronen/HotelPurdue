from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime as dt
from sqlalchemy import(
    Table,
    Column,
    Boolean,
    String,
    Integer,
    Float,
    DateTime,
    JSON,
    ARRAY,
    ForeignKey,
    Date,
    TIMESTAMP
)

Base = declarative_base()

class Credit_Card_Info(Base):
    __tablename__ = "credit_card_information"
    card_id = Column (Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable = False)
    card_number = Column(Integer, nullable=False)
    exp_date = Column(String, nullable=False)
    cvv_num = Column(Integer, nullable=False)
    #Children = relationship("Bill")

class Bill(Base):
    __tablename__ = "bill"
    bill_id = Column(Integer, primary_key=True, autoincrement=True)
    #customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    #reservation_id = Column(Integer, ForeignKey('reservation.reservation_id'))
    bill_date = Column(Date, nullable=False)
    room_charge = Column(Integer, nullable=False)
    bar_charge = Column(Integer, nullable=True)
    misc_charge = Column(Integer, nullable=True)
    payment_date = Column(Date, nullable=True)
    #card_id = Column(Integer, ForeignKey('credit_card_information.card_id'))
    notes = Column(String, nullable = True)




class Customer(Base):
    __tablename__ = "customer"
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    cust_fname = Column(String, nullable=False)
    cust_lname = Column(String, nullable=False)
    cust_number = Column(String, nullable=False)
    cust_email = Column(String, nullable=False)
    cust_street = Column(String, nullable=False)
    cust_state = Column(String, nullable=False)
    cust_country = Column(String, nullable=False)
    id_number = Column(Integer, nullable=False)
    doc_type = Column(String, nullable=False)
    notes = Column(String, nullable=True)
    #Children = relationship("Reservation", "Bill")


class Reservation(Base):
    __tablename__ = "reservation"
    reservation_id = Column (Integer, primary_key=True, autoincrement=True)
    #room_id = Column(Integer, ForeignKey('room_information.room_id'))
    #customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    reservation_date = Column(TIMESTAMP, nullable=False)
    guest_number = Column(Integer, nullable=False)
    #employee_id = Column(Integer, ForeignKey('employee.employee_id'))
    notes = Column(String, nullable=True)
    #Children = relationship("Bill")


class Employee(Base):
    __tablename__ = "employee"
    employee_id = Column (Integer, primary_key=True, autoincrement=True)
    emp_fullname = Column(String, nullable=False)
    #Children = relationship("Reservation")


class Room_Information(Base):
    __tablename__ = "room_information"
    room_id = Column (Integer, primary_key=True, autoincrement=True)
    #room_type = Column(String, ForeignKey('room_type.type_room'))
    room_number = Column(Integer, nullable=False)
    #Children = relationship("Reservation")

class Room_Type(Base):
    __tablename__ = "room_type"
    type_room = Column(String, primary_key=True, nullable=False)
    price = Column(Integer, nullable=False)
    max_occupancy = Column(Integer, nullable =False)
    #Children = relationship("Room_Information")






