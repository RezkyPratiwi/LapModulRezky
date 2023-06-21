# Pertemuan 5
# inisialisasi variabel berformat array
angka = [1, 2, 3, 4]
text = ["Satu", "Dua", "Tiga", "Empat"]

# Menampilkan nilai
buah = ["Apel", "Jeruk", "Anggur", "Pisang"]
nilai = buah[1]
print(nilai)

# Merubah
buah = [["apel", "jeruk", "jambu", "anggur"], ["nanas", "melon", "subak", "durian"]]

for i in range(len(buah)):
    for j in range(len(buah[i])):
        print(buah[i][j])

# Mengetahui Panjang
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
text = ["Satu", "Dua", "Tiga", "Empat"]

panjang = len(text)
print(panjang)

# Looping
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
text = ["Satu", "Dua", "Tiga", "Empat"]

for i in text:
    print(i)

# Menambah
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
text = ["Satu", "Dua", "Tiga", "Empat"]

text.append("Lima")
print(text)

# Remove
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
text = ["Satu", "Dua", "Tiga", "Empat"]

text.remove("Dua")
print(text)
angka.pop(2)
print(angka)

# Array 1 dimensi
text = ["Satu", "Dua", "Tiga", "Empat"]
for i in text:
    print(i)

# Array 2 Dimensi
buah = [["apel", "jeruk", "jambu", "anggur"], ["nanas", "melon", "subak", "durian"]]

for i in range(len(buah)):
    for j in range(len(buah[i])):
        print(buah[i][j])

# bilangan genap dari 1-10 dari data array.
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in angka:
    if i % 2 == 0:
        print(i)

# Latihan 1
array = []

data = int(input("Jumlah Pesan: "))

for i in range(data):
    Pesan = (input('Masukkan Pesan: '))
    array.append(Pesan)

print()
cari_pesan = input('pesan yang dicari: ')

for i in range(data):
    if(array[i] == cari_pesan):
        print(cari_pesan, 'ditemukan pada indeks ke-', i)
        break

    if(i+1 == data):
        print('Pesan tidak ditemukan')

# Latihan 2
nilai = []

for i in range(3):
    nilai.append(float(input("Masukkan nilai ke-{}: ".format(i + 1))))

total_nilai = sum(nilai)
rerata = total_nilai / len(nilai)

predikat = ""

if 100 > rerata >= 90:
    predikat = "A"
elif 90 > rerata >= 70:
    predikat = "B"
elif 70 > rerata >= 50:
    predikat = "C"
elif 50 > rerata >= 30:
    predikat = "D"
elif 30 > rerata >= 0:
    predikat = "E"
else:
    predikat = "Tidak valid"

print("Nilai rerata: {:.2f}".format(rerata))
print("Predikat: ", predikat)
