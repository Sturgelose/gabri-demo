# Programa que et busca productes a la base de dades.
def buscadorLaboratoriReactius(reactiu):
    import csv

    llista_noms = []
    llista_CAS = []
    llista_safata = []
    o = 0
    trobat = False

    with open('llistat_reactius_lab.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            llista_noms.append(line[0])
            llista_CAS.append(line[1])
            llista_safata.append(line[2])

        reactiu2 = reactiu.replace(",", ".")

    for i in llista_noms:
        if i == reactiu2:
            CAS = llista_CAS[o]
            safata = llista_safata[o]
            trobat = True
            break
        o += 1
    if not CAS:  # indica que no hi ha res.
        CAS = "Aques reactiu no té entrat el CAS."

    if trobat:
        print("Reactiu: " + reactiu, end=" // ")
        print("CAS: " + CAS, end=" // ")
        print("Safata: " + safata)
    else:
        print("El reactiu que busques no es troba a la llista.")


def buscadorLaboratoriCAS(CAS):
    import csv
    llista_noms = []
    llista_safata = []
    llista_cas = []
    o = 0
    trobat = False

    with open('llistat_reactius_lab.csv', 'r') as CSV_file:
        csv_reader = csv.reader(CSV_file)

        for line in csv_reader:
            llista_noms.append(line[0])
            llista_cas.append(line[1])
            llista_safata.append(line[2])

        for i in llista_cas:
            if i == CAS:
                reactiu = llista_noms[o]
                safata = llista_safata[o]
                trobat = True
                break
            o = o + 1

        if trobat:

            print("Reactiu: " + reactiu, end=" // ")
            print("CAS: " + CAS, end=" // ")
            print("Safata: " + safata)

        else:

            print("El CAS buscat no s'ha trobat. Prova d'introduir el nom del reactiu: ")
            print(buscadorLaboratoriReactius(input("Introdueixie el nom del reactiu: ")))


buscar = input("Vols buscar algun reacitu? si/no ")

while buscar == "si":
    print(buscadorLaboratoriCAS(input("Introdueixi el CAS: ")))
    buscar = input("Necessites buscar alguna cosa més? si/no ")

print("Torna quan vulguis!")
