# soal no 1 class python
#class python menggunakan BarangToko untuk memanajemen inventori toko
class BarangToko:
    def __init__(self, kode_barang, nama_barang, stok, harga):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self.stok = stok
        self.harga = harga

    def tambah_stok(self, jml):
        self.stok += jml
        print("Stok berhasil ditambahkan!")

    def kurangi_stok(self, jml):
        if jml <= self.stok:
            self.stok -= jml
            print("Stok berhasil dikurangi!")
        else:
            print("Stok tidak mencukupi!")

    def total_harga(self):
        return self.stok * self.harga

    def tampil_info(self):
        print("\nKode Barang :", self.kode_barang)
        print("Nama Barang :", self.nama_barang)
        print("Stok        :", self.stok)
        print("Harga       : Rp", self.harga)
        print("Total Nilai : Rp", self.total_harga())


# Membuat 3 objek barang
barang1 = BarangToko("L1", "Laptop Lenovo Legion", 10, 50000000)
barang2 = BarangToko("M2", "Mouse Razor", 20, 150000)
barang3 = BarangToko("K3", "Keyboard Razor", 15, 250000)

# Menyimpan objek ke dalam List
daftar_barang = [barang1, barang2, barang3]


# Menampilkan semua barang
def tampilkan_barang():
    print("\n=== DAFTAR BARANG ===")

    for barang in daftar_barang:
        barang.tampil_info()


# Memilih barang berdasarkan kode
def cari_barang(kode):
    for barang in daftar_barang:
        if barang.kode_barang == kode:
            return barang

    return None


# Menghitung total nilai semua barang
def hitung_total():
    total = 0

    for barang in daftar_barang:
        total += barang.total_harga()

    print("\nTotal nilai seluruh barang: Rp", total)


# Menu utama
while True:
    print("\n===== MENU INVENTARIS TOKO =====")
    print("1. Tampilkan semua barang")
    print("2. Tambah stok")
    print("3. Kurangi stok")
    print("4. Tampilkan total nilai barang")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tampilkan_barang()

    elif pilihan == "2":
        kode = input("Masukkan kode barang: ")
        barang = cari_barang(kode)
        if barang is not None:
            jumlah = int(input("Jumlah stok yang ditambahkan: "))
            barang.tambah_stok(jumlah)
            barang.tampil_info()
        else:
            print("Barang tidak ditemukan!")

    elif pilihan == "3":
        kode = input("Masukkan kode barang: ")
        barang = cari_barang(kode)
        if barang is not None:
            jumlah = int(input("Jumlah stok yang dikurangi: "))
            barang.kurangi_stok(jumlah)
            barang.tampil_info()
        else:
            print("Barang tidak ditemukan!")

    elif pilihan == "4":
        hitung_total()

    elif pilihan == "5":
        print("Terima kasih, program selesai!")
        break
    else:
        print("Pilihan tidak valid!")
