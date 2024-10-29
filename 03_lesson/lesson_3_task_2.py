from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 16 Pro Max", "+79275550055"),
    Smartphone("Samsung", "Galaxy Z Flip6", "+79024852146"),
    Smartphone("Xiaomi", "Poco X6 Pro", "+79637776363"),
    Smartphone("HUAWEI", "nova 12s", "+79033097063"),
    Smartphone("HONOR", "Magic V2", "+79171170107")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
