"""
Problem tanimi : Gemini ile Akilli Asistan Projesi : notlar, gorevler ve etkinlikler icin akilli asistan 
    - Amac : google gemini api tabanli yapay zeka kullanan bir akilli asistan gelistirme
    - Kullanicinin dogal dilde verdigi komutlari anlar, (sohbet botu) 
    - Kural tabanli olarak notlar ve etkinlikler olusturulacak
    - Akilli asistan, notlara ve etkinkliklere erişim saglayarak bize ozetleme, bilgi cikarma, takvim olusturma gibi ozellikler sunar. 
    
Model tanitimi : Google DeepMind Gemini 
    - Bu projede gemini-2.0-flash modelini kullanicaz. 
    
API tanimlama : https://ai.google.dev/gemini-api/docs?hl=tr

Plan/Program : 
    - assistant: gemini chatbot olusturulur. 
    - database: sqlite database olusturalim, notlar, ve etkinlikleri depolamak lazim. 
    - main: bilesenleri bir araya getirir. 

install libraries : 
    - pip install requests python-dotenv
import libraries : 
"""

# assistant.py dosyasindan gemini api yanitini alan ve kullanicinin niyetini belirleyen fonksiyonlari icerir. 
from assistant import get_gemini_response, detect_intent

# database.py dosyasindan veritabani islemleri gerceklestiren yardimci fonksiyonlarimiz 
from database.db_manager import initialize_db, add_event, add_note, get_notes, get_events

# veritabanini baslat
initialize_db()

# karsilama mesaji
print("Akilli Asistana Hoşgeldiniz")
print("Komutlar: not ekle | etkinlik ekle | notları göster | etkinlikleri göster | sohbet et | çıkış")

# Kullanicidan surekli komut almak icin
while True:
    cmd = input("Komut giriniz : ").strip().lower() # komutu al, bosluklari kirp, kucuk harf yap
    if cmd == "not ekle":
        content = input("Not içeriği nedir? ") # kullanicidan not icerigi al
        add_note(content)
        print("Not basariyla kaydedildi.")

    elif cmd == "etkinlik ekle":
        event = input("Etkinlik açıklaması? ")
        date = input("Etkinlik tarihi? ")
        add_event(event, date)
        print("Etkinlik başarıyla eklendi.")

    elif cmd == "notları göster": 
        notes = get_notes() # veritabanından tüm notları al
        if notes: 
            print("Kaydedilmiş notlar: ")
            for content, created_at in notes: 
                print(f"- [{created_at}] {notes}")
        else :
            print("Henüz hiç bir not eklenmedi.")
    elif cmd == "etkinlikleri göster":
        events = get_events()
        if events:
            print("Etkinlikler:")
            for event, event_date in events:
                print(f"{event_date}: {event}")
        else:
            print("Henüz etkinlik girilmemiş. ")
    elif cmd == "sohbet et":
        message = input("Kullanıcı: ").strip() # kullanicidan serbest metin al. 
        intend = detect_intent(message) # kullanicinin niyetini (not ozeti mi, etkinlik ozeti mi, normal sohbet mi) anlama 
        
        if intend == "not_ozet":
            notes = get_notes() # notlari veritabanindan al
            if not notes:
                print("Henuz ozetlenecek not bulunmuyor.")
                continue
            all_notes_text = "\n".join([f"- {note[0]}" for note in notes]) # tum notlari birlestir.
            prompt = f"Aşağıda bulunan notları özetler misin? \n\n {all_notes_text}" # gemini dan ozet iste
            summary = get_gemini_response(prompt)

            print("Not Özeti: \n")
            print(summary)
        elif intend == "etkinlik_ozet": 
            events = get_events()
            if not events: 
                print("Henüz özetlenecek not bulunamadı.")
                continue
            
            all_events_text = "\n".join([f"- {e[1]}: {e[0]}" for e in events]) # tum etkinlikleri listele
            prompt = f"Aşağıdaki takvim etkinliklerini kullanıcı isteğine göre  özetler misin\n\n{all_events_text}\n\n kullanıcı isteği: {message}"
            summary = get_gemini_response(prompt) # geminiden özet ister. 
            print("Etkinlik özeti: \n")      
            print(summary)
        else:
            reply = get_gemini_response(message)
            print(f"Akıllı asistan: {reply}")
    elif cmd  in ["çıkış", "exit", "quit"] : 
        break
    else: 
        print("Hatalı komut girdiniz. ")