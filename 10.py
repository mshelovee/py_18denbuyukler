#KLAVYEDEN GİRİLEN 10 KİŞİNİN YAŞLARI 18' DEN BÜYÜK OLANLARIN SAYISINI HESAPLAYAN PROGRAM
yaşlar = []
for i in range(10):
    yaş = int(input("{}. kişinin yaşını girin: ".format(i + 1))) 
    yaşlar.append(yaş)  
onsekizden_büyük_olanlar = 0 # on sekiz yasindan buyuk olanlarin sayisi
#append: listeler , birleştirir 
for yaş in yaşlar:
    if yaş > 18:
        onsekizden_büyük_olanlar += 1
print("18 yaşından büyük olan kişi sayısı:", onsekizden_büyük_olanlar)