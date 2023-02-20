ilkSayi = int(input("İlk sayıyı giriniz: "))

ikinciSayi = int(input("İkinci sayıyı giriniz: "))

islemSec = input("Yapmak istediğiniz işlem (topla, çarp, böl, çıkart) nedir: ")

if islemSec not in ["topla","çıkart","çarp","böl"]:

    exit

else:

    if islemSec == "topla":

        print("{} + {} = {}".format(ilkSayi, ikinciSayi, ilkSayi + ikinciSayi))

    elif islemSec == "çıkart":

        print("{} - {} = {}".format(ilkSayi, ikinciSayi, ilkSayi - ikinciSayi))

    elif islemSec == "çarp":

        print("{} * {} = {}".format(ilkSayi, ikinciSayi, ilkSayi * ikinciSayi))

    else:
        
        print("{} / {} = {}".format(ilkSayi, ikinciSayi, ilkSayi / ikinciSayi))
