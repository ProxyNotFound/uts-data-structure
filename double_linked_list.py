# soal no 2 double linked list
# implementasikan double linked list untuk simulasi playlist musik
class Node:
    def __init__(self, judul, penyanyi, durasi):
        self.judul = judul
        self.penyanyi = penyanyi
        self.durasi = durasi
        self.next = None
        self.prev = None

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    # Menambahkan lagu di akhir
    def tambah_lagu(self, judul, penyanyi, durasi):
        baru = Node(judul, penyanyi, durasi)

        if self.head is None:
            self.head = baru
            self.tail = baru
            self.current = baru
        else:
            self.tail.next = baru
            baru.prev = self.tail
            self.tail = baru

        print("Lagu berhasil ditambahkan!")

    # Menghapus lagu di awal
    def hapus_awal(self):
        if self.head is None:
            print("Playlist kosong!")
            return

        print("Menghapus lagu:", self.head.judul)

        if self.current == self.head:
            self.current = self.head.next

        self.head = self.head.next

        if self.head is None:
            self.tail = None
            self.current = None
        else:
            self.head.prev = None

    # Navigasi maju
    def next_lagu(self):
        if self.current is not None and self.current.next is not None:
            self.current = self.current.next
            self.tampilkan_sekarang()
        else:
            print("Tidak ada lagu berikutnya!")

    # Navigasi mundur
    def previous_lagu(self):
        if self.current is not None and self.current.prev is not None:
            self.current = self.current.prev
            self.tampilkan_sekarang()
        else:
            print("Tidak ada lagu sebelumnya!")

    # Menampilkan lagu yang sedang dipilih
    def tampilkan_sekarang(self):
        if self.current is not None:
            print("\nSedang diputar:")
            print("Judul   :", self.current.judul)
            print("Penyanyi:", self.current.penyanyi)
            print("Durasi  :", self.current.durasi)

    # Menampilkan semua lagu
    def tampilkan_semua(self):
        bantu = self.head

        print("\n===== DAFTAR PLAYLIST =====")

        if bantu is None:
            print("Playlist kosong!")
            return

        nomor = 1

        while bantu is not None:
            print(str(nomor) + ". " + bantu.judul)
            print("   Penyanyi:", bantu.penyanyi)
            print("   Durasi:", bantu.durasi)
            bantu = bantu.next
            nomor += 1

# Membuat playlist
playlist = Playlist()

# Menambahkan 7 lagu
playlist.tambah_lagu("Thinking Out Loud", "Ed Sheeran", "4:41")
playlist.tambah_lagu("Talking to the Moon", "Bruno Mars", "3:37")
playlist.tambah_lagu("Dear God", "Avenged Sevenfold", "6:34")
playlist.tambah_lagu("Let the World Burn", "Chris Grey", "3:07")
playlist.tambah_lagu("Best Friend", "Rex Orange County", "4:22")
playlist.tambah_lagu("No. 1 Party Anthem", "Arctic Monkeys", "4:03")
playlist.tambah_lagu("505", "Arctic Monkeys", "4:13")


# Menu utama
while True:
    print("\n===== PLAYLIST MUSIK =====")
    print("1. Tampilkan semua lagu")
    print("2. Tambah lagu di akhir")
    print("3. Hapus lagu di awal")
    print("4. Lagu berikutnya (Next)")
    print("5. Lagu sebelumnya (Previous)")
    print("6. Tampilkan lagu sekarang")
    print("7. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        playlist.tampilkan_semua()

    elif pilihan == "2":
        judul = input("Judul lagu: ")
        penyanyi = input("Nama penyanyi: ")
        durasi = input("Durasi (menit:detik): ")

        playlist.tambah_lagu(judul, penyanyi, durasi)

    elif pilihan == "3":
        playlist.hapus_awal()

    elif pilihan == "4":
        playlist.next_lagu()

    elif pilihan == "5":
        playlist.previous_lagu()

    elif pilihan == "6":
        playlist.tampilkan_sekarang()

    elif pilihan == "7":
        print("Playlist ditutup. Sampai jumpa!")
        break

    else:
        print("Pilihan tidak valid!")
