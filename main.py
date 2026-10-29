import os
from kombinasi import (tanpa_perulangan, dengan_batasan, 
                        aturan_perkalian, metode_komplement, 
                        teori_graf, dengan_perulangan)
from permutasi import (dengan_perulangan, unsur_berdampingan, 
                    unsur_identik, melingkar, 
                    n_objek_berbeda, r_dari_n_objek)
import time

def bersihkan_layar():
    os.system('cls' if os.name == 'nt' else 'clear')

def tekanEnter():
    input("\nTekan Enter untuk melanjutkan...")

def menu_permutasi():
    while True:
        bersihkan_layar()
        print("\n=== Menu Belajar Permutasi ===")
        print("1. Permutasi dengan perulangan")
        print("2. Permutasi dengan unsur berdampingan")
        print("3. Permutasi dengan unsur identik")
        print("4. Permutasi melingkar")
        print("5. Permutasi n objek berbeda")
        print("6. Permutasi r dari n objek")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input("Pilih materi (0-6): ")
        bersihkan_layar()
        
        if pilihan == '0':
            break
        elif pilihan == '1':
            dengan_perulangan.jalankan_modul()
            tekanEnter()
        elif pilihan == '2':
            unsur_berdampingan.jalankan_modul()
            tekanEnter()   
        elif pilihan == '3':
            unsur_identik.jalankan_modul()
            tekanEnter()
        elif pilihan == '4':
            melingkar.jalankan_modul()
            tekanEnter()
        elif pilihan == '5':
            n_objek_berbeda.jalankan_modul()
            tekanEnter()    
        elif pilihan == '6':
            r_dari_n_objek.jalankan_modul()
            tekanEnter()
        else:
            print("Pilihan tidak valid.")
            tekanEnter()

def menu_kombinasi():
    while True:
        bersihkan_layar()
        print("\n=== Menu Belajar Kombinasi ===")
        print("1. Kombinasi biasa tanpa perulangan")
        print("2. Kombinasi dengan batasan")
        print("3. Kombinasi biasa aturan perkalian")
        print("4. Kombinasi biasa metode komplemen")
        print("5. Kombinasi biasa teori graf")
        print("6. Kombinasi dengan perulangan")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input("Pilih materi (0-6): ")
        
        if pilihan == '0':
            break
        elif pilihan == '1':
            tanpa_perulangan.jalankan_modul()
            tekanEnter()
        elif pilihan == '2':
            dengan_batasan.jalankan_modul()
            tekanEnter()
        elif pilihan == '3':
            aturan_perkalian.jalankan_modul()
            tekanEnter()
        elif pilihan == '4':
            metode_komplement.jalankan_modul()
            tekanEnter()
        elif pilihan == '5':
            teori_graf.jalankan_modul()
            tekanEnter()
        elif pilihan == '6':
            dengan_perulangan.jalankan_modul()
            tekanEnter()
        else:
            print("Pilihan tidak valid.")

def main():
    while True:
        bersihkan_layar()
        print("\n" + "="*35)
        print("   PROGRAM BELAJAR MATEMATIKA   ")
        print("="*35)
        print("1. Mau Belajar Permutasi?")
        print("2. Mau Belajar Kombinasi?")
        print("0. Keluar")
        
        pilihan = input("\nMasukkan pilihan Anda (0/1/2): ")
        bersihkan_layar()
        
        if pilihan == '1':
            menu_permutasi()
        elif pilihan == '2':
            menu_kombinasi()
        elif pilihan == '0':
            print("Terima kasih telah belajar hari ini!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()