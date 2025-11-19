# SOAL 7 (MODIFIKASI): Kalkulator Simpel (+ dan - saja)

print("\n--- Soal 7 (Modifikasi): Kalkulator Simpel (+/-) ---")
try:
    # 1. Minta input dua angka dari user
    angka1 = float(input("Masukkan angka pertama: "))
    operator = input("Masukkan operator (+ atau -): ")
    angka2 = float(input("Masukkan angka kedua: "))

    hasil = 0

    # 2. Gunakan if-elif-else untuk menjalankan operasi
    if operator == '+':
        hasil = angka1 + angka2
    elif operator == '-':
        hasil = angka1 - angka2
    else:
        # Jika operator yang dimasukkan tidak valid
        print("Error: Operator tidak valid. Hanya menerima '+' atau '-'.")
        # Menghentikan eksekusi selanjutnya untuk menghindari hasil yang salah
        raise ValueError 

    # 3. Tampilkan hasilnya
    print(f"Hasil: {angka1} {operator} {angka2} = {hasil}")

except ValueError:
    print("Input tidak valid. Pastikan Anda memasukkan angka dan operator yang benar.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")

print("--------------------------------------------------")