# SOAL 3: Struktur Kontrol

print("\n--- Soal 3: Struktur Kontrol ---")
# 1. Minta input dari user dan konversi ke integer
# Menggunakan try-except untuk penanganan error jika user memasukkan non-angka
try:
    angka = int(input("Masukkan sebuah angka (positif, negatif, atau nol): "))

    # 2. Buat kondisi
    if angka > 0:
        # Jika angka lebih besar dari 0
        print("Angka positif")
    elif angka < 0:
        # Jika angka lebih kecil dari 0
        print("Angka negatif")
    else:
        # Jika angka tidak lebih besar dari 0 DAN tidak lebih kecil dari 0,
        # maka angka harus sama dengan 0
        print("Angka nol")
        
except ValueError:
    print("Input tidak valid. Harap masukkan bilangan bulat.")

print("----------------------------------")