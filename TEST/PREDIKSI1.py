# FILE: app.py
import streamlit as st
import pandas as pd
import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Judul
st.title("Prediksi Produksi Bibit Ikan Nila")

# Upload file CSV
uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

if uploaded_file is not None:
    try:
        # Baca data
        df = pd.read_csv(uploaded_file)

        # Tampilkan data awal
        st.subheader("Data Input")
        st.write(df)

        # Pastikan urutan dan nama kolom sama dengan training
        expected_cols = ['Suhu (°C)', 'pH', 'DO (mg/L)', 'Amonia (mg/L)', 'Pakan']
        if all(col in df.columns for col in expected_cols):
            X = df[expected_cols]
            y_pred = model.predict(X)

            # Gabung hasil prediksi ke data
            df['Prediksi Produksi Bibit (ekor)'] = y_pred.astype(int)

            st.subheader("Hasil Prediksi")
            st.write(df)

            # Download hasil
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Hasil Prediksi", data=csv, file_name="hasil_prediksi.csv", mime="text/csv")

        else:
            st.error(f"Kolom harus mengandung: {expected_cols}")

    except Exception as e:
        st.error(f"Terjadi error saat membaca file: {e}")
