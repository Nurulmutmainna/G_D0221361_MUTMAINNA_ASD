nama="mutmainna"
gaji_pokok= 1000000
lama_lembur = 11
gaji_lemburperjam=5000
gaji_lembur= gaji_lemburperjam *lama_lembur
gaji_kotor= gaji_pokok + gaji_lembur
pajak =9/100
potongan=gaji_pokok*pajak
gaji_bersih=gaji_kotor-potongan
print("nama: ",nama)
print("gaji pokok=Rp",gaji_pokok)
print("gaji_lembur/jam=Rp",gaji_lemburperjam)
print("gaji lembur =Rp",gaji_lembur)
print("gaji kotor  =Rp",gaji_kotor)
print("pajak =",pajak)