"""
- kullanıcıdan vize notu ve final notu alalım
- ortalama hesaplaması
- harf notu belirleme
- sonucu ekrana yazdırma
"""

# not hesaplama sistemi
def ortalama_hesapla(vize: float, final: float) -> float:
    """
    vize % 40, final % 60 olacak şekilde ortalama hesapla
    """
    ortalama = vize * 0.4 + final * 0.6
    return ortalama

def harf_notu_belirle(ortalama: float) -> str:
    """
    ortalama değerine göre harf notu döndürür
    """
    if ortalama >= 85:
        return "A"
    elif ortalama >= 70:
        return "B"
    elif ortalama >= 50:
        return "C"
    else:
        return "F"

def sonucu_yazdir(isim: str, ortalama: float, harf: str):
    """
    sonucu ekrana yazdırır
    """
    print(".......sonuc.......")
    print(f"öğrenci: {isim}")
    print(f"ortalama: {ortalama}")
    print(f"harf notu: {harf}")

# program akışı

isim = input("öğrenci adı: ")
vize = float(input("vize notu: "))
final = float(input("final notu: "))

ortalama = ortalama_hesapla(vize = vize, final = final)
harf = harf_notu_belirle(ortalama = ortalama)

sonucu_yazdir(isim = isim, ortalama = ortalama, harf = harf)