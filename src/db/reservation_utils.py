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
)

from src.db.models import Reservation

def insert_reservation_information(start_date, end_date, reservation_date, guest_number, notes):
    
    if not start_date or not end_date or not reservation_date or not guest_number:
        return False

    data = {
        "start_date": [start_date],
        "end_date": [end_date],
        "reservation_date": reservation_date,
        "guest_number": guest_number,
        "notes": [notes],

    }

    new_df = pd.DataFrame(data)
    update_table(new_df, Reservation)
    return True