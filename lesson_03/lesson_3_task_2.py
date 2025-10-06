from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79001112233"),
    Smartphone("Samsung", "Galaxy S24", "+79002223344"),
    Smartphone("Xiaomi", "13 Pro", "+79003334455"),
    Smartphone("Google", "Pixel 8", "+79004445566"),
    Smartphone("OnePlus", "12", "+79005556677")
]

for phone in catalog:
    print(f"{phone.brand}, {phone.model}, {phone.number}")