import random
import string


def sifre_uret(uzunluk=12):
    if uzunluk < 4:
        return "Şifre uzunluğu en az 4 olmalı!"

    # Her kategoriden en az 1 karakter ekle
    harf = random.choice(string.ascii_letters)  # a-z, A-Z
    rakam = random.choice(string.digits)  # 0-9
    ozel = random.choice(string.punctuation)  # !@#$%& vb.

    # Kalan karakterler rastgele seçilsin
    digerleri = ''.join(
        random.choice(string.ascii_letters + string.digits +
                      string.punctuation) for _ in range(uzunluk - 3))

    # Karakterleri karıştır
    sifre = harf + rakam + ozel + digerleri
    sifre = ''.join(random.sample(sifre, len(sifre)))

    return sifre


# Kullanıcıdan uzunluk al
uzunluk = input("Şifre uzunluğunu gir: ")
if uzunluk.isdigit():
    uzunluk = int(uzunluk)
    print("Oluşturulan Şifre:", sifre_uret(uzunluk))
else:
    print("Geçerli bir sayı gir!")
