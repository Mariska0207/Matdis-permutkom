from itertools import permutations
from math import factorial

print("STUDI KASUS: Pemilihan Pengurus\n")
print("Dari n calon akan dipilih r orang untuk menduduki r jabatan yang berbeda.")
print("Berapa banyak susunan pengurus yang mungkin?\n")

n = int(input("Banyaknya calon (n): "))
r = int(input("Banyaknya jabatan (r): "))
while r > n:
    r = int(input("r tidak boleh lebih besar dari n. Banyaknya jabatan (r): "))

calon = [input(f"Nama calon ke-{i}: ").strip() or f"Calon {i}" for i in range(1, n + 1)]
jabatan = [input(f"Nama jabatan ke-{i}: ").strip() or f"Jabatan {i}" for i in range(1, r + 1)]

total = factorial(n) // factorial(n - r)  # P(n,r) = n! / (n-r)!
sisa = n - r
uraian_n = " x ".join(str(i) for i in range(n, 0, -1))
uraian_sisa = " x ".join(str(i) for i in range(sisa, 0, -1)) or "1"
awal = f"P({n},{r})"

print("\nRumus:")
print("P(n,r) = n! / (n - r)!")

print("\nPenyelesaian:")
print(f"{awal} = {n}! / ({n} - {r})!")
print(f"{' ' * len(awal)} = {n}! / {sisa}!")
print(f"{' ' * len(awal)} = ({uraian_n}) / ({uraian_sisa})")
print(f"{' ' * len(awal)} = {factorial(n)} / {factorial(sisa)}")
print(f"{' ' * len(awal)} = {total}")

print(f"\nBanyak permutasi: {total}\n")

print("Daftar susunan:")
for i, susunan in enumerate(permutations(calon, r), start=1):
    print(f"{i}. " + ", ".join(f"{j}: {o}" for j, o in zip(jabatan, susunan)))

print(f"\nJadi, ada {total} susunan pengurus dari {n} calon untuk {r} jabatan.")