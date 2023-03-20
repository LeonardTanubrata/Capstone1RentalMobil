rentalmob = {
    '0001':{'ID':'0001',
            'Warna':'Hitam',
            'Jenis mobil':'Avanza', 
            'Transmisi':'Manual', 
            'Harga':'250000',
            'Plat':'BP0002'},

    '0002':{'ID':'0002',
            'Warna':'Kuning', 
            'Jenis mobil':'Brio', 
            'Transmisi':'Matic', 
            'Harga':'300000',
            'Plat':'BP0003'},

    '0003':{'ID':'0003',
            'Warna':'Perak', 
            'Jenis mobil':'Calya', 
            'Transmisi':'Manual', 
            'Harga':'200000',
            'Plat':'BP0004'},
    
    '0004':{'ID':'0004',
            'Warna':'Hitam', 
            'Jenis mobil':'Raize', 
            'Transmisi':'Matic', 
            'Harga':'400000',
            'Plat':'BP0005'},

    '0005':{'ID':'0005',
            'Warna':'Putih', 
            'Jenis mobil':'Innova', 
            'Transmisi':'Manual', 
            'Harga':'500000',
            'Plat':'BP0001'}
}




# Function Pilihan Salah/Tidak Tersedia
def tidak_tersedia():                               
    print ('''
    ============================================= 
              Pilihan Tidak Tersedia 
    ============================================= 
    ''')
    print ('''
    ======= Masukkan Kembali Pilihan Anda =======
    \n''')

# Function List Kalo Kosong
def nodata():                                       
    print ('''\n
    ============================================= 
                   Data Tidak Ada
    ============================================= 
    \n''')

 # Function Data Berhasil Tersimpan
def data_tersimpan():                                   
    print ('''
    ============================================= 
               Data Berhasil Disimpan 
    =============================================
    \n''')

# Function Data Terhapus
def data_terhapus():                                    
    print ('''
    ============================================= 
               Data Berhasil Dihapus 
    =============================================
    \n''')





def data_mobil():
    print('\n                  Daftar Mobil Janoi Car Rental \n    =============================================================')
    print(f'    {"ID":<5}| {"Warna":<10}| {"Jenis mobil":<12}| {"Transmisi":<10}| {"Harga":<7}| {"Plat":<9}\n    =============================================================')
    count = 0
    if len(rentalmob) == 0:
        nodata()
    for i, val in rentalmob.items():
        print(f"    {rentalmob[i]['ID']:<5}| {rentalmob[i]['Warna']:<10}| {rentalmob[i]['Jenis mobil']:<12}| {rentalmob[i]['Transmisi']:<10}| {rentalmob[i]['Harga']:<7}| {rentalmob[i]['Plat']:<9}")
        count = count+1


# Menu 1.2 cari data dalam data mobil
def cari_daftar():                                          
    if rentalmob == {} :
        nodata()
    else :
        pencarian = input("\n\n    Masukkan ID Yang Dicari: ")
        while len(pencarian) != 4 :
            print ('''\n\n    Masukkan 4 Angka ID (0-9)(Hanya Angka)\n\n''')
            pencarian = input("\n\n    Masukkan ID Yang Dicari: ")

        print('\n                  Daftar Mobil Janoi Car Rental \n     =============================================================')
        print(f'     {"ID":<5}| {"Warna":<10}| {"Jenis mobil":<12}| {"Transmisi":<10}| {"Harga":<7}| {"Plat":<9}\n     =============================================================')
        
        if pencarian in rentalmob:
                print(f"     {rentalmob[pencarian]['ID']:<5}| {rentalmob[pencarian]['Warna']:<10}| {rentalmob[pencarian]['Jenis mobil']:<12}| {rentalmob[pencarian]['Transmisi']:<10}| {rentalmob[pencarian]['Harga']:<7}| {rentalmob[pencarian]['Plat']:<9}")
                
        else:
            print (f'''\n
        === ID : "{pencarian}" Tidak Ditemukan ===
            \n\n''')

def menu1():
    while True:
        print('''
    ===========================
               Menu 1
    ===========================
    1. Report Mobil
    2. Cari Mobil Spesifik
    6. Kembali ke Menu Utama 
        ''')
        pilih_menu1 = (input('\n    Masukkan Pilihan Anda : '))
        if pilih_menu1 == '1':
            data_mobil()
            menu1()
            break
        elif pilih_menu1 == '2':
            cari_daftar()
            break
        elif pilih_menu1 == '6':
            main_menu()
            break
        else:
            tidak_tersedia()
            break



def menu2tambah () :
    pilihan_menu_create_data = input ('''
          
    ========================       
             Menu 2
    ========================
    1. Tambah Data Mobil
    6. Kembali ke Menu Utama
        
    Masukkan angka Menu yang ingin dijalankan : ''')
    if pilihan_menu_create_data == '1' :
        tambah_baru()
    elif pilihan_menu_create_data == '6' :
        main_menu()
    else:
        tidak_tersedia()

    
def tambah_baru():
    print(f'''
          
    ========================       
        Menu Tambah Mobil
    ========================

    {data_mobil()}
        
        ''')   
    id_baru = input('''    Masukkan 4 Angka ID Mobil Baru : ''')
    while len(id_baru) != 4 :
        print ('''\n\n    Masukkan 4 Angka (0-9)(Hanya Angka)\n\n''')
        id_baru = input('''    Masukkan 4 Angka ID Mobil Baru: ''')
    if id_baru in rentalmob:
            print ('''
    ======================
        Data Sudah Ada 
    ======================''')
            
            tambah_baru()
    if id_baru != rentalmob:
        warna_baru = input('''    Masukkan Warna Mobil Baru: ''')
        while len(warna_baru) > 10:
            print('\n    == Input Terlalu Panjang Silahkan Ulangi ==')
            return warna_baru
        jenis_baru = input('''    Masukkan Jenis Mobil Baru: ''')
        while len(jenis_baru) > 10:
            print('\n    == Input Terlalu Panjang Silahkan Ulangi ==')
            return jenis_baru
        transmisi_baru = input('''    Masukkan Transmisi Mobil Baru: ''')
        while len(transmisi_baru) > 10:
            print('\n    == Input Terlalu Panjang Silahkan Ulangi ==')
            return transmisi_baru
        harga_baru = (input('''    Masukkan Harga Mobil Baru: '''))
        if harga_baru.isalpha():
            print('\n    == Masukan Angka Bukan Huruf ! ==')
            return harga_baru
        while len(harga_baru) >= 7:
            print('\n    == Input Terlalu Panjang Silahkan Ulangi ==')
            return harga_baru
        plat_baru = input('''    Masukan Plat Mobil : ''')
        while len(plat_baru) >= 7:
            print('\n    == Input Terlalu Panjang Silahkan Ulangi ==')
            return plat_baru
        check = input(f'''    Input:
      ID Baru : {id_baru}

      Warna Mobil: {warna_baru}

      Jenis Mobil: {jenis_baru}

      Transmisi Mobil: {transmisi_baru}

      Harga Mobil: {harga_baru}
      
      Plat Mobil : {plat_baru}
\n    Tambahkan Data? (Y/N): ''')
        while check.lower() != 'y' :
            break
        else:
            rentalmob[id_baru]={'ID':id_baru.upper(),'Warna':warna_baru.capitalize(), 'Jenis mobil':jenis_baru.capitalize(), 'Transmisi':transmisi_baru.capitalize(), 'Harga':harga_baru.upper(), 'Plat':plat_baru.upper()}
            data_tersimpan()
        data_mobil()
        menu2tambah()
   

#Mengedit Data Mobil yang Sudah Ada 
def menu3ubah():                                  
    pilihan_menu_update = input('''
    ========================
             Menu 3
    ========================
    1. Update / Ubah Data
    6. Kembali ke Menu Utama
    
    Masukkan angka Menu yang ingin dijalankan : ''')
    if pilihan_menu_update == '1' :
        update_by_id()
    elif pilihan_menu_update == '6' :
        main_menu()
    else :
        tidak_tersedia()

def update_by_id():                                       
    data_mobil()
    cari_id = input('''\n\n    Masukkan 4 Angka ID (0-9)(Hanya angka): ''')
    while len(cari_id) != 4 :
        print ('''\n\n    Masukkan 4 Angka (0-9)(Hanya Angka)\n\n''')
        cari_id = input('''\n\n    Masukkan 4 Angka ID (0-9)(Hanya Angka):  ''')
    # for x in rentalmob.keys() :
    if cari_id in rentalmob :
            pilihan_update_id = input(f'''
    =================================
                  Menu 3
    =================================
    1. Ubah Warna Mobil
    2. Ubah Jenis Mobil
    3. Ubah Transmisi Mobil
    4. Ubah Harga Mobil
    5. Ubah Plat Mobil
        
    9. Kembali Ke Menu Sebelumnya
    6. Kembali Ke Menu Utama

    Data ID Ditemukan: "{cari_id}"
    =================================
    Pilih Menu : ''')
            if pilihan_update_id == '1' :
                ubah_warna = input('''    Warna Mobil Diganti Menjadi: ''')
                while len(ubah_warna) > 10:
                    print('\n    == Input Terlalu Panjang Silahkan Ulangi ==')
                    return ubah_warna
                check_warna = input(f'''    Ubah Warna Mobil Menjadi "{ubah_warna}" (Y/N): ''')
                while check_warna.lower() != 'y' :
                    break
                else:
                    rentalmob[cari_id]['Warna'] = ubah_warna.capitalize()
                    data_tersimpan()
                    data_mobil()
            elif pilihan_update_id == '2' :
                ubah_jenis = input('''    Jenis Mobil Diganti Menjadi: ''')
                while len(ubah_jenis) > 10:
                    print('\n    == Input Terlalu Panjang Silahkan Ulangi ==')
                    return ubah_jenis
                check_jenis = input(f'''    Ubah Jenis Mobil Menjadi "{ubah_jenis}" (Y/N): ''')
                while check_jenis.lower() != 'y' :
                    break
                else:
                    rentalmob[cari_id]['Jenis mobil'] = ubah_jenis
                    data_tersimpan()
                    data_mobil()
            elif pilihan_update_id == '3' :
                ubah_transmisi = input('''    Transmisi Mobil Diganti Menjadi: ''')
                while len(ubah_transmisi) > 10:
                    print('\n    == Input Terlalu Panjang Silahkan Ulangi ==')
                    return ubah_transmisi
                check_transmisi = input(f'''    Ubah Transmisi Mobil Menjadi "{ubah_transmisi}" (Y/N): ''')
                while check_transmisi.lower() != 'y' :
                    break
                else:
                    rentalmob[cari_id]['Transmisi'] = ubah_transmisi.capitalize()
                    data_tersimpan()
                    data_mobil()
            elif pilihan_update_id == '4' :
                ubah_harga = input('''    Harga Mobil Diganti Menjadi: ''')
                if ubah_harga.isalpha():
                    print('\n    == Masukan Angka Bukan Huruf ! ==')
                    return ubah_harga
                while len(ubah_harga) > 10:
                    print('\n    == Input Terlalu Panjang Silahkan Ulangi ==')
                    return ubah_harga
                check_harga = input(f'''    Ubah Harga Mobil Menjadi "{ubah_harga}" (Y/N): ''')
                while check_harga.lower() != 'y' :
                    break
                else:
                    rentalmob[cari_id]['Harga'] = ubah_harga.upper()
                    data_tersimpan()
                    data_mobil()
            elif pilihan_update_id == '5' :
                ubah_plat = input('''    Plat Mobil Diganti Menjadi: ''')
                while len(ubah_plat) > 10:
                    print('\n    == Input Terlalu Panjang Silahkan Ulangi ==')
                    return ubah_plat
                check_plat = input(f'''    Ubah Plat Mobil Menjadi "{ubah_plat}" (Y/N): ''')
                while check_plat.lower() != 'y' :
                    break
                else:
                    rentalmob[cari_id]['Plat'] = ubah_plat.upper()
                    data_tersimpan()
                    data_mobil()
            elif pilihan_update_id == '9' :
                menu3ubah()
            elif pilihan_update_id == '0' :
                main_menu()
            else:
                tidak_tersedia()
            menu3ubah()
    if cari_id not in rentalmob :
            print (f'''\n
    ID : "{cari_id}" Tidak Ditemukan
            \n\n''')
            menu3ubah()

# menu 4 delete data
def menu4delete():                                  
    data_mobil()

    pilihan_menu_delete = input('''
    ======================================
              HAPUS DATA MOBIL 
    ======================================
    1. Hapus Data (Input ID Mobil)
    6. Kembali Ke Menu Utama
    ======================================
    Pilih Menu : ''')
    if pilihan_menu_delete == '1' :
        hapus_data()
    elif pilihan_menu_delete == '6' :
        main_menu()
    else:
        tidak_tersedia()


def hapus_data():                                           # SUBMENU (4)-(1) HAPUS DATA -------------------
    data_mobil()
    cari_id = input('''\n\n    Masukkan 4 Angka ID Mobil (0-9)(Hanya Angka): ''')
    if len(cari_id) != 4 :
        print ('''\n\n    Masukkan 4 Angka (0-9)(Hanya Angka)\n\n''')
        cari_id = input('''\n\n    Masukkan 4 Angka ID (0-9): ''')
    print(f'    {"ID":<5}| {"Warna":<10}| {"Jenis mobil":<12}| {"Transmisi":<10}| {"Harga":<7}| {"Plat":<9}')
    # for x in rentalmob.keys() :
    if cari_id in rentalmob:
            print(f"    {rentalmob[cari_id]['ID']:<5}| {rentalmob[cari_id]['Warna']:<10}| {rentalmob[cari_id]['Jenis mobil']:<12}| {rentalmob[cari_id]['Transmisi']:<10}| {rentalmob[cari_id]['Harga']:<7}| {rentalmob[cari_id]['Plat']:<9}")
            pilihan_hapus_id = input(f'''\n\n    Anda Yakin Hapus Entry Dengan ID "{cari_id}" ? (Y/N): ''')
            while pilihan_hapus_id.lower() != 'y' :
                break
            else:
                del rentalmob[cari_id]
                data_terhapus()
                menu4delete()
            
    
    if cari_id not in rentalmob :
        print (f'''\n
    ID : "{cari_id}" Tidak Ditemukan
    \n\n''')  



def quit():
    in_quit = input('    Apakah Anda Yakin Ingin Keluar Y/N : ').upper()
    while True:
    
        if in_quit == 'Y' :
                print ('''\n\n
    ===============================================
                 SAMPAI JUMPA KEMBALI 
    ===============================================
            \n\n''')
                break
        elif in_quit == 'N':
            main_menu() 
            break

        else :
            tidak_tersedia()
            main_menu()
            break

def main_menu():
    pilihan_menu_utama= input(f'''\33[1m\33[92m
    ===========================       
              Hello!
    Welcome to Janoi Car Rental
    ===========================
    Menu Utama:
    1. Data Mobil
    2. Nambah Data Mobil
    3. Ubah Data Mobil
    4. Hapus Data Mobil
    5. Keluar
    ===========================
    Pilih Menu (1 - 5) : ''')
    while True:
        if pilihan_menu_utama == '1':
            menu1()
        elif pilihan_menu_utama == '2':
            menu2tambah()
        elif pilihan_menu_utama == '3':
            menu3ubah()
        elif pilihan_menu_utama == '4':
            menu4delete()
        elif pilihan_menu_utama == '5':
            quit()
            break
               
        else:
            tidak_tersedia()
            main_menu()






main_menu()