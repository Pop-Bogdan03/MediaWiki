# EXERCITII MEDIAWIKI


# Arie curte #0103
def validare_date(lungime, latime):
    return lungime.isnumeric() and latime.isnumeric()


def arie_curte(lungime, latime):
    # aria unui dreptunghi se obtine efectuand produsul dintre lungimea si latimea sa
    aria = lungime * latime
    # perimetrul unui dreptunghi se obtine efectuand suma dintre dublul lungimii si al latimii
    perimetrul = 2 * lungime + 2 * latime

    print(aria, perimetrul)


# Capete și picioare animale #0175
def validare_date(gaini, oi):
    flag = False
    if gaini.isnumeric() and oi.isnumeric():
        if 0 < int(gaini) < 1000000 and 0 < int(oi) < 1000000:
            flag = True
            return flag
        else:
            return flag
    else:
        return flag


def capete_picioare(gaini, oi):
    gaini = int(gaini)
    oi = int(oi)

    # numărul de capete se obține prin însumarea numărului de găini și de oi, deoarece amândouă au câte un cap
    capete = gaini + oi
    # numărul de picioare se obține prin însumarea dublului numărului de găini (găinile au cate 2 picioare) cu
    # împătritul numărului de oi (oile au cate 4 picioare)
    picioare = 2 * gaini + 4 * oi

    print(capete, picioare)


# Număr animale #0176
def validare_date(capete, picioare):
    flag = False
    if capete.isnumeric() and picioare.isnumeric():
        if 0 < int(capete) < 1000000 and 0 < int(picioare) < 1000000:
            flag = True
            return flag
        else:
            return flag
    else:
        return flag


def nr_animale(capete, picioare):
    capete = int(capete)
    picioare = int(picioare)

    picioare //= 2

    oi = picioare - capete
    gaini = capete - oi

    print(gaini, oi)


if __name__ == "__main__":
    # Arie curte #0103
    lungime = input()
    latime = input()

    if validare_date(lungime, latime) and 0 < int(lungime) < 10000 and 0 < int(latime) < 10000:
        print("Datele introduse corespund restrictiilor problemei.")
        arie_curte(int(lungime), int(latime))
    else:
        print("Datele introduse nu corespund restrictiilor problemei.")

    # Capete și picioare animale #0175
    gaini = input()
    oi = input()

    if validare_date(gaini, oi):
        print("Datele introduse corespund restrictiilor problemei.")
        capete_picioare(gaini, oi)
    else:
        print("Datele introduse nu corespund restrictiilor problemei.")

    # Număr animale #0176
    capete = input()
    picioare = input()

    if validare_date(capete, picioare):
        print("Datele introduse corespund restrictiilor problemei.")
        nr_animale(capete, picioare)
    else:
        print("Datele introduse nu corespund restrictiilor problemei.")

