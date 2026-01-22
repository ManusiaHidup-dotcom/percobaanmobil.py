import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="Display Gambar Evo 6", layout="centered")

st.title("Mitsubishi Lancer Evolution VI Rally")

# Opsi 1: Jika gambar ada di URL GitHub (Raw)
url = "https://raw.githubusercontent.com/USER_ANDA/REPO_ANDA/main/testevo6.png"

try:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    
    st.image(img, caption="Mitsubishi Lancer Evo VI - Rally Edition", use_container_width=True)
except:
    st.error("Gagal memuat gambar dari URL. Pastikan link Raw benar.")

# Opsi 2: Jika gambar berada di folder yang sama dengan file app.py di GitHub
# st.image("testevo6.png", caption="Versi Local Path")

st.write("Mobil ini merupakan ikon dari ajang WRC dengan livery Ralliart yang khas.")
