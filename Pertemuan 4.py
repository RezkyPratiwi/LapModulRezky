# Pertemuan 4
# Perulangan
for i in range(10):
    print("hallo world!")

# for range min/max
for i in range(1, 10):
    print(f"Perulangan ke- {i}")

# for range min/max step
for i in range(0, 20, 2):
    print(f"Step ke- {i}")
for i in range(20, 0, -2):
    print(i)

# Perulangan
i =0
while i <= 5:
    print("Hello World!")
    i +=1

# Perulangan Increment
a = 1
b = 10
while a < b:
    print("Step ke-", a)
    a +=1

# Perulangan decrement
a = 1
b = 10
while a < b:
    print("waktu anda sisa", a, "detik")
    a -=1

# Break dan Continue di For
# Break
for i in range(1, 10):
    print("Perulangan ke-", i)
    if i == 7:
        print("Perulangan ke-", i, "dihentikan")
        break
# Continue
for i in range(0, 10):
    if i == 5:
        continue

    print(i)

# Break dan Continue di While
# Break
a = 0
while True:
    print("step ke-", a, "!")
    a +=1
    if a == 7:
        print("step ke-", a, "dihetikan")
        break
# Continue
angka = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

i = -1
while i< len(angka):
    i +=1
    if i %2 ==0 and i > 0:
        print("skip")
        continue
    print(angka[i])

# Latihan 1
print ("LOGIN")
username = "RezkyPratiwi"
password = "rezky180104"
# variabel untuk menyimpan jumlah percobaan login
percobaan = 0

# tiga kali
while percobaan < 3:
    # meminta input dari user
    input_username = input("Masukkan username: ")
    input_password = input("Masukkan password: ")

    # cek apakah username dan password benar
    if input_username == username and input_password == password:
        print("Selamat datang!")
        break 
    else:
        print("Coba lagi.")
        percobaan += 1

# jika gagal login sebanyak tiga kali
if percobaan == 3:
    print("Gagal login.")

# Latihan 2
print("======MENCARI BILANGAN GENAP======")
max_range = int(input("Masukkan bilangan maksimal: "))
for i in range(1, max_range+1):
    if i % 2 == 0:
        print(i)

print("===PROGRAM MENCARI FPB")
bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))

faktor1 = []
faktor2 = []

for i in range(1, bil1+1):
    if bil1 % i == 0:
        faktor1.append(i)

for j in range(1, bil2+1):
    if bil2 % j == 0:
        faktor2.append(j)

# Latihan 3
FPB = []
for faktor in faktor1:
    if faktor in faktor2:
        FPB.append(faktor)
fpb = max(FPB)

print("FPB dari", bil1, "dan", bil2, "adalah", fpb)

# Tugas 1
print("===== PROGRAM MENGHITUNG  TOTAL BILANGAN =====")

total = 0
nilai=int(input("Masukkan bilangan: "))
print("Total Nilai =", end = ' ')  
while nilai >= 1:
    print(nilai, end = ' ')
    if 1 == nilai:
        print('=', end = ' ')
    else:
        print('+', end = ' ')
    total = total + nilai
    nilai = nilai - 1
print(total)

# Tugas 2
print("===== PROGRAM SEDERHANA MENGHITUNG PANGKAT =====")

nilai=int(input("Masukkan bilangan= "))
cacah=int(input("Masukkan pencacah= "))

hasil = 1

for i in range(cacah):
    hasil *= nilai
    
print("Hasil pangkat = {}".format(hasil))

# Tugas 3
print("====== PROGRAM SEDERHANA MENCARI KPK =====")

bil=int(input("Masukkan bilangan pertama = "))
bil2=int(input("Masukkan bilangan kedua= "))

if bil > bil2:
    bilangan_terbesar = bil
else:
    bilangan_terbesar = bil2
    
while True:
    if bilangan_terbesar % bil == 0 and bilangan_terbesar % bil2 == 0:
        kpk = bilangan_terbesar
        break
    bilangan_terbesar += 1
    
print("KPK = {}".format(kpk))

