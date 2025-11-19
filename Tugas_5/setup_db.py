import psycopg2
from psycopg2 import Error

# --- Detail Koneksi Server PostgreSQL ---
HOST = "localhost"
PORT = "5432"
USER = "postgres"
PASSWORD = "postgres"
DB_SERVER = "postgres"                                                                                                                                                                                                                           
DB_TARGET = "sales_db" 

SCHEMA_SQL = '''
-- Tabel customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    address TEXT,
    birthdate DATE
);

CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    price NUMERIC(10, 2),
    stock INT
);

CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE,
    total_amount NUMERIC(10, 2),
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS order_details (
    detail_id SERIAL PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT,
    price NUMERIC(10, 2),
    CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE RESTRICT
);
''' 

def create_database_and_schema():
    conn = None
    conn_target = None
    try:
        # 1. KONEKSI KE DATABASE SERVER (postgres) UNTUK MEMBUAT DATABASE
        conn = psycopg2.connect(host=HOST, port=PORT, user=USER, 
                                 password=PASSWORD, dbname=DB_SERVER)
        conn.autocommit = True
        c = conn.cursor()

        print(f"Mencoba membuat database '{DB_TARGET}'...")
        try:
            c.execute(f"CREATE DATABASE {DB_TARGET}")
            print(f"✅ Database '{DB_TARGET}' berhasil dibuat.")
        except psycopg2.errors.DuplicateDatabase:
            print(f"✅ Database '{DB_TARGET}' sudah ada, melanjutkan.")
        
        c.close()
        conn.close()

        # 2. KONEKSI KE sales_db DAN MEMBUAT TABEL
        print("\nMencoba membuat tabel di sales_db...")
        conn_target = psycopg2.connect(host=HOST, port=PORT, user=USER, 
                                     password=PASSWORD, dbname=DB_TARGET)
        conn_target.autocommit = True
        c_target = conn_target.cursor()
        
        # --- PERBAIKAN UTAMA: MENJALANKAN MULTIPLE STATEMENTS ---
        sql_queries = [q.strip() for q in SCHEMA_SQL.split(';') if q.strip()]

        for query in sql_queries:
            c_target.execute(query)
            
        print("✅ Semua tabel (customers, products, orders, order_details) berhasil dibuat.")
        
    except (Exception, Error) as error:
        print(f"❌ Terjadi Error: {error}")
        print("Pastikan server PostgreSQL aktif dan password/user sudah benar.")
        
    finally:
        if conn_target:
            conn_target.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    create_database_and_schema()