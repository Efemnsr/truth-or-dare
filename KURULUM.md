# 🎲 Doğruluk mu Cesaret mi? — Kurulum Talimatı

## Dosyalar
- `truth_or_dare.py` → Oyunun kaynak kodu
- `build.bat`        → EXE oluşturucu

---

## EXE Yapmak İçin

### Gereksinimler
- Python 3.x (3.14 dahil) kurulu olmalı
- Kurulum: https://python.org

### Adımlar
1. Her iki dosyayı aynı klasöre koy
2. `build.bat` dosyasına çift tıkla
3. `dist/DogrulukMuCesaretMi.exe` oluşacak
4. Bu EXE'yi istediğin yere taşıyabilirsin, başka şey gerekmez

### Manuel komut (CMD ile)
```
pip install pyinstaller
pyinstaller --onefile --windowed --name "DogrulukMuCesaretMi" truth_or_dare.py
```

---

## Oyun Nasıl Oynanır?
1. Oyuncu isimlerini tek tek yaz ve "Ekle" butonuna bas
2. En az 2 oyuncu gereklidir
3. "Oyunu Başlat" ile oyuna geç
4. Sistem rastgele 2 kişi seçer: Soran + Cevaplayan
5. DOĞRULUK veya CESARET seç
6. Soru aklına gelmezse veya beğenmezsen → "Soruyu Değiştir"
7. Tur bitti → "Yeni Tur" ile yeni 2 kişi seç
8. Her oyun açıldığında 50 doğruluk + 50 cesaret sorusu karıştırılır

---

## Özellikler
✅ İsim bazlı oyuncu ekleme (sınırsız)
✅ Rastgele 2 oyuncu seçimi
✅ Her oyunda karıştırılan 100 soru
✅ Soruyu değiştirme butonu
✅ Yeni tur butonu
✅ Koyu tema arayüz
