# soal no 5 soal gabungan (list, dictionary, set, dan tuple)

# TUPLE untuk menyimpan nama kolom yang tetap
kolom_barang = ("kode", "nama", "kategori", "jumlah")
# LIST berisi DICTIONARY untuk menyimpan data awal barang
daftar_barang = [
    {"kode": "B001", "nama": "Komputer", "kategori": "Elektronik", "jumlah": 15},
    {"kode": "B002", "nama": "Monitor", "kategori": "Elektronik", "jumlah": 10},
    {"kode": "B003", "nama": "Keyboard", "kategori": "Aksesori", "jumlah": 20},
    {"kode": "B004", "nama": "Mouse", "kategori": "Aksesori", "jumlah": 25},
    {"kode": "B005", "nama": "Proyektor", "kategori": "Elektronik", "jumlah": 3}
]

# SET untuk menyimpan kategori tanpa duplikasi
kategori_barang = set()

for barang in daftar_barang:
    kategori_barang.add(barang["kategori"])


# Fungsi untuk menampilkan seluruh barang
def tampilkan_barang():
    print("\n=== DAFTAR INVENTARIS LABORATORIUM ===")

    for barang in daftar_barang:
        print("\nKode Barang :", barang[kolom_barang[0]])
        print("Nama Barang :", barang[kolom_barang[1]])
        print("Kategori    :", barang[kolom_barang[2]])
        print("Jumlah      :", barang[kolom_barang[3]])


# Fungsi untuk menambahkan barang baru
def tambah_barang():
    print("\n=== TAMBAH BARANG ===")

    kode_barang = input("Masukkan kode barang: ")

    # Memeriksa apakah kode barang sudah digunakan
    for barang in daftar_barang:
        if barang["kode"].lower() == kode_barang.lower():
            print("\nGagal! Kode barang sudah digunakan.")
            return

    nama_barang = input("Masukkan nama barang: ")
    kategori = input("Masukkan kategori barang: ")
    jumlah_barang = int(input("Masukkan jumlah barang: "))

    # Membuat dictionary untuk barang baru
    barang_baru = {
        "kode": kode_barang,
        "nama": nama_barang,
        "kategori": kategori,
        "jumlah": jumlah_barang
    }

    # Menambahkan barang ke dalam list
    daftar_barang.append(barang_baru)

    # Memperbarui set kategori
    kategori_barang.add(kategori)

    print("\nBarang berhasil ditambahkan!")


# Fungsi untuk mencari barang berdasarkan kode
def cari_barang():
    print("\n=== CARI BARANG ===")

    kode_yang_dicari = input("Masukkan kode barang: ")

    for barang in daftar_barang:
        if barang["kode"].lower() == kode_yang_dicari.lower():
            print("\nBarang ditemukan!")
            print("Kode Barang :", barang["kode"])
            print("Nama Barang :", barang["nama"])
            print("Kategori    :", barang["kategori"])
            print("Jumlah      :", barang["jumlah"])
            return

    print("\nBarang tidak ditemukan!")


# Fungsi untuk menghitung seluruh unit barang
def hitung_total_barang():
    total_barang = 0

    for barang in daftar_barang:
        total_barang += barang["jumlah"]

    print("\nTotal seluruh unit barang:", total_barang)


# Fungsi untuk menampilkan kategori tanpa duplikasi
def tampilkan_kategori():
    print("\n=== KATEGORI BARANG ===")

    for kategori in kategori_barang:
        print("-", kategori)


# Menu utama program
while True:
    print("\n======================================")
    print("     INVENTARIS LABORATORIUM KOMPUTER")
    print("======================================")
    print("1. Tampilkan seluruh barang")
    print("2. Tambahkan barang baru")
    print("3. Cari barang berdasarkan kode")
    print("4. Hitung total seluruh unit barang")
    print("5. Tampilkan kategori barang")
    print("6. Keluar")
    print("======================================")

    pilihan_menu = input("Pilih menu (1-6): ")

    if pilihan_menu == "1":
        tampilkan_barang()

    elif pilihan_menu == "2":
        tambah_barang()

    elif pilihan_menu == "3":
        cari_barang()

    elif pilihan_menu == "4":
        hitung_total_barang()

    elif pilihan_menu == "5":
        tampilkan_kategori()

    elif pilihan_menu == "6":
        print("\nProgram inventaris selesai. Terima kasih!")
        break

    else:
        print("\nPilihan tidak valid!")
