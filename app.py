import streamlit as st 
import numpy as np
import pandas as pd
import get

st.set_page_config(
    page_title="Goggle Scrapy.sh",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# Google Results Scraping, abdalrahman shahrour",
    }
)

st.write('# Google Results Scraping')

element = st.empty()
element.line_chart()
query = element.text_input("enter ur query: ")

st.write(get.get_res(query))