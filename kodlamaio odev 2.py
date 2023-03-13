O_Liste=[]
while True:
  print("\n Öğrenci Kayıt Sistemi : \n istenilen işlem : \n \t 1-Yeni öğrenci ekle \n \t 2-Yeni öğrenci ekle (çoklu) \n \t 3-Öğrenci sil \n \t 4-Öğrenci sil (çoklu) \n \t 5-Öğrenci Listesini Dök \n \t 6-Öğrenci Numarası Göster")
  secim = int(input('seçim bekleniyor : '))


  def ogrenci_ekle ():
    ad , soyad = input("\n Öğrencinin Adı ve Soyadını \n aralarında boşluk olacak şekilde giriniz :").split()
    O_Liste.append(ad+"_"+soyad)

  def ogrenci_sil ():
    ad , soyad = input("\n Öğrencinin Adı ve Soyadını \n aralarında boşluk olacak şekilde giriniz :").split()
    O_Liste.remove(ad+"_"+soyad)

  def ogrenci_no():
    ad , soyad = input("\n Öğrencinin Adı ve Soyadını \n aralarında boşluk olacak şekilde giriniz :").split()
    index = O_Liste.index(ad+"_"+soyad)
    print(f"\n {ad} {soyad} 'nın öğrenci numarası : {index}")


  if secim ==1:
    ogrenci_ekle()

  elif secim==2:
    sayı_ekle=int(input("\n Kaç öğrenci ekleyceksiniz?"))
    for i in range(sayı_ekle):
      ogrenci_ekle()

  elif secim ==3:
    ogrenci_sil()

  elif secim==4:
    sayı_sil=int(input("\n Kaç öğrenci sileceksiniz?"))
    while sayı_sil>0:
      ogrenci_sil()
      sayı_sil -=1

  elif secim == 5:
    sıra=0
    print(f"\n Öğrenci listesi ({len(O_Liste)} öğrenci mevcut): ")
    for i in O_Liste:
      a=i.split("_")
      print(f"{sıra}  - {a[0]} {a[1]}")
      sıra +=1
  elif secim == 6:
    ogrenci_no()


  elif secim==7:
    break