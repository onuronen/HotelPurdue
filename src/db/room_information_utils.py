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
    fetch_customer_by_room_number
)

from src.db.models import Room_Information

def insert_room_information(room_type, room_number):
    
    if not room_type or not room_number:
        return False

    # check for duplicates - room number has to be unique
    room_number_df = fetch_customer_by_room_number(room_number)
    if not room_number_df.empty:
        return False

    data = {
        "room_type": [room_type],
        "room_number": [room_number]
    }

    new_df = pd.DataFrame(data)
    update_table(new_df, Room_Information)
    return True