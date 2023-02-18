import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


st.write("Hello World")


employee_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Department': ['Sales', 'Marketing', 'Sales', 'Engineering', 'Marketing'],
    'Salary': [50000, 60000, 55000, 70000, 65000]
})

# Define AgGrid options
grid_options = {
    'enableSorting': True,
    'enableFilter': True,
    'enableColResize': True,
    'rowSelection': 'single',
    'rowMultiSelectWithClick': True
}

AgGrid(employee_data)