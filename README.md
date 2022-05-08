# wordle-cozucu
Wordle Türkçe çözücü


Kullanım:
* bulunacak kelimenin uzunluğunu yazın.
* başlangıç kelimeleri ile birkaç deneme yapın.
* kelimede varolan harfleri(sarı ve yeşil harflerin hepsi) tek bir kelime gibi aralarında boşluk olmadan yazın. ör: "abcda" (aynı harfleri tekrar yazabilirsiniz)
* kelimede olmayan harfleri(gri harfler) tek bir kelime gibi aralarında boşluk olmadan yazın. ör: "aaglsskmzk" (aynı harfleri tekrar yazabilirsiniz)
* "varsa x. harf" diye soruluyorsa, x. indexte yeşil harf varsa yeşil harfi yazın. o indexteki harf belli değil ise boş bırakın(enter)
* eğer "varsa x. harf" sorusunu boş bıraktıysanız, "x. harfte olmayanlar" diye soracak, buraya, o indexteki tüm sarı harfleri tek bir kelime gibi yazın. ör: "ab" o basamakta hiç sarı harf yoksa boş bırakın(enter)
* tüm indexler için soruları cevapladıktan sonra kelimeleri tahmin edecek, eğer birden çok kelime kaldıysa, en mantıklısını seçip yeni kelime olarak deneyin.
* denediğiniz yeni kelime doğru değil ise bilmediğiniz bazı basamaklar için yeni bilgiler edindiniz, program loopta olduğu için size tekrardan başlangıç kelimeleri verecek ve hangi harflerin olduğunu soracak, süreci tekrar edin.

"hepsi.txt" içerisinde internetten bulduğum, her biri bir satırda yaklaşık 75 bin türkçe kelime var. Bu satırlardan bazıları tek bir kelime yerine kelime grubu içeriyor. Program kelime grubu içeren satırları görmezden geliyor. 
Çok küçük bir ihtimalle, internetteki bazı wordle türkçe oyunlarında program o kelime "hepsi.txt" dosyasında olmadığı için kelimeyi bulamayabiliyor. Benim karşılaştığım durumda örneğin ayrık yazılması gereken kelime grubu türkçeye uygunsuz biçimde yazıldığı için veritabanında bulamamıştı.
