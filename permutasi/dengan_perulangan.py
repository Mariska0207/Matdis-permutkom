from itertools import permutations

def tampilkan_cerita():
    print("====================================================================")
    print("STUDI: PIN LOGIN SISTEM 'STAR UNMUL'")
    print("Jenis: PERMUTASI DENGAN PENGULANGAN dengan rumus: n pangkat r")
    print("====================================================================")
    print("Cerita:")
    print("Sistem login kampus memakai PIN. Digit BOLEH SAMA (contoh: 112, 777).")
    print("Berapa banyak PIN yang mungkin? Seperti apa semua PIN-nya?")
    print("")
    print("Keterangan rumus n^r:")
    print("   n = banyak digit yang tersedia")
    print("   r = panjang PIN")
    print("=====================================================================")

def langkah_1(digit, n, panjang):
    print("")
    print("Langkah 1 - Digit yang tersedia:", " ".join(digit))
    print("Digit boleh dipakai berulang, jadi tiap posisi punya", n, "pilihan:")
    for posisi in range(1, panjang + 1):
        print("   Posisi", posisi, ":", n, "pilihan")

def langkah_2(n, panjang, total):
    print("")
    print("Langkah 2 - Rumus n^r =", n, "^", panjang)
    perkalian = ""
    for posisi in range(panjang):
        perkalian = perkalian + str(n)
        if posisi < panjang - 1:
            perkalian = perkalian + " x "
    print("  ", perkalian, "=", total, "PIN")

def buat_semua_pin(digit, panjang):
    daftar_digit = digit * panjang

    urutan_unik = set(permutations(daftar_digit, panjang))

    semua_pin = []
    for susunan in urutan_unik:
        pin = "".join(susunan)
        semua_pin.append(pin)

    semua_pin.sort()
    return semua_pin

def langkah_3(digit, semua_pin, total):
    print("")
    print("Langkah 3 - Semua", total, "PIN yang terbentuk:")

    for d in digit:
        print("")
        print("PIN yang diawali", d, ":")

        baris = ""
        hitung = 0

        for pin in semua_pin:
            if pin[0] == d:
                baris = baris + pin + "  "
                hitung = hitung + 1
                if hitung == 10:
                    print("   ", baris)
                    baris = ""
                    hitung = 0

        if baris != "":
            print("   ", baris)

def jalankan_modul():
    terbesar = 2
    panjang = 3

    n = terbesar + 1
    total = n ** panjang

    digit = []
    for angka in range(n):
        digit.append(str(angka))

    tampilkan_cerita()
    langkah_1(digit, n, panjang)
    langkah_2(n, panjang, total)
    semua_pin = buat_semua_pin(digit, panjang)
    langkah_3(digit, semua_pin, total)

if __name__ == "__main__":
    jalankan_modul()