import itertools
import math

# Data studi kasus (ubah di sini jika ingin mengganti item atau jumlah pilihan)
ITEM_TERSEDIA = ["Kopi", "Teh", "Susu"]
JUMLAH_PILIHAN = 3  # r = jumlah item yang dipilih

def kombinasi_dengan_pengulangan(item, r):
    """
    Membangkitkan semua kombinasi dengan pengulangan (combinations_with_replacement).
    Setiap item boleh dipilih lebih dari sekali, dan urutan tidak penting.
    """
    return list(itertools.combinations_with_replacement(item, r))

def hitung_matematis(n, r):
    """
    Menghitung rumus kombinasi dengan pengulangan:
    C(n + r - 1, r) = (n + r - 1)! / (r! * (n - 1)!)
    """
    return math.comb(n + r - 1, r)

def verifikasi(item, r, total_teoritis):
    """Cek apakah jumlah hasil iterasi sesuai dengan perhitungan rumus matematis."""
    hasil = list(itertools.combinations_with_replacement(item, r))
    return len(hasil) == total_teoritis

def tampilkan_studi_kasus():
    print("=" * 60)
    print("STUDI KASUS: PEMESANAN MINUMAN DI KAFE".center(60))
    print("=" * 60)
    print(f"Sebuah kafe menyediakan {len(ITEM_TERSEDIA)} jenis minuman berbeda")
    print(f"({', '.join(ITEM_TERSEDIA)}) untuk dipilih oleh pelanggan.")
    print(f"Seorang pelanggan memesan total {JUMLAH_PILIHAN} gelas minuman.")
    print("Karena stok melimpah, pelanggan boleh memilih jenis minuman")
    print("yang sama berulang kali (misal: 3 gelas Kopi sekaligus).")
    print("Berapa banyak kombinasi pesanan berbeda yang bisa dibuat?\n")

def jalankan_modul():
    n = len(ITEM_TERSEDIA)
    r = JUMLAH_PILIHAN
    
    tampilkan_studi_kasus()
    
    # 1. Perhitungan matematis
    total_kombinasi = hitung_matematis(n, r)
    hasil = kombinasi_dengan_pengulangan(ITEM_TERSEDIA, r)

    print("=" * 60)
    print("HASIL".center(60))
    print("=" * 60)
    print(f"Jumlah jenis item (n)    : {n} ({', '.join(ITEM_TERSEDIA)})")
    print(f"Jumlah yang dipilih (r)  : {r}")
    print(f"Rumus                    : C(n + r - 1, r) = C({n} + {r} - 1, {r}) = C({n + r - 1}, {r})")
    print(f"Perhitungan faktorial    : C({n + r - 1}, {r}) = {total_kombinasi} cara")
    print(f"Total kombinasi terdata  : {len(hasil)}\n")

    print("Daftar kombinasi pesanan yang terbentuk:")
    for i, kombo in enumerate(hasil, 1):
        print(f"{i:>5}. {list(kombo)}")

    # Verifikasi konsistensi hasil fungsi dan rumus matematis
    is_valid = verifikasi(ITEM_TERSEDIA, r, total_kombinasi)
    print(f"\nVerifikasi perhitungan   : {total_kombinasi} kombinasi "
        f"({'COCOK' if is_valid else 'TIDAK COCOK'})")

if __name__ == "__main__":
    jalankan_modul()