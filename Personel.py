from tkinter import *

class Personel:
    
    def __init__(self):

        anaPencere=Tk()
        anaPencere.title('Personel')
        menüÇubuğu=Menu(anaPencere)
        işlemler=Menu(menüÇubuğu,tearoff=0)
        menüÇubuğu.add_cascade(label='işlemler',menu=işlemler)
        işlemler.add_command(label='çıkış',command=anaPencere.destroy)
        anaPencere.config(menu=menüÇubuğu)

        #self.soyad=StringVar()
        self.yaş=StringVar()
        self.maaş=StringVar()
        self.sicilNumarası=StringVar()
        self.izinSüresi=StringVar()
        self.çalışmaSaati=StringVar()
        self.isim=StringVar()
        self.uzmanlık=StringVar()

        etiketUZMANLIK_ALANLARI=Label(anaPencere,text='Uzmanlık Alanları')
        etiketUZMANLIK_ALANLARI.grid(row=2,column=0,sticky=W)
        etiketİSİM=Label(anaPencere,text='İsimler')
        etiketİSİM.grid(row=22,column=0,sticky=W)
        yaşEtiketi=Label(anaPencere,text='Yaş:')
        yaşEtiketi.grid(row=15,column=0,sticky=E)
        maaşEtiketi=Label(anaPencere,text='Maaş:')    
        maaşEtiketi.grid(row=16,column=0,sticky=E)
        sicilNumarasıEtiketi=Label(anaPencere,text='Sicil Numarası:')
        sicilNumarasıEtiketi.grid(row=17,column=0,sticky=E)
        izinSüresiEtiketi=Label(anaPencere,text='İzin Süresi:')
        izinSüresiEtiketi.grid(row=18,column=0,sticky=E)
        çalışmaSaatiEtiketi=Label(anaPencere,text='Çalışma Süresi:')
        çalışmaSaatiEtiketi.grid(row=19,column=0,sticky=E)
        yaşGirdisi=Entry(anaPencere,state='readonly',textvariable=self.yaş)
        yaşGirdisi.grid(row=15,column=2)
        maaşGirdisi=Entry(anaPencere,state='readonly',textvariable=self.maaş)  
        maaşGirdisi.grid(row=16,column=2)
        sicilNumarasıGirdi=Entry(anaPencere,state='readonly',textvariable=self.sicilNumarası)
        sicilNumarasıGirdi.grid(row=17,column=2)
        izinSüresiGirdisi=Entry(anaPencere,state='readonly',textvariable=self.izinSüresi)
        izinSüresiGirdisi.grid(row=18,column=2)
        çalışmaSaatiGirdisi=Entry(anaPencere,state='readonly',textvariable=self.çalışmaSaati)
        çalışmaSaatiGirdisi.grid(row=19,column=2)

        yKaydırmaÇubuğuİsimler=Scrollbar(anaPencere,orient=VERTICAL)
        yKaydırmaÇubuğuİsimler.grid(sticky=NS,row=23,column=1)  
        yKaydırmaÇubuğuUzmanlıklar=Scrollbar(anaPencere,orient=VERTICAL)
        yKaydırmaÇubuğuUzmanlıklar.grid(sticky=NS,row=3,column=1)

        uzmanlıklar={line.split('-')[4] for line in open('Personel.txt','r')}
        uzmanlıklar=list(uzmanlıklar)
        uzmanlıklar.sort()
        self.uzmanlık.set(uzmanlıklar)

        self.listeKutusuUzmanlıklar=Listbox(anaPencere,yscrollcommand=yKaydırmaÇubuğuUzmanlıklar,listvariable=self.uzmanlık,exportselection=0)
        self.listeKutusuUzmanlıklar.grid(row=3,column=0)
        self.listeKutusuİsimler=Listbox(anaPencere,yscrollcommand=yKaydırmaÇubuğuİsimler,listvariable=self.isim,exportselection=0)
        self.listeKutusuİsimler.grid(row=23,column=0)
        
        yKaydırmaÇubuğuİsimler['command']=self.listeKutusuİsimler.yview    
        yKaydırmaÇubuğuUzmanlıklar['command']=self.listeKutusuUzmanlıklar.yview

        self.listeKutusuUzmanlıklar.bind('<<ListboxSelect>>',self.getir)
        self.listeKutusuİsimler.bind('<<ListboxSelect>>',self.getir2)


        anaPencere.mainloop()

    def getir(self,eylem):
        seçim=self.listeKutusuUzmanlıklar.get(self.listeKutusuUzmanlıklar.curselection())
        isimler=[line.split('-')[0] for line in open('Personel.txt','r') if line.split('-')[4]==seçim]
        
        self.isim.set(isimler)

    def getir2(self,eylem):
        seçim=self.listeKutusuİsimler.get(self.listeKutusuİsimler.curselection())
        bilgiler=[line.split('-') for line in open('Personel.txt','r') if line.split('-')[0]==seçim]  
        self.yaş.set(bilgiler[0][2])
        self.maaş.set(bilgiler[0][3])
        self.izinSüresi.set(bilgiler[0][7])
        self.çalışmaSaati.set(bilgiler[0][8])
        self.sicilNumarası.set(bilgiler[0][5])
        #self.soyad.set(bilgiler[0][1])
Personel()