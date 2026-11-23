# Hayvan Sağlığı İçin Akıllı Takip Sistemi

Termal ve davranışsal veri füzyonu ile hayvan sağlığını izleyen akıllı takip sistemi projesi. Bu depo, projenin veri seti üretimini ve makine öğrenmesi modeli eğitimini içerir.

## İçerik

| Dosya | Açıklama |
|---|---|
| `HayvanSagligiTakipSistemiModelEgitimi1.ipynb` | Veri analizi ve Random Forest ile sağlık durumu sınıflandırma modeli |
| `hayvanSagligiTakipSistemiDatasetOlusturma.py` | Sentetik veri seti üretim scripti |
| `gercekci_hayvan_veri_seti.csv` | Üretilen veri seti (3000 kayıt) |
| `yolo_uyumlu_hayvan_verisi.csv` | YOLO uyumlu biçimlendirilmiş veri seti |

## Veri Seti

Her kayıt bir hayvanın anlık durumunu temsil eder:

| Sütun | Açıklama |
|---|---|
| `Ortam_Isisi` | Ortam sıcaklığı (°C) |
| `Vucut_Isisi` | Vücut sıcaklığı (°C) |
| `Hareket` | Hareketlilik skoru (0–100) |
| `Durus` | Duruş kodu: 0 = yatıyor, 1 = oturuyor, 2 = ayakta |
| `Durum` | Sağlık durumu (hedef değişken) |

**Sınıflar:** `Saglikli`, `Mastitis_Riski`, `Sap_Riski`, `Tuberkuloz_Riski`

## Model

`scikit-learn` ile **Random Forest** sınıflandırıcı (`n_estimators=100`) kullanılır. Model; sıcaklık, hareket ve duruş verilerinden hayvanın sağlık durumunu tahmin eder.

## Kullanım

```bash
pip install pandas numpy matplotlib scikit-learn
python hayvanSagligiTakipSistemiDatasetOlusturma.py
jupyter notebook HayvanSagligiTakipSistemiModelEgitimi1.ipynb
```

> Not: Veri seti sentetik olarak üretilmiştir; gerçek saha verisi ile yeniden eğitim önerilir.
