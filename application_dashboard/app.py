import display_data
import promotion
import streamlit as st

PAGES = {
     "Data Overview": display_data,
     "Promotion Effect on Stores": promotion
}

selection = st.sidebar.radio("Go to page", list(PAGES.keys()))
page = PAGES[selection]
page.app()