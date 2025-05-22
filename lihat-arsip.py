import streamlit as st
import sqlite3
import os

# Koneksi ke database
conn = sqlite3.connect("arsip_surat.db")
cursor = conn.cursor()

st.title("📂 Daftar Arsip Surat")

# Ambil data surat yang tersimpan di database
cursor.execute("SELECT id, nomor_surat, perihal, file_path FROM surat_masuk")
data_surat = cursor.fetchall()

# Tampilkan daftar arsip
if data_surat:
    for surat in data_surat:
        id_surat, nomor_surat, perihal, file_path = surat
        with st.expander(f"{nomor_surat} - {perihal}"):
            st.write(f"**Nomor Surat:** {nomor_surat}")
            st.write(f"**Perihal:** {perihal}")

            # Tombol download jika file tersedia
            if file_path and os.path.exists(file_path):
                with open(file_path, "rb") as file:
                    st.download_button(
                        label="📄 Download Surat",
                        data=file,
                        file_name=os.path.basename(file_path),
                        mime="application/pdf"
                    )
            else:
                st.warning("File tidak ditemukan!")

else:
    st.info("Belum ada surat yang diarsipkan.")

# Tutup koneksi database
conn.close()
