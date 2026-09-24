from tkinter import messagebox
import math
veriler = {}

def sayi_al(entry, alan_adi, minimum=0, maksimum=None):
    deger = entry.get().strip()

    if deger == "":
        raise ValueError(f"{alan_adi} boş bırakılamaz.")

    deger = deger.replace(",", ".")

    try:
        deger = float(deger)

    except ValueError:
        raise ValueError(f"{alan_adi} sayı değeri olmalıdır.")

    if not math.isfinite(deger):
        raise ValueError(f"{alan_adi} geçerli bir sayı olmalıdır.")

    if minimum is not None and deger <= minimum:
        raise ValueError(f"{alan_adi} {minimum} değerinden büyük olmalıdır.")

    if maksimum is not None and deger > maksimum:
        raise ValueError(f"{alan_adi} {maksimum} değerinden büyük olamaz.")

    return deger

def verileri_kaydet(
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
):
    try:
        #Tesis Beslemesi
        besleme_miktari = sayi_al(besleme_miktari_entry,"Besleme Miktarı",minimum=0)
        besleme_tenoru =  sayi_al(besleme_tenoru_entry,"Besleme Tenörü",minimum=0,maksimum=100)

        #Rougher
        rougher_konsantre_katı = sayi_al(konsantre_katı_rougher_entry, "Rougher Konsantre Katı", minimum=0)
        rougher_konsantre_tenoru = sayi_al(konsantre_tenoru_rougher_entry, "Rougher Konsantre Tenörü", minimum=0, maksimum=100)
        rougher_artik_katı = sayi_al(artik_katı_rougher_entry, "Rougher Artık Katı", minimum=0)
        rougher_artik_tenoru = sayi_al(artik_tenoru_rougher_entry, "Rougher Artık Tenörü", minimum=0, maksimum=100)

        #Cleaner
        cleaner_konsantre_katı = sayi_al(konsantre_katı_cleaner_entry, "Cleaner Konsantre Katı", minimum=0)
        cleaner_konsantre_tenoru = sayi_al(konsantre_tenoru_cleaner_entry, "Cleaner Konsantre Tenörü", minimum=0, maksimum=100)
        cleaner_artik_katı = sayi_al(artik_katı_cleaner_entry, "Cleaner Artık Katı", minimum=0)
        cleaner_artik_tenoru = sayi_al(artik_tenoru_cleaner_entry, "Cleaner Artık Tenörü", minimum=0, maksimum=100)

        #Scavenger
        scavenger_konsantre_katı = sayi_al(konsantre_katı_scavenger_entry, "Scavenger Konsantre Katı", minimum=0)
        scavenger_konsantre_tenoru = sayi_al(konsantre_tenoru_scavenger_entry, "Scavenger Konsantre Tenörü", minimum=0, maksimum=100)
        scavenger_artik_katı = sayi_al(artik_katı_scavenger_entry, "Scavenger Artık Katı", minimum=0)
        scavenger_artik_tenoru = sayi_al(artik_tenoru_scavenger_entry, "Scavenger Artık Tenörü", minimum=0, maksimum=100)

    except ValueError as hata:
        messagebox.showerror("Hatalı Veri Girişi", str(hata))
        return



    veriler.clear()

    veriler["tesis_besleme"] = {
        "miktar": besleme_miktari,
        "tenor": besleme_tenoru
    }

    veriler["rougher"] = {
        "konsantre_katı": rougher_konsantre_katı,
        "konsantre_tenoru": rougher_konsantre_tenoru,
        "artik_katı": rougher_artik_katı,
        "artik_tenoru": rougher_artik_tenoru
    }

    veriler["cleaner"] = {
        "konsantre_katı": cleaner_konsantre_katı,
        "konsantre_tenoru": cleaner_konsantre_tenoru,
        "artik_katı": cleaner_artik_katı,
        "artik_tenoru": cleaner_artik_tenoru
    }

    veriler["scavenger"] = {
        "konsantre_katı": scavenger_konsantre_katı,
        "konsantre_tenoru": scavenger_konsantre_tenoru,
        "artik_katı": scavenger_artik_katı,
        "artik_tenoru": scavenger_artik_tenoru
    }

    messagebox.showinfo("Veriler", "Veriler başarıyla kaydedildi.")

