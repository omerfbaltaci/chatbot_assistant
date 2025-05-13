# .NET Soru-Cevap Chatbotu

Bu proje, C# ve .NET teknolojileriyle ilgili teknik soruları cevaplayabilen bir embedding tabanlı chatbot uygulamasıdır. Kullanıcıdan gelen sorular, önceden hazırlanmış veri setindeki sorularla karşılaştırılır ve yeterli benzerlikte bir eşleşme bulunamazsa Gemini API ile yanıt oluşturulur. Yeni sorular ve yanıtlar genişletilmiş veri setine kaydedilir.

### Özellikler

- FAISS ile hızlı benzerlik araması
- Gemini API ile yeni soru-cevap üretimi
- Genişletilebilir veri kümesi
- Yeni sorular `extended_data.json` içine otomatik olarak kaydedilir

### Veri Seti

* `data/main_data.json`: Önceden hazırlanmış C#/.NET teknik soru-cevapları
* `data/extended_data.json`: Kullanıcıdan gelen yeni sorular ve yanıtlar

## Kurulum

### 1. Ortamı Hazırlama (Manuel)

```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
pip install -r requirements.txt
````

`.env` dosyasına Gemini API anahtarınızı girin:

```
API_KEY=your-api-key
```

Çalıştırmak için:

```bash
python main.py
```

### 2. Docker ile Çalıştırma

#### 1- "Dockerfile" İçeriği

Kök dizine (`chatbot_assistant/`) şu içeriğe sahip bir `Dockerfile` oluştur:

```dockerfile
# Python base image
FROM python:3.10-slim

# Çalışma dizini
WORKDIR /app

# Gerekli dosyaları kopyala
COPY . .

# Gerekli paketleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Ortam değişkeni (istenirse)
ENV PYTHONUNBUFFERED=1

# Başlangıç komutu
CMD ["python", "main.py"]
````

#### 2- Docker Image Oluşturma

```bash
docker build -t chatbot-assistant .
```

#### 3- Container Çalıştırma

```bash
docker run -it --env API_KEY=your-api-key chatbot-assistant
```