from pathlib import Path

documentos = [

]

for ruta in Path("docs").glob("*.txt"):
    documentos.append((ruta.name, ruta.read_text(encoding="utf-8")))
print (len(documentos))

for nombre, variable in documentos:
    print(nombre)

