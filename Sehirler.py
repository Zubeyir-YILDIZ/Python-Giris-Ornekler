from tkinter import *

class sehirler:
    def __init__(self):
        anaPencere=Tk()
        anaPencere.title('TÜRKİYE-ŞEHİRLER')

        self.kısaltmaları=StringVar()
        self.şehirAdı=StringVar()
        self.nesiMeşhur=StringVar()
        self.bölgesi=StringVar()
        self.plakaKodu=StringVar()

        kisaltmaPenceresi=Frame(anaPencere)
        kisaltmaPenceresi.pack(side='left')
        bilgipenceresi1=Frame(anaPencere)
        bilgipenceresi1.pack(side='right')
        bilgipenceresi2=Frame(bilgipenceresi1)
        bilgipenceresi2.pack(side='bottom')
        bilgipenceresi3=Frame(bilgipenceresi1)
        bilgipenceresi3.pack(side='bottom')
        bilgipenceresi4=Frame(bilgipenceresi1)
        bilgipenceresi4.pack(side='bottom')

        kaydırmaÇubuğuY=Scrollbar(anaPencere,orient=VERTICAL)
        kaydırmaÇubuğuY.pack(side='right',fill=Y)
        
        etiket1=Label(kisaltmaPenceresi,text='Kısaltma')
        etiket1.pack(side='left')
        etiket2=Label(bilgipenceresi1,text='Şehir Adı:')
        etiket3=Label(bilgipenceresi2,text='Nesi Meşhur:')
        etiket4=Label(bilgipenceresi3,text='Bölgesi:')
        etiket5=Label(bilgipenceresi4,text='Plaka Kodu:')

        girdiKutusu1=Entry(bilgipenceresi1,state='readonly',textvariable=self.şehirAdı)
        girdiKutusu2=Entry(bilgipenceresi2,state='readonly',textvariable=self.nesiMeşhur)
        girdiKutusu3=Entry(bilgipenceresi3,state='readonly',textvariable=self.bölgesi)
        girdiKutusu4=Entry(bilgipenceresi4,state='readonly',textvariable=self.plakaKodu)

        etiket2.pack(side='left')
        girdiKutusu1.pack(side='left')
        etiket3.pack(side='left')
        girdiKutusu2.pack(side='left')
        etiket4.pack(side='left')
        girdiKutusu3.pack(side='right')
        etiket5.pack(side='left')
        girdiKutusu4.pack(side='right')
        
        self.kısaltmalar={line.split(',')[1].rstrip() for line in open('sehirler.txt','r')} #şehir adı,kısaltması,bölgesi,nesi meşhur,plaka kodu
        self.kısaltmalar=list(self.kısaltmalar)                                                         #tipinde bir metin belgesi
        self.kısaltmalar.sort()
        self.kısaltmaları.set(tuple(self.kısaltmalar))

        self.kısaltmaListesi=Listbox(kisaltmaPenceresi,height=10,width=len(self.kısaltmalar[1])+2,yscrollcommand=kaydırmaÇubuğuY.set,listvariable=self.kısaltmaları)
        #self.kısaltmaListesi.bind("<<ListboxSelect>>",self.bilgileriGetir)
        self.kısaltmaListesi.pack()
        
        kaydırmaÇubuğuY['command']=self.kısaltmaListesi.yview
          
        anaPencere.mainloop()
        
    def bilgileriGetir(self,eylem):
        indis=self.kısaltmaListesi.get(self.kısaltmaListesi.curselection())
        self.sehirBilgileri=[line.split(',') for line in open('sehirler.txt','r') if line.split(',')[1]==indis]
        self.şehirAdı.set(self.sehirBilgileri[0][0])
        self.bölgesi.set(self.sehirBilgileri[0][2])
        self.nesiMeşhur.set(self.sehirBilgileri[0][3])
        self.plakaKodu.set(self.sehirBilgileri[0][4])
    


sehirler()