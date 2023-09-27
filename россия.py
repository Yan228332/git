cat = input("введите категорию товара"). lower()
summa = float(input("введите сумму:"))
if cat == "продукты":
    if summa < 100:
     print("попробуй нашу выпечку")
   if summa > 99 and summa <501:
       print("как насчет орехов в шоколаде")
       