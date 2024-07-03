import csv

archivo = "web/vacantes.csv"
datos = []

with open(archivo, "r") as file:
    csv_reader = csv.reader(file)
    cuenta = 0
    for row in csv_reader:
        datos.append(row)

        cuenta += 1
        if cuenta >= 10:
            break
for fila in datos:
    print(fila)
