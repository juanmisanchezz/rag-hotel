from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from db import conectar, embedding, DIMENSIONES


documentos = [

]

for ruta in Path("docs").glob("*.txt"):
    documentos.append((ruta.name, ruta.read_text(encoding="utf-8")))
print (len(documentos))

for nombre, variable in documentos:
    print(nombre)

splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=60)

chunks = [

]

for nombre, texto in documentos:
    for trozo in splitter.split_text(texto):
        chunks.append((nombre, trozo))
print (len(chunks))

conn = conectar() 
conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
conn.execute("DROP TABLE IF EXISTS fragmentos")
conn.execute(f"CREATE TABLE fragmentos (id SERIAL PRIMARY KEY, documento TEXT, texto TEXT, embedding VECTOR({DIMENSIONES}))")
conn.execute("CREATE INDEX ON fragmentos USING hnsw (embedding vector_cosine_ops)")

for nombre, trozo in chunks:
    conn.execute("INSERT INTO fragmentos (documento, texto, embedding) VALUES (%s, %s, %s)",
    (nombre, trozo, embedding(trozo)))