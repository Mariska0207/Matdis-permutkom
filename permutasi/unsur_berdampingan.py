from itertools import permutations
from math import factorial

# Data studi kasus (ubah di sini kalau ingin ganti buku)
SEMUA_BUKU = ["Matematika", "Fisika", "Kimia", "Biologi"]
BERDAMPINGAN = ["Matematika", "Fisika"]

def permutasi_berdampingan(semua, berdampingan):
    lainnya = [x for x in semua if x not in berdampingan]
    unit = [None] + lainnya          # None = penanda blok
    hasil = []

    for susunan in permutations(unit):                 # susun blok + buku lain
        for dalam in permutations(berdampingan):       # urutan di dalam blok
            blok = "[" + " - ".join(dalam) + "]"
            hasil.append([blok if u is None else u for u in susunan])
    return hasil

def verifikasi(semua, berdampingan):
    """Cek semua permutasi biasa, hitung yang unsurnya berdampingan."""
    jumlah = 0
    for p in permutations(semua):
        posisi = sorted(p.index(x) for x in berdampingan)
        if posisi[-1] - posisi[0] == len(berdampingan) - 1:
            jumlah += 1
    return jumlah

def tampilkan_studi_kasus():
    print("=" * 55)
    print("STUDI KASUS: BUKU DI RAK".center(55))
    print("=" * 55)
    print(f"Seorang pustakawan menata {len(SEMUA_BUKU)} buku berbeda")
    print(f"({', '.join(SEMUA_BUKU)}) berjajar di sebuah rak.")
    print(f"Buku {' dan '.join(BERDAMPINGAN)} adalah satu paket,")
    print("sehingga harus diletakkan berdampingan.")
    print("Berapa banyak susunan berbeda yang bisa dibuat?\n")

def jalankan_modul():
    n = len(SEMUA_BUKU)
    k = len(BERDAMPINGAN)
    unit = n - k + 1                 # jumlah unit setelah blok dibentuk

    tampilkan_studi_kasus()
    hasil = permutasi_berdampingan(SEMUA_BUKU, BERDAMPINGAN)

    print("=" * 55)
    print("HASIL".center(55))
    print("=" * 55)
    print(f"Jumlah buku (n)        : {n}")
    print(f"Buku berdampingan (k)  : {k} ({', '.join(BERDAMPINGAN)})")
    print(f"Jumlah unit            : {unit} (1 blok + {n - k} buku lain)")
    print(f"Rumus                  : {unit}! x {k}!")
    print(f"Perhitungan            : {factorial(unit)} x {factorial(k)} = {factorial(unit) * factorial(k)}")
    print(f"Jumlah susunan         : {len(hasil)}\n")

    print("Susunan yang terbentuk ([ ] = blok berdampingan):")
    for i, susunan in enumerate(hasil, 1):
        print(f"{i:>5}. {' - '.join(susunan)}")

    cek = verifikasi(SEMUA_BUKU, BERDAMPINGAN)
    print(f"\nVerifikasi brute force : {cek} susunan "
        f"({'COCOK' if cek == len(hasil) else 'TIDAK COCOK'})")

if __name__ == "__main__":
    jalankan_modul()