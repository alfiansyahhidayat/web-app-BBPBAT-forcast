import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
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
    st.title("Upload dan EDA Data")

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

    if 'dataset' not in st.session_state:
        st.warning("Silakan upload data terlebih dahulu.")
        return

    df = st.session_state['dataset']

    st.subheader("Tampilan Data")
    st.dataframe(df)

    st.subheader("Ringkasan Statistik")
    st.write(df.describe())

    num_cols = df.select_dtypes(include=['int64', 'float64']).columns
    if num_cols.empty:
        st.warning("Tidak ada kolom numerik untuk dianalisis.")
        return

    # Histogram
    st.subheader("Distribusi Data per Kolom (Histogram)")
    selected_hist_col = st.selectbox("Pilih kolom numerik untuk histogram:", num_cols, key="hist")
    fig1, ax1 = plt.subplots()
    sns.histplot(df[selected_hist_col], kde=True, ax=ax1)
    ax1.set_title(f"Distribusi Histogram - {selected_hist_col}")
    st.pyplot(fig1)

    # Korelasi
    st.subheader("Korelasi Antar Fitur")
    corr = df.corr(numeric_only=True)
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax2)
    st.pyplot(fig2)

    # Scatter Plot
    st.subheader("Scatter Plot Dua Variabel")
    col1 = st.selectbox("Pilih X:", num_cols, key="scatter_x")
    col2 = st.selectbox("Pilih Y:", num_cols, key="scatter_y")
    fig3, ax3 = plt.subplots()
    sns.scatterplot(x=df[col1], y=df[col2], ax=ax3)
    ax3.set_title(f"Scatter Plot - {col1} vs {col2}")
    st.pyplot(fig3)

    # Boxplot
    st.subheader("Visualisasi Outlier (Boxplot)")
    selected_box_col = st.selectbox("Pilih kolom untuk boxplot:", num_cols, key="box")
    fig4, ax4 = plt.subplots()
    sns.boxplot(y=df[selected_box_col], ax=ax4)
    ax4.set_title(f"Boxplot - {selected_box_col}")
    st.pyplot(fig4)