firstname = ""
lastname = ""

while firstname != "Fahad" and lastname != "Farazi":
    firstname = input("Enter firstname: ").strip()
    lastname = input("Enter lastname: ").strip()
    if firstname == "Fahad" and lastname == "Farazi":
        print("Corrent Name")
    else:
        print("Wrong name")
