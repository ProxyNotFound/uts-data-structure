# soal no 4 bubble sort
# gunakan data nilai berikut: [75,90,65,85,70,95,80]
# Membuat list kosong untuk menyimpan nilai
daftar_nilai = []
# Fungsi untuk memasukkan nilai
def input_nilai():
    jumlah_data = int(input("\nMasukkan jumlah nilai: "))

    for nomor in range(jumlah_data):
        nilai = float(input(f"Masukkan nilai ke-{nomor + 1}: "))
        daftar_nilai.append(nilai)

    print("\nData nilai berhasil dimasukkan!")

# Fungsi untuk menampilkan data
def tampilkan_data():
    if len(daftar_nilai) == 0:
        print("\nBelum ada data nilai!")
    else:
        print("\nDaftar nilai:", daftar_nilai)

# Fungsi untuk mengurutkan data menggunakan Bubble Sort
def bubble_sort():
    if len(daftar_nilai) == 0:
        print("\nBelum ada data yang bisa diurutkan!")
        return

    jumlah_data = len(daftar_nilai)

    for indeks_luar in range(jumlah_data - 1):
        ada_pertukaran = False

        for indeks_dalam in range(jumlah_data - 1 - indeks_luar):
            if daftar_nilai[indeks_dalam] > daftar_nilai[indeks_dalam + 1]:
                daftar_nilai[indeks_dalam], daftar_nilai[indeks_dalam + 1] = daftar_nilai[indeks_dalam + 1], daftar_nilai[indeks_dalam]
                ada_pertukaran = True

        if ada_pertukaran == False:
            break

    print("\nData berhasil diurutkan menggunakan Bubble Sort!")

# Fungsi untuk menampilkan nilai tertinggi
def tampilkan_nilai_tertinggi():
    if len(daftar_nilai) == 0:
        print("\nBelum ada data nilai!")
    else:
        print("\nNilai tertinggi:", max(daftar_nilai))

# Fungsi untuk menampilkan nilai terendah
def tampilkan_nilai_terendah():
    if len(daftar_nilai) == 0:
        print("\nBelum ada data nilai!")
    else:
        print("\nNilai terendah:", min(daftar_nilai))

# Fungsi untuk menghitung rata-rata
def hitung_rata_rata():
    if len(daftar_nilai) == 0:
        print("\nBelum ada data nilai!")
    else:
        total_nilai = sum(daftar_nilai)
        jumlah_data = len(daftar_nilai)
        rata_rata = total_nilai / jumlah_data

        print("\nRata-rata nilai:", round(rata_rata, 2))

# Fungsi untuk menambahkan nilai baru
def tambah_nilai():
    nilai_baru = float(input("\nMasukkan nilai yang ingin ditambahkan: "))

    daftar_nilai.append(nilai_baru)

    print("\nNilai berhasil ditambahkan!")

    tampilkan_data()
    bubble_sort()
    tampilkan_data()

# Menu utama
while True:
    print("\n================================")
    print("       PROGRAM BUBBLE SORT")
    print("================================")
    print("1. Input nilai")
    print("2. Tampilkan data")
    print("3. Urutkan data")
    print("4. Nilai tertinggi")
    print("5. Nilai terendah")
    print("6. Hitung rata-rata")
    print("7. Tambahkan nilai baru dan urutkan")
    print("8. Keluar")
    print("================================")
    pilihan_menu = input("Pilih menu (1-8): ")
    if pilihan_menu == "1":
        input_nilai()

    elif pilihan_menu == "2":
        tampilkan_data()

    elif pilihan_menu == "3":
        bubble_sort()
        tampilkan_data()

    elif pilihan_menu == "4":
        tampilkan_nilai_tertinggi()

    elif pilihan_menu == "5":
        tampilkan_nilai_terendah()

    elif pilihan_menu == "6":
        hitung_rata_rata()

    elif pilihan_menu == "7":
        if len(daftar_nilai) == 0:
            print("\nMasukkan nilai terlebih dahulu!")
        else:
            tambah_nilai()

    elif pilihan_menu == "8":
        print("\nProgram selesai. Terima kasih!")
        break

    else:
        print("\nPilihan tidak valid! Silakan pilih 1-8.")
