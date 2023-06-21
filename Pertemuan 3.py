# Pertemuan 3
# If satu kondisi
nilai= int(input("masukkan bilangan bulat:"))
if(nilai>0):
    print("bilangan",nilai, "merupakan bilangan bulat")

# if dua kondisi
nilai = int(input("masukkan bilangan:"))
if(nilai %2 == 0):
    print("Bilangan",nilai, "merupakan bilangan genap")

# if tiga kondisi
nilai = int(input("Masukkan bilangan bulat:"))
if (nilai > 0):
    print("bilangan", nilai, "merupakan bilangan positif")
elif (nilai < 0): 
    print("Bilangan", nilai, "merupakan bilangan negatif")
else:
    print("Bilangan nol")

# Suhu
suhu = int(input("Masukkan suhu air: "))
if suhu <= 0:
    print("padat")
elif suhu < 100:
    print("cair")
else:
    print("uap")

# STATUS
gender = input("Perempuan atau laki-laki ? (L/P): ")
if(gender == 'L'):
    status = input("Anda sudah menikah atau belum? (Y/N): ")
    if(status == 'Y'):
        print("Hallo Bapak!")
    elif(status == 'N'):
        print("Hallo Mas!")
    else:
        print("Tidak ada dalam pilihan")
elif(gender == 'P'):
    status = input("Anda sudah menikah atau belum? (Y/N): ")
    if(status == 'Y'):
        print("Hallo Ibu!")
    elif(status == 'N'):
        print ("Halo Mba!")
    else:
        print("Tidak ada dalam pilihan")
else:
    print("Tidak ada dalam pilihan")

# data diri
print("===========INPUT==========")
nama = input("Nama: ")
jk = input("Jenis Kelamin (L/P): ")
agama = int(input("Agama: "))
if(agama==1):
    agama = "Islam"
elif(agama==2):
    agama = "Protestan"
elif(agama==3):
    agama = "Katolik"
elif(agama==4):
    agama = "Hindu"
elif(agama==5):
    agama = "Budha"
else:
    agama = "Agama tidak ditemukan"
print("==========OUTPUT========")

# Tugas 1 huruf vokal
user = input("Masukkan sebuah huruf: ")
if user.isalpha():
    if user.lower() in ['a', 'i', 'u', 'e', 'o']:
        print("Huruf vokal")
    else:
        print("Huruf konsonan")
else:
    print("Inputan bukan huruf")

# Tugas 2 validasi nilai
nilai_bilangan = int(input("Masukkan sebuah bilangan: "))
nilai_pembagi = int(input("Masukkan nilai pembagi: "))
if (nilai_pembagi == 0):
    print("nilai pembagi tidak boleh 0")
else:
    print(nilai_bilangan / nilai_pembagi)