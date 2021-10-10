import sys
import random
import math


class Siet(object):
    def __init__(self):
        self.velkost = 0
        self.vzdialenosti = [0]
        self.cesta = [0]

    def citajSiet(self, param):
        subor = open(param, 'r')
        self.velkost = int(subor.readline())
        self.vzdialenosti = [0] * self.velkost
        for i in range(self.velkost):
            riadok = subor.readline()
            self.vzdialenosti[i] = riadok.split(' ')
            for j in range(self.velkost):
                self.vzdialenosti[i][j] = int(self.vzdialenosti[i][j])

    def vypisCestu(self):
        return str(self.cesta) + "\n" + str(self.vypocitajDlzku(self.cesta))

    def vypocitajDlzku(self, cesta):
        dlzka = 0
        for i in range(len(cesta) - 1):
            dlzka = dlzka + self.vzdialenosti[cesta[i]][cesta[i + 1]]
        return dlzka

    def najdiCestu(self, teplota, pocet_prechodov_sucasny, pocet_prechodov_od_zmeny_t):
        self.__vytvorCestu(0)
        self.__simulatedAnnealing(teplota, pocet_prechodov_sucasny, pocet_prechodov_od_zmeny_t)

    def __vytvorCestu(self, mod):
        nespracovane = [0] * self.velkost
        self.cesta = [0] * 4
        for i in range(self.velkost):
            nespracovane[i] = i
        self.cesta[0] = 0
        del (nespracovane[0])
        self.cesta[1] = self.__vyberMax(0, nespracovane)
        self.cesta[2] = self.__vyberMax(self.cesta[1], nespracovane)
        nespracovaneDlzka = len(nespracovane)
        for i in range(nespracovaneDlzka):
            if mod == 0:
                self.__vlozNajblizsi(nespracovane)
            else:
                self.__vlozNavyhodnejsi(nespracovane)

    def __vyberMax(self, riadok, zoznam):
        maxIndex = 0
        maxHodnota = -1
        for i in range(len(zoznam)):
            if self.vzdialenosti[riadok][zoznam[i]] > maxHodnota:
                maxIndex = zoznam[i]
                maxHodnota = self.vzdialenosti[riadok][zoznam[i]]
        zoznam.remove(maxIndex)
        return maxIndex

    def __vlozNajblizsi(self, nespracovane):
        najblizsiIndex = -1
        najblizsiHodnota = sys.maxsize
        for i in range(len(nespracovane)):
            hodnota = 0
            for j in range(len(self.cesta)-1):
                hodnota = hodnota + self.vzdialenosti[self.cesta[j]][nespracovane[i]]
            if hodnota < najblizsiHodnota:
                najblizsiIndex = nespracovane[i]
                najblizsiHodnota = hodnota
        minCesta = sys.maxsize
        najlepsieMiesto = -1
        for i in range(len(self.cesta)-1):
            hodnota = self.__cestaUzol(self.cesta[i], najblizsiIndex, self.cesta[i+1])
            if hodnota < minCesta:
                minCesta = hodnota
                najlepsieMiesto = i + 1
        self.cesta.insert(najlepsieMiesto, najblizsiIndex)
        nespracovane.remove(najblizsiIndex)

    def __vlozNavyhodnejsi(self, nespracovane):
        najblizsiIndex = -1
        najblizsiHodnota = sys.maxsize
        najvhodnejsieMiesto = -1
        for i in range(len(self.cesta) - 1):
            for j in range(len(nespracovane)):
                hodnota = self.__cestaUzol(self.cesta[i], nespracovane[j], self.cesta[i + 1])
                if hodnota < najblizsiHodnota:
                    najblizsiIndex = nespracovane[j]
                    najvhodnejsieMiesto = i
                    najblizsiHodnota = hodnota
        self.cesta.insert(najvhodnejsieMiesto + 1, najblizsiIndex)
        nespracovane.remove(najblizsiIndex)

    def __cestaUzol(self, a, b, c):
        return self.vzdialenosti[a][b] + self.vzdialenosti[b][c] - self.vzdialenosti[a][c]

    def __simulatedAnnealing(self, maxT, u, q):
        # 0
        t = maxT
        optimalna_cesta = self.cesta
        optimalna_hodnota = self.vypocitajDlzku(self.cesta)

        aktualna_cesta = optimalna_cesta
        aktualna_hodnota = optimalna_hodnota
        # 1
        r = 0
        w = 0
        # 5
        while r != u:
            # 2
            r = r + 1
            w = w + 1
            if w == q:
                t = t / 2
                w = 0
            okolie = self.__vytvorOkoliaVymena(aktualna_cesta)
            skumana_cesta = okolie[random.randrange(len(okolie))]
            # 3
            skumana_hodnota = self.vypocitajDlzku(skumana_cesta)
            if skumana_hodnota <= aktualna_hodnota:
                r = 0
                aktualna_cesta = skumana_cesta
                aktualna_hodnota = skumana_hodnota
                if aktualna_hodnota <= optimalna_hodnota:
                    optimalna_cesta = aktualna_cesta
                    optimalna_hodnota = aktualna_hodnota
            else:
                # 4
                p = self.__simulatedAnnealingPravdepodobnostPrechodu(skumana_hodnota, aktualna_hodnota, t)
                if random.uniform(0.0, 1.0) <= p:
                    aktualna_hodnota = skumana_hodnota
                    aktualna_cesta = skumana_cesta
                    r = 0
        self.cesta = optimalna_cesta

    def __simulatedAnnealingPravdepodobnostPrechodu(self, f_curr, f_i, t):
        return math.exp(-((f_curr - f_i)) / t)

    def __vytvorOkoliaInverzia(self, aktualna_cesta):
        pocet = len(aktualna_cesta) - 2 - 4  # dlzka - okraje (tie sa netocia) - (5-1, aktualny a 4 do strany)
        vysledok = [0] * pocet
        for i in range(pocet):
            vysledok[i] = aktualna_cesta.copy()
            for j in range(math.floor(5 / 2)):
                temp = vysledok[i][1 + i + j]
                vysledok[i][1 + i + j] = vysledok[i][1 + i + 4 - j]
                vysledok[i][1 + i + 4 - j] = temp
        return vysledok

    def __vytvorOkoliaVymena(self, aktualna_cesta):
        konecny_index = len(aktualna_cesta) - 2 - 4 # dlzka - okraje (tie sa netocia) - (5-1, aktualny a 4 do strany)
        pocet = 0
        for i in range(5, konecny_index):
            pocet = pocet + konecny_index - (i)
        okolia = [0]*pocet
        for i in range(pocet):
            okolia[i] = aktualna_cesta.copy()
        if pocet > 0 :
            a = 0
            for i in range(konecny_index):
                for j in range(i + 5, konecny_index):
                    for k in range(5):
                        okolia[a][1+i+k] = aktualna_cesta[1+j+k]
                        okolia[a][1+j + k] = aktualna_cesta[1+i + k]
                    a = a + 1
        return okolia

    def najdiCestuNajblizsi1(self):
        nespracovane = [0] * self.velkost
        self.cesta = [0] * (self.velkost+1)
        for i in range(self.velkost):
            nespracovane[i] = i
        self.cesta[0] = 0
        del (nespracovane[0])
        nespracovaneDlzka = len(nespracovane)
        for i in range(1, self.velkost):
            najblizsiaHodnota = sys.maxsize
            najblizsiIndex = -1
            for j in range(len(nespracovane)):
                if self.vzdialenosti[i][nespracovane[j]] < najblizsiaHodnota:
                    najblizsiaHodnota = self.vzdialenosti[i][nespracovane[j]]
                    najblizsiIndex = j
            self.cesta[i] = najblizsiIndex


if __name__ == '__main__':
    siet = Siet()
    siet.citajSiet("Matica_TN_(0276).txt")
    #siet.citajSiet("test.txt")
    siet.najdiCestu(5000, 30, 25)
    #siet.najdiCestuNajblizsi1()
    print(siet.vypisCestu())
