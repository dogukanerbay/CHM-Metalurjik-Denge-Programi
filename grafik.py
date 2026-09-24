from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from veriler import veriler


def grafik(analiz_frame, font2, font3):

    for widget in analiz_frame.winfo_children():
        widget.destroy()

    if "tesis_besleme" not in veriler:

        uyarı_label = Label(analiz_frame, bg="white", fg="black", font=font3)
        uyarı_label.config(text="Önce Veri Girişi bölümünden verileri girip kaydediniz.")
        uyarı_label.pack(pady=30)
        return

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

    # ==========================================================
    # METAL MİKTARLARI
    # ==========================================================
    tesis_besleme_metali = besleme_miktari * besleme_tenoru / 100

    rougher_konsantre_metali = (rougher_konsantre_katı * rougher_konsantre_tenoru / 100)
    rougher_artık_metali = (rougher_artık_katı * rougher_artık_tenoru / 100)

    cleaner_konsantre_metali = (cleaner_konsantre_katı * cleaner_konsantre_tenoru / 100)
    cleaner_artık_metali = (cleaner_artık_katı * cleaner_artık_tenoru / 100)

    scavenger_konsantre_metali = (scavenger_konsantre_katı * scavenger_konsantre_tenoru / 100)
    scavenger_artık_metali = (scavenger_artık_katı * scavenger_artık_tenoru / 100)

    # ==========================================================
    # KADEME BESLEMELERİ
    # ==========================================================

    rougher_besleme_miktari = (besleme_miktari + cleaner_artık_katı + scavenger_konsantre_katı)
    rougher_besleme_metali = (tesis_besleme_metali + cleaner_artık_metali + scavenger_konsantre_metali)
    rougher_besleme_tenoru = (rougher_besleme_metali / rougher_besleme_miktari * 100)

    cleaner_besleme_miktari = rougher_konsantre_katı
    cleaner_besleme_tenoru = rougher_konsantre_tenoru

    scavenger_besleme_miktari = rougher_artık_katı
    scavenger_besleme_tenoru = rougher_artık_tenoru

    # ==========================================================
    # VERİMLER
    # ==========================================================

    rougher_verim = (rougher_konsantre_metali / rougher_besleme_metali * 100)
    cleaner_verim = (cleaner_konsantre_metali / rougher_konsantre_metali * 100)
    scavenger_verim = (scavenger_konsantre_metali / rougher_artık_metali * 100)

    # ==========================================================
    # ZENGİNLEŞTİRME ORANLARI
    # ==========================================================

    rougher_zenginlestirme = (rougher_besleme_miktari / rougher_konsantre_katı)
    cleaner_zenginlestirme = (cleaner_besleme_miktari / cleaner_konsantre_katı)
    scavenger_zenginlestirme = (scavenger_besleme_miktari / scavenger_konsantre_katı)

    # Başlık
    grafik_baslik = Label(analiz_frame,bg="white",fg="black",font=font2)
    grafik_baslik.config(text="Flotasyon Performans Grafikleri")
    grafik_baslik.pack(pady=10)

    # Grafik seçim alanı
    secim_frame = Frame(analiz_frame,bg="white")
    secim_frame.pack(padx=10,pady=10)

    # Grafik alanı
    grafik_frame = Frame(analiz_frame,bg="white")
    grafik_frame.pack(fill="both",expand=True,padx=10,pady=10)

    def grafik_temizle():

        for widget in grafik_frame.winfo_children():
            widget.destroy()

    def verim_grafigi():

        grafik_temizle()

        kademeler = ["Rougher", "Cleaner", "Scavenger"]
        verimler = [rougher_verim, cleaner_verim, scavenger_verim]

        figure = plt.Figure(figsize=(9, 5), dpi=100)
        ax = figure.add_subplot(111)

        ax.bar(kademeler, verimler)
        ax.set_title("Kademe Verim Karşılaştırması", pad=25)

        ax.set_xlabel("Flotasyon Kademesi")
        ax.set_ylabel("Verim (%)")
        ax.set_ylim(0, max(verimler) * 1.15)
        ax.grid(axis="y", alpha=0.3)

        for i, deger in enumerate(verimler):
            ax.text(i, deger + 2, f"{deger:.2f} %", ha="center")

        figure.tight_layout()
        canvas = FigureCanvasTkAgg(figure, master=grafik_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def tenor_grafigi():

        grafik_temizle()

        kademeler = ["Rougher", "Cleaner", "Scavenger"]

        besleme_tenorleri = [
            rougher_besleme_tenoru,
            cleaner_besleme_tenoru,
            scavenger_besleme_tenoru]

        konsantre_tenorleri = [
            rougher_konsantre_tenoru,
            cleaner_konsantre_tenoru,
            scavenger_konsantre_tenoru
        ]

        figure = plt.Figure(figsize=(9, 5), dpi=100)
        ax = figure.add_subplot(111)
        x = np.arange(len(kademeler))

        genislik = 0.35
        ax.bar(x - genislik / 2, besleme_tenorleri, genislik, label="Besleme Tenörü")
        ax.bar(x + genislik / 2, konsantre_tenorleri, genislik, label="Konsantre Tenörü")

        ax.set_title("Kademe Tenör Karşılaştırması", pad=25)

        ax.set_xlabel("Flotasyon Kademesi")

        ax.set_ylabel("Tenör (%)")

        ax.set_xticks(x)

        ax.set_xticklabels(kademeler)

        ax.legend()

        ax.grid(axis="y", alpha=0.3)

        figure.tight_layout()

        canvas = FigureCanvasTkAgg(figure, master=grafik_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def zenginlestirme_grafigi():

        grafik_temizle()

        kademeler = [
            "Rougher",
            "Cleaner",
            "Scavenger"
        ]

        oranlar = [
            rougher_zenginlestirme,
            cleaner_zenginlestirme,
            scavenger_zenginlestirme
        ]

        figure = plt.Figure(figsize=(9, 5), dpi=100)

        ax = figure.add_subplot(111)

        ax.bar(kademeler, oranlar)

        ax.set_title("Kademe Zenginleştirme Oranı", pad=25)

        ax.set_xlabel("Flotasyon Kademesi")

        ax.set_ylabel("Zenginleştirme Oranı")

        ax.grid(axis="y", alpha=0.3)

        for i, deger in enumerate(oranlar):

            ax.text(i, deger + 0.1, f"{deger:.2f}", ha="center")

        figure.tight_layout()

        canvas = FigureCanvasTkAgg(figure, master=grafik_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    # Grafik butonları
    verim_button = Button(secim_frame, font=font3, bg="white", command=verim_grafigi)
    verim_button.config(text="Kademe Verimleri")
    verim_button.pack(side="left", padx=5)

    tenor_button = Button(secim_frame, font=font3, bg="white", command=tenor_grafigi)
    tenor_button.config(text="Tenör Karşılaştırması")
    tenor_button.pack(side="left", padx=5)

    zenginlestirme_button = Button(secim_frame, text="Zenginleştirme Oranı", font=font3, bg="white", command=zenginlestirme_grafigi)
    zenginlestirme_button.pack(side="left", padx=5)

    # İlk açılışta verim grafiğini göster
    verim_grafigi()