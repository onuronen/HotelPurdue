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

from src.db.models import Employee

def insert_employee_information(emp_fullname):
    if not emp_fullname:
        return False

    data = {
        "emp_fullname": [emp_fullname]
    }

    new_df = pd.DataFrame(data)
    update_table(new_df, Employee)
    return True
