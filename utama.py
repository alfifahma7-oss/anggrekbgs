import streamlit as st
import pandas as pd
import os

# ==========================
# KONFIGURASI WEBSITE
# ==========================
st.set_page_config(
    page_title="Orchid Paradise 🌸",
    page_icon="🌱",
    layout="wide"
)

# ==========================
# STYLE / BACKGROUND
# ==========================
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
background: linear-gradient(
135deg,
#e8f5e9, /* Hijau pastel muda */
#fefefe,
#fff9c4  /* Kuning pastel muda */
);
}

[data-testid="stHeader"]{
background: rgba(0,0,0,0);
}

h1{
text-align:center;
color:#2e7d32; /* Hijau daun tua */
font-size:60px;
}

div[data-testid="column"]{
background:white;
padding:15px;
border-radius:20px;
box-shadow:0px 6px 15px rgba(0,0,0,0.12);
}

</style>
""", unsafe_allow_html=True)

# ==========================
# BANNER / FOTO UTAMA
# ==========================
# Menggunakan anggrek1.jpg sebagai banner utama di atas jika ada
if os.path.exists("anggrek1.jpg"):
    st.image("anggrek1.jpg", use_container_width=True, caption="Welcome to Orchid Paradise ✨")

# ==========================
# JUDUL
# ==========================
st.title("🌸 Orchid Paradise")
st.caption("Beautiful • Exotic • Elegance in Every Petal 🌿")

st.divider()

# ==========================
# BACA CSV ANGGREK
# ==========================
# Pastikan file "data_anggrek.csv" sudah satu folder dengan file python ini
df = pd.read_csv("data_anggrek.csv")

kategori_list = df["kategori"].unique()

for kat in kategori_list:

    st.header(f"🌿 {kat}")

    data_kat = df[df["kategori"] == kat]

    cols = st.columns(3)

    for index, row in data_kat.reset_index().iterrows():

        with cols[index % 3]:

            # FOTO ANGGREK
            if os.path.exists(str(row["foto"])):
                st.image(row["foto"], use_container_width=True)
            else:
                st.warning(f"Foto {row['foto']} tidak ditemukan")

            # NAMA ANGGREK
            st.subheader(row["nama"])

            # HARGA
            st.markdown(f"### 💸 Rp {row['harga']:,}")

            # STATUS (Tersedia / Habis)
            st.success(f"Status: {row['status']}")

            # TOMBOL ORDER
            if st.button(
                f"🛒 Pesan {row['nama']}",
                key=f"order_{kat}_{index}"
            ):
                st.success(f"{row['nama']} ditambahkan ke keranjang!")

    st.divider()

# ==========================
# FOOTER
# ==========================
st.subheader("📍 Hubungi Kami")

col1, col2 = st.columns(2)

with col1:
    st.info("""
🏪 **Orchid Paradise**

Yogyakarta, Indonesia
""")

with col2:

    no_hp = "6281234567890"

    pesan = "Halo Orchid Paradise! Saya ingin memesan bunga anggrek 🌸"

    link = f"https://wa.me/{no_hp}?text={pesan.replace(' ','%20')}"

    st.link_button(
        "📱 Pesan via WhatsApp",
        link
    )

st.caption("© 2026 Orchid Paradise — Beautiful Orchid Specialist 🌸")
