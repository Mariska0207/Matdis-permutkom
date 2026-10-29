import math
import time
from itertools import permutations

calon = ["Annisa", "Intan", "Mariska", "Dzaky", "Zuhri", "Farid", "Dopa", "Rega", "Rendy"]
jabatan = ["Ketua", "Sekretaris", "Bendahara"]

n = len(calon)
r = len(jabatan)

def tampilkan_materi():
    print("\n" + "="*65)
    print("MATERI: PERMUTASI r DARI n OBJEK ")
    print("="*65)
    print("Permutasi adalah cara menyusun objek dengan ")
    print("memperhatikan urutan (AB berbeda dengan BA).")
    print("Permutasi r dari n objek berarti memilih r objek dari ")
    print("n objek yang tersedia, lalu menyusunnya dalam urutan ")
    print("tertentu. Objek yang sudah dipilih tidak bisa dipilih lagi.")
    print("\nRumus Permutasi:")
    print("P(n, r) = n! / (n - r)!")
    print("\nKeterangan:")
    print("n = total objek keseluruhan yang tersedia")
    print("r = jumlah objek yang dipilih dan disusun")
    print("! = faktorial (contoh: 3! = 3 x 2 x 1)")
    print("="*65)

def tampilkan_studi_kasus():
    print("\n" + "="*70)
    print("STUDI KASUS ")
    print("="*70)
    print(f"Sebuah organisasi memiliki {n} calon pengurus (n = {n}):")
    print(", ".join(calon))
    print(f"\nDari calon tersebut akan dipilih {r} orang (r = {r}) untuk")
    print(f"menduduki {r} jabatan yang berbeda, yaitu {', '.join(jabatan)}.")
    print("Satu orang hanya boleh memegang satu jabatan.")
    print("\nPertanyaan:")
    print("Ada berapa banyak susunan pengurus yang mungkin?")
    print("="*70)

def tampilkan_jawaban():
    print("\n" + "="*55)
    print("JAWABAN & PEMBAHASAN ")
    print("="*55)
    print("Diketahui:")
    print(f"n = {n} (total calon)")
    print(f"r = {r} (jabatan yang diisi)")

    sisa = n - r
    total = math.factorial(n) // math.factorial(sisa)

    uraian_n = ""
    for i in range(n, 0, -1):
        uraian_n = uraian_n + str(i)
        if i > 1:
            uraian_n = uraian_n + " x "

    uraian_sisa = ""
    for i in range(sisa, 0, -1):
        uraian_sisa = uraian_sisa + str(i)
        if i > 1:
            uraian_sisa = uraian_sisa + " x "
    if sisa == 0:
        uraian_sisa = "1"

    print("\nLangkah Penyelesaian:")
    print(f"P({n}, {r}) = {n}! / ({n} - {r})!")
    print(f"P({n}, {r}) = {n}! / {sisa}!")
    print(f"P({n}, {r}) = ({uraian_n}) / ({uraian_sisa})")
    print(f"P({n}, {r}) = {math.factorial(n)} / {math.factorial(sisa)}")
    print(f"P({n}, {r}) = {total}")

    hasil = math.perm(n, r)

    print(f"\nKesimpulan:")
    print(f"Berdasarkan perhitungan, terdapat {hasil} susunan pengurus")
    print(f"berbeda untuk mengisi {r} jabatan dari {n} calon yang ada.")
    print("="*55)

def tampilkan_daftar_susunan():
    print("\n" + "="*55)
    print("DAFTAR SUSUNAN ")
    print("="*55)
    for i, susunan in enumerate(permutations(calon, r), start=1):
        print(f"{i}. " + ", ".join(f"{j}: {o}" for j, o in zip(jabatan, susunan)))
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