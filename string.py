
name = input("Enter your name :")

if len(name) < 5 and "a" in name:
    print("Nam mojaz ast.")
elif len(name) >= 5 and "a" in name:
    print("Nam toolani ba harf a.")
elif len(name) < 5 and "a" not in name:
    print("Nam na motabar.")
elif len(name) >= 5 and "a" not in name:
    print("Nam na motabar.")