# SOAL 4: Perulangan

# 1. Buat sebuah list buah
buah = ["apel", "jeruk", "pisang", "mangga"]

# 2. Gunakan perulangan for untuk menampilkan semua buah
print("\n--- Soal 4.2: Perulangan FOR (Menampilkan Buah) ---")
# Fungsi enumerate() memberikan index (i) dan nilai (b) pada setiap iterasi
for i, b in enumerate(buah):
    # i adalah index (dimulai dari 0), i+1 adalah nomor urut (dimulai dari 1)
    print(f"Buah ke-{i+1}: {b}")
print("--------------------------------------------------")


# 3. Gunakan perulangan while untuk mencetak angka dari 1 sampai 10
print("\n--- Soal 4.3: Perulangan WHILE (Mencetak Angka 1-10) ---")
# Inisialisasi variabel penghitung
counter = 1

# Kondisi perulangan: lakukan selama counter masih <= 10
while counter <= 10:
    print(counter)
    # Update/increment variabel penghitung agar loop berhenti suatu saat
    counter += 1 # sama dengan counter = counter + 1
print("-----------------------------------------------------")