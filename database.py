import sqlite3

conn = sqlite3.connect('enkripsi.db')
c = conn.cursor()

# Table Akun
c.execute("""CREATE TABLE IF NOT EXISTS akun(
                    Email VARCHAR(255) PRIMARY KEY,
                    Nama_lengkap VARCHAR(255),
                    Password VARCHAR(255) NOT NULL);
          """)
conn.commit()

# Table Key
c.execute("""CREATE TABLE IF NOT EXISTS key(
                    Email VARCHAR(255) PRIMARY KEY,
                    Key VARCHAR(255));
          """)
conn.commit()