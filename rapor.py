from tkinter import *
from tkinter import filedialog, messagebox
from veriler import veriler

def rapor(analiz_frame, font2, font3):

    for widget in analiz_frame.winfo_children():
        widget.destroy()

    #Veri kontrolü

    if "tesis_besleme" not in veriler:

        uyarı_label = Label(analiz_frame, bg="white", fg="black", font=font3)
        uyarı_label.config(text="Önce Veri Girişi bölümünden verileri girip kaydediniz.")
        uyarı_label.pack(pady=30)

        return

    #Veriler-----------------------------------------------------------------------------------------------------------

    besleme_miktari = veriler["tesis_besleme"]["miktar"]
    besleme_tenoru = veriler["tesis_besleme"]["tenor"]

    rougher_konsantre_katı = veriler["rougher"]["konsantre_katı"]
    rougher_konsantre_tenoru = veriler["rougher"]["konsantre_tenoru"]
    rougher_artık_katı = veriler["rougher"]["artik_katı"]
    rougher_artık_tenoru = veriler["rougher"]["artik_tenoru"]

    cleaner_konsantre_katı = veriler["cleaner"]["konsantre_katı"]
    cleaner_konsantre_tenoru = veriler["cleaner"]["konsantre_tenoru"]
    cleaner_artık_katı = veriler["cleaner"]["artik_katı"]
    cleaner_artık_tenoru = veriler["cleaner"]["artik_tenoru"]

    scavenger_konsantre_katı = veriler["scavenger"]["konsantre_katı"]
    scavenger_konsantre_tenoru = veriler["scavenger"]["konsantre_tenoru"]
    scavenger_artık_katı = veriler["scavenger"]["artik_katı"]
    scavenger_artık_tenoru = veriler["scavenger"]["artik_tenoru"]

    #Metal Miktarı

    tesis_besleme_metali = (besleme_miktari * besleme_tenoru / 100)

    rougher_konsantre_metali = (rougher_konsantre_katı * rougher_konsantre_tenoru / 100)
    rougher_artık_metali = (rougher_artık_katı * rougher_artık_tenoru / 100)

    cleaner_konsantre_metali = (cleaner_konsantre_katı * cleaner_konsantre_tenoru / 100)
    cleaner_artık_metali = (cleaner_artık_katı * cleaner_artık_tenoru / 100)

    scavenger_konsantre_metali = (scavenger_konsantre_katı * scavenger_konsantre_tenoru / 100)
    scavenger_artık_metali = (scavenger_artık_katı * scavenger_artık_tenoru / 100)

    #Beslemeler

    rougher_besleme_miktari = (besleme_miktari + cleaner_artık_katı + scavenger_konsantre_katı)
    rougher_besleme_metali = (tesis_besleme_metali + cleaner_artık_metali + scavenger_konsantre_metali)
    rougher_besleme_tenoru = (rougher_besleme_metali / rougher_besleme_miktari * 100)

    cleaner_besleme_miktari = rougher_konsantre_katı
    cleaner_besleme_tenoru = rougher_konsantre_tenoru
    cleaner_besleme_metali = rougher_konsantre_metali

    scavenger_besleme_miktari = rougher_artık_katı
    scavenger_besleme_tenoru = rougher_artık_tenoru
    scavenger_besleme_metali = rougher_artık_metali

    #Verimler

    rougher_verim = (rougher_konsantre_metali / rougher_besleme_metali * 100)
    cleaner_verim = (cleaner_konsantre_metali / cleaner_besleme_metali * 100)
    scavenger_verim = (scavenger_konsantre_metali / scavenger_besleme_metali * 100)

    #Zenginleştirme Oranları

    rougher_zenginlestirme = (rougher_besleme_miktari / rougher_konsantre_katı)
    cleaner_zenginlestirme = (cleaner_besleme_miktari / cleaner_konsantre_katı)
    scavenger_zenginlestirme = (scavenger_besleme_miktari / scavenger_konsantre_katı)

    #Nihai Ürünler

    nihai_konsantre_miktari = cleaner_konsantre_katı
    nihai_konsantre_tenoru = cleaner_konsantre_tenoru
    nihai_konsantre_metali = cleaner_konsantre_metali

    nihai_artık_miktari = scavenger_artık_katı
    nihai_artık_tenoru = scavenger_artık_tenoru
    nihai_artık_metali = scavenger_artık_metali

    #Genel Performans

    genel_verim = (nihai_konsantre_metali / tesis_besleme_metali * 100)
    genel_zenginlestirme = (besleme_miktari / nihai_konsantre_miktari)
    metal_kaybi = (nihai_artık_metali / tesis_besleme_metali * 100)

    #Genel Denge

    kutle_dengesi = (besleme_miktari - nihai_konsantre_miktari - nihai_artık_miktari)
    metal_dengesi = (tesis_besleme_metali - nihai_konsantre_metali - nihai_artık_metali)

    if abs(kutle_dengesi) < 0.01:
        kutle_denge_durumu = "Sağlandı"
    else:
        kutle_denge_durumu = "Sağlanmadı"

    if abs(metal_dengesi) < 0.01:
        metal_denge_durumu = "Sağlandı"
    else:
        metal_denge_durumu = "Sağlanmadı"

    #Rougher, Cleaner ,Scavenger Kütle ve Metal Dengeleri

    rougher_kutle_dengesi = (rougher_besleme_miktari - rougher_konsantre_katı - rougher_artık_katı)
    cleaner_kutle_dengesi = (cleaner_besleme_miktari - cleaner_konsantre_katı - cleaner_artık_katı)
    scavenger_kutle_dengesi = (scavenger_besleme_miktari - scavenger_konsantre_katı - scavenger_artık_katı)

    rougher_metal_dengesi = (rougher_besleme_metali - rougher_konsantre_metali - rougher_artık_metali)
    cleaner_metal_dengesi = (cleaner_besleme_metali - cleaner_konsantre_metali - cleaner_artık_metali)
    scavenger_metal_dengesi = (scavenger_besleme_metali - scavenger_konsantre_metali - scavenger_artık_metali)

    def denge_durumu(dengesi):
        if abs(dengesi) < 0.01:
            return "Sağlandı"
        else:
            return "Sağlanmadı"

    rougher_kutle_denge_durumu = denge_durumu(rougher_kutle_dengesi)
    cleaner_kutle_denge_durumu = denge_durumu(cleaner_kutle_dengesi)
    scavenger_kutle_denge_durumu = denge_durumu(scavenger_kutle_dengesi)

    rougher_metal_denge_durumu = denge_durumu(rougher_metal_dengesi)
    cleaner_metal_denge_durumu = denge_durumu(cleaner_metal_dengesi)
    scavenger_metal_denge_durumu = denge_durumu(scavenger_metal_dengesi)

    # -----------------------------------------------------------------------------------------------------------------
    # RAPOR ALANI
    # -----------------------------------------------------------------------------------------------------------------



    rapor_baslik = Label(analiz_frame, text="Flotasyon Performans Raporu", bg="white", font=font2)
    rapor_baslik.pack(pady=10)

    rapor_frame = Frame(analiz_frame, bg="white")
    rapor_frame.pack(fill="both", expand=True, padx=20, pady=10)

    scroll_bar = Scrollbar(rapor_frame)
    scroll_bar.pack(side="right", fill="y")

    rapor_text = Text(rapor_frame, font=("Arial", 11), bg="white", relief="solid", borderwidth=1,
                      yscrollcommand=scroll_bar.set)
    rapor_text.pack(fill="both", expand=True)

    scroll_bar.config(command=rapor_text.yview)

    # ----------------------------------------------------------------------------------------------------------------
    # RAPOR METNİ
    # -----------------------------------------------------------------------------------------------------------------

    rapor_metni = f"""
============================================================
             FLOTASYON PERFORMANS RAPORU
============================================================


GENEL DEVRE ANALİZİ
------------------------------------------------------------

Tesis Beslemesi          : {besleme_miktari:.2f} t/h
Besleme Tenörü           : {besleme_tenoru:.2f} %

Final Konsantre          : {nihai_konsantre_miktari:.2f} t/h
Final Konsantre Tenörü   : {nihai_konsantre_tenoru:.2f} %
Final Konsantre Metali   : {nihai_konsantre_metali:.2f} t/h

Final Artık              : {nihai_artık_miktari:.2f} t/h
Final Artık Tenörü       : {nihai_artık_tenoru:.2f} %
Final Artık Metali       : {nihai_artık_metali:.2f} t/h


GENEL PERFORMANS
------------------------------------------------------------

Genel Verim              : {genel_verim:.2f} %
Zenginleştirme Oranı     : {genel_zenginlestirme:.2f}
Metal Kaybı              : {metal_kaybi:.2f} %


KADEME PERFORMANSLARI
------------------------------------------------------------

ROUGHER

Besleme Miktarı          : {rougher_besleme_miktari:.2f} t/h
Besleme Tenörü           : {rougher_besleme_tenoru:.2f} %
Konsantre Miktarı        : {rougher_konsantre_katı:.2f} t/h
Konsantre Tenörü         : {rougher_konsantre_tenoru:.2f} %
Verim                    : {rougher_verim:.2f} %
Zenginleştirme Oranı     : {rougher_zenginlestirme:.2f}


CLEANER

Besleme Miktarı          : {cleaner_besleme_miktari:.2f} t/h
Besleme Tenörü           : {cleaner_besleme_tenoru:.2f} %
Konsantre Miktarı        : {cleaner_konsantre_katı:.2f} t/h
Konsantre Tenörü         : {cleaner_konsantre_tenoru:.2f} %
Verim                    : {cleaner_verim:.2f} %
Zenginleştirme Oranı     : {cleaner_zenginlestirme:.2f}


SCAVENGER

Besleme Miktarı          : {scavenger_besleme_miktari:.2f} t/h
Besleme Tenörü           : {scavenger_besleme_tenoru:.2f} %
Konsantre Miktarı        : {scavenger_konsantre_katı:.2f} t/h
Konsantre Tenörü         : {scavenger_konsantre_tenoru:.2f} %
Verim                    : {scavenger_verim:.2f} %
Zenginleştirme Oranı     : {scavenger_zenginlestirme:.2f}


GENEL DENGE KONTROLÜ
------------------------------------------------------------

Kütle Dengesi Farkı      : {kutle_dengesi:.2f} t/h
Kütle Dengesi Durumu     : {kutle_denge_durumu}

Metal Dengesi Farkı      : {metal_dengesi:.2f} t/h
Metal Dengesi Durumu     : {metal_denge_durumu}


KADEME KÜTLE DENGELERİ
------------------------------------------------------------

Rougher                  : {rougher_kutle_dengesi:.2f} t/h
Rougher Durumu           : {rougher_kutle_denge_durumu}

Cleaner                  : {cleaner_kutle_dengesi:.2f} t/h
Cleaner Durumu           : {cleaner_kutle_denge_durumu}

Scavenger                : {scavenger_kutle_dengesi:.2f} t/h
Scavenger Durumu         : {scavenger_kutle_denge_durumu}


KADEME METAL DENGELERİ
------------------------------------------------------------

Rougher                  : {rougher_metal_dengesi:.2f} t/h
Rougher Durumu           : {rougher_metal_denge_durumu}

Cleaner                  : {cleaner_metal_dengesi:.2f} t/h
Cleaner Durumu           : {cleaner_metal_denge_durumu}

Scavenger                : {scavenger_metal_dengesi:.2f} t/h
Scavenger Durumu         : {scavenger_metal_denge_durumu}


RAPOR SONU
============================================================
"""

    rapor_text.insert("1.0", rapor_metni)

    rapor_text.config(state="disabled")

    # ==========================================================
    # KAYDETME FONKSİYONU
    # ==========================================================

    def raporu_kaydet():

        dosya_yolu = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Metin Dosyası", "*.txt"), ("Tüm Dosyalar", "*.*")], title="Raporu Kaydet")

        if dosya_yolu:

            with open(dosya_yolu, "w", encoding="utf-8") as dosya:

                dosya.write(rapor_metni)

            messagebox.showinfo("Rapor", "Rapor başarıyla kaydedildi.")

    # ==========================================================
    # KAYDET BUTONU
    # ==========================================================

    kaydet_button = Button(analiz_frame, text="Raporu Kaydet", font=font3, bg="white", command=raporu_kaydet)
    kaydet_button.pack(pady=10)