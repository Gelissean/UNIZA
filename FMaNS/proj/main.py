from FMaNS.proj.Dataset import Dataset
from FMaNS.proj.Siet import Siet
from FMaNS.proj.Bunka import Bunka
from FMaNS.proj.funkcie import Sigmoid01Function, SgnFunction, to_multi, get_index


def vytvor_siet():
    # stupen1 = [Bunka(sgn_function, vahy=[1, 1], theta=-1.5), Bunka(sgn_function, vahy=[1, 1], theta=-0.5)]
    # stupen2 = [Bunka(sgn_function, vahy=[-2, 1], theta=-0.5)]

    stupen1 = [Bunka(Sigmoid01Function, vahy=[1, 1], theta=-1.5), Bunka(Sigmoid01Function, vahy=[1, 1], theta=-0.5)]
    stupen2 = [Bunka(Sigmoid01Function, vahy=[-2, 1], theta=-0.5)]
    return Siet([stupen1, stupen2])


def vytvor_siet_random():
    stupen1 = [Bunka(Sigmoid01Function, pocet_vstupov=2), Bunka(Sigmoid01Function, pocet_vstupov=2)]
    stupen2 = [Bunka(Sigmoid01Function, pocet_vstupov=2)]
    return Siet([stupen1, stupen2], epsilon=0.01, gamma=0.1, repeats=100)


def main_set():
    siet = vytvor_siet()
    vypis_vystup(siet)


def main_random():
    Sigmoid01Function.t = 1
    siet = vytvor_siet_random()
    vstupy = [[i, j] for j in range(2) for i in range(2)]
    vystupy = [[(i + j) % 2] for j in range(2) for i in range(2)]

    vypis_vystup(siet)
    print("--- start fitting ---")
    siet.trenuj(vstupy, vystupy)
    print("--- done fitting ---")
    vypis_vystup(siet)


def vypis_vystup(siet):
    for i in range(2):
        for j in range(2):
            vysledok = siet.krok([i, j])
            print("Pre vstup: " + str(i) + ', ' + str(j) + " je vystup " + str(vysledok[0]))


def main_cisla():
    Sigmoid01Function.t = 1
    pocty = [28 * 28, 10]
    stupen1 = [Bunka(Sigmoid01Function, pocet_vstupov=28 * 28) for i in range(pocty[0])]
    stupen2 = [Bunka(Sigmoid01Function, pocet_vstupov=pocty[0]) for i in range(pocty[1])]
    siet = Siet([stupen1, stupen2], epsilon=0.01, gamma=0.1, repeats=10, output_function=get_index,
                training_convert=to_multi)

    dataset = Dataset("C:\\Praca\\Skola\\UNIZA\\python\\generic\\FMaNS\\proj\\data\\train-images.idx3-ubyte",
                      "C:\\Praca\\Skola\\UNIZA\\python\\generic\\FMaNS\\proj\\data\\train-labels.idx1-ubyte")
    vstupy = dataset.ins
    vystupy = dataset.outs

    vystupy_temp = [to_multi(vystupy[i], 10) for i in range(len(vystupy))]

    siet.trenuj(vstupy, vystupy)
    print("Natrenovane")
    vystup = siet.krok(vstupy[1])
    print(vystupy[1])
    print(vystup)


def to_bits(input):
    return [input >> i & 0b1 for i in range(5)]


def to_num(inputs):
    a = 0
    for i in range(len(inputs)):
        a += inputs[i] << i
    return a


def main_neparne_vacsie():
    Sigmoid01Function.t = 1
    siet = Siet([[Bunka(Sigmoid01Function, pocet_vstupov=5)]], epsilon=0.01, gamma=0.1, repeats=100)
    funkcia = lambda a: int(a % 2 == 1 and a > 8)

    vstupy = [to_bits(i) for i in range(32)]
    vystupy = [[funkcia(i)] for i in range(32)]

    [print(str(i) + " : " + zarovnaj(siet.krok(to_bits(i))[0]) + " : " + str(siet.krok(to_bits(i))[0])) for i in range(32)]
    siet.trenuj(vstupy, vystupy)
    [print(str(i) + " : " + zarovnaj(siet.krok(to_bits(i))[0]) + " : " + str(siet.krok(to_bits(i))[0])) for i in range(32)]

def zarovnaj(cislo):
    if cislo < 0.1:
        return "0"
    elif cislo > 0.9:
        return "1"
    return "undefined"

def main_neparne_vacsie_static():
    Sigmoid01Function.t = 0.1
    siet = Siet([[Bunka(Sigmoid01Function, vahy=[2, 0, 0, 1, 1], theta=-2.5)]], epsilon=0.01, gamma=0.1, repeats=100)
    funkcia = lambda a: int(a % 2 == 1 and a > 8)

    vstupy = [to_bits(i) for i in range(32)]
    vystupy = [[funkcia(i)] for i in range(32)]

    [print(str(i) + " : " + zarovnaj(siet.krok(to_bits(i))[0]) + " : " + str(siet.krok(to_bits(i))[0])) for i in range(32)]


def main_and():
    Sigmoid01Function.t = 0.1
    siet = Siet([[Bunka(Sigmoid01Function, pocet_vstupov=2)]], epsilon=0.01, gamma=0.1, repeats=100)
    vstupy = [[i, j] for j in range(2) for i in range(2)]
    vystupy = [[(i & j) % 2] for j in range(2) for i in range(2)]

    vypis_vystup(siet)
    print("--- start fitting ---")
    siet.trenuj(vstupy, vystupy)
    print("--- done fitting ---")
    vypis_vystup(siet)


def delta():
    bunka = Bunka(Sigmoid01Function, pocet_vstupov=2)
    vstupy = [[i, j] for j in range(2) for i in range(2)]
    vystupy_and = [vstup[0] & vstup[1] for vstup in vstupy]
    vystupy_or = [vstup[0] | vstup[1] for vstup in vstupy]
    gamma, epsilon, r = 0.1, 0.00001, 100
    for vstup in vstupy:
        print(str(vstup[0]) + " " + str(vstup[1]) + " : " + str(bunka.spracuj(vstup)))
    print("and")
    _delta_inner(bunka, epsilon, gamma, r, vstupy, vystupy_and)
    for vstup in vstupy:
        print(str(vstup[0]) + " " + str(vstup[1]) + " : " + str(bunka.spracuj(vstup)))
    print("or")
    _delta_inner(bunka, epsilon, gamma, r, vstupy, vystupy_or)
    for vstup in vstupy:
        print(str(vstup[0]) + " " + str(vstup[1]) + " : " + str(bunka.spracuj(vstup)))

def _delta_inner(bunka, epsilon, gamma, r, vstupy, vystupy):
    pocet = 0
    while pocet < r:
        import random
        index = random.randint(0, len(vstupy) - 1)
        vstup = vstupy[index]
        vystup_ocakavany = vystupy[index]
        vystup = bunka.spracuj(vstup)
        do_update = False
        if pow(vystup_ocakavany - vystup, 2) > epsilon:
            do_update = True
        if do_update:
            delta_w = [gamma * (vystup_ocakavany - vystup) * x for x in vstupy[index]]
            delta_theta = gamma * (vystup_ocakavany - vystup)
            bunka.update(delta_w, delta_theta)
            pocet = 0
        else:
            pocet += 1


def main_2_sames():
    Sigmoid01Function.t = 0.1
    siet = Siet([[Bunka(Sigmoid01Function, pocet_vstupov=3) for i in range(2)], [Bunka(Sigmoid01Function, pocet_vstupov=2)]], epsilon=0.01, gamma=0.1, repeats=500)
    vstupy = [[i, j, k] for k in range(2) for j in range(2) for i in range(2) ]
    vystupy = [[int((vstup[0] + vstup[1] + vstup[2]) % 3 > 0)] for vstup in vstupy]


    for vstup in vstupy:
        print(str(vstup[0]) + " " + str(vstup[1]) + " " + str(vstup[2]) + " : " + str(siet.krok(vstup)))
    print("--- start fitting ---")
    siet.trenuj(vstupy, vystupy)
    print("--- done fitting ---")
    for vstup in vstupy:
        print(str(vstup[0]) + " " + str(vstup[1]) + " " + str(vstup[2]) + " : " + str(siet.krok(vstup)))


def main():
    print("haro warudo")
    # Sigmoid01Function.t = 2
    # print("ideal:")
    # main_set()
    # print("random: ")
    main_random()
    # main_neparne_vacsie()
    # main_neparne_vacsie_static()
    # main_cisla()
    # main_and()
    # delta()
    # main_2_sames()


if __name__ == "__main__":
    main()
