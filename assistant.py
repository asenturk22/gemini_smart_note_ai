import os # ortam degiskenleri ve dosya yolu
import requests # http istekleri yapmak icin
from dotenv import load_dotenv # .env dosyasindan ortam degiskenlerini yuklemek icin 

# .env dosyasini yukle
load_dotenv()

# .env dosyasindaki GEMINI_API_KEY  degiskenine alalim. 
api_key = os.getenv("GEMINI_API_KEY")

# eger api anahtari yoksa kullaniciya hata gonder
if not api_key:
  raise ValueError("GEMINI_API_KEY .env dosyasında mevcut değil.")

# gemini 2.0 flash modeline ait api url'i (google ai tarafindan aldik)
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent" 

# api cagrisi icin gerekli http basliklari
headers = {
  "Content-Type": "application/json", # JSON formatinda veri gonderecegimizi belirtiyoruz. 
  "X-Goog-Api-Key": api_key  # yetkilendirme icin api anahtari 
}

def get_gemini_response(prompt: str) -> str :  # gemini api'sine prompt gonderip yanit alinacak
  # api'ye gonderilecek json yapisi
  payload = {
    "contents": [
      {
        "parts": [
          {"text":prompt} # kullanicidan gelen mesaji icren bolum
        ]
      }
    ]
  }

  # gemini api ye http post istegi gonderelim. 
  response = requests.post(url, headers=headers, json=payload)

  # istek basarili ise (http 200)
  if response.status_code == 200 : 
    try:
      result = response.json() # json formatindaki yaniti sozluge ceviririz. 
      return result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e: 
      # eger json yapisi beklenildigi gibi degilse hata dondurur. 
      return f"Yanıt hatası : {e}"

  else : 
    return f"api hatası {response.status_code} : {response.text}"


# kullanici mesajina gore niyet siniflandirmasi yapan bir fonksiyon
def detect_intent(message):
  # gemini icin ozel bir gorev prompt'u olustur. Mesajin hangi kategoriye ait oldugunu tespit etsin. 
  prompt = f"""
    Kullanıcının aşağıdaki cümlesini sınıflandır. 

    Etiketlerden sadece birini döndür. 
    - not_ozet (eğer notları özetlemesini istiyorsa)
    - etkinlik_ozet (eğer etkinlikleri görmek yada özet istiyorsa)
    - normal (diğer her şey) 

    Cümle: "{message}"
    Yalnızca etiket döndür: (örnek: not_ozet)
  """

  # prompt'u gonder ve cevap al
  response = get_gemini_response(prompt)
  return response.strip().lower()

if __name__ == "__main__":
  user_input = input("Kullanıcı : ")
  answer = get_gemini_response(user_input)
  print(f"Akıllı Asistan Yanıtı : {answer}")