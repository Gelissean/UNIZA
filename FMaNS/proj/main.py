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
    siet = Siet([[Bunka(Sigmoid01Function, pocet_vstupov=2), Bunka(Sigmoid01Function, pocet_vstupov=2), Bunka(Sigmoid01Function, pocet_vstupov=2)],[Bunka(Sigmoid01Function, pocet_vstupov=3), Bunka(Sigmoid01Function, pocet_vstupov=3)],[Bunka(Sigmoid01Function, pocet_vstupov=2)]], epsilon=0.01, gamma=0.1, repeats=100)
    vstupy = [[i, j] for j in range(2) for i in range(2)]
    vystupy = [[(i & j) % 2] for j in range(2) for i in range(2)]

    vypis_vystup(siet)
    print("--- start fitting ---")
    siet.trenuj(vstupy, vystupy)
    print("--- done fitting ---")
    vypis_vystup(siet)


def main():
    print("haro warudo")
    # Sigmoid01Function.t = 2
    # print("ideal:")
    # main_set()
    # print("random: ")
    # main_random()
    # main_neparne_vacsie()
    # main_neparne_vacsie_static()
    # main_cisla()
    main_and()


if __name__ == "__main__":
    main()
