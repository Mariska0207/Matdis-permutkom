from itertools import permutations
from math import factorial
from collections import Counter

JUMLAH_LAMPU = {"Merah": 2, "Kuning": 2, "Hijau": 1}

def buat_daftar_lampu(jumlah):
    daftar = []
    for warna, banyak in jumlah.items():
        daftar += [warna] * banyak
    return daftar

def permutasi_identik(daftar):
    return sorted(set(permutations(daftar)))

def hitung_rumus(jumlah):
    n = sum(jumlah.values())
    penyebut = 1
    for banyak in jumlah.values():
        penyebut *= factorial(banyak)
    return n, penyebut, factorial(n) // penyebut

def tampilkan_studi_kasus(jumlah):
    n = sum(jumlah.values())
    rincian = ", ".join(f"{b} {w.lower()}" for w, b in jumlah.items())
    print("=" * 55)
    print("STUDI KASUS: LAMPU HIAS BERJAJAR".center(55))
    print("=" * 55)
    print(f"Seorang dekorator memasang {n} lampu hias pada seutas")
    print(f"tali, terdiri dari {rincian}.")
    print("Lampu yang warnanya sama dianggap identik (tidak bisa")
    print("dibedakan satu sama lain).")
    print("Berapa banyak susunan warna berbeda yang bisa dibuat?\n")

def main():
    tampilkan_studi_kasus(JUMLAH_LAMPU)

    daftar = buat_daftar_lampu(JUMLAH_LAMPU)
    hasil = permutasi_identik(daftar)
    n, penyebut, jumlah_rumus = hitung_rumus(JUMLAH_LAMPU)

    pembilang_str = f"{n}!"
    penyebut_str = " x ".join(f"{b}!" for b in JUMLAH_LAMPU.values())
    penyebut_angka = " x ".join(str(factorial(b)) for b in JUMLAH_LAMPU.values())

    print("=" * 55)
    print("HASIL".center(55))
    print("=" * 55)
    print(f"Jumlah lampu (n)       : {n}")
    for warna, banyak in JUMLAH_LAMPU.items():
        print(f"  - {warna:<8} : {banyak} lampu")
    print(f"Rumus                  : n! / (n1! x n2! x ...)")
    print(f"                       = {pembilang_str} / ({penyebut_str})")
    print(f"                       = {factorial(n)} / ({penyebut_angka})")
    print(f"                       = {factorial(n)} / {penyebut} = {jumlah_rumus}")
    print(f"Jumlah susunan         : {len(hasil)}\n")

    print("Susunan yang terbentuk:")
    for i, susunan in enumerate(hasil, 1):
        print(f"{i:>5}. {' - '.join(susunan)}")

    print(f"\nVerifikasi brute force : {len(hasil)} susunan unik dari "
        f"{factorial(n)} permutasi biasa "
        f"({'COCOK' if len(hasil) == jumlah_rumus else 'TIDAK COCOK'})")

if __name__ == "__main__":
    main()