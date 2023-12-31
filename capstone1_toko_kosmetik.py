# Toko Kosmetik Your Beauty
# ===========================

# Mengimport modul math sebagai m
import math as m


# Daftar stok barang
stok = {
    "biore": {"kategori": "sabun", "nama": "Biore", "kemasan": "tube 100 ml", "stok": 10, "harga": 10000},
    "emina": {"kategori": "kosmetik","nama": "Emina","kemasan": "Jar 30 gr","stok": 5,"harga": 15000},
    "skintific": {"kategori": "skincare","nama": "Skintific","kemasan": "tube 30 gr","stok": 10,"harga": 80000},
    "missha": {"kategori": "kosmetik","nama": "Missha","kemasan": "tube 20 ml","stok": 15,"harga": 50000},
    "azarine": {"kategori": "skincare","nama": "Azarine","kemasan": "tube 100 ml","stok": 20,"harga": 70000},
        }

# Password admin
Password = "667788"

# Keranjang belanja
keranjang = []

# Fungsi untuk menampilkan stok semua barang
def tampilkan_stok_semua():
    while True:  # Looping untuk memberi pengguna opsi memilih metode tampilan lain setelah satu selesai
        # Memeriksa apakah stok kosong atau tidak
        if len(stok) == 0:
            print("Tidak ada stok yang tersedia")
            break
        else:
            # Menanyakan user untuk sorting
            print("Pilih Metode Tampilan:")
            print("1. Tampilkan Semua")
            print("2. Urutkan Berdasarkan Abjad")
            print("3. Cari Berdasarkan Kata Kunci")
            print("4. Kembali ke Menu Utama")
            pilihan = int(input("Masukkan pilihan Anda (1-4): "))

            if pilihan == 2:
                print("Pilih kolom untuk pengurutan:")
                print("1. Nama Barang")
                print("2. Kategori")
                kolom_pilihan = int(input("Masukkan pilihan Anda (1-2): "))

                if kolom_pilihan == 1:
                    sorted_keys = sorted(stok.keys(), key=lambda x: (stok[x]['nama'], stok[x]['kategori']))  # Sort by 'nama' then 'kategori'
                else:
                    sorted_keys = sorted(stok.keys(), key=lambda x: (stok[x]['kategori'], stok[x]['nama']))  # Sort by 'kategori' then 'nama'

                # Menampilkan header tabel
                print("Daftar Barang :")
                print("==============================================================================")
                print("| kategori       | Nama Barang      | Kemasan          | Stok  | Harga/pcs   |")
                print("==============================================================================")

                # Menampilkan setiap barang dalam stok
                for key in sorted_keys:
                    # Menampilkan baris tabel dengan format yang sesuai
                    print("| {:14s} | {:16s} | {:16s} | {:5d} | {:12d} |".format(
                        stok[key]["kategori"], stok[key]["nama"], stok[key]["kemasan"], stok[key]["stok"], stok[key]["harga"]
                    ))

            elif pilihan == 3:
                kata_kunci = input("Masukkan kata kunci pencarian: ").lower()
                sorted_keys = [key for key in stok if kata_kunci in stok[key]['nama'].lower() or kata_kunci in stok[key]['kategori'].lower()]

                # Menampilkan header tabel
                print("Daftar Barang :")
                print("==============================================================================")
                print("| kategori       | Nama Barang      | Kemasan          | Stok  | Harga/pcs   |")
                print("==============================================================================")

                # Menampilkan setiap barang dalam stok
                for key in sorted_keys:
                    # Menampilkan baris tabel dengan format yang sesuai
                    print("| {:14s} | {:16s} | {:16s} | {:5d} | {:12d} |".format(
                        stok[key]["kategori"], stok[key]["nama"], stok[key]["kemasan"], stok[key]["stok"], stok[key]["harga"]
                    ))

            elif pilihan == 4:
                break  # Keluar dari loop dan kembali ke menu utama
            elif pilihan == 1:
                # Menampilkan header tabel
                print("Daftar Barang :")
                print("==============================================================================")
                print("| kategori       | Nama Barang      | Kemasan          | Stok  | Harga/pcs   |")
                print("==============================================================================")

                # Menampilkan setiap barang dalam stok
                for key in stok.keys():
                    # Menampilkan baris tabel dengan format yang sesuai
                    print("| {:14s} | {:16s} | {:16s} | {:5d} | {:12d} |".format(
                        stok[key]["kategori"], stok[key]["nama"], stok[key]["kemasan"], stok[key]["stok"], stok[key]["harga"]
                    ))

            # Menampilkan footer tabel
            print("===============================================================================")

            # Menanyakan apakah pengguna ingin memilih metode tampilan lain
            next_step = input("Ingin memilih metode tampilan lain? (Y/N): ")
            if next_step.lower() != 'y':
                break


# Fungsi untuk menambahkan stok barang baru
def tambah_stok():
    while True:
        # Memasukkan nama barang yang ingin ditambahkan
        input_nama = input("Masukkan Nama Barang yang Ingin Ditambahkan: ")
        item_baru = input_nama.replace(" ", "")

        # Memeriksa panjang karakter nama barang baru
        while len(input_nama) > 15:
            print("Maks. Karakter 15, mohon input ulang.")
            input_nama = input("Masukkan Nama Barang yang Ingin Ditambahkan: ")
            item_baru = input_nama.replace(" ", "")

        # Memeriksa apakah barang dengan nama yang sama sudah ada dalam stok
        if item_baru.lower() not in stok.keys():
            # Memasukkan kemasan barang baru
            input_kemasan = input("Masukkan Kemasan dari Barang yang ingin ditambahkan: ")

            # Memeriksa panjang karakter kemasan barang baru
            while len(input_kemasan) > 15:
                print("Maks. Karakter 15, mohon input ulang.")
                input_kemasan = input("Masukkan Kemasan dari Barang yang ingin ditambahkan: ")

            # Memasukkan kategori barang baru
            input_kategori = input("Masukkan Kategori dari Barang yang ingin ditambahkan: ")

            # Memeriksa panjang karakter kategori barang baru
            while len(input_kategori) > 15:
                print("Maks. Karakter 15, mohon input ulang.")
                input_kategori = input("Masukkan Kategori dari Barang yang ingin ditambahkan: ")

            # Memasukkan jumlah stok barang baru
            input_qty = float(input("Masukkan Jumlah Stok dari Barang yang ingin ditambahkan: "))

            # Memasukkan harga per pcs barang baru
            input_harga = int(input("Masukkan Harga per pcs dari Barang yang ingin ditambahkan: "))

            # Konfirmasi penambahan barang baru
            checker2 = input(f"Apakah Anda yakin ingin menambahkan barang {input_nama} {input_kategori} dengan jumlah {m.ceil(input_qty)} dan harga {input_harga}? (Y/N): ")

            if checker2.lower() != "y":
                break
            else:
                # Menambahkan barang baru ke stok
                stok[item_baru.lower()] = {
                    "kategori": input_kategori.capitalize(),
                    "nama": input_nama.capitalize(),
                    "kemasan": input_kemasan.capitalize(),
                    "stok": m.ceil(input_qty),
                    "harga": input_harga
                }
                tampilkan_stok_semua()
                break
        else:
            print("Barang dengan nama yang sama sudah ada dalam daftar, tidak dapat menambahkan barang.")
            break

# Fungsi untuk mengupdate stok barang
def update_stok():
    # Memilih opsi update atau penghapusan barang
    update_stok = int(input("===== UPDATE STOK =====\n1. Update Barang\n2. Hapus Barang\n3. Kembali ke Menu Utama\n\nUpdate yang Ingin Dipilih (1-3): "))

    # Mengupdate barang
    if update_stok == 1:
        tampilkan_stok_semua()
        item_updatestok = input("Masukkan nama barang yang ingin diupdate: ")
        item_update = item_updatestok.replace(" ", "")

        # Memeriksa apakah barang yang ingin diupdate ada dalam stok
        while item_update.lower() in stok.keys():
            jenis_update = int(input("====== UPDATE BARANG =====\n1. Nama Barang\n2. Kemasan\n3. Kategori\n4. stok\n5. Harga/pcs\n6. Kembali ke Menu Utama\nBarang yang ingin diupdate (1-6): "))

            # Mengupdate nama barang
            if jenis_update == 1:
                item_baru = input("Masukkan nama barang baru: ")
                nama_baru = item_baru.replace(" ", "")

                # Memeriksa panjang karakter nama baru
                while len(item_baru) > 15:
                    print("Maks. Karakter 15, mohon input ulang.")
                    item_baru = input("Masukkan nama barang baru: ")
                    nama_baru = item_baru.replace(" ", "")

                # Memeriksa apakah nama baru sudah ada dalam stok
                while nama_baru.lower() in stok.keys():
                    print("Nama Barang Sudah Ada, Masukkan Nama Baru")
                    item_baru = input("Masukkan nama barang baru: ")
                    nama_baru = item_baru.replace(" ", "")

                # Konfirmasi update nama barang
                checker3 = input(f"Apakah Anda yakin ingin menambahkan update nama {item_updatestok} menjadi {item_baru}? (Y/N): ")
                if checker3.lower() != "y":
                    break
                else:
                    # Mengupdate stok barang
                    stok[nama_baru.lower()] = stok[item_update.lower()]
                    del stok[item_update.lower()]
                    stok[nama_baru.lower()]["nama"] = item_baru.capitalize()
                    tampilkan_stok_semua()
                    break

            # Mengupdate kemasan barang
            elif jenis_update == 2:
                kemasan_baru = input("Masukkan detail kemasan baru: ")

                # Memeriksa panjang karakter kemasan baru
                while len(kemasan_baru) > 15:
                    print("Maks. Karakter 15, mohon input ulang.")
                    kemasan_baru = input("Masukkan detail kemasan baru: ")

                # Konfirmasi update kemasan barang
                checker4 = input(f"Apakah Anda yakin ingin menambahkan update kemasan {item_updatestok} menjadi {kemasan_baru}? (Y/N): ")
                if checker4.lower() != "y":
                    break
                else:
                    # Mengupdate stok barang
                    stok[item_update.lower()]["kemasan"] = kemasan_baru.capitalize()
                    tampilkan_stok_semua()
                    break

            # Mengupdate kategori barang
            elif jenis_update == 3:
                kategori_baru = input("Masukkan detail kategori baru: ")

                # Memeriksa panjang karakter kategori baru
                while len(kategori_baru) > 15:
                    print("Maks. Karakter 15, mohon input ulang.")
                    kategori_baru = input("Masukkan detail kategori baru: ")

                # Konfirmasi update kategori barang
                checker5 = input(f"Apakah Anda yakin ingin menambahkan update kategori {item_updatestok} menjadi {kategori_baru}? (Y/N): ")
                if checker5.lower() != "y":
                    break
                else:
                    # Mengupdate stok barang
                    stok[item_update.lower()]["kategori"] = kategori_baru.capitalize()
                    tampilkan_stok_semua()
                    break

            # Mengupdate jumlah stok barang
            elif jenis_update == 4:
                stok_baru = int(input("Masukkan jumlah stok baru: "))

                # Konfirmasi update jumlah stok barang
                checker6 = input(f"Apakah Anda yakin mengupdate jumlah stok {item_updatestok} menjadi {m.ceil(stok_baru)}? (Y/N): ")
                if checker6.lower() != "y":
                    break
                else:
                    # Mengupdate stok barang
                    stok[item_update.lower()]["stok"] = stok_baru
                    tampilkan_stok_semua()
                    break

            # Mengupdate harga barang
            elif jenis_update == 5:
                harga_baru = int(input("Masukkan harga barang baru: "))

                # Konfirmasi update harga barang
                checker7 = input(f"Apakah Anda yakin mengupdate harga {item_updatestok} menjadi {m.ceil(harga_baru)}? (Y/N): ")
                if checker7.lower() != "y":
                    break
                else:
                    # Mengupdate stok barang
                    stok[item_update.lower()]["harga"] = harga_baru
                    tampilkan_stok_semua()
                    break

            # Kembali ke menu utama
            elif jenis_update == 6:
                break

            else:
                break

        # Barang yang ingin diupdate tidak ditemukan dalam stok
        else:
            print("Barang yang Anda masukkan tidak terdaftar, update tidak dapat dilakukan.")

    # Menghapus barang dari stok
    elif update_stok == 2:
        tampilkan_stok_semua()
        input_delete = input("Masukkan nama barang yang ingin dihapus: ")
        checker8 = input(f"Apakah Anda yakin ingin menghapus seluruh informasi untuk barang {input_delete}? (Y/N): ")
        while checker8.lower() != "y":
            break
        else:
            nama_delete = input_delete.replace(" ", "")
            del stok[nama_delete.lower()]
            tampilkan_stok_semua()

    # Kembali ke menu utama
    while update_stok == 3:
        break

    # Memeriksa jika opsi update yang dipilih tidak tersedia
    if update_stok != 1 and update_stok != 2 and update_stok != 3:
        print("Pilihan yang Anda pilih tidak tersedia. Silahkan dicoba lagi.")

# Fungsi untuk melakukan proses belanja
def belanja():
    # Menampilkan stok barang yang tersedia
    tampilkan_stok_semua()

    # Mengulang proses pembelian barang
    while True:
        # Meminta input nama barang yang ingin dibeli
        input_beli = input("Masukkan Nama Barang Yang Ingin Dibeli: ")
        nama_beli = input_beli.replace(" ", "")

        # Memeriksa barang yang ingin dibeli dalam stok
        if nama_beli.lower() not in stok.keys():
            print("Barang yang ingin dibeli tidak ditemukan")
        else:
            # Meminta input jumlah barang yang ingin dibeli
            qty_beli = float(input("Masukkan Jumlah Yang Ingin Dibeli: "))

            # Memeriksa ketersediaan stok barang yang ingin dibeli
            if qty_beli > stok[nama_beli.lower()]["stok"]:
                print("Stok tidak cukup. Stok {} sisa {}".format(stok[nama_beli.lower()]["nama"], stok[nama_beli.lower()]["stok"]))
            elif qty_beli <= 0:
                print("Jumlah pembelian tidak boleh kurang dari 1")
            else:
                # Menambahkan barang ke dalam keranjang belanja
                keranjang.append([stok[nama_beli.lower()]["nama"], stok[nama_beli.lower()]["kemasan"], qty_beli, stok[nama_beli.lower()]["harga"], stok[nama_beli.lower()]["nama"].replace(" ", "")])

            # Menampilkan isi keranjang belanja
            print("Keranjang Belanja\n\t| Nama Barang \t| Kemasan \t| Qty \t| Harga \t| Total Harga")
            for item in keranjang:
                print("\t| {} \t| {} \t| {} \t| {} \t| {}".format(item[0], item[1], m.ceil(item[2]), item[3], m.ceil(item[2] * item[3])))

            # Meminta konfirmasi untuk melanjutkan belanja atau tidak
            checker = input("Apakah Ingin Membeli barang Lain? (Y/N): ")
            if checker.lower() != "y":
                break

    # Memeriksa jika keranjang belanja kosong
    while len(keranjang) == 0:
        break

    # Proses pembayaran jika terdapat barang dalam keranjang belanja
    else:
        # Menampilkan isi keranjang belanja
        print("Keranjang Belanja\n\t| Nama Barang \t| Kemasan\t| Qty \t| Harga \t| Total Harga")
        total = 0
        for item in keranjang:
            print("\t| {} \t| {} \t| {} \t| {} \t| {}".format(item[0], item[1], m.ceil(item[2]), item[3], m.ceil(item[2] * item[3])))
            total += item[2] * item[3]

        # Meminta input jumlah uang dari pembeli
        while True:
            print('Total Yang Harus Dibayar = {}'.format(m.ceil(total)))
            input_uang = int(input('Masukkan jumlah uang: '))

            # Memeriksa jumlah uang yang diberikan oleh pembeli
            if input_uang > total:
                kembali = input_uang - total
                print('======Terima kasih sudah berbelanja di TOKO KOSMETIK YOUR BEAUTY======\n\nUang kembalian Anda sebesar : {}'.format(m.ceil(kembali)))

                # Mengurangi stok barang yang telah dibeli
                for item in keranjang:
                    stok[item[4].lower()]["stok"] -= m.ceil(item[2])

                # Mengosongkan keranjang belanja
                keranjang.clear()
                break
            elif input_uang == total:
                print('======Terima kasih sudah berbelanja di TOKO KOSMETIK YOUR BEAUTY======')

                # Mengurangi stok barang yang telah dibeli
                for item in keranjang:
                    stok[(item[4].lower())]["stok"] -= m.ceil(item[2])

                # Mengosongkan keranjang belanja
                keranjang.clear()
                break
            else:
                kekurangan = total - input_uang
                print('MOHON MAAF, Uang Anda kurang sebesar {}'.format(m.ceil(kekurangan)))

# Memulai program dengan menampilkan menu login

while True:
    user_input = int(input("===========================================\nSELAMAT DATANG DI TOKO KOSMETIK YOUR BEAUTY\n===========================================\n\nMasuk Sebagai:\n1. Admin TOKO KOSMETIK YOUR BEAUTY\n2. Pembeli\n3. Keluar Program\n\nMasukkan Menu Login (1-3): "))

    # Menu login untuk admin
    while user_input == 1:
        login_admin = input("Masukkan Kata Passowrd Admin: ")

        # Memeriksa Password yang dimasukkan
        if login_admin == Password:
            pilih_menu_admin = int(input("===================================\n| ADMIN TOKO KOSMETIK YOUR BEAUTY |\n===================================\n\n===== MENU UTAMA =====\n1. Tampilkan Stok Barang\n2. Tambah Barang\n3. Update Stok\n4. Kembali ke Menu Utama\n\nInput Menu Yang Ingin Dipilih (1-4): "))

            # Menampilkan stok barang
            if pilih_menu_admin == 1:
                tampilkan_stok_semua()

            # Menambahkan stok barang baru
            elif pilih_menu_admin == 2:
                tambah_stok()

            # Mengupdate stok barang
            elif pilih_menu_admin == 3:
                update_stok()

            # Kembali ke menu utama
            elif pilih_menu_admin != 1 and pilih_menu_admin != 2 and pilih_menu_admin != 3 and pilih_menu_admin != 4:
                print("Menu yang Anda pilih tidak tersedia. Silahkan dicoba lagi.")

            # Meminta input menu login kembali setelah selesai
            else:
                user_input = int(input("===========================================\nSELAMAT DATANG DI TOKO KOSMETIK YOUR BEAUTY\n===========================================\n\nMasuk Sebagai:\n1. Admin TOKO KOSMETIK YOUR BEAUTY\n2. Pembeli\n3. Keluar Program\n\nMasukkan Menu Login (1-3): "))

        else:
            print("Password yang Dimasukkan Salah. Login gagal")
            user_input = int(input("===========================================\nSELAMAT DATANG DI TOKO KOSMETIK YOUR BEAUTY\n===========================================\n\nMasuk Sebagai:\n1. Admin TOKO KOSMETIK YOUR BEAUTY\n2. Pembeli\n3. Keluar Program\n\nMasukkan Menu Login (1-3):"))

    # Menu login untuk pPembeli
    while user_input == 2:
        pilih_menu_cust = int(input("===========\n| Pembeli |\n===========\n\n=========== MENU UTAMA ===========\n1. Tampilkan Daftar Barang\n2. Belanja\n3. Kembali ke Menu Utama\n\nInput Menu Yang Ingin Dipilih (1-3): "))

        # Menampilkan stok barang
        if pilih_menu_cust == 1:
            tampilkan_stok_semua()

        # Memulai proses pembelian
        elif pilih_menu_cust == 2:
            belanja()

        # Kembali ke menu utama
        elif pilih_menu_cust != 1 and pilih_menu_cust != 2 and pilih_menu_cust != 3:
            print("Menu yang Anda pilih tidak tersedia. Silahkan dicoba lagi.")

        # Meminta input menu login kembali setelah selesai
        else:
            user_input = int(input("===========================================\nSELAMAT DATANG DI TOKO KOSMETIK YOUR BEAUTY\n===========================================\n\nMasuk Sebagai:\n1. Admin TOKO KOSMETIK YOUR BEAUTY\n2. Pembeli\n3. Keluar Program\n\nMasukkan Menu Login (1-3):"))

    # Memeriksa jika user memilih menu yang tidak tersedia
    if user_input != 1 and user_input != 2 and user_input != 3:
        print("Menu yang Anda pilih tidak tersedia. Silahkan dicoba lagi.")

    else:
        break