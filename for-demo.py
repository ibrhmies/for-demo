sayilar = [1,5,15,35,57,72]

urunler = ["ahmet","mehmet","ayşe","esma","yaşar"]

# 1-> listedeki tüm elemanları yazdırın
for i in sayilar:
    print(i)


# 2-> sayilar listesindeki hangi sayilar 5 in katıdır

for i in sayilar:
    if (i % 5 ==0):
        print(i)

# 3-> sayilar listesindeki sayılar toplamı kaçtır
top= 0
for i in sayilar:
    top= top+i   
print(top)
# print komutunu for döngüsü dışına yazmamızın sebebi bize en son değer olan toplamı versi  eğer döngünün içinde olursa habire bir değerle sonrakini toplayıp ekrana yazdıracak.


# 4-> sayilar listesindeki çift sayiların karesini alın.

for i in sayilar:
    if (i % 2 == 0):
        print(i**2)


# 5-> urunler listesindeki her bir elemanın 2. karakterlerini yazdırın.

for i in urunler:
    print(i[2])


#6-> urunler listesinde a harfi bulunan elemanları yazın.

for i in urunler:
    if (i.count("a")):
        print(i)
        