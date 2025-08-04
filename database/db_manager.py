import sqlite3 # SQLite veritabani isimleri icin gerekli modul
import os

# veritabani dosyasinin yolunu olustur.  data/assistant.db
DB_PATH = os.path.join("data","assistant.db")

# veritabanini baslatan fonksiyon
def initialize_db():
  # eger data klasoru yoksa olustursun
  os.makedirs("data", exist_ok=True)

  # veritabanina baglan ve dosya yoksa olustur. 
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()

  # eger not tablosu yoksa olustur. 
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes(
      id INTEGER PRIMARY KEY AUTOINCREMENT,           -- otomatik ortam birincil anahtar
      content TEXT NOT NULL,                          -- not icerigi
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- varsayilan olarak suanki zaman
    )"""
  )

  cursor.execute("""
    CREATE TABLE IF NOT EXISTS calendar (
      id INTEGER PRIMARY KEY AUTOINCREMENT, 
      event TEXT  NOT NULL,                           -- etkinlik aciklamasi bos olamaz
      event_date TEXT NOT NULL                        -- etkinlik tarihi
    )
  """)

  # degisiklikleri kaydeder
  conn.commit()

  # baglantiyi kapat
  conn.close()

# veritabanina yeni not ekleme islemi 
def add_note(content):
  # veritabanina baglan
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()

  # content'i notes tablosuna ekle. 
  cursor.execute("INSERT INTO notes (content) VALUES (?)", (content, ))

  # degisiklikleri kaydet 
  conn.commit()

  # baglantiyi kapat
  conn.close()

# veritabanina yeni bir etkinlik ekleyen fonksiyon
def add_event(event, event_date):
  # veritabanina baglan
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()

  # etkinlik ve tarih bilgilerini "calendar" tablosuna ekle
  cursor.execute("INSERT INTO calendar (event, event_date) VALUES (?, ?)", {event, event_date})

  # degisiklikleri kaydet 
  conn.commit()

  # baglantiyi kapat
  conn.close()

# Tum notlari veritabanindan sirali bir sekilde getiren fonksiyon
def get_notes():
  # veritabanina baglan
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()

  # "notes" tablosundan icerik ve tarih bilgilerini zaman sirasina gore getir. 
  cursor.execute("SELECT content, created_at FROM notes ORDER BY created_at DESC")

  # sonuclari liste olarak alalim. 
  notes = cursor.fetchall()

  # baglantiyi kapat
  conn.close()

  return notes

# tum etkinlikleri veritabanindan sirali sekilde getiren fonksiyon
def get_events():
  # veritabanina baglan
  conn = sqlite3.connect(DB_PATH)
  cursor = conn.cursor()

  # 'calendar' tablosundan etkinlikleri tarihe gore siralayip getirelim. 
  cursor.execute("SELECT event, event_date FROM calendar ORDER BY event_date")

  # sonuclari alalim. 
  events = cursor.fetchall()

  # baglantiyi kapatalim
  conn.close()

  return events