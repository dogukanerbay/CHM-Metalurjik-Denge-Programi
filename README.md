# Flotasyon Projesi

Python ve Tkinter kullanılarak geliştirilen **Flotasyon Projesi**, flotasyon devresindeki tesis beslemesi ile Rougher, Cleaner ve Scavenger kademelerine ait verilerin girilmesini, performans sonuçlarının hesaplanmasını, grafiklerin oluşturulmasını ve sonuçların raporlanmasını sağlar.

## Program Özellikleri

Program içerisinde aşağıdaki bölümler bulunmaktadır:

- Genel
- Veri Girişi
- Hesaplamalar
- Grafik
- Rapor

---

## 1. Veri Girişi

Programın hesaplama ve grafik bölümlerini kullanabilmek için öncelikle **Veri Girişi** bölümünden veriler girilir.

### Tesis Beslemesi

- Besleme Miktarı
- Besleme Tenörü

### Rougher

- Konsantre Katı
- Konsantre Tenörü
- Artık Katı
- Artık Tenörü

### Cleaner

- Konsantre Katı
- Konsantre Tenörü
- Artık Katı
- Artık Tenörü

### Scavenger

- Konsantre Katı
- Konsantre Tenörü
- Artık Katı
- Artık Tenörü

Veriler girildikten sonra **Verileri Kaydet** işlemi ile program içerisinde kullanılmak üzere kaydedilir.

Programda boş bırakılan, sayı olmayan veya belirlenen sınırların dışında kalan değerler için hata mesajı gösterilir.

---

## 2. Hesaplamalar

Veriler kaydedildikten sonra **Hesaplamalar** bölümünden flotasyon kademelerine ait sonuçlar görüntülenebilir.

Programda;

- Metal miktarları
- Kademe beslemeleri
- Besleme tenörleri
- Kademe verimleri
- Zenginleştirme oranları
- Nihai konsantre
- Nihai artık
- Genel verim
- Genel zenginleştirme oranı
- Metal kaybı
- Kütle dengeleri
- Metal dengeleri

hesaplanır.

Rougher, Cleaner ve Scavenger kademeleri ayrı olarak değerlendirilir.

---

## 3. Grafik

**Grafik** bölümünde hesaplanan sonuçlar grafik olarak görüntülenir.

Programda üç farklı grafik bulunmaktadır:

### Kademe Verimleri

Rougher, Cleaner ve Scavenger kademelerinin verimleri karşılaştırılır.

### Tenör Karşılaştırması

Her kademe için:

- Besleme Tenörü
- Konsantre Tenörü

karşılaştırmalı olarak gösterilir.

### Zenginleştirme Oranı

Rougher, Cleaner ve Scavenger kademelerinin zenginleştirme oranları karşılaştırılır.

Program açıldığında grafik bölümünde varsayılan olarak **Kademe Verimleri** grafiği gösterilir.

---

## 4. Rapor

**Rapor** bölümü, girilen veriler ve yapılan hesaplamalar üzerinden flotasyon performans raporu oluşturur.

Raporda;

### Genel Devre Analizi

- Tesis Beslemesi
- Besleme Tenörü
- Final Konsantre
- Final Konsantre Tenörü
- Final Konsantre Metali
- Final Artık
- Final Artık Tenörü
- Final Artık Metali

gösterilir.

### Genel Performans

- Genel Verim
- Zenginleştirme Oranı
- Metal Kaybı

gösterilir.

### Kademe Performansları

Rougher, Cleaner ve Scavenger için;

- Besleme Miktarı
- Besleme Tenörü
- Konsantre Miktarı
- Konsantre Tenörü
- Verim
- Zenginleştirme Oranı

gösterilir.

### Genel Denge Kontrolü

- Kütle Dengesi Farkı
- Kütle Dengesi Durumu
- Metal Dengesi Farkı
- Metal Dengesi Durumu

gösterilir.

### Kademe Kütle Dengeleri

Rougher, Cleaner ve Scavenger kademelerinin kütle dengesi farkları ve denge durumları gösterilir.

### Kademe Metal Dengeleri

Rougher, Cleaner ve Scavenger kademelerinin metal dengesi farkları ve denge durumları gösterilir.

Denge kontrolünde fark belirlenen tolerans içerisinde olduğunda **"Sağlandı"**, aksi durumda **"Sağlanmadı"** ifadesi gösterilir.

---

## 5. Raporu Kaydetme

Oluşturulan rapor **Raporu Kaydet** butonu kullanılarak bilgisayara `.txt` formatında kaydedilebilir.

Kaydetme sırasında dosyanın adı ve konumu kullanıcı tarafından seçilir.

---

## Kullanım Sırası

Programın temel kullanım sırası:

**1. Veri Girişi**

↓

**2. Verileri Kaydet**

↓

**3. Hesaplamalar**

↓

**4. Grafik**

↓

**5. Rapor**

Bu sırayla kullanıldığında girilen veriler üzerinden hesaplama, grafik ve raporlama işlemleri gerçekleştirilebilir.
