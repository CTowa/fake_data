from faker import Faker
import psycopg2
import pymysql
from pymongo import MongoClient
import random

fake = Faker()

# --- PostgreSQL (usuarios) ---
def insertar_usuarios_postgres(cantidad):
    conn = psycopg2.connect(
        dbname="bd_usuarios",
        user="postgres",
        password="utec",
        host="172.31.95.108",
        port="8005"
    )
    cur = conn.cursor()
    for _ in range(cantidad):
        username = fake.user_name()
        email = fake.email()
        password = fake.password(length=10)
        dni = fake.random_number(digits=8, fix_len=True)
        cur.execute(
            "INSERT INTO usuarios (username, email, password, dni) VALUES (%s, %s, %s, %s)",
            (username, email, password, str(dni))
        )
    conn.commit()
    cur.close()
    conn.close()
    print(f"{cantidad} usuarios insertados en PostgreSQL")

# --- MySQL (peliculas) ---
def insertar_peliculas_mysql(cantidad):
    conn = pymysql.connect(
        host="172.31.95.108",
        user="root",
        password="utec",
        db="bd_cartelera",
        port="8082"
    )
    cur = conn.cursor()
    for _ in range(cantidad):
        titulo = fake.catch_phrase()
        genero = random.choice(["Acción", "Drama", "Comedia", "Terror", "Ciencia Ficción"])
        duracion = random.randint(80, 180)
        fecha_estreno = fake.date_time_this_decade().strftime('%Y-%m-%d %H:%M:%S')
        cur.execute(
            "INSERT INTO peliculas (titulo, genero, duracion, fecha_estreno) VALUES (%s, %s, %s, %s)",
            (titulo, genero, duracion, fecha_estreno)
        )
    conn.commit()
    cur.close()
    conn.close()
    print(f"{cantidad} películas insertadas en MySQL")

# --- MongoDB (reservas) ---
def insertar_reservas_mongo(cantidad):
    client = MongoClient("mongodb://172.31.95.108:27017/")
    db = client["reserva"]
    tickets = db["tickets"]  # nombre de la colección
    docs = []
    for _ in range(cantidad):
        docs.append({
            "usuario": fake.user_name(),
            "fecha": fake.date_this_year().isoformat(),
            "pelicula_nombre": fake.catch_phrase(),
            "peliculaId": fake.random_int(min=1, max=10000),
            "usuarioId": fake.random_int(min=1, max=10000)
        })
    tickets.insert_many(docs)
    print(f"{cantidad} reservas insertadas en MongoDB")

# --- Ejecutar todos ---
insertar_usuarios_postgres(20000)
insertar_peliculas_mysql(20000)
insertar_reservas_mongo(2000)