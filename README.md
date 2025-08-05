# 🤖 Gemini Smart Note AI
> Gemini AI ile güçlendirilmiş akıllı not, görev ve etkinlik asistanı

Doğal dil işleme ile notlarınızı yönetin, görevlerinizi organize edin ve etkinliklerinizi planlayın.

## 📋 Proje Hakkında

Bu proje, Google Gemini 2.0 Flash AI modelini kullanarak kullanıcıların doğal dilde verdiği komutları anlayan ve notlar ile etkinlikleri yöneten akıllı bir asistan geliştirmeyi hedeflemektedir. Kullanıcılar sohbet botu gibi etkileşim kurabilir, kural tabanlı sistemle notlar ve etkinlikler oluşturabilir.

## 🎯 Temel Özellikler

✅ SQLite veritabanı ile not ve etkinlik yönetimi
🔄 Gemini AI entegrasyonu 
💬 Doğal dil işleme 
📝 Not Yönetimi: Notları ekleme, görüntüleme ve özetleme
📅 Etkinlik Yönetimi: Tarihli etkinlikler oluşturma ve yönetme
🔍 Akıllı Özetleme: AI destekli not ve etkinlik özetleri
⚡ CLI Arayüzü: Kolay kullanımlı komut satırı arayüzü

## 🚀 Mevcut Fonksiyonlar

### Main Application (main.py)

Ana uygulama döngüsü ve kullanıcı komutlarını yönetir:

| Komut | Açıklama |
|-------|----------|
| `not ekle` | Yeni not oluşturur |
| `etkinlik ekle` | Tarihli etkinlik ekler |
| `notları göster` | Kaydedilmiş notları listeler |
| `etkinlikleri göster` | Kaydedilmiş etkinlikleri listeler |
| `sohbet et` | AI ile serbest sohbet ve akıllı özetleme |
| `çıkış` | Uygulamadan çıkar |

### AI Assistant (assistant.py)

Gemini AI entegrasyonu ve niyet analizi:

| Fonksiyon | Açıklama |
|-----------|----------|
| `get_gemini_response(prompt)` | Gemini API'sine istek gönderir |
| `detect_intent(message)` | Kullanıcı mesajını sınıflandırır |

**Niyet Kategorileri:**

- **not_ozet:** Notları özetleme isteği
- **etkinlik_ozet:** Etkinlikleri özetleme isteği
- **normal:** Genel sohbet

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
requests
python-dotenv
SQLite3 (Python built-in)
```

🔧 Kurulum

#### Repository'yi klonlayın:

```bash
git clone https://github.com/asenturk22/gemini_smart_note_ai.git
cd gemini_smart_note_ai
```

#### Gerekli kütüphaneleri yükleyin:

```bash
pip install requests python-dotenv
```

#### API anahtarını ayarlayın:

`.env` dosyası oluşturun ve Gemini API anahtarınızı ekleyin:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

**API Anahtarı Alma:**

- Google AI Studio adresine gidin
- Hesap oluşturun/giriş yapın
- API anahtarı oluşturun
- Anahtarı .env dosyasına ekleyin

#### Veritabanını başlatın:

```python
from database.db_manager import initialize_db
initialize_db()
```

####  Uygulamayı başlatın:

```bash
python main.py
```



📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!