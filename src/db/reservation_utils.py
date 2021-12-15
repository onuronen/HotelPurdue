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
    fetch_reservation_by_start_date,
    fetch_reservation_by_fullname
)

from src.db.models import Reservation

def insert_reservation_information(full_name, start_date, end_date, reservation_date, guest_number, notes):
    
    if not start_date or not end_date or not reservation_date or not guest_number:
        return False

    data = {
        "full_name": [full_name],
        "start_date": [start_date],
        "end_date": [end_date],
        "reservation_date": reservation_date,
        "guest_number": guest_number,
        "notes": [notes],

    }

    new_df = pd.DataFrame(data)
    update_table(new_df, Reservation)
    return True


def fetch_reservation_information(start_date):
    if not start_date:
        return False

    reservation_df = fetch_reservation_by_start_date(start_date).to_dict("records")
    return reservation_df


def fetch_reservation_information_by_name(full_name):
    if not full_name:
        return False

    reservation_df = fetch_reservation_by_fullname(full_name).to_dict("records")
    return reservation_df