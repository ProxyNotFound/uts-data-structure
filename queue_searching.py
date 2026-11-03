# soal no 3 queue dan searching
# simulasikan sistem antrean pendaftaran pasien klinik dengan fitur pencarian data pasien

from collections import deque
# Membuat antrean pasien
antrian = deque()

# 1. Menambahkan pasien (ENQUEUE)
def tambah_pasien():
    print("\n=== TAMBAH PASIEN ===")

    id_pasien = input("Masukkan ID pasien: ")
    nama = input("Masukkan nama pasien: ")
    keluhan = input("Masukkan keluhan: ")

    pasien = {
        "id_pasien": id_pasien,
        "nama": nama,
        "keluhan": keluhan
    }

    antrian.append(pasien)

    print("\nPasien berhasil ditambahkan!")


# 2. Melayani pasien (DEQUEUE)
def layani_pasien():
    print("\n=== LAYANI PASIEN ===")

    if len(antrian) == 0:
        print("Antrean kosong!")
    else:
        pasien = antrian.popleft()

        print("Pasien sedang dilayani:")
        print("ID Pasien :", pasien["id_pasien"])
        print("Nama      :", pasien["nama"])
        print("Keluhan   :", pasien["keluhan"])


# 3. Mencari pasien (LINEAR SEARCH)
def cari_pasien():
    print("\n=== CARI PASIEN ===")

    nama_cari = input("Masukkan nama pasien: ")

    ditemukan = False

    for pasien in antrian:
        if pasien["nama"].lower() == nama_cari.lower():

            print("\nPasien ditemukan!")
            print("ID Pasien :", pasien["id_pasien"])
            print("Nama      :", pasien["nama"])
            print("Keluhan   :", pasien["keluhan"])

            ditemukan = True
            break

    if not ditemukan:
        print("Pasien tidak ditemukan!")


# 4. Menampilkan seluruh antrean
def tampilkan_antrian():
    print("\n=== DAFTAR ANTREAN PASIEN ===")

    if len(antrian) == 0:
        print("Antrean masih kosong!")
    else:
        nomor = 1

        for pasien in antrian:
            print("\nNomor Antrean:", nomor)
            print("ID Pasien    :", pasien["id_pasien"])
            print("Nama         :", pasien["nama"])
            print("Keluhan      :", pasien["keluhan"])

            nomor += 1


# 5. Menu utama
while True:
    print("\n================================")
    print("      SISTEM ANTREAN KLINIK")
    print("================================")
    print("1. Tambah pasien")
    print("2. Layani pasien")
    print("3. Cari pasien")
    print("4. Tampilkan antrean")
    print("5. Keluar")
    print("================================")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_pasien()

    elif pilihan == "2":
        layani_pasien()

    elif pilihan == "3":
        cari_pasien()

    elif pilihan == "4":
        tampilkan_antrian()

    elif pilihan == "5":
        print("\nTerima kasih!")
        print("Program antrean klinik selesai.")
        break

    else:
        print("\nPilihan tidak valid! Silakan pilih 1-5.")
