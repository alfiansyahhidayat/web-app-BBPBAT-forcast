# === prediksi.py (inside feature/) ===
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

MODEL_PATH = 'model_regresi.pkl'

def show():
    st.title("Prediksi Produksi Bibit Ikan Nila (MLR)")

    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
    except:
        st.error("❌ Model belum tersedia. Pastikan file 'model_regresi.pkl' ada di direktori.")
        return

    st.subheader("Input Data Prediksi Manual")


    suhu = st.number_input("Suhu (°C)", min_value=0.0)
    ph = st.number_input("pH", min_value=0.0)
    do = st.number_input("DO (mg/L)", min_value=0.0)
    amonia = st.number_input("Amonia (mg/L)", min_value=0.0)
    pakan = st.number_input("Pakan (kg)", min_value=0.0)

    input_data = pd.DataFrame({
        "Suhu (°C)": [suhu],
        "pH": [ph],
        "DO (mg/L)": [do],
        "Amonia (mg/L)": [amonia],
        "Pakan": [pakan]
    })

    if st.button("Prediksi"):
        hasil = model.predict(input_data)[0]
        st.markdown(f"""
    <div style="background-color:#1c4532; padding:20px; border-radius:10px; margin-top:20px">
        <h3 style="color:#90EE90; text-align:center;">
            ✅ Prediksi Produksi Bibit:<br> 
            <span style="font-size:40px;">{int(hasil):,} ekor</span>
        </h3>
    </div>
""", unsafe_allow_html=True)

    # Evaluasi jika dataset tersedia
    if 'dataset' in st.session_state:
        df = st.session_state['dataset']

        expected_cols = ["Tahun", "bulan", "Minggu", "Suhu (°C)", "pH", "DO (mg/L)", "Amonia (mg/L)", "Pakan", "Produksi Bibit (ekor)"]
        if not all(col in df.columns for col in expected_cols):
            st.warning(f"⚠️ Dataset tidak memiliki semua kolom: {expected_cols}")
            return

        X = df[["Suhu (°C)", "pH", "DO (mg/L)", "Amonia (mg/L)", "Pakan"]]
        y = df["Produksi Bibit (ekor)"]
        y_pred = model.predict(X)

 

        st.subheader("Perbandingan Nilai Aktual vs Prediksi")
        df_compare = df.copy()
        df_compare["Prediksi"] = y_pred
        st.dataframe(df_compare[["Produksi Bibit (ekor)", "Prediksi"]].head(20))

        fig, ax = plt.subplots()
        ax.plot(y.values, label='Aktual', marker='o')
        ax.plot(y_pred, label='Prediksi', marker='x')
        ax.set_title("Kurva Aktual vs Prediksi")
        ax.set_ylabel("Produksi Bibit (ekor)")
        ax.legend()
        st.pyplot(fig)

        st.subheader("Distribusi Error (Residual)")
        residuals = y - y_pred
        fig2, ax2 = plt.subplots()
        sns.histplot(residuals, kde=True, ax=ax2)
        ax2.set_title("Distribusi Residual")
        st.pyplot(fig2)
