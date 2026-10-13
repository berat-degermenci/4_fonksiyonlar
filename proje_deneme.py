def ortalama_hesapla (vize: float, final: float) -> float:
    ortalama = vize *0.4 + final *0.6
    return ortalama

def harf_notu_belirle(ortalama: float) -> str:

    if ortalama >= 85:
        return "A"
    elif ortalama >= 70:
        return "B"
    elif ortalama >= 50:
        return "C"
    else:
        return "F"

def sonucu_yazdir(isim: str, ortalama: float, harf: str):

    print(f"öğrenci: {isim}")
    print(f"ortalama: {ortalama}")
    print(f"harf notu: {harf}")

isim = input("öğrenci ismi: ")
vize = float(input("vize notu: "))
final = float(input("final notu: "))

ortalama = ortalama_hesapla(vize = vize, final = final)
harf = harf_notu_belirle(ortalama = ortalama)

sonucu_yazdir(isim = isim, ortalama = ortalama, harf = harf)