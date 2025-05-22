# C#/.NET Teknik Chatbot

Bu proje, C# ve .NET teknolojileri hakkında teknik soruları yanıtlayan yapay zeka destekli bir chatbot sistemidir. Sorular, mevcut bir soru-cevap veri setiyle karşılaştırılır; yeterli benzerlik bulunamazsa OpenAI API üzerinden yeni cevaplar alınır ve sistem güncellenir.

## Özellikler

- FAISS ile hızlı embedding tabanlı arama
- Teknik sorgu kontrolü
- Belirli benzerlik skorlarına göre karar ağacı
- OpenAI GPT ile yanıt üretimi
- JSON tabanlı veri güncelleme
- FastAPI REST servisi
- Ngrok ile internete açılabilir API yapısı

## Nasıl Çalıştırılır?

1. Gerekli bağımlılıkları yükleyin:
   ```bash
   pip install -r requirements.txt
    ````

2. `.env` dosyanıza OpenAI API anahtarınızı ekleyin:

   ```
   OPENAI_API_KEY=your-key-here
   ```

3. FastAPI sunucusunu başlatın:

   ```bash
   uvicorn main:app --reload
   ```

4. Sunucu çalışırken, local sunucunuzu ngrok ile tünelleyin:

   ```bash
   ngrok http 8000
   ```

5. Ngrok'un size verdiği HTTPS adresini, Landbot gibi platformlara webhook endpoint olarak tanımlayabilirsiniz.

## API Kullanımı

* `POST /ask`
  Gövde:

  ```json
  {
    "question": "C# ile arayüz nasıl yapılır?"
  }
  ```