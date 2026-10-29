from itertools import permutations
from math import factorial

# Data studi kasus (ubah di sini kalau ingin ganti rasa/jumlah)
CUPCAKE = ["Coklat", "Stroberi", "Vanila", "Matcha"]

def permutasi_melingkar(elemen):
    pertama = elemen[0]
    sisa = elemen[1:]
    return [[pertama] + list(p) for p in permutations(sisa)]

def tampilkan_studi_kasus(cupcake):
    n = len(cupcake)
    print("=" * 55)
    print("STUDI KASUS: CUPCAKE DI PIRING BERPUTAR".center(55))
    print("=" * 55)
    print(f"Seorang pemilik kafe ingin menata {n} cupcake dengan")
    print(f"rasa berbeda ({', '.join(cupcake)})")
    print("di sebuah piring saji yang bisa diputar. Karena piring")
    print("bisa diputar, susunan yang hanya berbeda posisi putar")
    print("dianggap sama.")
    print("Berapa banyak tampilan berbeda yang bisa dibuat?\n")

def jalankan_modul():
    n = len(CUPCAKE)
    tampilkan_studi_kasus(CUPCAKE)

    hasil = permutasi_melingkar(CUPCAKE)

    print("=" * 55)
    print("HASIL".center(55))
    print("=" * 55)
    print(f"Cupcake yang tersedia : {', '.join(CUPCAKE)}")
    print(f"Jumlah cupcake (n)    : {n}")
    print(f"Rumus (n-1)!          : ({n}-1)! = {factorial(n - 1)}")
    print(f"Jumlah susunan        : {len(hasil)}\n")
    print("Susunan searah jarum jam:")
    for i, susunan in enumerate(hasil, 1):
        print(f"{i:>5}. {' -> '.join(susunan)}")

if __name__ == "__main__":
    jalankan_modul()