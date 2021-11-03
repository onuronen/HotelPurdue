import pandas as pd
import datetime as dt
import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from src.db.crud import (
    update_table,
    fetch_rows,
    fetch_customer_by_id
)

from src.db.models import Customer

def insert_customer_information(first_name, last_name,number, email, street, state, country, id_number, doc_type, notes):

    if not first_name or not last_name or not number or not email or not street or not state or not country or not doc_type:
        return False

    
    # check for duplicates - id number has to be unique
    id_df = fetch_customer_by_id(id_number)
    if not id_df.empty:
        return False
    

    data = {
        "cust_fname": [first_name],
        "cust_lname": [last_name],
        "cust_number": [number],
        "cust_email": [email],
        "cust_street": [street],
        "cust_state": [state],
        "cust_country": [country],
        "id_number": id_number,
        "doc_type": [doc_type],
        "notes": [notes]
    }

    new_df = pd.DataFrame(data)
    update_table(new_df, Customer)
    return True
    



    
    



