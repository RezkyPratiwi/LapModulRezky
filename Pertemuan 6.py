# Pertemuan 6
# Funcion
def hitung_luas_persegi(sisi):
    hasil = sisi * sisi
    return hasil

print("Luas persegi: %d" % hitung_luas_persegi(10))

# Prosedur
def hitung_luas_segitiga(alas, tinggi):
    hasil = (alas * tinggi) / 2
    print("Luas segitiga: %f" % hasil)

hitung_luas_segitiga(10, 5)

# Fungsi untuk menghitung luas persegi
def hitung_luas(sisi):
    luas = sisi ** 2
    return luas

def hitung_keliling(sisi):
    keliling = 4 * sisi
    return keliling

sisi = int(input("Masukkan panjang sisi persegi: "))

luas = hitung_luas(sisi)
keliling = hitung_keliling(sisi)

print("Luas persegi dengan sisi", sisi, "adalah", luas)
print("Keliling persegi dengan sisi", sisi, "adalah", keliling)

# dengan method prosedur
def hitung_keliling_persegi(sisi):
    keliling = 4 * sisi
    print("Keliling persegi adalah: {}".format (keliling))

def hitung_luas_persegi(sisi):
    luas = sisi*sisi
    print("luas persegi adalah: {}".format (luas))

sisi = int(input ("Masukkan sisi: "))
hitung_keliling_persegi(sisi)
hitung_luas_persegi(sisi)


# Latihan 2
def perbandingan_bilangan(a, b):
    if a > b:
        print(f"{a} lebih besar dari {b}")
    elif a < b:
        print(f"{a} lebih kecil dari {b}")
    else:
        print("Bilangan a dan b sama besar")
bilangan_a = int(input("Masukkan bilangan 1: "))
bilangan_b = int(input("Masukkan bilangan 2: "))
perbandingan_bilangan(bilangan_a, bilangan_b)

# Tugas 1
def cek_ganjil_genap(bilangan):
    if bilangan % 2 == 0:
        print(f"Bilangan yang anda masukkan adalah genap")
    else:
        print(f"Bilangan yang anda masukkan adalah ganjil")

def angka():
    bil = int(input("Masukkan bilangan: "))
    cek_ganjil_genap(bil)

angka()

# Tugas 2
def hitung_luas_lingkaran(jari_jari):
    luas = 3.14 * jari_jari**2
    return luas

def hitung_keliling_lingkaran(jari_jari):
    keliling = 3.14 * jari_jari**2
    return keliling

def angka():
    jari_jari = int(input("Masukkan jari-jari: "))
    
    keliling = hitung_keliling_lingkaran(jari_jari)
    luas = hitung_luas_lingkaran(jari_jari)

    print("Luas lingkaran:", luas)
    print("Keliling lingkaran:", keliling)

angka()

# Tugas 3
print("==KALKULATOR==")
def penjumlahan(angka1, angka2):
    return angka1 + angka2

def pengurangan(angka1, angka2):
    return angka1 - angka2

def perkalian(angka1, angka2):
    return angka1 * angka2

def pembagian(angka1, angka2):
    return angka1 / angka2

def angka():
    while True:
        print("=== Kalkulator Sederhana ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan Anda (1-5): ")

        if pilihan == "5":
            print("Terima kasih! Program berakhir.")
            break

        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))

        if pilihan == "1":
            hasil = penjumlahan(angka1, angka2)
            operasi = "Penjumlahan"
        elif pilihan == "2":
            hasil = pengurangan(angka1, angka2)
            operasi = "Pengurangan"
        elif pilihan == "3":
            hasil = perkalian(angka1, angka2)
            operasi = "Perkalian"
        elif pilihan == "4":
            hasil = pembagian(angka1, angka2)
            operasi = "Pembagian"
        else:
            print("Pilihan tidak valid. Silakan pilih angka 1-5.")
            continue

        print(f"Hasil {operasi}: {hasil}\n")

angka()
