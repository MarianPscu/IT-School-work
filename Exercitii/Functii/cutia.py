def pret_cutie(inaltime, latime, lungime, tip_carton):

    price = 0



    if tip_carton == 1:
        price = 25

    elif tip_carton == 2:
        price += price + (25*10) // 100

    else:
        price += price + (25*20) // 100