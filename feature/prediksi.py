import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def show():
    st.title("Prediksi Hasil Panen Ikan Air Tawar (MLR)")

    if 'dataset' not in st.session_state:
        st.warning("Silakan upload data terlebih dahulu melalui menu 'Historis'.")
        return

    df = st.session_state['dataset']
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if len(numeric_cols) < 2:
        st.error("Data harus memiliki minimal 2 kolom numerik (fitur dan target).")
        return

    st.subheader("Pilih Variabel")
    x_cols = st.multiselect("Fitur (X) - Bisa pilih lebih dari satu", numeric_cols)
    y_col = st.selectbox("Target (Y)", [col for col in numeric_cols if col not in x_cols])
   
    if not x_cols:
        st.warning("Pilih minimal satu fitur untuk melanjutkan.")
        return

    X = df[x_cols]
    y = df[y_col]

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    st.success(f"Model telah dilatih untuk memprediksi `{y_col}` berdasarkan `{', '.join(x_cols)}`.")

    mse = mean_squared_error(y, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y, y_pred)

    st.write("### Evaluasi Model")
    st.write(f"- **R² Score:** {r2:.4f}")
    st.write(f"- **RMSE:** {rmse:.2f}")

    # Prediksi Manual
    st.subheader("Coba Prediksi Baru")
    input_data = []
    for col in x_cols:
        val = st.number_input(f"Masukkan nilai untuk {col}", value=float(X[col].mean()))
        input_data.append(val)

    pred_y = model.predict([input_data])[0]
    st.info(f"Prediksi {y_col} untuk input {dict(zip(x_cols, input_data))} adalah **{pred_y:.2f}**")

    # Perbandingan
    st.subheader("Perbandingan Nilai Aktual vs Prediksi")
    comparison_df = df.copy()
    comparison_df['Prediksi'] = y_pred
    st.dataframe(comparison_df[[y_col, 'Prediksi']].head(20))

    fig2, ax2 = plt.subplots()
    ax2.plot(y.values, label='Aktual', marker='o')
    ax2.plot(y_pred, label='Prediksi', marker='x')
    ax2.set_title("Aktual vs Prediksi")
    ax2.set_ylabel(y_col)
    ax2.legend()
    st.pyplot(fig2)

    # Error
    st.subheader("Visualisasi Error (Residual)")
    residuals = y - y_pred
    fig3, ax3 = plt.subplots()
    sns.histplot(residuals, kde=True, ax=ax3)
    ax3.set_title("Distribusi Residual (Error)")
    st.pyplot(fig3)
