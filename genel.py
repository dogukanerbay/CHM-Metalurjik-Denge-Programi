from tkinter import *
from veriler import veriler
import numpy as np

genel_sonuclar = {}

#Analiz - Genel
def genel(analiz_frame,font2,font3):

    for widget in analiz_frame.winfo_children():
        widget.destroy()

    if "tesis_besleme" not in veriler:
        uyarı_label = Label(analiz_frame,bg="white",fg="black",font=font3)
        uyarı_label.config(text = "Önce Veri Girişi bölümünden verileri girip kaydediniz.")
        uyarı_label.pack(pady=30)
        return

    # GENEL DEVRE ANALİZİ
    besleme_miktari = np.array(veriler["tesis_besleme"]["miktar"])
    cleaner_konsantre_miktari = np.array(veriler["cleaner"]["konsantre_katı"])
    scavenger_artık_miktari = np.array(veriler["scavenger"]["artik_katı"])

    # ==========================================================
    # PERFORMANS SONUÇLARI
    # ==========================================================

    besleme_tenoru = np.array(veriler["tesis_besleme"]["tenor"])
    scavenger_artık_tenoru = np.array(veriler["scavenger"]["artik_tenoru"])
    cleaner_konsantre_tenoru = np.array(veriler["cleaner"]["konsantre_tenoru"])
    tesis_verimi =  ((cleaner_konsantre_miktari*cleaner_konsantre_tenoru) / (besleme_miktari*besleme_tenoru))*100
    zenginleştirme_oranı = besleme_miktari / cleaner_konsantre_miktari
    metal_kaybı =((scavenger_artık_miktari*scavenger_artık_tenoru)/(besleme_miktari*besleme_tenoru))*100

    # ==========================================================
    # DENGE
    # ==========================================================

    kutle_dengesi = abs(besleme_miktari- cleaner_konsantre_miktari- scavenger_artık_miktari)

    tesis_besleme_metali = (besleme_miktari * besleme_tenoru / 100)
    nihai_konsantre_metali = (cleaner_konsantre_miktari *cleaner_konsantre_tenoru / 100)
    nihai_artık_metali = (scavenger_artık_miktari * scavenger_artık_tenoru / 100)
    metal_dengesi = abs(tesis_besleme_metali- nihai_konsantre_metali- nihai_artık_metali)

    #Genel - Genel Devre Analizi----------------------------------------------------------------------------------------
    genel_baslık = Label(analiz_frame,text="Genel Devre Analizi",bg="white",fg="black",font=font2)
    genel_baslık.pack(padx=5,pady=10)

    #Bilgi Frame
    bilgi_frame = Frame(analiz_frame,bg="white")
    bilgi_frame.pack(padx=5,pady=5)

    #Besleme
    besleme_label = Label(bilgi_frame,bg="white",fg="black",font=font3)
    besleme_label.config(text="Tesis Besleme Miktarı")
    besleme_label.grid(row=0, column=1, padx=30, pady=5)

    besleme_deger = Label(bilgi_frame,bg="white",fg="black",font=font3)
    besleme_deger.config(text=f"{besleme_miktari:.2f} t/h")
    besleme_deger.grid(row=1, column=1, padx=30, pady=5)

    #Konsantre
    konsantre_label = Label(bilgi_frame,bg="white",fg="black",font=font3)
    konsantre_label.config(text="Nihai Konsantre Miktarı")
    konsantre_label.grid(row=0, column=2, padx=30, pady=5)

    konsantre_deger = Label(bilgi_frame,bg="white",fg="black",font=font3)
    konsantre_deger.config(text=f"{cleaner_konsantre_miktari:.2f} t/h")
    konsantre_deger.grid(row=1, column=2, padx=30, pady=5)

    #Artık
    artık_label = Label(bilgi_frame,bg="white",fg="black",font=font3)
    artık_label.config(text="Nihai Artık Miktarı")
    artık_label.grid(row=0, column=3, padx=30, pady=5)

    artık_deger = Label(bilgi_frame,bg="white",fg="black",font=font3)
    artık_deger.config(text=f"{scavenger_artık_miktari:.2f} t/h")
    artık_deger.grid(row=1, column=3, padx=30, pady=5)

    #Başlık - Performans Sonuçları--------------------------------------------------------------------------------------
    performans_sonucları_label = Label(analiz_frame,bg="white",fg="black",font=font2)
    performans_sonucları_label.config(text="Performans Sonuçları")
    performans_sonucları_label.pack(padx=5,pady=10)

    performans_frame = Frame(analiz_frame,bg="white")
    performans_frame.pack(padx=5,pady=5)

    #Besleme Tenörü
    besleme_tenoru_genel_label = Label(performans_frame,bg="white",fg="black",font=font3)
    besleme_tenoru_genel_label.config(text="Besleme Tenörü")
    besleme_tenoru_genel_label.grid(row=0, column=0, padx=5, pady=5)

    besleme_tenoru_genel = Label(performans_frame,bg="white",fg="black",font=font3)
    besleme_tenoru_genel.config(text=f"{besleme_tenoru:.2f} %")
    besleme_tenoru_genel.grid(row=1, column=0, padx=5, pady=5)

    #Konsantre Tenörü
    konsantre_tenoru_label = Label(performans_frame,bg="white",fg="black",font=font3)
    konsantre_tenoru_label.config(text="Konsantre Tenörü")
    konsantre_tenoru_label.grid(row=0, column=1, padx=5, pady=5)

    konsantre_tenoru = Label(performans_frame,bg="white",fg="black",font=font3)
    konsantre_tenoru.config(text=f"{cleaner_konsantre_tenoru:.2f} %")
    konsantre_tenoru.grid(row=1, column=1, padx=5, pady=5)

    #Artık Tenörü
    artık_tenoru_label = Label(performans_frame,bg="white",fg="black",font=font3)
    artık_tenoru_label.config(text="Artık Tenörü")
    artık_tenoru_label.grid(row=0, column=2, padx=5, pady=5)

    artık_tenoru = Label(performans_frame,bg="white",fg="black",font=font3)
    artık_tenoru.config(text=f"{scavenger_artık_tenoru:.2f} %")
    artık_tenoru.grid(row=1, column=2, padx=5, pady=5)

    #Verim
    verim_label = Label(performans_frame,bg="white",fg="black",font=font3)
    verim_label.config(text="Tesis Verimi")
    verim_label.grid(row=0, column=3, padx=5, pady=5)

    verim = Label(performans_frame,bg="white",fg="black",font=font3)
    verim.config(text =f"% {tesis_verimi:.2f}")
    verim.grid(row=1, column=3, padx=5, pady=5)

    #Zenginleştirme Oranı
    zenginleştirme_oranı_label = Label(performans_frame,bg="white",fg="black",font=font3)
    zenginleştirme_oranı_label.config(text="Zenginleştirme Oranı")
    zenginleştirme_oranı_label.grid(row=0, column=4, padx=5, pady=5)

    zenginleştirme_oranı_genel = Label(performans_frame,bg="white",fg="black",font=font3)
    zenginleştirme_oranı_genel.config(text =f" {zenginleştirme_oranı:.2f}")
    zenginleştirme_oranı_genel.grid(row=1, column=4, padx=5, pady=5)

    #Metal Kaybı
    metal_kaybı_label = Label(performans_frame,bg="white",fg="black",font=font3)
    metal_kaybı_label.config(text="Metal Kaybı")
    metal_kaybı_label.grid(row=0, column=5, padx=5, pady=5)

    metal_kaybı_genel = Label(performans_frame,bg="white",fg="black",font=font3)
    metal_kaybı_genel.config(text=f"% {metal_kaybı:.2f}")
    metal_kaybı_genel.grid(row=1, column=5, padx=5, pady=5)


    #Başlık - Denge-----------------------------------------------------------------------------------------------------
    denge_label = Label(analiz_frame,bg="white",fg="black",font=font2)
    denge_label.config(text="Denge")
    denge_label.pack(padx=5,pady=10)

    denge_frame = Frame(analiz_frame,bg="white")
    denge_frame.pack(padx=5,pady=5)

    #Kütle Dengesi
    kutle_denge_label = Label(denge_frame,bg="white",fg="black",font=font3)
    kutle_denge_label.config(text="Kütle Dengesi")
    kutle_denge_label.grid(row=0, column=0, padx=5, pady=5)

    kutle_denge_genel = Label(denge_frame,bg="white",fg="black",font=font3)
    kutle_denge_genel.config(text=f"{kutle_dengesi:.2f}")
    kutle_denge_genel.grid(row=1, column=0, padx=5, pady=5)

    #Metal Denge
    metal_denge_label = Label(denge_frame,bg="white",fg="black",font=font3)
    metal_denge_label.config(text="Metal Dengesi")
    metal_denge_label.grid(row=0, column=1, padx=5, pady=5)

    metal_denge_genel = Label(denge_frame,bg="white",fg="black",font=font3)
    metal_denge_genel.config(text=f"{metal_dengesi:.2f}")
    metal_denge_genel.grid(row=1, column=1, padx=5, pady=5)

    #Denge Hatası
    denge_hatası_label = Label(denge_frame,bg="white",fg="black",font=font3)
    denge_hatası_label.config(text="Denge Hatası")
    denge_hatası_label.grid(row=0, column=2, padx=5, pady=5)

    denge_hatası_genel = Label(denge_frame,bg="white",fg="black",font=font3)
    denge_hatası_genel.grid(row=1, column=2, padx=5, pady=5)

    if (kutle_dengesi <0.01) and (metal_dengesi<0.01):
        denge_hatası_genel.config(text="Denge Sağlandı", fg="green")
    else:
        denge_hatası_genel.config(text="Denge Sağlanmadı", fg="red")
