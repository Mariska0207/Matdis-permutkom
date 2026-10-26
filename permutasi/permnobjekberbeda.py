import math
import time
from itertools import permutations

mahasiswa = ["Nisa", "Mariska", "Intan", "Jaki", "Juhri"]

n = len(mahasiswa)

def tampilkan_materi():
    print("\n" + "="*55)
    print(" 📖 MATERI: PERMUTASI n OBJEK BERBEDA ")
    print("="*55)
    print("Permutasi adalah cara menyusun objek dengan ")
    print("memperhatikan urutan (AB berbeda dengan BA).")
    print("Permutasi n objek berbeda berarti menyusun seluruh ")
    print("n objek yang tersedia, tanpa ada objek yang tersisa.")
    print("\nRumus Permutasi:")
    print("P(n) = n!")
    print("\nKeterangan:")
    print("n = total objek berbeda yang disusun")
    print("! = faktorial (contoh: 3! = 3 x 2 x 1)")
    print("="*55)

def tampilkan_studi_kasus():
    print("\n" + "="*55)
    print(" 💡 STUDI KASUS ")
    print("="*55)
    print(f"Terdapat {n} mahasiswa (n = {n}):")
    print(", ".join(mahasiswa))
    print("\nKelima mahasiswa tersebut akan berfoto berjajar ")
    print("dalam satu baris.")
    print("\nPertanyaan:")
    print("Ada berapa banyak susunan berdiri yang mungkin?")
    print("="*55)

def tampilkan_jawaban():
    print("\n" + "="*55)
    print(" 📝 JAWABAN & PEMBAHASAN ")
    print("="*55)
    print("Diketahui:")
    print(f"n = {n} (total mahasiswa)")

    total = math.factorial(n)

    uraian = ""
    for i in range(n, 0, -1):
        uraian = uraian + str(i)
        if i > 1:
            uraian = uraian + " x "

    print("\nLangkah Penyelesaian:")
    print(f"P({n}) = {n}!")
    print(f"P({n}) = {uraian}")
    print(f"P({n}) = {total}")

    hasil = len(list(permutations(mahasiswa)))

    print(f"\nKesimpulan:")
    print(f"Berdasarkan perhitungan, terdapat {hasil} susunan berbeda")
    print(f"untuk {n} mahasiswa yang berfoto dalam satu baris.")
    print("="*55)

def tampilkan_daftar_susunan():
    print("\n" + "="*55)
    print(" 📋 DAFTAR SUSUNAN ")
    print("="*55)
    for i, susunan in enumerate(permutations(mahasiswa), start=1):
        print(f"{i}. " + " - ".join(susunan))
    print("="*55 + "\n")

def jalankan_modul():
    tampilkan_materi()
    time.sleep(2)
    tampilkan_studi_kasus()
    time.sleep(2)
    tampilkan_jawaban()
    time.sleep(2)
    tampilkan_daftar_susunan()

if __name__ == "__main__":
    jalankan_modul()