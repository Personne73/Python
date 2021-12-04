# programme de la suite de Syracuse

def syracuse(n):
    """
    Fonction calculant la suite de syracuse d'un entier n

    :param n: un entier n

    :return:
        le temps de vol,
        le temps de vol en altitude,
        l'altitude maximale

    """
    k = 0  # temps de vol (le plus petit indicie k tel que uk = 1)

    brain = n
    i = 0  # temps de vol en altitude (plus petit indice k tel que u(k+1) <= u0

    val_max = 0  # valeur maximale de la suite

    while n != 1:
        if n % 2 == 0:
            n = n // 2
            k += 1
        else:
            n = 3 * n + 1
            k += 1

        if n >= brain:
            i += 1

        if n > val_max:
            val_max = n

    return k, i - 1, val_max


# k, i, val_max = syracuse(15)
# print(f"temps de vol : {k}, temps de vol en altitude : {i}, altitude maximale : {val_max}")

# variable qui vont stocker respectivement les valeurs max de l'altitude maximale, du temps de vol et du temps de vol
# en altitude des suites de Syracuse

altitude_max = 0
tps_vol_max = 0
tps_vol_alt_max = 0

for i in range(1, 10000):

    tps_vol, tps_vol_alt, altitude = syracuse(i)

    if altitude > altitude_max:
        altitude_max = altitude
    if tps_vol > tps_vol_max:
        tps_vol_max = tps_vol
    if tps_vol_alt > tps_vol_alt_max:
        tps_vol_alt_max = tps_vol_alt


print(f"La valeur maximum de l'altitude maximale des suites de Syracuse pour n = 1 jusqu'à n = 9999 est {altitude_max}"
      f"\nLa valeur maximum du temps de vol des suites de Syracuse pour n = 1 jusqu'à n = 9999 est {tps_vol_max}"
      f"\nLa valeur maximun du temps de vol en altitude des suites de Syracuse pour n = 1 jusqu'à n = 9999 est {tps_vol_alt_max}")