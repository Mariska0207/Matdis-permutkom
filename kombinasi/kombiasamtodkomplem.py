import math
import time

def tampilkan_materi():
    print("\n" + "="*55)
    print(" 📖 MATERI: KOMBINASI METODE KOMPLEMEN ")
    print("="*55)
    print("Metode komplemen digunakan untuk mempersingkat perhitungan")
    print("saat syarat memiliki banyak skenario cabang, khususnya")
    print("pada soal dengan kata kunci 'minimal' atau 'paling sedikit'.")
    print("\nPrinsip Penyelesaian:")
    print("Alih-alih menghitung satu per satu skenario yang diminta,")
    print("Anda cukup mengurangkan Total Seluruh Kemungkinan dengan")
    print("kemungkinan yang TIDAK diinginkan (lawan/komplemen).")
    print("="*55)

def tampilkan_studi_kasus():
    print("\n" + "="*55)
    print(" 💡 STUDI KASUS ")
    print("="*55)
    print("Dalam sebuah kelompok terdapat 7 pria dan 4 wanita.")
    print("Anda diminta memilih 3 orang perwakilan dari kelompok itu.")
    print("\nSyarat Batasan:")
    print("Tim perwakilan harus berisi minimal 1 wanita.")
    print("\nPertanyaan:")
    print("Ada berapa banyak cara memilih perwakilan tersebut?")
    print("="*55)

def tampilkan_jawaban():
    print("\n" + "="*55)
    print(" 📝 JAWABAN & PEMBAHASAN ")
    print("="*55)
    print("Langkah 1: Menghitung total seluruh kemungkinan tanpa syarat")
    print("Memilih 3 orang dari total 11 orang (7 pria + 4 wanita)")
    print("C(11, 3) = 11! / (3! * (11-3)!) = 165 cara")
    print("\nLangkah 2: Menghitung kejadian yang TIDAK diinginkan (Komplemen)")
    print("Lawan dari 'minimal 1 wanita' adalah 'TIDAK ADA WANITA' (Semua Pria)")
    print("Memilih 3 pria dari total 7 pria")
    print("C(7, 3) = 7! / (3! * (7-3)!) = 35 cara")
    print("\nLangkah 3: Kurangkan Total dengan Komplemen")
    print("Total susunan = 165 - 35 = 130 cara")
    
    # Membuktikan perhitungan menggunakan fungsi bawaan Python
    total_kemungkinan = math.comb(11, 3)
    komplemen = math.comb(7, 3)
    hasil_akhir = total_kemungkinan - komplemen
    
    print(f"\nKesimpulan:")
    print(f"Secara perhitungan sistem: {total_kemungkinan} - {komplemen} = {hasil_akhir}")
    print(f"Terdapat {hasil_akhir} cara untuk memilih minimal 1 wanita.")
    print("="*55 + "\n")

def jalankan_modul():
    tampilkan_materi()
    time.sleep(2)
    tampilkan_studi_kasus()
    time.sleep(2)
    tampilkan_jawaban()

if __name__ == "__main__":
    jalankan_modul()