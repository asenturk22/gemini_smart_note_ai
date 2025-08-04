# 🤖 Gemini Smart Note AI
> Gemini AI ile güçlendirilmiş akıllı not, görev ve etkinlik asistanı

Doğal dil işleme ile notlarınızı yönetin, görevlerinizi organize edin ve etkinliklerinizi planlayın.

## 📋 Proje Hakkında

Bu proje, Google Gemini AI kullanarak kullanıcıların doğal dilde verdiği komutları anlayan ve notlar ile etkinlikleri yöneten akıllı bir asistan geliştirmeyi hedeflemektedir.

## 🎯 Temel Özellikler

✅ SQLite veritabanı ile not ve etkinlik yönetimi
🔄 Gemini AI entegrasyonu 
💬 Doğal dil işleme 
📅 Akıllı takvim yönetimi 

## 🚀 Mevcut Fonksiyonlar

### Database Manager (database/db_manager.py)


| Fonksiyon           | Açıklama                                   |
|---------------------|---------------------------------------------|
| `initialize_db()`   | Veritabanı ve tabloları oluşturur           |
| `add_note(content)` | Yeni not ekler                              |
| `add_event(event, event_date)` | Yeni etkinlik ekler               |
| `get_notes()`       | Tüm notları tarihe göre sıralar            |
| `get_events()`      | Tüm etkinlikleri tarihe göre sıralar       |


📦 Gereksinimler

```bash
Python 3.7+
SQLite3 (Python built-in)
```

🔧 Kurulum

#### Repository'yi klonlayın:

```bash
git clone https://github.com/asenturk22/gemini_smart_note_ai.git
cd gemini_smart_note_ai
```

#### Veritabanını başlatın:

```python
from database.db_manager import initialize_db
initialize_db()
```

## 🛠️ Geliştirme Durumu

 - SQLite veritabanı altyapısı
 - Temel CRUD işlemleri
 - Gemini AI entegrasyonu
 - Doğal dil işleme
 - CLI arayüzü
 - Akıllı tarih/saat çıkarma
 - Export/Import özellikleri

📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.