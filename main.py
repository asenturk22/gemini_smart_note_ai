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

