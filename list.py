frut_list = ["apple","orange","bannana"]
name = "apple"
match name:
    case "apple":
        if name in frut_list:
            print("exist")
        else:
            print("not exist")
    case "orange":
        if name in frut_list:
            print("exist")
        else:
            print("not exist")
    case "orange":
        if name in frut_list:
            print("exist")
        else:
            print("not exist")
    case _:
        print("invalid value")

