import streamlit as st

st.title("🎈 Identifikasi Jenis Plastik Pada Kode Resin")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
from PIL import Image
import numpy as np
# Jika Anda menggunakan model machine learning (misalnya TensorFlow/Keras)
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image

# Daftar nama kelas kode plastik (sesuaikan dengan model Anda)
CLASS_NAMES = {
    0: "1 (PET atau PETE)",
    1: "2 (HDPE)",
    2: "3 (PVC atau V)",
    3: "4 (LDPE)",
    4: "5 (PP)",
    5: "6 (PS)",
    6: "7 (Lain-lain)"
}

# Informasi detail tentang setiap kode plastik
PLASTIC_INFO = {
    "1 (PET atau PETE)": "Polyethylene Terephthalate. Umumnya digunakan untuk botol minuman ringan, wadah makanan, dan serat pakaian. Dianggap aman untuk penggunaan sekali pakai, tetapi dapat melepaskan zat berbahaya jika digunakan berulang kali atau terkena panas.",
    "2 (HDPE)": "High-Density Polyethylene. Digunakan untuk botol susu, botol deterjen, botol sampo, pipa, dan beberapa kantong plastik. Dianggap sebagai salah satu plastik yang lebih aman dan dapat didaur ulang.",
    "3 (PVC atau V)": "Polyvinyl Chloride. Digunakan dalam pipa, kabel, mainan, dan beberapa kemasan makanan. Mengandung klorin dan phthalates yang dapat berbahaya bagi kesehatan dan lingkungan. Daur ulang PVC sulit dan jarang dilakukan.",
    "4 (LDPE)": "Low-Density Polyethylene. Digunakan untuk kantong plastik, cling wrap, botol lunak, dan pelapis karton susu. Dianggap relatif aman tetapi tidak mudah didaur ulang di banyak tempat.",
    "5 (PP)": "Polypropylene. Digunakan untuk wadah makanan, tutup botol, sedotan, dan perlengkapan medis. Kuat, tahan panas, dan relatif aman. Dapat didaur ulang.",
    "6 (PS)": "Polystyrene (Styrofoam). Digunakan untuk wadah makanan sekali pakai, cangkir kopi, dan bahan pengemas. Sulit didaur ulang dan dapat melepaskan styrene yang berpotensi berbahaya.",
    "7 (Lain-lain)": "Kategori ini mencakup semua jenis plastik lain, termasuk polycarbonate (PC), polylactic acid (PLA), acrylic, nylon, dan fiberglass. Sifat dan daur ulang bervariasi tergantung jenis plastiknya. Beberapa mungkin mengandung BPA (Bisphenol A) yang berbahaya."
}

# --- Fungsi untuk melakukan identifikasi kode plastik ---
# Placeholder untuk model machine learning atau logika identifikasi gambar lainnya
# Jika Anda menggunakan model ML, uncomment bagian di bawah dan sesuaikan path model
# @st.cache_resource
# def load_plastic_model(model_path):
# """Memuat model machine learning untuk identifikasi plastik."""
# try:
# model = load_model(model_path)
# return model
# except Exception as e:
# st.error(f"Gagal memuat model: {e}")
# return None

# def preprocess_image(image, target_size=(224, 224)):
# """Memproses gambar untuk input ke model."""
# if image.mode != "RGB":
# image = image.convert("RGB")
# image = image.resize(target_size)
# image = np.array(image)
# image = image / 255.0 # Normalisasi
# image = np.expand_dims(image, axis=0)
# return image

def identify_plastic_code(image_file):
    """
    Fungsi placeholder untuk mengidentifikasi kode plastik dari gambar.
    Ganti logika di bawah ini dengan metode identifikasi gambar Anda.
    """
    image = Image.open(image_file)
    width, height = image.size

    # Contoh logika sederhana berdasarkan ukuran dan format (untuk demonstrasi)
    if width * height > 15000 and image.format in ["JPEG", "JPG"]:
        return {"prediction": "1 (PET atau PETE)", "probability": 0.75}
    elif image.format == "PNG":
        return {"prediction": "2 (HDPE)", "probability": 0.82}
    elif "styrofoam" in str(image_file.name).lower():
        return {"prediction": "6 (PS)", "probability": 0.68}
    else:
        return {"prediction": "Tidak dapat mengidentifikasi", "probability": 0.5}

# --- Tampilan Aplikasi Streamlit ---
st.title("Aplikasi Identifikasi Kode Plastik Berbasis Gambar")
st.write("Unggah gambar yang jelas dari bagian bawah wadah plastik yang menunjukkan kode daur ulang untuk identifikasi.")
st.info("Pastikan gambar fokus dan kode plastik terlihat jelas untuk hasil terbaik.")

# Sidebar untuk informasi tambahan dan panduan
with st.sidebar:
    st.header("Panduan Penggunaan")
    st.markdown(
        """
        1. Unggah gambar kode plastik menggunakan tombol di bawah.
        2. Pastikan gambar hanya berisi satu kode plastik dan terlihat jelas.
        3. Klik tombol **"Identifikasi"** untuk melihat hasilnya.
        4. Hasil identifikasi akan ditampilkan di bawah gambar.
        5. Informasi detail tentang jenis plastik yang terdeteksi akan muncul.
        """
    )
    st.subheader("Tentang Kode Plastik")
    st.markdown(
        """
        Kode daur ulang plastik adalah simbol yang mengidentifikasi jenis resin plastik yang digunakan dalam pembuatan produk. Memahami kode ini penting untuk daur ulang dan mengetahui potensi risiko kesehatan terkait penggunaan plastik tertentu.
        """
    )

# Widget untuk mengunggah gambar
uploaded_file = st.file_uploader("Pilih gambar kode plastik...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Menampilkan gambar yang diunggah
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang Diunggah.", use_column_width=True)

    # Tombol untuk memproses gambar
    if st.button("Identifikasi"):
        with st.spinner("Menganalisis gambar..."):
            result = identify_plastic_code(uploaded_file)

        st.subheader("Hasil Identifikasi:")
        if "prediction" in result:
            st.write(f"Kode Plastik yang Terdeteksi: **{result['prediction']}**")
            if "probability" in result and result["probability"] is not None:
                st.write(f"Probabilitas: **{result['probability']:.2f}**")
            if result["prediction"] in PLASTIC_INFO:
                st.info(PLASTIC_INFO[result["prediction"]])
            elif result["prediction"] == "Tidak dapat mengidentifikasi":
                st.warning("Tidak dapat mengidentifikasi kode plastik dengan tingkat kepercayaan yang tinggi. Coba unggah gambar lain yang lebih jelas.")
        else:
            st.error("Terjadi kesalahan dalam proses identifikasi.")

else:
    st.info("Silakan unggah gambar kode plastik untuk memulai identifikasi.")
import streamlit as st

# Sidebar navigasi
menu = st.sidebar.radio("Navigasi", ["Beranda", "Informasi", "Identifikasi Resin (RIC)"])

# Halaman Beranda
if menu == "Beranda":
    st.title("Selamat Datang di Aplikasi Identifikasi Resin")
    st.write("""
    Aplikasi ini membantu Anda mengenali jenis plastik berdasarkan kode RIC (Resin Identification Code).
    Pilih menu di sebelah kiri untuk mulai.
    """)

# Halaman Informasi
elif menu == "Informasi":
    st.title("Tentang Resin Identification Code (RIC)")
    st.write("""
    **Resin Identification Code (RIC)** adalah sistem pengkodean numerik dari 1 sampai 7
    yang digunakan untuk mengidentifikasi jenis plastik atau resin dalam produk.

    Kode ini biasanya ditemukan pada kemasan plastik, berbentuk segitiga panah dengan angka di dalamnya.
    """)

# Halaman Identifikasi Resin
elif menu == "Identifikasi Resin (RIC)":
    st.title("Identifikasi Resin Berdasarkan Kode (RIC)")

    ric_code = st.selectbox("Pilih Kode Resin (1-7)", [1, 2, 3, 4, 5, 6, 7])

    resin_info = {
        1: ("PET (Polyethylene Terephthalate)", "Botol air mineral, botol minuman ringan."),
        2: ("HDPE (High-Density Polyethylene)", "Botol susu, wadah sabun, galon kecil."),
        3: ("PVC (Polyvinyl Chloride)", "Pipa air, pembungkus kabel, kemasan minyak."),
        4: ("LDPE (Low-Density Polyethylene)", "Kantong belanja, bungkus makanan."),
        5: ("PP (Polypropylene)", "Wadah makanan, tutup botol, sedotan."),
        6: ("PS (Polystyrene)", "

# Footer
st.markdown("---")
st.markdown("Dibuat dengan Streamlit oleh [Kelompok 1/PLI]")
