from tkinter import *
from genel import genel
from veri import veri
from hesaplamalar import hesaplamalar
from grafik import grafik
from rapor import rapor

window = Tk()

window.title("Flotasyon Performans Analizi")
window.geometry("1200x700")
window.minsize(1100, 600)
window.config(bg="white")

#Fontlar
font1 =("Arial", 20, "bold")
font2 = ("Arial", 15, "bold")
font3 = ("Arial", 13)

#Başlık
baslik = Label(window,text="Flotasyon Performans Analizi",bg="white",fg="black",font=(font1))
baslik.pack(pady=20)

#Menu
menu_frame = Frame( window, bg="white" )
menu_frame.pack( fill="x", padx=30, pady=10 )

def butona_bas(button):
    genel_button.config(bg="white",fg="black")
    veri_button.config(bg="white",fg="black")
    hesaplamalar_button.config(bg="white",fg="black")
    grafik_button.config(bg="white",fg="black")
    rapor_button.config(bg="white",fg="black")
    button.config(bg="green",fg="white")


genel_button = Button(menu_frame,font=font2,command=lambda:(genel(analiz_frame, font2, font3), butona_bas(genel_button)))
genel_button.config(text="Genel",bg="white",fg="black")
genel_button.pack(side="left",expand=True,fill="x",padx=5)

veri_button = Button(menu_frame, font=font2,command=lambda:(veri(analiz_frame, font2, font3), butona_bas(veri_button)))
veri_button.config(text="Veri",bg="white",fg="black")
veri_button.pack(side="left",expand=True,fill="x",padx=5)

hesaplamalar_button = Button(menu_frame,font=font2)
hesaplamalar_button.config(text="Hesaplamalar",bg="white",fg="black",command=lambda: (hesaplamalar(analiz_frame,font2,font3),butona_bas(hesaplamalar_button)))
hesaplamalar_button.pack(side="left",expand=True,fill="x",padx=5)


grafik_button = Button(menu_frame,bg="white",fg="black", font=font2, command=lambda: (grafik(analiz_frame, font2, font3), butona_bas(grafik_button)))
grafik_button.config(text="Grafik",bg="white",fg="black")
grafik_button.pack(side="left",expand=True,fill="x",padx=5)

rapor_button = Button(menu_frame, font=font2,bg="white",fg="black", command=lambda: (rapor(analiz_frame, font2, font3), butona_bas(rapor_button)))
rapor_button.config(text="Rapor")
rapor_button.pack(side="left", expand=True, fill="x", padx=5)

#Analiz
analiz_frame= Frame(window, bg="white")
analiz_frame.pack( fill="both",expand=True, padx=30, pady=10 )

window.mainloop()