import random 

isimler = input("İsim aralarına virgul koyarak isim giriniz: \n")

isimlerDizi = isimler.split(',')
ogrenciSayi = len(isimlerDizi)

kisi = input("Gruplar kaç kişilik olsun? \n")
kisiSayi = int(kisi)

takim = ogrenciSayi / kisiSayi 
takimSayi = int(takim )

for i in range(takimSayi +1 ):
    for a in range(kisiSayi):
        if len(isimlerDizi) != 0:  
            grup_ind= random.randint(0, len(isimlerDizi) -1)
            grup = isimlerDizi[grup_ind ]
            print (grup )
            del isimlerDizi[grup_ind ]
        
    print ("\n")
