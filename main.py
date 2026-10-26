import os
from kombinasi import (kombbiasatanpaperulang, 
                        kombdgnbatasan, 
                        kombiasaaturanperk, 
                        kombiasamtodkomplem, 
                        kombiasateorigraf, 
                        komdgnperulang)
from permutasi import (permdgnperulangan, 
                    permdgnunsurberdampingan, 
                    permdgnunsuridentik, 
                    permmelingkar, 
                    permnobjekberbeda, 
                    permrdarinobjek)
import time


def tekanEnter():
    input("\nTekan Enter untuk melanjutkan...")

def menu_permutasi():
    while True:
        print("\n=== Menu Belajar Permutasi ===")
        print("1. Permutasi dengan perulangan (permdgnperulangan.py)")
        print("2. Permutasi dengan unsur berdampingan (permdgnunsurberdampingan.py)")
        print("3. Permutasi dengan unsur identik (permdgnunsuridentik.py)")
        print("4. Permutasi melingkar (permmelingkar.py)")
        print("5. Permutasi n objek berbeda (permnobjekberbeda.py)")
        print("6. Permutasi r dari n objek (permrdarinobjek.py)")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input("Pilih materi (0-6): ")
        
        if pilihan == '0':
            break
        elif pilihan == '1':
            permdgnperulangan.jalankan_modul()
            tekanEnter()
        elif pilihan == '2':
            permdgnunsurberdampingan.jalankan_modul()
            tekanEnter()   
        elif pilihan == '3':
            permdgnunsuridentik.jalankan_modul()
            tekanEnter()
        elif pilihan == '4':
            permmelingkar.jalankan_modul()
            tekanEnter()
        elif pilihan == '5':
            permnobjekberbeda.jalankan_modul()
            tekanEnter()    
        elif pilihan == '6':
            permrdarinobjek.jalankan_modul()
            tekanEnter()
        else:
            print("Pilihan tidak valid.")
            tekanEnter()

def menu_kombinasi():
    while True:
        print("\n=== Menu Belajar Kombinasi ===")
        print("1. Kombinasi biasa tanpa perulangan (kombbiasatanpaperulang.py)")
        print("2. Kombinasi dengan batasan (kombdgnbatasan.py)")
        print("3. Kombinasi biasa aturan perkalian (kombiasaaturanperk.py)")
        print("4. Kombinasi biasa metode komplemen (kombiasamtodkomplem.py)")
        print("5. Kombinasi biasa teori graf (kombiasateorigraf.py)")
        print("6. Kombinasi dengan perulangan (komdgnperulang.py)")
        print("0. Kembali ke Menu Utama")
        
        pilihan = input("Pilih materi (0-6): ")
        
        if pilihan == '0':
            break
        elif pilihan == '1':
            kombbiasatanpaperulang.jalankan_modul()
            tekanEnter()
        elif pilihan == '2':
            kombdgnbatasan.jalankan_modul()
            tekanEnter()
        elif pilihan == '3':
            kombiasaaturanperk.jalankan_modul()
            tekanEnter()
        elif pilihan == '4':
            kombiasamtodkomplem.jalankan_modul()
            tekanEnter()
        elif pilihan == '5':
            kombiasateorigraf.jalankan_modul()
            tekanEnter()
        elif pilihan == '6':
            komdgnperulang.jalankan_modul()
            tekanEnter()
        else:
            print("Pilihan tidak valid.")

def main():
    while True:
        print("\n" + "="*35)
        print("   PROGRAM BELAJAR MATEMATIKA   ")
        print("="*35)
        print("1. Mau Belajar Permutasi?")
        print("2. Mau Belajar Kombinasi?")
        print("0. Keluar")
        
        pilihan = input("\nMasukkan pilihan Anda (0/1/2): ")
        
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