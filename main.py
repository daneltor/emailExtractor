import re
import csv

# MODFICAR NOMBRE DEL ARCHIVO A LEER
in_file = open("prueba.txt", "r", encoding="utf-8")
emails = []

for linea in in_file:
    email = re.findall(r"[a-zA-Z0-9\.\-+_]+@[a-zA-Z0-9\.\-+_]+\.[a-zA-Z]+", linea)
    i = 0
    for i in range(len(email)):
        if email[i] not in emails:
            emails.append(email[i])
            print("Se agrego: ", email[i])

in_file.close()

# MODIFICAR NOMBRE DEL ARCHIVO A GUARDAR LOS CORREOS
with open('extraidos.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for email in emails:
        writer.writerow([email])

exit(0)
