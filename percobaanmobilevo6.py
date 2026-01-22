import streamlit as st

# Mengatur judul halaman
st.set_page_config(page_title="Modifikasi Mitsubishi Evo 6")

st.title("Project Modifikasi Mobil")

# Menampilkan gambar yang ada di folder yang sama
# Cukup panggil nama filenya saja
st.image("testevo6.png", caption="Mitsubishi Lancer Evolution VI - Rally Look")

st.write("""
Mobil ini adalah hasil render 3D untuk project modifikasi. 
Livery yang digunakan terinspirasi dari tim Ralliart.
""")
