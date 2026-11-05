envanter=[]
mevcut_oda="Evin girişi"
odalar ={
"Evin girişi":["Çekiç","Dolap"],
"Mutfak":["Anahtar',Kıskaç',Güvenlik Anahtarı"],
"Yatak Odası":["Oyuncak Ayı"],
"Bodrum":["Karpuz","Kod"],
"Garaj":["Araba Parçası","Levye"]}
while True:
 print(f"nŞu an {mevcut_oda}odasındasın")
 secim=input("Ne yapmak istersin?")
 if secim.lower()=="envanter":
 if not envanter:
   print("Envanterin boş")
