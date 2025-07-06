import streamlit as st
import pandas as pd
import os

TEMP_DIR = "temp_data"
os.makedirs(TEMP_DIR, exist_ok=True)

def save_uploaded_file(uploaded_file):
    file_path = os.path.join(TEMP_DIR, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def load_data(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith((".xlsx", ".xls")):
        return pd.read_excel(file_path, engine="openpyxl")
    return None

def show():
    st.title("Upload dan Tampilkan Data")

    uploaded_file = st.file_uploader("Pilih file CSV atau Excel", type=["csv", "xlsx", "xls"])

    if uploaded_file is not None:
        file_path = save_uploaded_file(uploaded_file)
        df = load_data(file_path)
        st.session_state['dataset'] = df
        st.session_state['file_path'] = file_path
        st.success("File berhasil diunggah dan disimpan.")
    elif 'file_path' in st.session_state:
        file_path = st.session_state['file_path']
        df = load_data(file_path)
        st.session_state['dataset'] = df
        st.info("File lama dimuat ulang dari penyimpanan sementara.")

    if 'dataset' in st.session_state:
        st.write("Data lengkap:")
        st.dataframe(st.session_state['dataset'])
