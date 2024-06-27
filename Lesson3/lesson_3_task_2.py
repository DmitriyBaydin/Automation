from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "Iphone 17Pro", "+79261234567"))
catalog.append(Smartphone("Samsung", "Galaxy A54", "+79162223344"))
catalog.append(Smartphone("Huawei", "Nova 11Pro", "+79039999999"))
catalog.append(Smartphone("Xiaomi", "13Pro", "+79687775533"))
catalog.append(Smartphone("Asus", "Zenphone 10", "+79269876543"))


for phone in catalog:
    print(f"{phone.mark} - {phone.model}. {phone.number}")
