age =  int(input("Enter your age :"))
city = input("Enter your city :")
score = int(input("Enter your score :"))

vip_city =["tehran","esfahan","tabriz"]

if age >= 18:
    if city in vip_city:
        if score >= 80:
            print("dasresi Talaie.")
        elif score >= 50 and score < 80:
            print("dasresi Noghreie.")
    else:
        print("dasresi Mamooli.")
else:
    print("dastresi gheir mojaz.")