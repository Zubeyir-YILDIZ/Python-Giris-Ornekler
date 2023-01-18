ornekMetin=open("ornek_metin.txt","r")
metin= ornekMetin.readline()    

while(metin!=""):
    metin=ornekMetin.readline()
    metin_liste=metin.split(" ")
    ad_soyad=metin_liste[0]
    if(len(ad_soyad.split("-"))==3):
        ad=ad_soyad.split("-")[0]+" "+ ad_soyad.split("-")[1]
        soyad=ad_soyad.split("-")[2]
    else:
        ad=ad_soyad.split("-")[0]
        soyad=ad_soyad.split("-")[1]
    notlar=metin_liste[-1]
    not1=int(notlar.split("/")[0])
    not2=int(notlar.split("/")[1])
    not3=int(notlar.split("/")[2])
    ortalama=not1*0.3 + not2*0.3 + not3*0.4
    if(len(metin_liste)==4):
        bolum=metin_liste[1]+" "+metin_liste[2]
    else:
        bolum=metin_liste[1]
    if(ortalama>=60 and not3>=70):
        g=open("gecenler.txt","a")
        g.write(ad+soyad+" ")
        g.write(bolum+" ")
        g.write(str(not1)+" "+str(not2)+" "+str(not3)+" ")
        g.write("Ortalama= "+str(ortalama)+" ")
        g.write("\n")
    else:
        k=open("kalanlar.txt","a")
        k.write(ad+soyad+" ")
        k.write(bolum+" ")
        k.write(str(not1)+" "+str(not2)+" "+str(not3)+" ")
        k.write("Ortalama= "+str(ortalama)+" ")
        k.write("\n")
ornekMetin.close()



