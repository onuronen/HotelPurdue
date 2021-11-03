import pandas as pd
import datetime as dt
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.db.crud import (
    update_table,
    fetch_rows,
    fetch_customer_by_card_number
)

from src.db.models import Credit_Card_Info

def insert_credit_card_information(full_name, card_number, exp_date, cvv):
    
    if not full_name or not card_number or not exp_date or not cvv:
        return False

    # check for duplicates - id number has to be unique
    card_df = fetch_customer_by_card_number(card_number)
    if not card_df.empty:
        return False

    data = {
        "full_name": [full_name],
        "card_number": card_number,
        "exp_date": [exp_date],
        "cvv_num": cvv
    }

    new_df = pd.DataFrame(data)
    update_table(new_df, Credit_Card_Info)
    return True

