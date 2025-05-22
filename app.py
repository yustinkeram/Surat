import os
import streamlit as st
from database import insert_surat, get_all_surat

# Pastikan folder uploads ada
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# **Form Input Surat**
st.title("📂 Arsip Surat Digital")
st.write("Tambahkan surat baru ke dalam database:")

nomor_surat = st.text_input("Nomor Surat")
tanggal = st.date_input("Tanggal")
pengirim = st.text_input("Pengirim")
perihal = st.text_input("Perihal")

# **Upload File Surat**
uploaded_file = st.file_uploader("Upload Surat (PDF)", type=["pdf"])

if st.button("Simpan Surat"):
    if nomor_surat and tanggal and pengirim and perihal and uploaded_file:
        # Simpan file ke folder uploads/
        file_path = os.path.join("uploads", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Simpan data ke MongoDB
        insert_surat(nomor_surat, tanggal, pengirim, perihal, file_path)
        st.success("✅ Surat berhasil disimpan!")
    else:
        st.error("❌ Harap isi semua kolom dan upload file.")

# **Menampilkan Daftar Surat**
st.write("### 📜 Daftar Surat yang Tersimpan:")

data = get_all_surat()
if data:
    for surat in data:
        file_link = f"[Buka Surat]({surat['file_path']})" if surat["file_path"] else "Tidak ada file"
        st.write(f"📄 **{surat['nomor_surat']}** | {surat['tanggal']} | {surat['pengirim']} | {surat['perihal']} | {file_link}")
else:
    st.write("Belum ada data.")
