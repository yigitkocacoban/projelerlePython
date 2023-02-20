import math
import random

oyuncu1, oyuncu2, oyuncu3, oyuncu4, oyuncu5 = 0, 0, 0, 0, 0

puanDurumu = ["Gamer 1", oyuncu1, "Gamer 2", oyuncu2, "Gamer 3", oyuncu3, "Gamer 4", oyuncu4, "Gamer 5", oyuncu5]

print(puanDurumu)

gamer1 = int(input("Oyuncu 1, sayı giriniz (1-100)"))
if gamer1 > 100:
    exit
gamer2 = int(input("Oyuncu 2, sayı giriniz (1-100)"))
if gamer2 > 100:
    exit
gamer3 = int(input("Oyuncu 3, sayı giriniz (1-100)"))
if gamer3 > 100:
    exit
gamer4 = int(input("Oyuncu 4, sayı giriniz (1-100)"))
if gamer4 > 100:
    exit
gamer5 = int(input("Oyuncu 5, sayı giriniz (1-100)"))
if gamer5 > 100:
    exit


oyuncuTahminleri = [gamer1, gamer2, gamer3, gamer4, gamer5]

random.shuffle(oyuncuTahminleri)
randomTahmin = random.choice(oyuncuTahminleri)


if randomTahmin == gamer1:
    oyuncu1+=1
    oyuncu2-=1
    oyuncu3-=1
    oyuncu4-=1
    oyuncu5-=1
    print("1. oyuncu kazandı.")
elif randomTahmin == gamer2:
    oyuncu1-=1
    oyuncu2+=1
    oyuncu3-=1
    oyuncu4-=1
    oyuncu5-=1
    print("2. oyuncu kazandı.")
elif randomTahmin == gamer3:
    oyuncu1-=1
    oyuncu2-=1
    oyuncu3+=1
    oyuncu4-=1
    oyuncu5-=1
    print("3. oyuncu kazandı.")
elif randomTahmin == gamer4:
    oyuncu1-=1
    oyuncu2-=1
    oyuncu3-=1
    oyuncu4+=1
    oyuncu5-=1
    print("4. oyuncu kazandı.")
elif randomTahmin == gamer5:
    oyuncu1-=1
    oyuncu2-=1
    oyuncu3-=1
    oyuncu4-=1
    oyuncu5+=1
    print("5. oyuncu kazandı.")
else:
    exit

    print(randomTahmin)


    
