jumlah_item= 0
listvrbl=[]
while jumlah_item != 9 :
    print("--------")
    print("1. menampilkan nilai")
    print("2. menambahkan nama barang ke dalam list")
    print("3. menghapus nama barang dari list")
    print("4. mengubah barang dalam list")
    print("5. menampilakan barang dalam list")
    print("6. memeriksa barang dalam list")
    print("7. mencari index barang")
    print("9. keluar")
    jumlah_item = int(input("pilih salah satu menu:"))
    if jumlah_item== 1 :
        barang = 0
        if len (listvrbl) > 0 :
            while barang < len(listvrbl[barang]):
                print(barang,".",listvrbl[barang])
                barang = barang = 1
        else :
            print("tidak ada list:")
    elif jumlah_item == 2 :
        name = input("masukkan  barang :")
        listvrbl.append(name)
        print(listvrbl)
    elif jumlah_item == 3 :
        del_name = input("masukkan barang yang ingin dihapus :")
        if del_name in listvrbl :
            item_number = listvrbl.index(del_name)
            del listvrbl[item_number]
            print(listvrbl)
        else :
            print (del_name, "barang tidak ditemukan")
    elif jumlah_item == 4 :
        old_name = input("barang apa yang ingin di ubah :")
        if old_name in listvrbl:
            item_number = listvrbl.index(old_name)
            new_item = input("barang baru :")
            listvrbl[item_number]= new_item
            print(listvrbl)
        else :
            print(old_name, " barang tidak ditemukan")
    elif jumlah_item == 5 :
        print(listvrbl)
    elif jumlah_item == 6 :
        barang_yang_ingin_dicari = input("masukkan barang yang ingin dicari :")
        if barang_yang_ingin_dicari in listvrbl :
            print("barang ini terdapat dalam listvrbl")
        elif barang_yang_ingin_dicari not in listvrbl:
            print("barang ini tidak terdapat dalam namelist")
    elif jumlah_item == 7 :
        print(listvrbl)
        barang_yang_ingin_dicari = input("masukkan barang yang ingin dicari :")
        print(barang_yang_ingin_dicari,"berada pada indeks",listvrbl.index(barang_yang_ingin_dicari))
        
print("see uu")
