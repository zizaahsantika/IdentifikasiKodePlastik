import streamlit as st
from PIL import Image
import numpy as np

from streamlit_lottie import st_lottie
import requests

# Fungsi untuk mengambil animasi dari URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# URL Lottie (bisa ganti sesuai preferensi)
lottie_loading = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_j1adxtyb.json")  # animasi loading

uploaded_file = st.file_uploader("Pilih gambar kode plastik...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang Diunggah", use_column_width=True)

    if st.button("Identifikasi"):
        with st.spinner("Menganalisis gambar..."):
            # Tambahkan animasi loading
            st_lottie(lottie_loading, height=200, key="loading")
            result = identify_plastic_code(uploaded_file)

        st.subheader("Hasil Identifikasi:")
        st.write(f"**Kode Plastik:** {result['prediction']}")
        st.write(f"**Probabilitas:** {result['probability']:.2f}")

        if result["prediction"] in PLASTIC_INFO:
            st.info(PLASTIC_INFO[result["prediction"]])
        elif result["prediction"] == "Tidak dapat mengidentifikasi":
            st.warning("Gambar tidak cukup jelas atau format tidak dikenali.")

# === Data Kode Plastik ===
CLASS_NAMES = {
    0: "1 (PET atau PETE)",
    1: "2 (HDPE)",
    2: "3 (PVC atau V)",
    3: "4 (LDPE)",
    4: "5 (PP)",
    5: "6 (PS)",
    6: "7 (Lain-lain)"
}

PLASTIC_INFO = {
    "1 (PET atau PETE)": "Polyethylene Terephthalate. Umumnya digunakan untuk botol minuman ringan, wadah makanan, dan serat pakaian.",
    "2 (HDPE)": "High-Density Polyethylene. Digunakan untuk botol susu, botol deterjen, botol sampo, pipa, dan beberapa kantong plastik.",
    "3 (PVC atau V)": "Polyvinyl Chloride. Digunakan dalam pipa, kabel, mainan, dan beberapa kemasan makanan.",
    "4 (LDPE)": "Low-Density Polyethylene. Digunakan untuk kantong plastik, cling wrap, botol lunak, dan pelapis karton susu.",
    "5 (PP)": "Polypropylene. Digunakan untuk wadah makanan, tutup botol, sedotan, dan perlengkapan medis.",
    "6 (PS)": "Polystyrene (Styrofoam). Digunakan untuk wadah makanan sekali pakai, cangkir kopi, dan bahan pengemas.",
    "7 (Lain-lain)": "Kategori ini mencakup plastik lain seperti polycarbonate, PLA, acrylic, dan lainnya. Beberapa mungkin mengandung BPA."
}

# === Fungsi Identifikasi Dummy ===
def identify_plastic_code(image_file):
    image = Image.open(image_file)
    width, height = image.size
    if width * height > 15000 and image.format in ["JPEG", "JPG"]:
        return {"prediction": "1 (PET atau PETE)", "probability": 0.75}
    elif image.format == "PNG":
        return {"prediction": "2 (HDPE)", "probability": 0.82}
    elif "styrofoam" in str(image_file.name).lower():
        return {"prediction": "6 (PS)", "probability": 0.68}
    else:
        return {"prediction": "Tidak dapat mengidentifikasi", "probability": 0.5}

# === Sidebar Navigasi ===
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Beranda", "Identifikasi Kode Plastik", "Daftar Kode Plastik"])

# === Halaman Beranda ===
if page == "Beranda":
    st.title("📦 Aplikasi Identifikasi Kode Plastik (RIC)")
    st.write("""
    Aplikasi ini membantu Anda mengidentifikasi **kode daur ulang plastik (Resin Identification Code / RIC)** berdasarkan gambar simbol daur ulang.
    
    Gunakan menu di sebelah kiri untuk:
    - Mengunggah gambar kode plastik dan mengidentifikasinya
    - Melihat daftar lengkap kode dan informasi daur ulang plastik
    """)

# === Halaman Identifikasi ===
elif page == "Identifikasi Kode Plastik":
    st.title("🔍 Identifikasi Kode Plastik dari Gambar")
    st.write("Unggah gambar dari kode plastik pada kemasan untuk mulai proses identifikasi.")

    uploaded_file = st.file_uploader("Pilih gambar kode plastik...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar yang Diunggah", use_column_width=True)

        if st.button("Identifikasi"):
            with st.spinner("Menganalisis gambar..."):
                result = identify_plastic_code(uploaded_file)

            st.subheader("Hasil Identifikasi:")
            st.write(f"**Kode Plastik:** {result['prediction']}")
            st.write(f"**Probabilitas:** {result['probability']:.2f}")

            if result["prediction"] in PLASTIC_INFO:
                st.info(PLASTIC_INFO[result["prediction"]])
            elif result["prediction"] == "Tidak dapat mengidentifikasi":
                st.warning("Gambar tidak cukup jelas atau format tidak dikenali.")

# === Halaman Daftar Kode Plastik ===
elif page == "Daftar Kode Plastik":
    st.title("📘 Daftar Kode Plastik (RIC)")

    for kode, info in PLASTIC_INFO.items():
        st.subheader(kode)
        st.write(info)
        st.markdown("---")

# === Footer ===
st.markdown("**Dibuat oleh Kelompok 1 - Proyek PLI**")
