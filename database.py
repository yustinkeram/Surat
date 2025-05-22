from pymongo import MongoClient

# Koneksi ke MongoDB (ganti URI jika perlu)
client = MongoClient("mongodb://localhost:27017/")
db = client["arsip_surat"]  # Nama database
collection = db["surat_masuk"]  # Nama koleksi

# Fungsi untuk menyimpan surat ke database
def insert_surat(nomor_surat, tanggal, pengirim, perihal, file_path):
    surat = {
        "nomor_surat": nomor_surat,
        "tanggal": str(tanggal),
        "pengirim": pengirim,
        "perihal": perihal,
        "file_path": file_path
    }
    collection.insert_one(surat)

# Fungsi untuk mengambil semua surat
def get_all_surat():
    return list(collection.find({}))  # Mengubah cursor MongoDB ke list
