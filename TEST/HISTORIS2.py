import streamlit as st

def show():
    st.title("📘 Panduan Penggunaan Aplikasi")
    st.caption("Versi 1.0 | Prediksi Produksi Bibit Ikan Nila")

    st.markdown("### 🧭 Langkah-langkah Penggunaan Aplikasi")

    with st.expander("📁 1. Upload Data"):
        st.markdown("""
        - Akses menu **EDA** di navigasi atas.
        - Klik **Upload File**, lalu unggah file berformat `.csv` atau `.xlsx`.
        - Pastikan file memiliki kolom seperti berikut:
            - `Tahun`, `Bulan`, `Minggu`, `Suhu (°C)`, `pH`, `DO (mg/L)`, 
              `Amonia (mg/L)`, `Pakan`, `Produksi Bibit (ekor)`
        - ✅ Jika berhasil, data akan langsung ditampilkan dan tersimpan untuk sesi tersebut.
        """)

    with st.expander("📊 2. Eksplorasi Data (EDA)"):
        st.markdown("""
        - Lihat statistik deskriptif secara otomatis.
        - Tampilkan grafik:
            - Histogram 📈
            - Scatter plot 🔵
            - Korelasi antar fitur (Heatmap) 🔥
            - Deteksi outlier (Boxplot) 🚨
        - Gunakan dropdown dan pilihan interaktif untuk memilih kolom data.
        """)

    with st.expander("🤖 3. Prediksi Produksi Bibit"):
        st.markdown("""
        - Masuk ke menu **Prediksi**.
        - Masukkan nilai-nilai:
            - Pakan (kg)
            - Amonia (mg/L)
            - Minggu ke-
        - Klik tombol **Prediksi**.
        - Output:
            - Nilai prediksi produksi bibit ikan nila 🎯
            - Evaluasi model (R², RMSE, MAE)
            - Visualisasi grafik prediksi aktual vs model 📉
            - Distribusi error 🔍
        """)

    with st.expander("ℹ️ 4. Menu Tentang"):
        st.markdown("""
        - Berisi latar belakang dan tujuan aplikasi.
        - Dapat menjadi referensi bagi pengguna umum untuk memahami konteks penelitian.
        """)

    st.divider()

    st.markdown("""
    🔐 **Catatan Penting:**
    - Gunakan data yang sudah bersih dan lengkap.
    - Pastikan nama kolom tidak ada yang typo.
    - Aplikasi ini bersifat statis dan tidak menyimpan data pengguna secara permanen.
    """)

    st.info("Jika mengalami kendala atau menemukan bug, hubungi pengembang melalui halaman **Tentang**.")

    st.success("📌 Selamat menggunakan aplikasi prediksi ini!")
