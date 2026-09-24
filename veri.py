from tkinter import *
from veriler import verileri_kaydet

def veri(analiz_frame,font2,font3):

    for widget in analiz_frame.winfo_children():
        widget.destroy()

    analiz_frame.grid_columnconfigure(0, weight=1)
    analiz_frame.grid_columnconfigure(1, weight=1)
    analiz_frame.grid_columnconfigure(2, weight=1)

    analiz_frame.grid_rowconfigure(1, weight=1)
    analiz_frame.grid_rowconfigure(2, weight=1)

    #Tesis Beslemesi----------------------------------------------------------------------------------------------------
    tesis_beslemesi_frame = Frame(analiz_frame,bg="white")
    tesis_beslemesi_frame.grid(row=1,column=0,padx=10,pady=10)

    besleme_verigirisi_label = Label(tesis_beslemesi_frame,bg="white",font=font2)
    besleme_verigirisi_label.config(text = "Tesis Beslemesi")
    besleme_verigirisi_label.grid(row=0,column=0,padx=10,pady=10,columnspan=2)

    #Besleme Miktarı
    besleme_miktari_label = Label(tesis_beslemesi_frame,bg="white",font=font3)
    besleme_miktari_label.config(text="Besleme Miktarı")
    besleme_miktari_label.grid(row=1,column=0,padx=10,pady=10)

    besleme_miktari_entry =Entry(tesis_beslemesi_frame,bg="white",font=font3,width=10)
    besleme_miktari_entry.grid(row=1,column=1,padx=10,pady=10)

    #Besleme Tenörü
    besleme_tenoru_label = Label(tesis_beslemesi_frame,bg="white",font=font3)
    besleme_tenoru_label.config(text="Besleme Tenörü")
    besleme_tenoru_label.grid(row=2,column=0,padx=10,pady=10)

    besleme_tenoru_entry = Entry(tesis_beslemesi_frame,bg="white",font=font3,width=10)
    besleme_tenoru_entry.grid(row=2,column=1,padx=10,pady=10)

    #Rougher Devresi----------------------------------------------------------------------------------------------------
    #Rougher Frame
    rougher_frame = Frame(analiz_frame,bg="white")
    rougher_frame.grid(row=1,column=1,padx=10,pady=10)

    #Rougher Başlık
    rougher_baslik_label = Label(rougher_frame,bg="white",font=font2)
    rougher_baslik_label.config(text = "Rougher")
    rougher_baslik_label.grid(row=0,column=0,padx=10,pady=10,columnspan=2)

    #Konsantre Katı - Rougher
    konsantre_katı_rougher_label = Label(rougher_frame,bg="white",font=font3)
    konsantre_katı_rougher_label.config(text = "Konsantre Katı")
    konsantre_katı_rougher_label.grid(row=1,column=0,padx=10,pady=10)

    konsantre_katı_rougher_entry = Entry(rougher_frame,bg="white",font=font3,width=10)
    konsantre_katı_rougher_entry.grid(row=1,column=1,padx=10,pady=10)

    #Konsantre Tenörü - Rougher
    konsantre_tenoru_rougher_label = Label(rougher_frame,bg="white",font=font3)
    konsantre_tenoru_rougher_label.config(text="Konsantre Tenörü")
    konsantre_tenoru_rougher_label.grid(row=2,column=0,padx=10,pady=10)

    konsantre_tenoru_rougher_entry = Entry(rougher_frame,bg="white",font=font3,width=10)
    konsantre_tenoru_rougher_entry.grid(row=2,column=1,padx=10,pady=10)

    #Artık Katı - Rougher
    artik_katı_rougher_label = Label(rougher_frame,bg="white",font=font3)
    artik_katı_rougher_label.config(text = "Artık Katı")
    artik_katı_rougher_label.grid(row=3,column=0,padx=10,pady=10)

    artik_katı_rougher_entry = Entry(rougher_frame,bg="white",font=font3,width=10)
    artik_katı_rougher_entry.grid(row=3,column=1,padx=10,pady=10)

    #Artık Tenörü - Rougher
    artik_tenoru_rougher_label = Label(rougher_frame,bg="white",font=font3)
    artik_tenoru_rougher_label.config(text="Artık Tenörü")
    artik_tenoru_rougher_label.grid(row=4,column=0,padx=10,pady=10)

    artik_tenoru_rougher_entry = Entry(rougher_frame,bg="white",font=font3,width=10)
    artik_tenoru_rougher_entry.grid(row=4,column=1,padx=10,pady=10)

    #Cleaner Devresi----------------------------------------------------------------------------------------------------
    #Cleaner Frame
    cleaner_frame = Frame(analiz_frame,bg="white")
    cleaner_frame.grid(row=2,column=0,padx=10,pady=10)

    #Cleaner Başlık
    cleaner_baslik_label = Label(cleaner_frame, bg="white", font=font2)
    cleaner_baslik_label.config(text="Cleaner")
    cleaner_baslik_label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

    # Konsantre Katı - Cleaner
    konsantre_katı_cleaner_label = Label(cleaner_frame, bg="white", font=font3)
    konsantre_katı_cleaner_label.config(text="Konsantre Katı")
    konsantre_katı_cleaner_label.grid(row=1, column=0, padx=10, pady=10)

    konsantre_katı_cleaner_entry = Entry(cleaner_frame, bg="white", font=font3, width=10)
    konsantre_katı_cleaner_entry.grid(row=1, column=1, padx=10, pady=10)

    # Konsantre Tenörü - Cleaner
    konsantre_tenoru_cleaner_label = Label(cleaner_frame, bg="white", font=font3)
    konsantre_tenoru_cleaner_label.config(text="Konsantre Tenörü")
    konsantre_tenoru_cleaner_label.grid(row=2, column=0, padx=10, pady=10)

    konsantre_tenoru_cleaner_entry = Entry(cleaner_frame, bg="white", font=font3, width=10)
    konsantre_tenoru_cleaner_entry.grid(row=2, column=1, padx=10, pady=10)

    # Artık Katı - Cleaner
    artik_katı_cleaner_label = Label(cleaner_frame, bg="white", font=font3)
    artik_katı_cleaner_label.config(text="Artık Katı")
    artik_katı_cleaner_label.grid(row=3, column=0, padx=10, pady=10)

    artik_katı_cleaner_entry = Entry(cleaner_frame, bg="white", font=font3, width=10)
    artik_katı_cleaner_entry.grid(row=3, column=1, padx=10, pady=10)

    # Artık Tenörü - Cleaner
    artik_tenoru_cleaner_label = Label(cleaner_frame, bg="white", font=font3)
    artik_tenoru_cleaner_label.config(text="Artık Tenörü")
    artik_tenoru_cleaner_label.grid(row=4, column=0, padx=10, pady=10)

    artik_tenoru_cleaner_entry = Entry(cleaner_frame, bg="white", font=font3, width=10)
    artik_tenoru_cleaner_entry.grid(row=4, column=1, padx=10, pady=10)

    #Scavenger Devresi----------------------------------------------------------------------------------------------------
    #Scavenger Frame
    scavenger_frame = Frame(analiz_frame,bg="white")
    scavenger_frame.grid(row=2,column=1,padx=10,pady=10)

    #scavenger Başlık
    scavenger_baslık_label = Label(scavenger_frame,bg="white",font=font2)
    scavenger_baslık_label.config(text = "Scavenger")
    scavenger_baslık_label.grid(row=0,column=0,padx=10,pady=10,columnspan=2)

    #Konsantre Katı - scavenger
    konsantre_katı_scavenger_label = Label(scavenger_frame,bg="white",font=font3)
    konsantre_katı_scavenger_label.config(text = "Konsantre Katı")
    konsantre_katı_scavenger_label.grid(row=1,column=0,padx=10,pady=10)

    konsantre_katı_scavenger_entry = Entry(scavenger_frame,bg="white",font=font3,width=10)
    konsantre_katı_scavenger_entry.grid(row=1,column=1,padx=10,pady=10)

    #Konsantre Tenörü - scavenger
    konsantre_tenoru_scavenger_label = Label(scavenger_frame,bg="white",font=font3)
    konsantre_tenoru_scavenger_label.config(text="Konsantre Tenörü")
    konsantre_tenoru_scavenger_label.grid(row=2,column=0,padx=10,pady=10)

    konsantre_tenoru_scavenger_entry = Entry(scavenger_frame,bg="white",font=font3,width=10)
    konsantre_tenoru_scavenger_entry.grid(row=2,column=1,padx=10,pady=10)

    #Artık Katı - scavenger
    artik_katı_scavenger_label = Label(scavenger_frame,bg="white",font=font3)
    artik_katı_scavenger_label.config(text = "Artık Katı")
    artik_katı_scavenger_label.grid(row=3,column=0,padx=10,pady=10)

    artik_katı_scavenger_entry = Entry(scavenger_frame,bg="white",font=font3,width=10)
    artik_katı_scavenger_entry.grid(row=3,column=1,padx=10,pady=10)

    #Artık Tenörü - scavenger
    artik_tenoru_scavenger_label = Label(scavenger_frame,bg="white",font=font3)
    artik_tenoru_scavenger_label.config(text="Artık Tenörü")
    artik_tenoru_scavenger_label.grid(row=4,column=0,padx=10,pady=10)

    artik_tenoru_scavenger_entry = Entry(scavenger_frame,bg="white",font=font3,width=10)
    artik_tenoru_scavenger_entry.grid(row=4,column=1,padx=10,pady=10)

    # Verileri Kaydet--------------------------------------------------------------------------------------------------
    kaydet_frame = Frame(analiz_frame, bg="white")
    kaydet_frame.grid(row=2, column=2, sticky="s", padx=10, pady=10)

    verileri_kaydet_button = Button(
        kaydet_frame,
        bg="white",
        font=font3,
        text="Verileri Kaydet",
        command=lambda: verileri_kaydet(
            besleme_miktari_entry,
            besleme_tenoru_entry,

            konsantre_katı_rougher_entry,
            konsantre_tenoru_rougher_entry,
            artik_katı_rougher_entry,
            artik_tenoru_rougher_entry,

            konsantre_katı_cleaner_entry,
            konsantre_tenoru_cleaner_entry,
            artik_katı_cleaner_entry,
            artik_tenoru_cleaner_entry,

            konsantre_katı_scavenger_entry,
            konsantre_tenoru_scavenger_entry,
            artik_katı_scavenger_entry,
            artik_tenoru_scavenger_entry
        )
    )

    verileri_kaydet_button.grid(row=0,column=1,padx=10,pady=10)



