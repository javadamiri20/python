admin_name = "Ali"

user_name = input("Enter your user name :")

age = int(input("Enter your age :"))

if age >= 18:
    if admin_name is user_name:
        print("Admin is activ.")
    elif user_name is not admin_name:
        print("karbar adi.")
else:
    print("karbar kam sen.")
