sorular = [
    "1. Bir yarışta ikinciyi geçen kaçıncı olur?\n A-) Birinci\n B-) İkinci\n C-) Üçüncü\n D-) Yarış dışı kalır\n",
    "2. 'Gece gündüz çalışıyorum ama bir adım bile ilerleyemiyorum' diyen şey nedir?\n A-) Duvar saati\n B-) Karınca\n C-) Tembel öğrenci\n D-) Vantilatör\n",
	"3. Hangi ayda 28 gün vardır?\n A-) Sadece Şubat\n B-) Dört yılda bir Şubat\n C-) Bütün aylarda\n D-) Hiçbirinde\n",
    "4. Türkçede 'iki kelimeyi bir araya getiremeyen' birine ne denir?\n A-) Sessiz\n B-) Boşluk tuşu (Space)\n C-) Dalgın\n D-) Utangaç\n",
    "5. Ağzı var dili yok, nefesi var canı yok, karnı tok sırtı pek. Bu nedir?\n A-) Kardan adam\n B-) Fırın\n C-) Düdüklü tencere\n D-) Körük\n",
    "6. Kırıldığında işe yarayan şey nedir?\n A-) Bardak\n B-) Ceviz\n C-) Yumurta\n D-) Ayna\n",
    "7. Islakken kurutan şey nedir?\n A-) Güneş\n B-) Rüzgar\n C-) Havlu\n D-) Fön makinesi\n",
    "8. Bir adam yağmur altında şemsiyesiz ve şapkasız yürüyor ama tek bir saç teli bile ıslanmıyor. Neden?\n A-) Çok hızlı koşuyor\n B-) Ağaçların altından yürüyor\n C-) Adam keldir\n D-) Yağmur asitlidir\n",
    "9. Şehirden şehre, köyden köye gider ama hiç hareket etmez. Bu nedir?\n A-) Bulut\n B-) Yol\n D-) Tren\n D-) Rüzgar\n",
    "10. Sana ait olan ama senden çok başkalarının kullandığı şey nedir?\n A-) Telefonun\n B-) Paran\n C-) Adın\n D-) Evin\n",
    "11. Bir çiftçinin 17 koyunu vardı. 9'u hariç hepsi hastalanıp öldü. Çiftçinin kaç canlı koyunu kaldı?\n A-) 8\n B-) 9\n C-) 0\n D-) 17\n",
    "12. Doktorunuz size 3 hap verir ve bunları yarımşar saat arayla almanızı söyler. İlaçların tamamı kaç saatte biter?\n A-) 1 saat\n B-) 1.5 saat\n C-) 2 saat\n D-) Yarım saat\n",
    "13. Bir gölde her gün iki katına çıkan nilüferler var. Gölün tamamı 48 günde kaplandığına göre, yarısı kaçıncı günde kaplanmıştır?\n A-) 24\n B-) 47\n C-) 12\n D-) 36\n",
    "14. Bir sepette 5 elma var. 5 kişiye, sepette 1 elma kalacak şekilde birer elma dağıtılırsa bu nasıl mümkün olur?\n A-) İmkânsızdır\n B-) Biri yarım elma alır\n C-) Son kişiye elma sepetle verilir\n D-) Elmalardan biri çürüktür\n",
    "15. 30'u yarıma (0.5) bölüp 10 eklerseniz sonuç kaç olur?\n A-) 25\n B-) 70\n C-) 40\n D-) 50\n",
    "16. Bir saat ustası bir saati tamir etmek için 3 dakika harcıyor. 10 saati aynı tempoda tamir etmesi kaç dakika sürer?\n a-) 30 dakika\n b-) 27 dakika\n c-) 33 dakika\n d-) 3 dakika\n",
    "17. 5 makine, 5 dakikada 5 düğme üretiyorsa; 100 makine, 100 düğmeyi kaç dakikada üretir?\n a-) 100 dakika\n b-) 50 dakika\n c-) 5 dakika\n d-) 1 dakika\n",
    "18. Bir tuğlanın ağırlığı 1 kg artı yarım tuğla kadardır. Bir tuğla kaç kg'dır?\n A-) 1.5 kg\n B-) 2 kg\n C-) 2.5 kg\n D-) 3 kg\n",
    "19. 10 metrelik bir kuyuya düşen kurbağa her gün 3 metre yukarı zıplıyor, gece ise uyurken 2 metre aşağı kayıyor. Kurbağa kaç günde kuyudan çıkar?\n A-) 10 gün\n B-) 8 gün\n C-) 7 gün\n D-) 9 gün\n",
	"20. Bir elektrikli tren kuzeye doğru 80 km/s hızla gidiyor. Rüzgar ise güneye doğru 20 km/s hızla esiyor. Trenin dumanı hangi yöne doğru uçar?\n A-) Güneye\n B-) Kuzeye\n C-) Batıya\n D-) Elektrikli trenin dumanı çıkmaz\n"
			]
			
dogru_cevaplar = [
    "B", "A", "C", "B", "D", "C", "C", "C", "B", "C",
    "B", "A", "B", "C", "B", "A", "C", "B", "B", "D"
]

alınan_cevaplar = []

dogru_sayısı = 0

print("Bu program sizi 10 sözel 10 sayısal olmak üzere 10 soruluk bir teste tabi tutucaktır şimdiden başarılar \n")
isim = input("Adınızı Giriniz: ")
print("")
			
for s in sorular:
	print(s)
	while True:
		cevap = input("Cevap: ").upper()
		print ("")
		if cevap not in ["A", "B", "C", "D","a", "b", "c", "d"]:
			print("Lütfen Şıklardan birini seçiniz! \n")
		else :
			alınan_cevaplar.append(cevap)
			print("-" * 50)
			print("")
			break

for i in range(len(alınan_cevaplar)):
	if alınan_cevaplar[i] == dogru_cevaplar[i]:
		dogru_sayısı += 1

print("=" * 45)
print(f"Tebrikler {isim}! Test tamamnlandı.")
print(f"Skorunuz: {dogru_sayısı}/20\n")

if dogru_sayısı == 20:
    rutbe = "Büyük Usta / Mantık Tanrısı"
    yorum = "Hiçbir tuzağa düşmediniz, dikkatiniz kusursuz!"
elif dogru_sayısı >= 16:
    rutbe = "Zeka Küpü"
    yorum = "Çok sağlam bir mantığınız var, ufak detaylar gözünüzden kaçmıyor."
elif dogru_sayısı >= 11:
    rutbe = "Dikkatli Çırak"
    yorum = "Ortalamanın üzerindesiniz ama birkaç ters köşe soruya takılmışsınız."
elif dogru_sayısı >= 6:
    rutbe = "Ters Köşe Mağduru"
    yorum = "Sorular biraz kafa karıştırmış, şaşırtmacalara dikkat etmelisiniz."
else:
    rutbe = "Çaylak Dedektif"
    yorum = "Bugün şansınız pek yaver gitmemiş, acele etmeden tekrar deneyin!"

print(f"Rütbeniz: {rutbe}")
print(f"Yorum: {yorum}")

print("=" * 60)

print("\n--- TEST CEVAP ANAHTARI VE SONUÇLARINIZ ---\n")

for i in range(len(sorular)):
    soru_metni = sorular[i]
    kullanici_cevabi = alınan_cevaplar[i]
    dogru_cevap = dogru_cevaplar[i]
    
    print(soru_metni)
    print(f"Doğru Cevap: {dogru_cevap.upper()}")
    
    if kullanici_cevabi == dogru_cevap:
        print(f"Durum: [ DOĞRU ] (Verdiğiniz cevap: {kullanici_cevabi.upper()})")
    else:
        print(f"Durum: [ YANLIŞ! ] -> (Verdiğiniz cevap '{kullanici_cevabi.upper()}' yanlıştır)")
        
    if i < len(sorular) - 1:
        input("\nSonraki soruya geçmek için [Enter] tuşuna basınız...")
    else:
        input("\nTüm soruları incelediniz. Çıkmak için [Enter] tuşuna basınız...")
    
    print("-" * 50)
