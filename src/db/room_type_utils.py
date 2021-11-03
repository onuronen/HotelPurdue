import pandas as pd
import datetime as dt
import os
import sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from src.db.crud import (
    update_table,
    fetch_rows
)

from src.db.models import Room_Type


def insert_room_type(room_type, price, max_occupancy):
    
    if not price or not max_occupancy:
        return False

    data = {
        "type_room": room_type,
        "price": [price],
        "max_occupancy": [max_occupancy]
    }

    new_df = pd.DataFrame(data)
    update_table(new_df, Room_Type)
    return True