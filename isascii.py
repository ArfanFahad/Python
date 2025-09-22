data = ["John", "Müller", "Satoshi", "علي"]

for name in data:
    if not name.isascii():
        print(f"Non-ASCII detected: {name}")


text = "café ☕"
if not text.isascii():
    clean_text = text.encode("ascii", "ignore").decode()
    print(clean_text)


username = "Fahad😊"

if username.isascii():
    print("Valid username")
else: 
    print("Invalid username: Non-Ascii found")


