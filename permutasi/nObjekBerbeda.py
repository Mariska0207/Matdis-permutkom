from itertools import permutations
from math import factorial

print("STUDI KASUS: Susunan Foto Mahasiswa\n")
print("Sebanyak n mahasiswa akan berfoto berjajar dalam satu baris.")
print("Berapa banyak susunan berdiri yang mungkin?\n")

n = int(input("Banyaknya mahasiswa (n): "))
mahasiswa = [input(f"Nama mahasiswa ke-{i}: ").strip() or f"Mahasiswa {i}" for i in range(1, n + 1)]

total = factorial(n)  # P(n) = n!
uraian = " x ".join(str(i) for i in range(n, 0, -1)) or "1"
awal = f"P({n})"

print("\nRumus:")
print("P(n) = n!")

print("\nPenyelesaian:")
print(f"{awal} = {n}!")
print(f"{' ' * len(awal)} = {uraian}")
print(f"{' ' * len(awal)} = {total}")

print(f"\nBanyak permutasi: {total}\n")

print("Daftar susunan:")
for i, susunan in enumerate(permutations(mahasiswa), start=1):
    print(f"{i}. " + " - ".join(susunan))

print(f"\nJadi, ada {total} susunan berbeda untuk {n} mahasiswa.")