# Pertemuan 7
# Sorting
import timeit
print("Ascending")
print(" ")

# Insertion Sort
def insertion_sorting(array) :
    start = timeit.default_timer()
    for i in range(1, len(array)) :
        item = array [i]
        j = i - 1

        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item

    stop = timeit.default_timer()
    print(f"Insertcion sort successfull Elapsed time: +{stop - start}")
    return array

list_1 = [34, 22, 24, 36, 29, 30, 18, 10]
print(f"Before: {list_1}")
insertion_sorting(list_1)
print(f"After: {list_1}")

# Bubble Sorting
def bubble_sorting(array):
    Start = timeit.default_timer()
    for i in range(1, len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    stop = timeit.default_timer()
    print(f"Bubble sort successfull Elapsed time: +{stop - Start}")
    return array
    
list_1 = [34, 22, 24, 36, 29, 30, 18, 10]
print(f"Before: {list_1}")
bubble_sorting(list_1)
print(f"After: {list_1}")

# Selection Sort
def selection_sort(array):
    Start = timeit.default_timer()
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    stop = timeit.default_timer()
    print(f"Selection sort successfull Elapsed time: +{stop - Start}")
    return array
    
list_1 = [4, 2, 3, 5, 8, 1, 7, 6]
print(f"Before: {list_1}")
selection_sort(list_1)
print(f"After: {list_1}")

# LATIHAN
def addMahasiswa():
    jumlah = int(input("Jumlah mahasiswa: "))
    mahasiswa = []
    while jumlah > 0:
        nama = input("Nama mahasiswa: ")
        mahasiswa.append(nama)
        jumlah -= 1
    
    panggil(mahasiswa)

def removeMahasiswa(arrayMahasiswa):
    print("Data mahasiswa %s" % arrayMahasiswa)
    mahasiswa = input("Hapus mahasiswa: ")
    arrayMahasiswa.remove(mahasiswa)
    print("Data Mahasiswa %s" % arrayMahasiswa)
    panggil(arrayMahasiswa)

def ascMahasiswa(arrayMahasiswa):
    arrayMahasiswa.sort()
    print(arrayMahasiswa)
    panggil(arrayMahasiswa)

def viewMahasiswa(arrayMahasiswa):
    for x in arrayMahasiswa:
        print("Nama Mahasiswa %s" % x)
    panggil(arrayMahasiswa)

def panggil(arrayMahasiswa):
    print("\n<=========Menu Data Mahasiswa=========>")
    print("1. Tambah Data Mahasiswa")
    print("2. Hapus Data Mahasiswa")
    print("3. Urutkan Data Mahasiswa")
    print("4. Lihat Data Mahasiswa")
    print("5. Tutup")

    pilih = int(input("Pilih: "))
    if pilih == 1:
        addMahasiswa()
    elif pilih == 2:
        removeMahasiswa(arrayMahasiswa)
    elif pilih == 3:
        ascMahasiswa(arrayMahasiswa)
    elif pilih == 4:
        viewMahasiswa(arrayMahasiswa)
    else:
        print("Selesai")

panggil([])

# Tugas 1
def bubble_sort(array):
    for i in range (len(array)):
        for j in range (len(array)-i-1):
            if array [j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array 

indeks_prestasi_semester = [3.8, 2.9, 3.3, 4.0, 2.7]
print("Indeks Prestasi Semester (IPS)")
print("List sebelum diurutkan : ", indeks_prestasi_semester)
print("List setelah diurutkan : ", bubble_sort(indeks_prestasi_semester))

# Tugas 2
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        if array[min_index] > array[j]:
            min_index = j

        array[i], array[min_index] = array[min_index], array[i]
    
    return array

nama_anggota = ["Zhafira", "Nirmala", "Askara", "Nalendra", "Cakra", "Sastra", "Agni", "Bagas", "Jerome", "Kiara"]
print("Before : " , nama_anggota)
print("After : " ,selection_sort(nama_anggota))

# Tugas 3
buku = []

def asc_insertion_sort(array):
    for i in range (1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item
    
    return array

def dsc_insertion_sort(array):
    for i in range (1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] < item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = item
    
    return array

def addBuku():
    total = int(input("Masukkan Total Buku : "))
    count = 1
    while(total > 0):
        nama = input(f'Masukkan Judul Buku ke-{count} : ')
        buku.append(nama)
        count+=1
        total = total - 1

    while(True):
        total = total - 1
        if(total < 0):
           break 

def menu():
    addBuku()
    print("<========== Urutkan ? =========>")
    print("1. Insertion Ascending")
    print("2. Insertion Descending")

    pilih = int(input("Pilih: "))
    if (pilih == 1):
        print("Sorting Buku Secara Ascending")
        asc_insertion_sort(buku)
    elif (pilih == 2):
        print("Sorting Buku Secara Descending")
        dsc_insertion_sort(buku)
    else:
        print("Pilihan tidak tersedia..")

    hitung = 1
    for i in buku:
        print(f'Judul Buku ke-{hitung} : ', i)
        hitung+=1



menu()