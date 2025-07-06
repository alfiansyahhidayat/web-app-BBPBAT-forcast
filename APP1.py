
import streamlit as st
from streamlit_option_menu import option_menu
from feature import beranda,tentang
from TEST import HISTORIS2, EDA1, PREDIKSI1
# Custom CSS
st.markdown("""
    <style>
    .nav-pills .nav-link.active {
        background-color: #0d6efd !important;
        color: white !important;
        border-bottom: 5px solid #0d6efd;
    }
    .nav-pills .nav-link {
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# Horizontal menu
selected = option_menu(
    menu_title=None,
    options=["Beranda", "Guide line", "EDA", "Prediksi", "Tentang"],
    icons=["house", "book", "bar-chart", "graph-up", "info-circle"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

if selected == "Beranda":
    beranda.show()
elif selected == "Guide line":
    HISTORIS2.show()
elif selected == "EDA":
    EDA1.show()
elif selected == "Prediksi":
    PREDIKSI1.show()
elif selected == "Tentang":
    tentang.run()