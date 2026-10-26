import itertools
import math

# Data studi kasus sederhana: Memilih Paket Makan Siang
MAKANAN = ["Nasi Goreng", "Mie Goreng"]             # Kelompok 1 (n1 = 2)
PILIHAN_MAKANAN = 1                                  # Dipilih r1 = 1 jenis

MINUMAN = ["Es Teh", "Es Jeruk", "Air Mineral"]      # Kelompok 2 (n2 = 3)
PILIHAN_MINUMAN = 1                                  # Dipilih r2 = 1 jenis

def kombinasi_tanpa_pengulangan(item, r):
    """
    Membangkitkan semua kombinasi tanpa pengulangan (combinations).
    Urutan tidak penting dan setiap item hanya boleh dipilih sekali.
    """
    return list(itertools.combinations(item, r))

def hitung_matematis(n, r):
    """
    Menghitung rumus kombinasi biasa:
    C(n, r) = n! / (r! * (n - r)!)
    """
    return math.comb(n, r)

def verifikasi(k1, r1, k2, r2, total_teoritis):
    """Cek apakah jumlah hasil iterasi perkalian kartesian sesuai dengan perhitungan rumus matematis."""
    res1 = list(itertools.combinations(k1, r1))
    res2 = list(itertools.combinations(k2, r2))
    total_cartesian = len(res1) * len(res2)
    return total_cartesian == total_teoritis

def tampilkan_studi_kasus():
    print("=" * 60)
    print("STUDI KASUS: PEMILIHAN PAKET MAKAN SIANG".center(60))
    print("=" * 60)
    print(f"1. Pilihan Makanan : {MAKANAN} (Dipilih {PILIHAN_MAKANAN})")
    print(f"2. Pilihan Minuman : {MINUMAN} (Dipilih {PILIHAN_MINUMAN})")
    print("Aturan: Masing-masing dipilih tanpa pengulangan, urutan tidak penting,")
    print("total variasi paket dihitung menggunakan Aturan Perkalian.\n")

def jalankan_modul():
    n1 = len(MAKANAN)
    r1 = PILIHAN_MAKANAN
    n2 = len(MINUMAN)
    r2 = PILIHAN_MINUMAN
    
    tampilkan_studi_kasus()
    
    # 1. Perhitungan matematis dengan aturan perkalian
    c1 = hitung_matematis(n1, r1)
    c2 = hitung_matematis(n2, r2)
    total_kombinasi = c1 * c2

    # Membangkitkan kombinasi per kelompok lalu dikalikan (Cartesian Product)
    hasil_1 = kombinasi_tanpa_pengulangan(MAKANAN, r1)
    hasil_2 = kombinasi_tanpa_pengulangan(MINUMAN, r2)
    semua_paket = list(itertools.product(hasil_1, hasil_2))

    print("=" * 60)
    print("HASIL".center(60))
    print("=" * 60)
    print(f"Kombinasi Makanan     : C({n1}, {r1}) = {c1} cara")
    print(f"Kombinasi Minuman     : C({n2}, {r2}) = {c2} cara")
    print(f"Rumus Aturan Perkalian: C({n1},{r1}) × C({n2},{r2}) = {c1} × {c2}")
    print(f"Perhitungan total paket: {total_kombinasi} kemungkinan paket")
    print(f"Total paket terdata   : {len(semua_paket)}\n")

    print("Daftar kombinasi paket yang terbentuk:")
    for i, paket in enumerate(semua_paket, 1):
        mkn, mnw = paket
        gabungan = list(mkn) + list(mnw)
        print(f"{i:>2}. Makanan: {list(mkn)} | Minuman: {list(mnw)} --> Paket: {gabungan}")

    # Verifikasi konsistensi hasil fungsi dan rumus matematis
    is_valid = verifikasi(MAKANAN, r1, MINUMAN, r2, total_kombinasi)
    print(f"\nVerifikasi perhitungan   : {total_kombinasi} kombinasi "
        f"({'COCOK' if is_valid else 'TIDAK COCOK'})")

if __name__ == "__main__":
    jalankan_modul()