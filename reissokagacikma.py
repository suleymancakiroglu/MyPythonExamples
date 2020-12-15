week=["Pazartesi","pazartesi","Salı","salı","Çarşamba","çarşamba","Perşembe","perşembe","Cuma","cuma"]
weekends=["Cumartesi","cumartesi","Pazar","pazar"]

day=str(input("Hangi gün? :"))
if day in week:
    work=str(input("Çalışıyor iseniz 'Evet', Çalışmıyorssanız 'Hayır'yazınız :"))
    if work=="Evet":
        print("Çalışın LAN!")
    else:
        Age=input("Yaşınız kaç? :")
        if 20<int(Age)<65:
            print("İstersen gez istersen yat.")
        else:
            time=input("Saat kaç? :")
            if 10<round(float(time))<20:
                print("Neree gidiyon yat aşşa!")
elif day in weekends:
    time=input("Saat kaç? :")
    if 10<round(float(time))<20:
        Age=input("Yaşınız kaç?")
        if 20<int(Age)<65:
            print("İstersen gez istersen yat.")
        else:
            print("Neree gidiyon yat aşşa!")
    else:
        print("Neree gidiyon yat aşşa!")
else:
    print("Silivri soğuktur kardeşim çok kurcalama!")