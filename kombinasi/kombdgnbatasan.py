import math
import time

def tampilkan_materi():
    print("\n" + "="*55)
    print(" 📖 MATERI: KOMBINASI DENGAN BATASAN (SYARAT) ")
    print("="*55)
    print("Kombinasi dengan batasan adalah penyusunan objek yang")
    print("memiliki syarat tertentu yang harus dipenuhi.")
    print("Misalnya: objek tertentu harus ikut, tidak boleh ikut,")
    print("atau harus memenuhi kuota/komposisi dari beberapa kelompok.")
    print("\nPrinsip Penyelesaian:")
    print("Selesaikan setiap syarat batasannya terlebih dahulu")
    print("menggunakan kombinasi, lalu kalikan antar hasil tersebut")
    print("jika kejadian saling berkaitan (Aturan Perkalian).")
    print("="*55)

def tampilkan_studi_kasus():
    print("\n" + "="*55)
    print(" 💡 STUDI KASUS ")
    print("="*55)
    print("Sebuah divisi IT memiliki 6 programmer dan 4 desainer.")
    print("Manajer ingin membentuk tim khusus berisi 4 orang.")
    print("\nSyarat Batasan:")
    print("Tim tersebut harus terdiri dari tepat 2 programmer")
    print("dan 2 desainer.")
    print("\nPertanyaan:")
    print("Ada berapa banyak cara susunan tim yang bisa dibentuk?")
    print("="*55)

def tampilkan_jawaban():
    print("\n" + "="*55)
    print(" 📝 JAWABAN & PEMBAHASAN ")
    print("="*55)
    print("Langkah 1: Memilih 2 programmer dari total 6 programmer")
    print("C(6, 2) = 6! / (2! * (6-2)!) = 15 cara")
    print("\nLangkah 2: Memilih 2 desainer dari total 4 desainer")
    print("C(4, 2) = 4! / (2! * (4-2)!) = 6 cara")
    print("\nLangkah 3: Mengalikan kedua hasil (Aturan Perkalian)")
    print("Total susunan = 15 x 6 = 90 susunan")
    
    # Membuktikan perhitungan menggunakan fungsi bawaan Python
    programmer = math.comb(6, 2)
    desainer = math.comb(4, 2)
    total_susunan = programmer * desainer
    
    print(f"\nKesimpulan:")
    print(f"Secara perhitungan sistem: {programmer} x {desainer} = {total_susunan}")
    print(f"Terdapat {total_susunan} cara berbeda untuk membentuk tim tersebut.")
    print("="*55 + "\n")

def jalankan_modul():
    tampilkan_materi()
    time.sleep(2)
    tampilkan_studi_kasus()
    time.sleep(2)
    tampilkan_jawaban()

if __name__ == "__main__":
    jalankan_modul()