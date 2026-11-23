from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter 

documentos = [

]

for ruta in Path("docs").glob("*.txt"):
    documentos.append((ruta.name, ruta.read_text(encoding="utf-8")))
print (len(documentos))

for nombre, variable in documentos:
    print(nombre)

splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=60)