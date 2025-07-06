import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def show():
    st.title("Exploratory Data Analysis (EDA)")
    st.write("Halaman ini menampilkan analisis eksploratif dari data historis.")

    if 'dataset' not in st.session_state:
        st.warning("Silakan upload data terlebih dahulu melalui menu 'Historis'.")
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
