from tkinter import *
from veriler import veriler

sonuclar = {}

def hesaplamalar(analiz_frame,font2,font3):

    for widget in analiz_frame.winfo_children():
        widget.destroy()

    if "tesis_besleme" not in veriler:
        Label(analiz_frame,text="Önce Veri bölümünden verileri girip kaydediniz.",bg="white",font=font3).pack(pady=30)
        return


    # ==========================================================
    # TESİS BESLEMESİ
    # ==========================================================

    besleme_miktari = (veriler["tesis_besleme"]["miktar"])
    besleme_tenoru = (veriler["tesis_besleme"]["tenor"])

    # Tesis besleme metal miktarı
    tesis_besleme_metali = (besleme_miktari * besleme_tenoru / 100)

    # ==========================================================
    # ROUGHER VERİLERİ
    # ==========================================================

    rougher_konsantre_katı = (veriler["rougher"]["konsantre_katı"])
    rougher_konsantre_tenoru = veriler["rougher"]["konsantre_tenoru"]

    rougher_artık_katı = (veriler["rougher"]["artik_katı"])
    rougher_artık_tenoru = (veriler["rougher"]["artik_tenoru"])

    # ==========================================================
    # CLEANER VERİLERİ
    # ==========================================================

    cleaner_konsantre_katı = veriler["cleaner"]["konsantre_katı"]
    cleaner_konsantre_tenoru = veriler["cleaner"]["konsantre_tenoru"]

    cleaner_artık_katı = veriler["cleaner"]["artik_katı"]
    cleaner_artık_tenoru = veriler["cleaner"]["artik_tenoru"]


    # ==========================================================
    # SCAVENGER VERİLERİ
    # ==========================================================

    scavenger_konsantre_katı = veriler["scavenger"]["konsantre_katı"]
    scavenger_konsantre_tenoru = veriler["scavenger"]["konsantre_tenoru"]

    scavenger_artık_katı = veriler["scavenger"]["artik_katı"]
    scavenger_artık_tenoru = veriler["scavenger"]["artik_tenoru"]


    # ==========================================================
    # CLEANER METAL MİKTARLARI
    # ==========================================================

    cleaner_konsantre_metali = (cleaner_konsantre_katı * cleaner_konsantre_tenoru / 100)
    cleaner_artık_metali = (cleaner_artık_katı *cleaner_artık_tenoru / 100)

    # ==========================================================
    # SCAVENGER METAL MİKTARLARI
    # ==========================================================

    scavenger_konsantre_metali = (scavenger_konsantre_katı * scavenger_konsantre_tenoru / 100)
    scavenger_artık_metali = ( scavenger_artık_katı * scavenger_artık_tenoru / 100)

    # ==========================================================
    # ROUGHER GERİ DÖNÜŞLERİ
    # ==========================================================

    # Cleaner artığı Rougher'a geri döner
    cleaner_artık_geri_donus = cleaner_artık_katı

    # Scavenger konsantresi Rougher'a geri döner
    scavenger_konsantre_geri_donus = scavenger_konsantre_katı

    # ==========================================================
    # ROUGHER TOPLAM BESLEMESİ
    # ==========================================================

    rougher_besleme_miktari = (besleme_miktari + cleaner_artık_geri_donus + scavenger_konsantre_geri_donus)

    # Rougher beslemesine giren toplam metal
    rougher_besleme_metali = (tesis_besleme_metali + cleaner_artık_metali + scavenger_konsantre_metali)

    # Rougher gerçek besleme tenörü
    rougher_besleme_tenoru = (rougher_besleme_metali /rougher_besleme_miktari) * 100

    # ==========================================================
    # ROUGHER ÜRÜN METALLERİ
    # ==========================================================

    rougher_konsantre_metali = (rougher_konsantre_katı *rougher_konsantre_tenoru / 100)
    rougher_artık_metali = (rougher_artık_katı * rougher_artık_tenoru / 100)

    # ==========================================================
    # ROUGHER PERFORMANSI
    # ==========================================================

    rougher_verim = (rougher_konsantre_metali /rougher_besleme_metali) * 100
    rougher_zenginlestirme = rougher_besleme_miktari / rougher_konsantre_katı

    # ==========================================================
    # CLEANER BESLEMESİ
    # ==========================================================

    cleaner_besleme_miktari = rougher_konsantre_katı
    cleaner_besleme_metali = rougher_konsantre_metali
    cleaner_besleme_tenoru = rougher_konsantre_tenoru

    # ==========================================================
    # CLEANER PERFORMANSI
    # ==========================================================

    cleaner_verim = (cleaner_konsantre_metali /cleaner_besleme_metali) * 100
    cleaner_zenginlestirme = cleaner_besleme_miktari / cleaner_konsantre_katı

    # ==========================================================
    # SCAVENGER BESLEMESİ
    # ==========================================================

    scavenger_besleme_miktari = rougher_artık_katı
    scavenger_besleme_metali = rougher_artık_metali
    scavenger_besleme_tenoru = rougher_artık_tenoru

    # ==========================================================
    # SCAVENGER PERFORMANSI
    # ==========================================================

    scavenger_verim = (scavenger_konsantre_metali /scavenger_besleme_metali) * 100
    scavenger_zenginlestirme = scavenger_besleme_miktari / scavenger_konsantre_katı

    # ==========================================================
    # NİHAİ ÜRÜNLER
    # ==========================================================

    nihai_konsantre_miktari = cleaner_konsantre_katı
    nihai_konsantre_tenoru = cleaner_konsantre_tenoru
    nihai_konsantre_metali = cleaner_konsantre_metali

    nihai_artık_miktari = scavenger_artık_katı
    nihai_artık_tenoru = scavenger_artık_tenoru
    nihai_artık_metali = scavenger_artık_metali

    # ==========================================================
    # GENEL DEVRE PERFORMANSI
    # ==========================================================

    genel_verim = (nihai_konsantre_metali /tesis_besleme_metali) * 100
    genel_zenginlestirme = (besleme_miktari /cleaner_konsantre_katı)
    metal_kaybi = (nihai_artık_metali /tesis_besleme_metali) * 100

    # ==========================================================
    # DENGE
    # ==========================================================

    kutle_dengesi_farki = (besleme_miktari -nihai_konsantre_miktari - nihai_artık_miktari)
    metal_dengesi_farki = (tesis_besleme_metali -nihai_konsantre_metali - nihai_artık_metali)

    #------------------------------------------------------------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------------
    #Rougher-----------------------------------------------------------------------------------------------------------
    rougher_hesaplamalar_frame = Frame(analiz_frame,bg="white")
    rougher_hesaplamalar_frame.grid(row=0,column=0,padx=10,pady=10)

    rougher_hesaplamalar_label =Label(rougher_hesaplamalar_frame,bg="white",font=font2)
    rougher_hesaplamalar_label.config(text="Rougher")
    rougher_hesaplamalar_label.grid(row=1,column=0,padx=10,pady=10)

    #Besleme Metal Miktarı
    besleme_metal_miktarı_label_hesaplamalar =Label(rougher_hesaplamalar_frame,bg="white",font=font3)
    besleme_metal_miktarı_label_hesaplamalar.config(text="Besleme Metal Miktarı")
    besleme_metal_miktarı_label_hesaplamalar.grid(row=2,column=0,padx=10,pady=10)

    besleme_metal_miktarı_hesaplamalar = Label(rougher_hesaplamalar_frame, bg="white", font=font3)
    besleme_metal_miktarı_hesaplamalar.config(text=f"{rougher_besleme_metali:.2f}")
    besleme_metal_miktarı_hesaplamalar.grid(row=2, column=1, padx=10, pady=10)

    #Konsantre Metal Miktarı
    konsantre_metal_miktarı_label_hesaplamalar =Label(rougher_hesaplamalar_frame,bg="white",font=font3)
    konsantre_metal_miktarı_label_hesaplamalar.config(text="Konsantre Metal Miktarı")
    konsantre_metal_miktarı_label_hesaplamalar.grid(row=3,column=0,padx=10,pady=10)

    konsantre_metal_miktarı_hesaplamalar = Label(rougher_hesaplamalar_frame, bg="white", font=font3)
    konsantre_metal_miktarı_hesaplamalar.config(text=f"{rougher_konsantre_metali:.2f}")
    konsantre_metal_miktarı_hesaplamalar.grid(row=3, column=1, padx=10, pady=10)

    #Artık Metal Miktarı
    artık_metal_miktarı_label_hesaplamalar =Label(rougher_hesaplamalar_frame,bg="white",font=font3)
    artık_metal_miktarı_label_hesaplamalar.config(text="Artık Metal Miktarı")
    artık_metal_miktarı_label_hesaplamalar.grid(row=4,column=0,padx=10,pady=10)

    artık_metal_miktarı_hesaplamalar = Label(rougher_hesaplamalar_frame, bg="white", font=font3)
    artık_metal_miktarı_hesaplamalar.config(text=f"{rougher_artık_metali:.2f}")
    artık_metal_miktarı_hesaplamalar.grid(row=4, column=1, padx=10, pady=10)

    #Verim
    verim_label_hesaplamalar =Label(rougher_hesaplamalar_frame,bg="white",font=font3)
    verim_label_hesaplamalar.config(text="Verim")
    verim_label_hesaplamalar.grid(row=5,column=0,padx=10,pady=10)

    verim_hesaplamalar = Label(rougher_hesaplamalar_frame, bg="white",font=font3)
    verim_hesaplamalar.config(text=f"{rougher_verim:.2f}")
    verim_hesaplamalar.grid(row=5, column=1, padx=10, pady=10)

    #Zenginleştirme Oranı
    zenginleştirme_oranı_label_hesaplamalar =Label(rougher_hesaplamalar_frame,bg="white",font=font3)
    zenginleştirme_oranı_label_hesaplamalar.config(text="Zenginleştirme Oranı")
    zenginleştirme_oranı_label_hesaplamalar.grid(row=6,column=0,padx=10,pady=10)

    zenginleştirme_oranı_hesaplamalar = Label(rougher_hesaplamalar_frame, bg="white",font=font3)
    zenginleştirme_oranı_hesaplamalar.config(text=f"{rougher_zenginlestirme:.2f}")
    zenginleştirme_oranı_hesaplamalar.grid(row=6, column=1, padx=10, pady=10)

    #Cleaner------------------------------------------------------------------------------------------------------------
    cleaner_hesaplamalar_frame = Frame(analiz_frame,bg="white")
    cleaner_hesaplamalar_frame.grid(row=0,column=1,padx=10,pady=10)

    cleaner_hesaplamalar_label =Label(cleaner_hesaplamalar_frame,bg="white",font=font2)
    cleaner_hesaplamalar_label.config(text="Cleaner")
    cleaner_hesaplamalar_label.grid(row=1,column=0,padx=10,pady=10)

    #Besleme Metal Miktarı
    besleme_metal_miktarı_cleaner_label_hesaplamalar =Label(cleaner_hesaplamalar_frame,bg="white",font=font3)
    besleme_metal_miktarı_cleaner_label_hesaplamalar.config(text="Besleme Metal Miktarı")
    besleme_metal_miktarı_cleaner_label_hesaplamalar.grid(row=2,column=0,padx=10,pady=10)

    besleme_metal_miktarı_cleaner_hesaplamalar = Label(cleaner_hesaplamalar_frame, bg="white", font=font3)
    besleme_metal_miktarı_cleaner_hesaplamalar.config(text=f"{cleaner_besleme_metali:.2f}")
    besleme_metal_miktarı_cleaner_hesaplamalar.grid(row=2, column=1, padx=10, pady=10)

    #Konsantre Metal Miktarı
    konsantre_metal_miktarı_cleaner_label_hesaplamalar =Label(cleaner_hesaplamalar_frame,bg="white",font=font3)
    konsantre_metal_miktarı_cleaner_label_hesaplamalar.config(text="Konsantre Metal Miktarı")
    konsantre_metal_miktarı_cleaner_label_hesaplamalar.grid(row=3,column=0,padx=10,pady=10)

    konsantre_metal_miktarı_cleaner_hesaplamalar = Label(cleaner_hesaplamalar_frame, bg="white", font=font3)
    konsantre_metal_miktarı_cleaner_hesaplamalar.config(text=f"{cleaner_konsantre_metali:.2f}")
    konsantre_metal_miktarı_cleaner_hesaplamalar.grid(row=3, column=1, padx=10, pady=10)

    #Artık Metal Miktarı
    artık_metal_miktarı_cleaner_label_hesaplamalar =Label(cleaner_hesaplamalar_frame,bg="white",font=font3)
    artık_metal_miktarı_cleaner_label_hesaplamalar.config(text="Artık Metal Miktarı")
    artık_metal_miktarı_cleaner_label_hesaplamalar.grid(row=4,column=0,padx=10,pady=10)

    artık_metal_miktarı_cleaner_hesaplamalar = Label(cleaner_hesaplamalar_frame, bg="white",font=font3)
    artık_metal_miktarı_cleaner_hesaplamalar.config( text=f"{cleaner_artık_metali:.2f}")
    artık_metal_miktarı_cleaner_hesaplamalar.grid(row=4, column=1, padx=10, pady=10)

    #Verim
    verim_cleaner_label_hesaplamalar =Label(cleaner_hesaplamalar_frame,bg="white",font=font3)
    verim_cleaner_label_hesaplamalar.config(text="Verim")
    verim_cleaner_label_hesaplamalar.grid(row=5,column=0,padx=10,pady=10)

    verim_cleaner_hesaplamalar = Label(cleaner_hesaplamalar_frame, bg="white",font=font3)
    verim_cleaner_hesaplamalar.config(  text=f"{cleaner_verim:.2f}")
    verim_cleaner_hesaplamalar.grid(row=5, column=1, padx=10, pady=10)

    #Zenginleştirme Oranı
    zenginleştirme_oranı_cleaner_label_hesaplamalar =Label(cleaner_hesaplamalar_frame,bg="white",font=font3)
    zenginleştirme_oranı_cleaner_label_hesaplamalar.config(text="Zenginleştirme Oranı")
    zenginleştirme_oranı_cleaner_label_hesaplamalar.grid(row=6,column=0,padx=10,pady=10)

    zenginleştirme_oranı_cleaner_hesaplamalar = Label(cleaner_hesaplamalar_frame, bg="white",font=font3)
    zenginleştirme_oranı_cleaner_hesaplamalar.config(text=f"{cleaner_zenginlestirme:.2f}")
    zenginleştirme_oranı_cleaner_hesaplamalar.grid(row=6, column=1, padx=10, pady=10)

    # Scavenger------------------------------------------------------------------------------------------------------------
    scavenger_hesaplamalar_frame = Frame(analiz_frame, bg="white")
    scavenger_hesaplamalar_frame.grid(row=0, column=2, padx=10, pady=10)

    scavenger_hesaplamalar_label = Label(scavenger_hesaplamalar_frame, bg="white", font=font2)
    scavenger_hesaplamalar_label.config(text="Scavenger")
    scavenger_hesaplamalar_label.grid(row=1, column=0, padx=10, pady=10)

    # Besleme Metal Miktarı
    besleme_metal_miktarı_scavenger_label_hesaplamalar = Label(scavenger_hesaplamalar_frame, bg="white", font=font3)
    besleme_metal_miktarı_scavenger_label_hesaplamalar.config(text="Besleme Metal Miktarı")
    besleme_metal_miktarı_scavenger_label_hesaplamalar.grid(row=2, column=0, padx=10, pady=10)

    besleme_metal_miktarı_scavenger_hesaplamalar = Label(scavenger_hesaplamalar_frame, bg="white", font=font3)
    besleme_metal_miktarı_scavenger_hesaplamalar.config(text=f"{scavenger_besleme_metali:.2f}")
    besleme_metal_miktarı_scavenger_hesaplamalar.grid(row=2, column=1, padx=10, pady=10)

    # Konsantre Metal Miktarı
    konsantre_metal_miktarı_scavenger_label_hesaplamalar = Label(scavenger_hesaplamalar_frame, bg="white", font=font3)
    konsantre_metal_miktarı_scavenger_label_hesaplamalar.config(text="Konsantre Metal Miktarı")
    konsantre_metal_miktarı_scavenger_label_hesaplamalar.grid(row=3, column=0, padx=10, pady=10)

    konsantre_metal_miktarı_scavenger_hesaplamalar = Label(scavenger_hesaplamalar_frame, bg="white", font=font3)
    konsantre_metal_miktarı_scavenger_hesaplamalar.config(text=f"{scavenger_konsantre_metali:.2f}")
    konsantre_metal_miktarı_scavenger_hesaplamalar.grid(row=3, column=1, padx=10, pady=10)

    # Artık Metal Miktarı
    artık_metal_miktarı_scavenger_label_hesaplamalar = Label(scavenger_hesaplamalar_frame, bg="white", font=font3)
    artık_metal_miktarı_scavenger_label_hesaplamalar.config(text="Artık Metal Miktarı")
    artık_metal_miktarı_scavenger_label_hesaplamalar.grid(row=4, column=0, padx=10, pady=10)

    artık_metal_miktarı_scavenger_hesaplamalar = Label(scavenger_hesaplamalar_frame, bg="white",font=font3)
    artık_metal_miktarı_scavenger_hesaplamalar.config(text=f"{scavenger_artık_metali:.2f}")
    artık_metal_miktarı_scavenger_hesaplamalar.grid(row=4, column=1, padx=10, pady=10)

    # Verim
    verim_scavenger_label_hesaplamalar = Label(scavenger_hesaplamalar_frame, bg="white", font=font3)
    verim_scavenger_label_hesaplamalar.config(text="Verim")
    verim_scavenger_label_hesaplamalar.grid(row=5, column=0, padx=10, pady=10)

    verim_scavenger_hesaplamalar = Label(scavenger_hesaplamalar_frame, bg="white", font=font3)
    verim_scavenger_hesaplamalar.config(text=f"{scavenger_verim:.2f}")
    verim_scavenger_hesaplamalar.grid(row=5, column=1, padx=10, pady=10)

    # Zenginleştirme Oranı
    zenginleştirme_oranı_scavenger_label_hesaplamalar = Label(scavenger_hesaplamalar_frame, bg="white", font=font3)
    zenginleştirme_oranı_scavenger_label_hesaplamalar.config(text="Zenginleştirme Oranı")
    zenginleştirme_oranı_scavenger_label_hesaplamalar.grid(row=6, column=0, padx=10, pady=10)

    zenginleştirme_oranı_scavenger_hesaplamalar = Label(scavenger_hesaplamalar_frame, bg="white",font=font3)
    zenginleştirme_oranı_scavenger_hesaplamalar.config(text=f"{scavenger_zenginlestirme:.2f}")
    zenginleştirme_oranı_scavenger_hesaplamalar.grid(row=6, column=1, padx=10, pady=10)

    #Genel-------------------------------------------------------------------------------------------------------------
    genel_hesaplamalar_frame = Frame(analiz_frame, bg="white")
    genel_hesaplamalar_frame.grid(row=0, column=3, padx=10, pady=10)

    genel_hesaplamalar_label = Label(genel_hesaplamalar_frame, bg="white", font=font2)
    genel_hesaplamalar_label.config(text="Genel")
    genel_hesaplamalar_label.grid(row=1, column=0, padx=10, pady=10)

    # Besleme Metal Miktarı
    besleme_metal_miktarı_genel_label_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)
    besleme_metal_miktarı_genel_label_hesaplamalar.config(text="Besleme Metal Miktarı")
    besleme_metal_miktarı_genel_label_hesaplamalar.grid(row=2, column=0, padx=10, pady=10)

    besleme_metal_miktarı_genel_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)
    besleme_metal_miktarı_genel_hesaplamalar.config(text=f"{tesis_besleme_metali:.2f}")
    besleme_metal_miktarı_genel_hesaplamalar.grid(row=2, column=1, padx=10, pady=10)

    # Konsantre Metal Miktarı
    konsantre_metal_miktarı_genel_label_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)
    konsantre_metal_miktarı_genel_label_hesaplamalar.config(text="Konsantre Metal Miktarı")
    konsantre_metal_miktarı_genel_label_hesaplamalar.grid(row=3, column=0, padx=10, pady=10)

    konsantre_metal_miktarı_genel_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)
    konsantre_metal_miktarı_genel_hesaplamalar.config(text=f"{nihai_konsantre_metali:.2f}")
    konsantre_metal_miktarı_genel_hesaplamalar.grid(row=3, column=1, padx=10, pady=10)

    # Artık Metal Miktarı
    artık_metal_miktarı_genel_label_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)
    artık_metal_miktarı_genel_label_hesaplamalar.config(text="Artık Metal Miktarı")
    artık_metal_miktarı_genel_label_hesaplamalar.grid(row=4, column=0, padx=10, pady=10)

    artık_metal_miktarı_genel_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", text="-", font=font3)
    artık_metal_miktarı_genel_hesaplamalar.config(text=f"{nihai_artık_metali:.2f}")
    artık_metal_miktarı_genel_hesaplamalar.grid(row=4, column=1, padx=10, pady=10)

    # Verim
    verim_genel_label_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)
    verim_genel_label_hesaplamalar.config(text="Verim")
    verim_genel_label_hesaplamalar.grid(row=5, column=0, padx=10, pady=10)

    verim_genel_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)
    verim_genel_hesaplamalar.config( text=f"{genel_verim:.2f}")
    verim_genel_hesaplamalar.grid(row=5, column=1, padx=10, pady=10)

    # Zenginleştirme Oranı
    zenginleştirme_oranı_genel_label_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)
    zenginleştirme_oranı_genel_label_hesaplamalar.config(text="Zenginleştirme Oranı")
    zenginleştirme_oranı_genel_label_hesaplamalar.grid(row=6, column=0, padx=10, pady=10)

    zenginleştirme_oranı_genel_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)
    zenginleştirme_oranı_genel_hesaplamalar.config(text=f"{genel_zenginlestirme:.2f}")
    zenginleştirme_oranı_genel_hesaplamalar.grid(row=6, column=1, padx=10, pady=10)

    #Metal Kaybı
    metal_kaybi_genel_label_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)
    metal_kaybi_genel_label_hesaplamalar.config(text="Metal Kaybı")
    metal_kaybi_genel_label_hesaplamalar.grid(row=7, column=0, padx=10, pady=10)

    metal_kaybi_genel_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)
    metal_kaybi_genel_hesaplamalar.config(text=f"{metal_kaybi:.2f}")
    metal_kaybi_genel_hesaplamalar.grid(row=7, column=1, padx=10, pady=10)


    # Kütle Dengesi Farkı
    kutle_dengesi_farki_label_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)
    kutle_dengesi_farki_label_hesaplamalar.config(text="Kütle Dengesi Farkı")
    kutle_dengesi_farki_label_hesaplamalar.grid(row=8, column=0, padx=10, pady=10)

    kutle_dengesi_farki_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)

    kutle_dengesi_farki_hesaplamalar.config(text=f"{kutle_dengesi_farki:.2f}")

    kutle_dengesi_farki_hesaplamalar.grid(row=8, column=1, padx=10, pady=10)

    # Metal Dengesi Farkı
    metal_dengesi_farki_label_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)
    metal_dengesi_farki_label_hesaplamalar.config(text="Metal Dengesi Farkı")
    metal_dengesi_farki_label_hesaplamalar.grid(row=9, column=0, padx=10, pady=10)

    metal_dengesi_farki_hesaplamalar = Label(genel_hesaplamalar_frame, bg="white", font=font3)
    metal_dengesi_farki_hesaplamalar.config(text=f"{metal_dengesi_farki:.2f}")
    metal_dengesi_farki_hesaplamalar.grid(row=9, column=1, padx=10, pady=10)

    sonuclar.clear()

    sonuclar["besleme_miktari"] = besleme_miktari
    sonuclar["nihai_konsantre_miktari"] = nihai_konsantre_miktari
    sonuclar["nihai_artık_miktari"] = nihai_artık_miktari

    sonuclar["besleme_tenoru"] = besleme_tenoru
    sonuclar["nihai_konsantre_tenoru"] = nihai_konsantre_tenoru

    sonuclar["genel_verim"] = genel_verim
    sonuclar["genel_zenginlestirme"] = genel_zenginlestirme
    sonuclar["metal_kaybi"] = metal_kaybi

    sonuclar["kutle_dengesi"] = kutle_dengesi_farki
    sonuclar["metal_dengesi"] = metal_dengesi_farki

    sonuclar["rougher_verim"] = rougher_verim
    sonuclar["cleaner_verim"] = cleaner_verim
    sonuclar["scavenger_verim"] = scavenger_verim

    sonuclar["rougher_zenginlestirme"] = rougher_zenginlestirme
    sonuclar["cleaner_zenginlestirme"] = cleaner_zenginlestirme
    sonuclar["scavenger_zenginlestirme"] = scavenger_zenginlestirme

    sonuclar["rougher_besleme_tenoru"] = rougher_besleme_tenoru
    sonuclar["cleaner_besleme_tenoru"] = cleaner_besleme_tenoru
    sonuclar["scavenger_besleme_tenoru"] = scavenger_besleme_tenoru

    sonuclar["rougher_konsantre_tenoru"] = rougher_konsantre_tenoru
    sonuclar["cleaner_konsantre_tenoru"] = cleaner_konsantre_tenoru
    sonuclar["scavenger_konsantre_tenoru"] = scavenger_konsantre_tenoru