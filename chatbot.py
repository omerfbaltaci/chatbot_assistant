from veri_seti import veri_seti
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = set(stopwords.words('turkish'))

# Veriseti zaten yüklü, ilk satırda import ettim.

def temizle(metin):
    metin = metin.lower().translate(str.maketrans('', '', string.punctuation))
    kelimeler = metin.split()
    kelimeler = [kelime for kelime in kelimeler if kelime not in stop_words]
    return ' '.join(kelimeler)


def chatbot(kullanici_sorusu):
    temiz_soru = temizle(kullanici_sorusu)
    sorular = [temizle(item["question"]) for item in veri_seti]

    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform(sorular + [temiz_soru])

    benzerlikler = cosine_similarity(tfidf[-1], tfidf[:-1])
    en_yakin_index = benzerlikler.argmax()
    en_yuksek_benzerlik = benzerlikler[0][en_yakin_index]

    if en_yuksek_benzerlik > 0.4:
        return veri_seti[en_yakin_index]["answer"]
    else:
        return "Sorulan soruya dair uygun bir yanıt bulunamadı."

# Test
while True:
    giris = input("\nSorunuzu yazınız (çıkmak için 'çık'): ")
    if giris.lower() == "çık":
        break
    print("Chatbot:", chatbot(giris))
