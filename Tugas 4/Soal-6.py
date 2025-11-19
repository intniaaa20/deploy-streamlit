# SOAL 6 (MODIFIKASI): List dan Nilai Kosmetik

# 1. Buat list harga kosmetik
harga_kosmetik = [45000, 120000, 75000, 250000, 30000]
print("\n--- Soal 6 (Modifikasi): List Harga Kosmetik ---")
print(f"List Harga Awal: {harga_kosmetik}")

# 2. Tambahkan harga baru 150000
harga_kosmetik.append(150000)
print(f"Setelah ditambahkan: {harga_kosmetik}")

# 3. Urutkan list dari termahal ke termurah (Descending)
harga_kosmetik.sort(reverse=True)
print(f"Setelah diurutkan (Termahal ke Termurah): {harga_kosmetik}")

# 4. Hitung harga rata-rata
total_harga = sum(harga_kosmetik)
jumlah_produk = len(harga_kosmetik)
rata_rata_harga = total_harga / jumlah_produk

# 5. Tampilkan hasilnya (menggunakan format mata uang sederhana)
print(f"Total Harga Semua Produk: Rp{total_harga:,}")
print(f"Jumlah Produk: {jumlah_produk}")
# Format dengan koma sebagai pemisah ribuan
print(f"Harga Rata-Rata Produk: Rp{rata_rata_harga:,.2f}")
print("--------------------------------------------------")