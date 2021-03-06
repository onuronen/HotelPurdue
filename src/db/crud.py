import logging
import pandas as pd
from sqlalchemy import func, create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.db.models import Base, Credit_Card_Info, Bill, Customer, Reservation, Employee, Room_Information
from src.app.config import postgres_config

logger = logging.getLogger(__name__)
conn_str = f"postgresql://{postgres_config['user']}:{postgres_config['password']}@{postgres_config['host']}/{postgres_config['database']}"
engine = create_engine(conn_str)
Session = sessionmaker(bind=engine)

def create_tables():
    logger.info("Creating the database if it does not already exist")
    Base.metadata.create_all(bind=engine)


def fetch_rows(BaseClass):
    """
    :param BaseClass: Base child-class object from /src/db/models.py
    :returns: pandas.DataFrame
    """
    session = Session()

    try:
        result = session.query(BaseClass)

    finally:
        session.close()

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None


def update_table(new_df, BaseClass):
    """"
    :param new_df: pandas.DataFrame containing rows to be loaded into Postgres
    :param BaseClass: Base child-class (sqlalchemy model)
    """""

    session = Session()
    session.bulk_insert_mappings(
        BaseClass,
        new_df.to_dict(orient="records"))
    session.commit()
    session.close()


def fetch_customer_by_id(id_number):
    session = Session()

    try:
        result = session.query(Customer).filter(Customer.id_number == id_number)

    finally:
        session.close()

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None


def fetch_customer_by_card_number(card_number):
    session = Session()

    try:
        result = session.query(Credit_Card_Info).filter(Credit_Card_Info.card_number == card_number)

    finally:
        session.close()

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None


def fetch_customer_by_room_number(room_number):
    session = Session()

    try:
        result = session.query(Room_Information).filter(Room_Information.room_number == room_number)

    finally:
        session.close()

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None

def fetch_customer_by_email(email):
    session = Session()

    try:
        result = session.query(Customer).filter(Customer.cust_email == email)

    finally:
        session.close()

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None


def fetch_card_by_full_name(full_name):
    session = Session()

    try:
        result = session.query(Credit_Card_Info).filter(Credit_Card_Info.full_name == full_name)

    finally:
        session.close()

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None

def fetch_reservation_by_start_date(start_date):
    session = Session()

    try:
        result = session.query(Reservation).filter(Reservation.start_date == start_date)

    finally:
        session.close()

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None


def fetch_customer_by_name(first_name, last_name):
    session = Session()

    try:
        result = session.query(Customer).filter(Customer.cust_fname == first_name).filter(Customer.cust_lname == last_name)

    finally:
        session.close()

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None


def fetch_reservation_by_fullname(full_name):
    session = Session()

    try:
        result = session.query(Reservation).filter(Reservation.full_name == full_name)

    finally:
        session.close()

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None




from sqlalchemy import asc
def rooms_by_ascending():
    session = Session()

    try:
        result = session.query(Room_Information).order_by(asc(Room_Information.room_number))
    finally:
        session.close()

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None


from sqlalchemy import desc
def reservation_by_desc():
    session = Session()

    try:
        result = session.query(Reservation).order_by(desc(Reservation.guest_number))
    finally:
        session.close()

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None

from sqlalchemy import func
def count_all_customers():
    session = Session()

    try:
        result = session.query(func.count(Customer.customer_id))
    finally:
        session.close()

    print(result)

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None

from sqlalchemy import func
def count_customerids_groupby_country():
    session = Session()

    try:
        result = session.query(Customer.cust_country, func.count(Customer.customer_id)).group_by(Customer.cust_country)
    finally:
        session.close()

    print(result)

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None


from sqlalchemy import func
def subquery_get_suite_rooms():
    session = Session()

    try:
        subquery = session.query(Room_Information.room_number).filter(Room_Information.room_type == "suite").subquery()
        result = session.query(Room_Information).filter(Room_Information.room_number.in_(subquery))
    finally:
        session.close()

    print(result)

    if result is not None:
        df = pd.read_sql(result.statement, result.session.bind)
        return df

    else:
        return None



def delete_by_fullname(BaseClass, full_name):
    session = Session()
    session.query(BaseClass).filter(BaseClass.full_name == full_name).delete()
    session.commit()
    session.close()

def delete_by_name_customer(first_name, last_name):
    session = Session()
    session.query(Customer).filter(Customer.cust_fname == first_name).filter(Customer.cust_lname == last_name).delete()
    session.commit()
    session.close()

#print(tryout5())


#create_tables()

if __name__ == '__main__':
    pass