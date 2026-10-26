import itertools
import math

# Data studi kasus Teori Graf: Himpunan simpul (vertex) dari sebuah jaringan komputer sederhana
HIMPUNAN_SIMpul = ["A", "B", "C", "D"]  # Total n = 4 simpul
JUMLAH_SIMpul_SISI = 2                   # r = 2 simpul untuk membentuk satu sisi (edge)

def kombinasi_tanpa_pengulangan(item, r):
    """
    Membangkitkan semua kombinasi tanpa pengulangan (combinations).
    Urutan tidak penting dan setiap item hanya boleh dipilih sekali.
    """
    return list(itertools.combinations(item, r))

def hitung_matematis(n, r):
    """
    Menghitung rumus kombinasi biasa untuk menentukan jumlah maksimum sisi graf:
    C(n, r) = n! / (r! * (n - r)!)
    """
    return math.comb(n, r)

def verifikasi(item, r, total_teoritis):
    """Cek apakah jumlah hasil iterasi sesuai dengan perhitungan rumus matematis."""
    hasil = list(itertools.combinations(item, r))
    return len(hasil) == total_teoritis

def tampilkan_studi_kasus():
    print("=" * 65)
    print("STUDI KASUS: PEMBENTUKAN SISI (EDGE) PADA GRAF (TEORI GRAF)".center(65))
    print("=" * 65)
    print(f"Sebuah graf tak berarah memiliki himpunan simpul V = {HIMPUNAN_SIMpul}")
    print(f"dengan total {len(HIMPUNAN_SIMpul)} simpul (n).")
    print(f"Setiap sisi (edge) menghubungkan tepat r = {JUMLAH_SIMpul_SISI} simpul yang berbeda.")
    print("Aturan: Tanpa pengulangan, urutan simpul tidak penting (Sisi A-B = B-A),\n"
        "serta tidak ada sisi ke diri sendiri (loop).\n")

def jalankan_modul():
    n = len(HIMPUNAN_SIMpul)
    r = JUMLAH_SIMpul_SISI
    
    tampilkan_studi_kasus()
    
    # 1. Perhitungan matematis kombinasi graf
    total_kombinasi = hitung_matematis(n, r)
    hasil = kombinasi_tanpa_pengulangan(HIMPUNAN_SIMpul, r)

    print("=" * 65)
    print("HASIL".center(65))
    print("=" * 65)
    print(f"Jumlah simpul (n)        : {n} ({', '.join(HIMPUNAN_SIMpul)})")
    print(f"Simpul per sisi (r)      : {r}")
    print(f"Rumus Kombinasi C(n, r)  : C({n}, {r}) = {n}! / ({r}! * ({n} - {r})!)")
    print(f"Perhitungan total sisi   : {total_kombinasi} buah sisi")
    print(f"Total sisi terdata       : {len(hasil)}\n")

    print("Daftar kombinasi sisi (pasangan simpul) yang terbentuk:")
    for i, sisi in enumerate(hasil, 1):
        print(f"{i:>2}. Sisi menghubungkan simpul: {list(sisi)} --> [Edge {sisi[0]}-{sisi[1]}]")

    # Verifikasi konsistensi hasil fungsi dan rumus matematis
    is_valid = verifikasi(HIMPUNAN_SIMpul, r, total_kombinasi)
    print(f"\nVerifikasi perhitungan   : {total_kombinasi} kombinasi "
        f"({'COCOK' if is_valid else 'TIDAK COCOK'})")

if __name__ == "__main__":
    jalankan_modul()