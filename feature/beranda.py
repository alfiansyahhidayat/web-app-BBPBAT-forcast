import streamlit as st
from PIL import Image

def show():
    st.markdown("""
    <h1 style='text-align: center;'>Selamat Datang di Aplikasi Prediksi Produksi Ikan</h1>
    <h4 style='text-align: center; color: gray;'>Balai Besar Perikanan Budidaya Air Tawar (BBPBAT) Sukabumi</h4>
    """, unsafe_allow_html=True)

    st.write("📌 Sistem ini bertujuan untuk membantu memprediksi hasil panen ikan air tawar berdasarkan data historis yang tersedia, dengan pendekatan Machine Learning.")

    # Tampilkan logo / gambar utama
    image = Image.open("../gambar/BBPBAT.jpg")

    st.image(image, caption='Budidaya Ikan Air Tawar - BBPBAT Sukabumi', use_column_width=True)

    # Fitur Aplikasi
    st.subheader("✨ Fitur Utama Aplikasi")
    st.markdown("""
    - 📁 Upload dan kelola data historis produksi ikan
    - 📊 Eksplorasi data dan visualisasi (EDA)
    - 🔍 Prediksi hasil produksi menggunakan Machine Learning
    - 📌 Informasi dan profil BBPBAT Sukabumi
    """)

    # Jenis komoditas ikan
    st.subheader("🐟 Jenis Komoditas Budidaya Ikan Air Tawar")
    jenis_ikan = [
        "Ikan Mas", "Ikan Nila", "Ikan Lele", "Ikan Patin", "Ikan Gurame", "Ikan mas",
        "Ikan Arwana", "Ikan Louhan", "Ikan paus", "Ikan Guppy", "Ikan Discus", "Ikan Oscar"
    ]
    col1, col2 = st.columns(2)
    with col1:
        for i in jenis_ikan[:len(jenis_ikan)//2]:
            st.write(f"• {i}")
    with col2:
        for i in jenis_ikan[len(jenis_ikan)//2:]:
            st.write(f"• {i}")

    # Video Profil
    st.subheader("🎥 Video Profil BBPBAT")
    st.video("https://youtu.be/DQrQ7nbbrqQ?si=zPRa-8jJFwaZczKt")



