import os

import psycopg
from dotenv import load_dotenv
from pgvector.psycopg import register_vector

load_dotenv()

MODELO = "paraphrase-multilingual-MiniLM-L12-v2"
DIMENSIONES = 384

def conectar():
    conexion = psycopg.connect(os.environ["DATABASE_URL"], autocommit=True )
    register_vector(conexion)

    return conexion

_modelo = None

def embedding(textos):
    global _modelo
    if _modelo is None:
        from sentence_transformers import SentenceTransformer
        _modelo = SentenceTransformer(MODELO)
    return _modelo.encode(textos, normalize_embeddings=True)

