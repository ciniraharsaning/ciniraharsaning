dict_data_mobil = {
  # Key 0: Dictionary containing information about Avanza car
  0: {
    'Nama Mobil': 'Avanza',
    'Manufacturer': 'Toyota',
    'Jumlah Penumpang': 7,
    'Harga Sewa': 300000,
    'ID Mobil': ''
  },
  # Key 1: Dictionary containing information about Mobilio car
  1: {
    'Nama Mobil': 'Mobilio',
    'Manufacturer': 'Honda',
    'Jumlah Penumpang': 7,
    'Harga Sewa': 350000,
    'ID Mobil': ''
  },
  # Key 2: Dictionary containing information about 330i car
  2: {
    'Nama Mobil': '330i',
    'Manufacturer': 'BMW',
    'Jumlah Penumpang': 5,
    'Harga Sewa': 500000,
    'ID Mobil': ''
  }
}

list_id_mobil = []

# 0. Menu utama dengan opsi 4 menu (Read, Create, Update, Delete)

def menu_utama():
    print ('''
DATA LIST MOBIL RENTAL
-----------------------------------------------------
1. Tampilkan List Mobil
2. Tambahkan Data Mobil
3. Edit Data Mobil
4. Delete Data Mobil
5. Exit
        ''')

    while True:
        input_menu_utama = input('Masukkan angka yang ingin di pilih: ')

        if input_menu_utama.isnumeric():
            if input_menu_utama == '1': # masuk ke Menu Tampilkan List Mobil
                menu_tampilkan_list_mobil()
            elif input_menu_utama == '2': # masuk ke Menu Tambahkan Data Mobil
                menu_tambahkan_data_mobil()
            elif input_menu_utama == '3': # masuk ke Menu Edit Data Mobil
                menu_edit_data()
            elif input_menu_utama == '4': # masuk ke Menu Hapus Data Mobil
                menu_hapus_data()
            elif input_menu_utama == '5': # masuk ke Menu Exit
                menu_exit()
            else:
                print('Maaf, nomor menu yang dimasukkan tidak ditemukan. Silahkan masukkan nomor menu kembali.')
        else:
            print('Maaf, input yang dimasukkan bukanlah angka. Silahkan masukkan nomor menu kembali.')

###########################################################################################################################################################################################

# 1. Menu Read (Tampilkan List Mobil)

def menu_tampilkan_list_mobil():
    print('''
MENU TAMPILKAN DATA
-----------------------------------------------------
1. Tampilkan Semua Data
2. Cari Data Mobil dengan ID Kendaraan
3. Kembali ke Menu Utama
        ''')
    while True:
        input_tampilkan_data = input('Masukkan angka yang ingin di pilih: ')

        if input_tampilkan_data.isnumeric():
            if input_tampilkan_data == '1': # masuk ke Menu Tampilkan Semua Data
                tampilkan_data()
            elif input_tampilkan_data == '2': # masuk ke Menu Cari Data Mobil
                cari_data_mobil()
            elif input_tampilkan_data == '3': # balik ke Menu Utama
                menu_utama()
            else:
                print('Maaf, nomor menu yang dimasukkan tidak ditemukan. Silahkan masukkan nomor menu kembali.')
        else:
            print('Maaf, input yang dimasukkan bukanlah angka. Silahkan masukkan nomor menu kembali.')

# 1.1. Tampilkan Semua Data Mobil

def tampilkan_data():
    print ('\nLIST DATA MOBIL RENTAL')  # Judul
    print ("{:<10} | {:<15} | {:<15} | {:<15} | {:<16} | {:<14}".format('INDEX', 'ID MOBIL', 'NAMA MOBIL','MANUFACTURER', 'JUMLAH PENUMPANG', 'HARGA SEWA' ))  # Header
    print ('-----------+-----------------+-----------------+-----------------+------------------+---------------') # Header

    if len(dict_data_mobil.keys()) >= 1: # Cek jumlah data di dalam dictionary
        list_id_mobil.clear()  
        append_id_mobil()

        menu_tampilkan_list_mobil()
    else: 
        print('\nTidak ada data mobil. Silahkan tambahkan data mobil terlebih dahulu.')
        menu_tampilkan_list_mobil()

# 1.1.1. If the data exist

def append_id_mobil():
    angka_belakang = 1

    for id_in_mobil in dict_data_mobil.keys(): # ambil keys dari dictionary : 0,1,2, dst.
            
        id_mobil = dict_data_mobil[id_in_mobil]['Nama Mobil'][0:2:1] + dict_data_mobil[id_in_mobil]['Manufacturer'][0:2:1]
        id_mobil = id_mobil.upper()

        id_mobil_masuk_list = str(f'{id_mobil}00{angka_belakang}')
        #
            
        if id_mobil_masuk_list in list_id_mobil:

            angka_belakang = angka_belakang + 1
            id_mobil_masuk_list = str(f'{id_mobil}00{angka_belakang}')

            list_id_mobil.append(id_mobil_masuk_list)
            dict_data_mobil[id_in_mobil]['ID Mobil'] = id_mobil_masuk_list

        else:
            angka_belakang = 1
            id_mobil_masuk_list = str(f'{id_mobil}00{angka_belakang}')

            list_id_mobil.append(id_mobil_masuk_list)
            dict_data_mobil[id_in_mobil]['ID Mobil'] = id_mobil_masuk_list


        print ("{:<10} | {:<15} | {:<15} | {:<15} | {:<2} seats{:<8} | Rp. {:<10}".format(id_in_mobil, id_mobil_masuk_list, dict_data_mobil[id_in_mobil]['Nama Mobil'], dict_data_mobil[id_in_mobil]['Manufacturer'], dict_data_mobil[id_in_mobil]['Jumlah Penumpang'], '', dict_data_mobil[id_in_mobil]['Harga Sewa']))

# 1.2. Cari Data Mobil dengan ID 

def cari_data_mobil():
    input_cari_data_mobil = input ('Silahkan masukkan ID mobil: ').strip()
    input_cari_data_mobil_upper = input_cari_data_mobil.upper()
    counter = 0

    for id in list_id_mobil:
        if len(dict_data_mobil) >= 1:
            if input_cari_data_mobil_upper == id:
                index = list_id_mobil.index(input_cari_data_mobil_upper)

                print ('Data berhasil ditemukan.')
                print ("{:<10} | {:<15} | {:<15} | {:<15} | {:<16} | {:<14}".format('INDEX', 'ID MOBIL', 'NAMA MOBIL','MANUFACTURER', 'JUMLAH PENUMPANG', 'HARGA SEWA' ))
                print ('-----------+-----------------+-----------------+-----------------+------------------+---------------')
                print ("{:<10} | {:<15} | {:<15} | {:<15} | {:<2} seats{:<8} | Rp. {:<10}".format(index, id, dict_data_mobil[index]['Nama Mobil'], dict_data_mobil[index]['Manufacturer'], dict_data_mobil[index]['Jumlah Penumpang'], '', dict_data_mobil[index]['Harga Sewa']))
                
                menu_tampilkan_list_mobil()

            counter = counter + 1

            if counter == len(dict_data_mobil):
                print('Data mobil tidak berhasil ditemukan.\n')
                cari_data_mobil()

        else:
            print('\nTidak ada data mobil. Silahkan tambahkan data mobil terlebih dahulu.')
            menu_tampilkan_list_mobil()

###########################################################################################################################################################################################

# 2. Menu Create (Tambahkan Data Mobil)

def menu_tambahkan_data_mobil():
    print('''
MENU TAMBAHKAN DATA MOBIL
-----------------------------------------------------
1. Masukkan Data Mobil Baru
2. Kembali ke Menu Utama
        ''')
    while True:
        input_tambahkan_data = input('Masukkan angka yang ingin di pilih: ')

        if input_tambahkan_data.isnumeric():
            if input_tambahkan_data == '1': # masuk ke Menu Masukkan Data Mobil Baru
                tambah_data_mobil()
            elif input_tambahkan_data == '2': # balik ke Menu Utama
                menu_utama()
            else:
                print('Maaf, nomor menu yang dimasukkan tidak ditemukan. Silahkan masukkan nomor menu kembali.')
        else:
            print('Maaf, input yang dimasukkan bukanlah angka. Silahkan masukkan nomor menu kembali.')

# 2.1. Masukkan / Tambahkan Data Mobil Baru

def tambah_data_mobil():
    print ()
    global nama_mobil
    nama_mobil = input ('Masukkan nama mobil yang ingin ditambahkan: ').strip()
    nama_mobil = nama_mobil.capitalize()

    global manufacturer_mobil
    manufacturer_mobil = input ('Masukkan manufacturer mobil: ').strip()
    manufacturer_mobil = manufacturer_mobil.capitalize()

    input_jumlah_penumpang_mobil()

    input_harga_sewa_mobil()
        
    print ('\nApakah data mobil sudah sesuai?\n')
    print ("{:<15} | {:<15} | {:<16} | {:<14}".format('NAMA MOBIL','MANUFACTURER', 'JUMLAH PENUMPANG', 'HARGA SEWA' ))
    print ('----------------+-----------------+------------------+---------------')
    print ("{:<15} | {:<15} | {:<2} seats{:<8} | Rp. {:<10}".format(nama_mobil, manufacturer_mobil, jumlah_penumpang_mobil, '', harga_sewa_mobil))

    print ('''
Tekan Y apabila sudah sesuai.
Tekan N apabila belum sesuai.
        ''')

    konfirmasi_tambah_data()

# 2.1.1. Input Jumlah Penumpang Mobil

def input_jumlah_penumpang_mobil():
    global jumlah_penumpang_mobil
    jumlah_penumpang_mobil = (input ('Masukkan kapasitas penumpang dari mobil: ')).strip()

    if jumlah_penumpang_mobil.isnumeric():

        jumlah_penumpang_mobil = int(jumlah_penumpang_mobil)
        while 1 > jumlah_penumpang_mobil or 8 < jumlah_penumpang_mobil:
            print ('\nMaaf, jumlah penumpang yang dimasukkan tidak sesuai.')
            input_jumlah_penumpang_mobil()
    
    else:
        print ('\nInput yang dimasukkan bukanlah angka.')
        input_jumlah_penumpang_mobil()

# 2.1.2. Input Harga Sewa Mobil

def input_harga_sewa_mobil():
    global harga_sewa_mobil
    harga_sewa_mobil = (input ('Masukkan harga sewa dari mobil: ')).strip()

    if harga_sewa_mobil.isnumeric():

        if harga_sewa_mobil[0] == '0':
            print ('Harga sewa tidak bisa diawali oleh angka 0. \nSilahkan masukkan harga sewa kembali.\n')
            input_harga_sewa_mobil()

        elif len(harga_sewa_mobil) < 3 or int(harga_sewa_mobil) < 10000:
            print ('Harga yang dimasukkan terlalu rendah.\n')
            input_harga_sewa_mobil()
        
        elif len(harga_sewa_mobil) > 9:
            print ('Harga yang dimasukkan terlalu tinggi.\n')
            input_harga_sewa_mobil()
        else:
            pass

    else:
        print ('Input yang dimasukkan bukanlah angka.\n')
        input_harga_sewa_mobil() 

# 2.1.3. Konfirmasi Tambah Data

def konfirmasi_tambah_data():
    input_tambah_data = input('Masukkan huruf Y/N: ').strip()
    input_tambah_data = input_tambah_data.upper()

    list_angka_index = list(dict_data_mobil.keys())
    # hasilnya [0,1,2,3, dst.]

    if input_tambah_data.isalpha():
        if input_tambah_data == 'Y':

            while True:
                temp_dict = {max(list_angka_index) + 1: {'Nama Mobil' : nama_mobil, 'Manufacturer' : manufacturer_mobil, 'Jumlah Penumpang' : jumlah_penumpang_mobil, 'Harga Sewa' : harga_sewa_mobil, 'ID Mobil' : ' '}}
                
                # global dict_data_mobil
                dict_data_mobil.update(temp_dict)

                print ('Data mobil berhasil ditambahkan.')
                menu_tambahkan_data_mobil()
        
        elif input_tambah_data == 'N':
            print ('Penambahan data mobil dibatalkan. Silahkan masukkan kembali data mobil.')
            menu_tambahkan_data_mobil()

        else:
            print ('Maaf huruf yang dimasukkan tidak sesuai. Silahkan coba lagi.')
            konfirmasi_tambah_data()

    else:
        print ('Maaf, input yang dimasukkan bukanlah huruf. Silahkan masukkan huruf kembali.')
        konfirmasi_tambah_data()

###########################################################################################################################################################################################

# 3. Menu Update / Edit (Edit Data Mobil)

def menu_edit_data():
    print('''
MENU EDIT DATA MOBIL
-----------------------------------------------------
1. Edit Data Mobil
2. Kembali ke Menu Utama
        ''')
    while True:
        input_menu_edit = input('Masukkan angka yang ingin di pilih: ')

        if input_menu_edit.isnumeric():
            if input_menu_edit == '1': # masuk ke Menu Ubah Data Mobil
                edit_data_mobil()
            elif input_menu_edit == '2': # balik ke Menu Utama
                menu_utama()
            else:
                print('Maaf, nomor menu yang dimasukkan tidak ditemukan. Silahkan masukkan nomor menu kembali.')
        else:
            print('Maaf, input yang dimasukkan bukanlah angka. Silahkan masukkan nomor menu kembali.')

# 3.1. Edit Data Mobil

def edit_data_mobil():
    list_id_mobil.clear()

    print ("{:<10} | {:<15} | {:<15} | {:<15} | {:<16} | {:<14}".format('INDEX', 'ID MOBIL', 'NAMA MOBIL','MANUFACTURER', 'JUMLAH PENUMPANG', 'HARGA SEWA' ))
    print ('-----------+-----------------+-----------------+-----------------+------------------+---------------')
    append_id_mobil()

    if len(dict_data_mobil) >= 1:

        print('\nMobil manakah yang ingin diubah?')

        input_edit_data = input ('Masukkan ID kendaraan yang ingin diubah: ').strip()
        input_edit_data = input_edit_data.upper()
        counter = 0

        for id_edit in list_id_mobil:

            if input_edit_data == id_edit:
                
                global index_edit
                index_edit = list_id_mobil.index(input_edit_data)

                print()
                print ("{:<10} | {:<15} | {:<15} | {:<15} | {:<16} | {:<14}".format('INDEX', 'ID MOBIL', 'NAMA MOBIL','MANUFACTURER', 'JUMLAH PENUMPANG', 'HARGA SEWA' ))
                print ('-----------+-----------------+-----------------+-----------------+------------------+---------------')
                print ("{:<10} | {:<15} | {:<15} | {:<15} | {:<2} seats{:<8} | Rp. {:<10}".format(index_edit, input_edit_data, dict_data_mobil[index_edit]['Nama Mobil'], dict_data_mobil[index_edit]['Manufacturer'], dict_data_mobil[index_edit]['Jumlah Penumpang'], '', dict_data_mobil[index_edit]['Harga Sewa']))
                print('''
Kolom apakah yang ingin diedit?''')

                cari_kolom()
            
            counter = counter + 1
        
        if counter == len(dict_data_mobil):
            print('Data mobil tidak berhasil ditemukan.')
            menu_edit_data()
    
    else:
        print ('\nTidak ada data mobil. Silahkan tambahkan data mobil terlebih dahulu.')
        menu_edit_data()

# 3.1.1. Cari Kolom untuk diedit

def cari_kolom():
    print(f'''Nama Mobil / Manufacturer / Jumlah Penumpang / Harga Sewa\n''')

    input_kolom_edit = input('Masukkan nama kolom yang ingin diubah isinya: ').strip()
    input_kolom_edit = input_kolom_edit.upper() + '.'

    if input_kolom_edit.isalnum():
        print ('Maaf, input hanya dapat berupa alfabet saja. Silahkan masukkan nama kolom kembali')
        cari_kolom()

    elif input_kolom_edit.isnumeric():
        print ('Maaf, input input yang dimasukkan bukan huruf. Silahkan masukkan nama kolom kembali')
        cari_kolom()

    else:
        if input_kolom_edit == 'NAMA MOBIL.':

            input_kolom_nama = input ('Masukkan nama mobil baru: ').capitalize()

            while True:

                print(f'''Apakah perubahan nama mobil sudah sesuai?

Tekan huruf Y apabila sudah sesuai.
Tekan huruf N apabila belum sesuai.
                ''')

                input_konfirmasi_nama_mobil = input ('Masukkan huruf Y/N: ').strip()
                input_konfirmasi_nama_mobil = input_konfirmasi_nama_mobil.upper()

                if input_konfirmasi_nama_mobil == 'Y':

                    dict_data_mobil[index_edit]['Nama Mobil'] = input_kolom_nama

                    print ('Data nama mobil berhasil di ubah.')
                    menu_edit_data()
                
                elif input_konfirmasi_nama_mobil == 'N':
                    print ('Data nama mobil tidak berhasil di ubah.')
                    menu_edit_data()
                
                else:
                    print ('Maaf huruf yang dimasukkan tidak sesuai. Silahkan coba lagi.')
                    continue
#------------------------------------------------------------------------------------------------------------------
        elif input_kolom_edit == 'MANUFACTURER.':

            input_kolom_manufacturer = input ('Masukkan manufacturer mobil baru: ').capitalize().strip()

            while True:
                
                print(f'''Apakah perubahan manufacturer sudah sesuai?

Tekan huruf Y apabila sudah sesuai.
Tekan huruf N apabila belum sesuai.
                ''')

                input_konfirmasi_manufacturer = input ('Masukkan huruf Y/N: ').strip()
                input_konfirmasi_manufacturer = input_konfirmasi_manufacturer.upper()

                if input_konfirmasi_manufacturer == 'Y':

                    dict_data_mobil[index_edit]['Manufacturer'] = input_kolom_manufacturer

                    print ('Data manufacturer berhasil di ubah.')
                    menu_edit_data()
                
                elif input_konfirmasi_manufacturer == 'N':
                    print ('Data manufacturer tidak berhasil di ubah.')
                    menu_edit_data()
                
                else:
                    print ('Maaf huruf yang dimasukkan tidak sesuai. Silahkan coba lagi.')
                    continue

#------------------------------------------------------------------------------------------------------------------
        elif input_kolom_edit == 'JUMLAH PENUMPANG.':

            input_jumlah_penumpang_mobil()

            while True:
                print(f'''Apakah perubahan jumlah penumpang sudah sesuai?

Tekan huruf Y apabila sudah sesuai.
Tekan huruf N apabila belum sesuai.
                ''')

                input_konfirmasi_penumpang = input ('Masukkan huruf Y/N: ').strip()
                input_konfirmasi_penumpang = input_konfirmasi_penumpang.upper()

                if input_konfirmasi_penumpang == 'Y':

                    dict_data_mobil[index_edit]['Jumlah Penumpang'] = input_jumlah_penumpang_mobil()

                    print ('Data jumlah penumpang berhasil di ubah.')
                    menu_edit_data()
                
                elif input_konfirmasi_penumpang == 'N':
                    print ('Data jumlah penumpang tidak berhasil di ubah.')
                    menu_edit_data()
                
                else:
                    print ('Maaf huruf yang dimasukkan tidak sesuai. Silahkan coba lagi.')
                    continue

#------------------------------------------------------------------------------------------------------------------
        elif input_kolom_edit == 'HARGA SEWA.':

            input_harga_sewa_mobil()

            while True:
                print(f'''Apakah perubahan harga sewa sudah sesuai?

Tekan huruf Y apabila sudah sesuai.
Tekan huruf N apabila belum sesuai.
                ''')

                input_konfirmasi_harga = input ('Masukkan huruf Y/N: ').strip()
                input_konfirmasi_harga = input_konfirmasi_harga.upper()

                if input_konfirmasi_harga == 'Y':

                    dict_data_mobil[index_edit]['Harga Sewa'] = input_harga_sewa_mobil()

                    print ('Data harga sewa berhasil di ubah.')
                    menu_edit_data()
                
                elif input_konfirmasi_harga == 'N':
                    print ('Data harga sewa tidak berhasil di ubah.')
                    menu_edit_data()
                
                else:
                    print ('Maaf huruf yang dimasukkan tidak sesuai. Silahkan coba lagi.')
                    continue
#------------------------------------------------------------------------------------------------------------------
        elif input_kolom_edit == 'ID MOBIL.':
            print('ID Mobil tidak dapat diubah. Silahkan input kolom lain.')
            cari_kolom()
#------------------------------------------------------------------------------------------------------------------
        else:
            print ('Kolom tidak ditemukan. Silahkan masukkan nama kolom kembali')
            cari_kolom()

###########################################################################################################################################################################################

# 4. Menu Delete (Hapus Data Mobil)

def menu_hapus_data():
    print('''
MENU DELETE DATA MOBIL
-----------------------------------------------------
1. Delete Data Mobil sesuai ID Kendaraan
2. Kembali ke Menu Utama
        ''')
    while True:
        input_menu_delete = input('Masukkan angka yang ingin di pilih: ')

        if input_menu_delete.isnumeric():
            if input_menu_delete == '1': # masuk ke Menu Hapus Data Mobil
                remove_data()
                break
            elif input_menu_delete == '2': # balik ke Menu Utama
                menu_utama()
            else:
                print('Maaf, nomor menu yang dimasukkan tidak ditemukan. Silahkan masukkan nomor menu kembali.')
        else:
            print('Maaf, input yang dimasukkan bukanlah angka. Silahkan masukkan nomor menu kembali.')

# 4.1. Delete Data

def remove_data():
    list_id_mobil.clear()

    print ("{:<10} | {:<15} | {:<15} | {:<15} | {:<16} | {:<14}".format('INDEX', 'ID MOBIL', 'NAMA MOBIL','MANUFACTURER', 'JUMLAH PENUMPANG', 'HARGA SEWA' ))
    print ('-----------+-----------------+-----------------+-----------------+------------------+---------------')
    append_id_mobil()

    if len(dict_data_mobil) <= 0:
        print('\nTidak ada data mobil. Silahkan tambahkan data mobil terlebih dahulu.')
        menu_hapus_data()
    
    else:

        print ()
        input_hapus_data = input ('Masukkan ID kendaraan yang ingin dihapus: ').strip()
        input_hapus_data = input_hapus_data.upper()
        
        global count_remove
        count_remove = 0

        counter = 0

        for index in dict_data_mobil.keys():

            id_remove = dict_data_mobil[index]['ID Mobil']
            # ambil id mobilnya based on index dari setiap index dari dictionary besar

            if input_hapus_data == id_remove:
                # input nya dibandingin sama 

                print()
                print(f"Apakah anda yakin mobil dengan ID '{input_hapus_data}' akan dihapus?")
                print ("{:<10} | {:<15} | {:<15} | {:<15} | {:<16} | {:<14}".format('INDEX', 'ID MOBIL', 'NAMA MOBIL','MANUFACTURER', 'JUMLAH PENUMPANG', 'HARGA SEWA' ))
                print ('-----------+-----------------+-----------------+-----------------+------------------+---------------')
                print ("{:<10} | {:<15} | {:<15} | {:<15} | {:<2} seats{:<8} | Rp. {:<10}".format(index, input_hapus_data, dict_data_mobil[index]['Nama Mobil'], dict_data_mobil[index]['Manufacturer'], dict_data_mobil[index]['Jumlah Penumpang'], '', dict_data_mobil[index]['Harga Sewa']))

                print('''
Tekan huruf Y apabila sudah sesuai.
Tekan huruf N apabila belum sesuai.
                ''')

                konfirmasi_remove_data = input ('Masukkan huruf Y/N: ')
                konfirmasi_remove_data = konfirmasi_remove_data.upper()

                if konfirmasi_remove_data == 'Y':
                    del dict_data_mobil[index]
                    print (f"Data dengan ID '{input_hapus_data}' telah berhasil dihapus.")

                    menu_hapus_data()

                elif konfirmasi_remove_data == 'N':
                    remove_data()

                else:
                    print ('Maaf huruf yang dimasukkan tidak sesuai. Silahkan coba lagi.')
                    remove_data()
                    
            counter = counter + 1
            
        if counter == len(dict_data_mobil):
            print('Data mobil tidak berhasil ditemukan.')
            menu_hapus_data()

###########################################################################################################################################################################################

# 5. Menu Exit Confirmation

def menu_exit():
    print ('''
Apakah anda yakin ingin mengakhiri program ini?
           
Input 1: apabila ingin mengakhiri program.
Input 2: apabila ingin kembali ke menu utama.
           ''')
    
    while True:
        input_exit_confirmation = input('Masukkan angka yang ingin di pilih: ')

        if input_exit_confirmation:
            if input_exit_confirmation == '1': # exit program
                print('Terima kasih. Sampai jumpa kembali')
                break
            elif input_exit_confirmation == '2': # balik ke Menu Utama
                menu_utama()
            else:
                print('Maaf, nomor menu yang dimasukkan tidak ditemukan. Silahkan masukkan nomor menu kembali.')
        else:
            print('Maaf, input yang dimasukkan bukanlah angka. Silahkan masukkan nomor menu kembali.')

menu_utama()
