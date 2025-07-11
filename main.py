# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:32:15 2024

@author: SyedNajeebURehman
"""
import streamlit as st
from cleaning import data_cleaning
import pandas as pd
from io import BytesIO

st.title("CABIN EXCEEDANCE REPORT")

upload_file = st.file_uploader("Choose Excel file", type=["xlsx", "xls"])

if upload_file:
    try:
        clean_data, merged_data = data_cleaning(upload_file)
        
        st.write("Clean Data Preview")
        st.dataframe(clean_data.head())
        
        # Create download button
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            clean_data.to_excel(writer, sheet_name='Clean_Data', index=False)
            merged_data.to_excel(writer, sheet_name='Merged_Data', index=False)
        
        st.download_button(
            "Download Full Report",
            output.getvalue(),
            "Crew_Exceedance_Report.xlsx",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    except Exception as e:
        st.error(f"Error: {str(e)}")
