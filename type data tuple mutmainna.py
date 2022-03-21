#perulangan
tuple=(3,4,5,6)
for i in (tuple) :
	print(i)
	
#mengupdate
tuple=(3,4,5,6)
tup =list(tuple)
tup [0] ="angka"
print(tup)

#menghapus
tup.remove("angka")
print(tup)

#menambahkan
tup.extend(["bilangan"])
print(tup)
