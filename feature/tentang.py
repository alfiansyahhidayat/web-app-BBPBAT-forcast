import streamlit as st
from PIL import Image

def run():
    st.title("Tentang Aplikasi")

    st.markdown("""
    <div style="text-align: justify;">
    Aplikasi ini dikembangkan untuk membantu Balai Besar Perikanan Budidaya Air Tawar (BBPBAT) Sukabumi dalam 
    <b>memprediksi produksi ikan air tawar</b> berdasarkan data historis yang tersedia.
    <br><br>
    Dengan memanfaatkan <b>teknologi Machine Learning</b>, aplikasi ini mampu melakukan analisis data dan memberikan estimasi 
    produksi ikan berdasarkan berbagai faktor, seperti lingkungan dan pakan.
    <br><br>
    Fitur-fitur yang tersedia meliputi:
    <ul>
        <li><b>Beranda:</b> Informasi singkat dan pengantar aplikasi</li>
        <li><b>Historis:</b> Upload dan eksplorasi data historis</li>
        <li><b>EDA:</b> Analisis eksploratif untuk memahami pola dalam data</li>
        <li><b>Prediksi:</b> Prediksi hasil produksi ikan menggunakan algoritma Machine Learning</li>
    </ul>
    <br>
    Aplikasi ini dirancang agar dapat digunakan dengan mudah oleh siapa saja, baik oleh pengelola perikanan maupun masyarakat umum.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Teknologi yang Digunakan")
    st.markdown("""
    - Python
    - Streamlit
    - Scikit-learn
    - Pandas
    - Matplotlib / Seaborn
    """)

    st.subheader("Data")
    st.markdown("Data diperoleh dari Balai Besar Perikanan Budidaya Air Tawar Sukabumi (BBPBAT) dan bersifat historis.")

    st.subheader("Kontak")
    st.markdown("""
    Jika Anda memiliki pertanyaan atau saran, silakan hubungi:
    - Email: info@bbpbat.go.id
    - Telepon: (0266) 123-4567
    """)

    # Tambahkan logo atau gambar lembaga jika perlu
    try:
        image = Image.open("gambar//logo_bbpbat.png")  # pastikan path benar
        st.image(image, width=200)
    except:
        pass
    st.markdown("""
    <div style="text-align: center;">
        <p>© 2023 Balai Besar Perikanan Budidaya Air Tawar Sukabumi</p>
        <p>All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)    