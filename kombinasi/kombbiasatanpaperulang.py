import math
import time

def tampilkan_materi():
    print("\n" + "="*55)
    print(" 📖 MATERI: KOMBINASI BIASA TANPA PERULANGAN ")
    print("="*55)
    print("Kombinasi adalah cara memilih atau mengelompokkan objek ")
    print("tanpa memperhatikan urutan (AB sama dengan BA).")
    print("Tanpa perulangan berarti objek yang sudah dipilih tidak ")
    print("bisa dipilih kembali.")
    print("\nRumus Kombinasi:")
    print("C(n, r) = n! / (r! * (n - r)!)")
    print("\nKeterangan:")
    print("n = total objek keseluruhan yang tersedia")
    print("r = jumlah objek yang dipilih")
    print("! = faktorial (contoh: 3! = 3 x 2 x 1)")
    print("="*55)

def tampilkan_studi_kasus():
    print("\n" + "="*55)
    print(" 💡 STUDI KASUS ")
    print("="*55)
    print("Dalam sebuah tim, terdapat 5 orang programmer (n = 5).")
    print("Manajer IT ingin memilih 3 orang (r = 3) untuk ")
    print("mengerjakan proyek aplikasi baru.")
    print("\nPertanyaan:")
    print("Ada berapa banyak cara berbeda yang bisa dilakukan ")
    print("manajer untuk membentuk tim proyek tersebut?")
    print("="*55)

def tampilkan_jawaban():
    print("\n" + "="*55)
    print(" 📝 JAWABAN & PEMBAHASAN ")
    print("="*55)
    print("Diketahui:")
    print("n = 5 (total programmer)")
    print("r = 3 (programmer yang dipilih)")
    
    print("\nLangkah Penyelesaian:")
    print("C(5, 3) = 5! / (3! * (5 - 3)!)")
    print("C(5, 3) = 5! / (3! * 2!)")
    print("C(5, 3) = (5 x 4 x 3 x 2 x 1) / ((3 x 2 x 1) x (2 x 1))")
    print("C(5, 3) = 120 / (6 x 2)")
    print("C(5, 3) = 120 / 12")
    print("C(5, 3) = 10")
    
    # Membuktikan perhitungan menggunakan fungsi bawaan Python
    n = 5
    r = 3
    hasil = math.comb(n, r)
    
    print(f"\nKesimpulan:")
    print(f"Berdasarkan perhitungan, terdapat {hasil} cara/kombinasi berbeda")
    print("untuk memilih 3 programmer dari 5 programmer yang ada.")
    print("="*55 + "\n")

def jalankan_modul():
    tampilkan_materi()
    time.sleep(2) # Memberikan jeda waktu agar pengguna bisa membaca
    tampilkan_studi_kasus()
    time.sleep(2)
    tampilkan_jawaban()

if __name__ == "__main__":
    jalankan_modul()