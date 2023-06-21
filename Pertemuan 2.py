# Pertemuan2
# fungsi print
belajar = "Halo, hari ini kita belajar python"
print(belajar)

# menggunakan+
dina = "batu"
nita = "beling"
kiky = "mie"
print("makanan favorit dina.{}". format(dina))
# menggunakan f-string
print(f"makanan favorit ={kiky}")

# Menggabungkan text dan variabel menggunakan tanda koma(,) 
panjang = 20
lebar = 5
luas = panjang * lebar
print("luas", luas)

# INPUT STRING
nama = input("Nama: ")
nim = input("NIM: ")
print("Nama Lengkap: " + nama)
print("NIM: " + nim)

# INPUT INTEGER
panjang = int(input("PANJANG: "))
lebar = int(input("LEBAR: "))
luas = panjang * lebar
print("Luas Persegi Panjang:", luas)

# tugas 1
print("Biodata Diri")
nama = "Rezky Pratiwi"
print("Nama Lengkap:" + nama)
nim = "2211104029"
print("NIM:" + nim)
kelas = "SE06A"
print("Kelas:" + kelas)
TTL = "Sengkang, 18 Januari 2004"
print("TTL:" + TTL)
alamat = "Jl.Raya Gn.Tugel"
print("Alamat:" + alamat)
nomor_hp = "085342575424"
print("Nomor Hp:" + nomor_hp)
prodi = "Software Engineering"
print("Prodi:" + prodi)
hobi = "Menyanyi"
print("Hobi:" + hobi)

# Tugas 2
print("Balok")
panjang = int(input("Masukkan panjang balok: "))
lebar = int(input("Masukkan lebar balok: "))
tinggi = int(input("Masukkan tinggi balok: "))
volume = panjang * lebar * tinggi
print("Volume balok adalah:", volume)

print("Kubus")
sisi = int(input("Masukkan panjang sisi kubus: "))
volume = sisi * 3
print("Volume kubus adalah:", volume)
