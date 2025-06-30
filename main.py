# -*- coding: utf-8 -*-
"""
Updated to handle Excel files and proper date formatting
"""

import streamlit as st
import pandas as pd
from io import BytesIO
import sys
import os

# Add the directory containing cleaning.py to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from cleaning import data_cleaning
except ImportError as e:
    st.error(f"Import Error: {str(e)}")
    st.stop()

st.title("CABIN EXCEEDANCE REPORT")

upload_file = st.file_uploader("Choose a file to Upload", type=["xlsx", "xls"])

if upload_file is not None:
    try:
        clean_data, merged_data = data_cleaning(upload_file)
        
        st.write("Clean_data_1")
        st.dataframe(clean_data.head())
        
        st.write("Merged_data")
        st.dataframe(merged_data.head())
        
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            clean_data.to_excel(writer, sheet_name='Clean_Data', index=False)
            merged_data.to_excel(writer, sheet_name='Merged_Data', index=False)
        
        st.download_button(
            label='Download Clean File as Excel',
            data=output.getvalue(),
            file_name='Crew_Exceedance_Report.xlsx',
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
        
    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
