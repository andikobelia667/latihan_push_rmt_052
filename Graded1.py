list_pesanan =[]

def tambah_pesanan():
    enter = input("Mau Pesan Apa")
    catetan = input("Catetannya apa")
    pesanan = {"nama" : enter, "catetan" : catetan}

    list_pesanan.append(pesanan)
    print(f'{enter} Berhasil ditambahkan\n')

def hapus_pesanan():
    hapus = input('Apa pesanan yang mau dihapus ?\n')
    for pesanan in list_pesanan :
        if pesanan ["nama"] == hapus :
            list_pesanan.remove(pesanan)
            print('Berhasil dihapus')
            break

        else :
            print('Kamu belom memesan itu')
    else :
            print('Kamu belom ada pesanan')
    

def lihat_pesanan():
    if len(list_pesanan) > 0 :
        print(list_pesanan)
    else :
        print('Kamu Tidak ada Pesanan')

def menu():

    while True:
        print("\n Selamat Datang :")
        print("1. Pesan")
        print("2. Hapus Pesanan")
        print("3. Lihat Pesanan")
        print("4. Tidak jadi pesan")
        print("Mau yang mana")
        
        pilihan = int(input("Pilih nomor berapa ?"))

        if pilihan == 1:
            tambah_pesanan()

        elif pilihan == 2:
            hapus_pesanan()

        elif pilihan == 3:
            lihat_pesanan()

        elif pilihan == 4:
            print("Ditunggu kedatangan selanjutnya\n")
            break

        else :
            print("Menu yang kamu pilih tidak  ada")

menu()