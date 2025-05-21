# convert_to_txt.py

import csv

def convert_csv_to_txt(csv_filename, txt_filename):
    with open(csv_filename, mode='r', encoding='utf-8') as csv_file, \
         open(txt_filename, mode='w', encoding='utf-8') as txt_file:

        reader = csv.DictReader(csv_file)
        for row in reader:
            pregunta = row.get("Preguntas y comentarios", "").strip()
            respuesta = row.get("Respuesta", "").strip()

            txt_file.write(f"Pregunta y Comentarios: {pregunta}\n")
            txt_file.write(f"Respuesta: {respuesta}\n")
            txt_file.write("---SEPARATOR---\n\n")

if __name__ == "__main__":
    convert_csv_to_txt("reviews.csv", "output.txt")
