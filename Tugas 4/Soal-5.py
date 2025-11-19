# SOAL 5 (MODIFIKASI): Fungsi Luas Segitiga

# 1. Buat fungsi untuk menghitung luas segitiga
def luas_segitiga(alas, tinggi):
    """Menerima alas dan tinggi lalu mengembalikan luas segitiga."""
    # Rumus: 0.5 * alas * tinggi
    luas = 0.5 * alas * tinggi
    return luas

# Variabel input
a = 8
t = 12

# 2. Hitung dan tampilkan luasnya
hasil_luas = luas_segitiga(a, t)

print("\n--- Soal 5 (Modifikasi): Luas Segitiga ---")
print(f"Alas: {a}, Tinggi: {t}")
print(f"Luas Segitiga: {hasil_luas}")
print("------------------------------------------")