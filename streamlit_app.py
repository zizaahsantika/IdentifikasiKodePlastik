import streamlit as st

# Data kode plastik dan penjelasan resin
PLASTIC_INFO = {
    "1": "🔵 **PET (Polyethylene Terephthalate)**\n\nBiasa digunakan untuk botol air minum, botol soda. Dapat didaur ulang, namun tidak disarankan untuk dipakai ulang.",
    "2": "🟢 **HDPE (High-Density Polyethylene)**\n\nDipakai untuk botol susu, botol deterjen. Aman dan sering didaur ulang.",
    "3": "🟡 **PVC (Polyvinyl Chloride)**\n\nSering digunakan untuk pipa, bungkus plastik. Sulit didaur ulang dan bisa berbahaya jika terbakar.",
    "4": "🟣 **LDPE (Low-Density Polyethylene)**\n\nDigunakan untuk kantong plastik, bungkus makanan. Tidak selalu diterima di tempat daur ulang.",
    "5": "🟠 **PP (Polypropylene)**\n\nContohnya tutup botol, wadah makanan microwave. Tahan panas dan bisa didaur ulang.",
    "6": "🔴 **PS (Polystyrene)**\n\nUntuk styrofoam, wadah makanan cepat saji. Sulit didaur ulang dan berpotensi berbahaya.",
    "7": "⚫ **Other**\n\nCampuran plastik atau plastik baru seperti PLA. Sulit untuk didaur ulang secara umum."
}

# === Navigasi Sidebar ===
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman", ["Identifikasi Kode Plastik", "Daftar Kode Plastik"])

# === Halaman 1: Identifikasi Berdasarkan Input Angka ===
if page == "Identifikasi Kode Plastik":
    st.title("🔍 Identifikasi Resin Berdasarkan Kode Angka")

    kode_input = st.text_input("Masukkan kode plastik (1-7):")

    if kode_input:
        if kode_input in PLASTIC_INFO:
            st.subheader(f"Kode Plastik: {kode_input}")
            st.markdown(PLASTIC_INFO[kode_input])
        else:
            st.error("⚠️ Kode tidak valid. Masukkan angka antara 1 sampai 7.")

# === Halaman 2: Daftar Lengkap Kode Plastik ===
elif page == "Daftar Kode Plastik":
    st.title("📘 Daftar Kode Plastik (RIC)")

    for kode, info in PLASTIC_INFO.items():
        st.subheader(f"Kode {kode}")
        st.markdown(info)
        st.markdown("---")

# === Footer ===
st.markdown("---")
st.markdown("**Dibuat oleh Kelompok 1 - Proyek PLI**")
