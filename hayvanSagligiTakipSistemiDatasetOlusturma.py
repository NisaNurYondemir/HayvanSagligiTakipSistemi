import pandas as pd
import numpy as np

n_samples = 3000 

# 1. Ortam Koşulları
ambient_temps = np.random.uniform(20, 45, n_samples)

# 2. Temel Vücut Isısı
base_temp = 38.5 + np.where(ambient_temps > 35, (ambient_temps - 35) * 0.08, 0)
vucut_isisi = base_temp + np.random.normal(0, 0.2, n_samples)

# 3. Temel Hareketlilik ve Duruş (Sağlıklı Hayvanlar)
# Duruş Kodları: 0: Yatıyor, 1: Oturuyor, 2: Ayakta
hareket = np.random.normal(70, 10, n_samples)
durus = np.random.choice([2, 1, 0], size=n_samples, p=[0.7, 0.2, 0.1]) # Sağlıklı hayvan genelde ayaktadır.

data = pd.DataFrame({
    'Ortam_Isisi': ambient_temps,
    'Vucut_Isisi': vucut_isisi,
    'Hareket': hareket,
    'Durus': durus,
    'Durum': 'Saglikli'
})

# --- HASTALIK VE DURUŞ İLİŞKİLENDİRMESİ ---

# A. Mastitis (%25): Hareket azalır, hayvan daha fazla oturmaya veya yatmaya başlar
mask_mastitis = np.random.choice([True, False], size=n_samples, p=[0.25, 0.75])
data.loc[mask_mastitis, 'Vucut_Isisi'] += np.random.uniform(0.5, 1.2)
data.loc[mask_mastitis, 'Hareket'] -= np.random.uniform(15, 30)
# Mastitis olan hayvanın yatma veya oturma olasılığı artar
data.loc[mask_mastitis, 'Durus'] = np.random.choice([0, 1, 2], size=mask_mastitis.sum(), p=[0.4, 0.4, 0.2])
data.loc[mask_mastitis, 'Durum'] = 'Mastitis_Riski'

# B. Şap (%5): Hareket çok düşük, hayvan neredeyse tamamen yatıyor (Ağrılı ayaklar)
mask_sap = np.random.choice([True, False], size=n_samples, p=[0.05, 0.95])
data.loc[mask_sap, 'Vucut_Isisi'] += np.random.uniform(1.5, 2.5)
data.loc[mask_sap, 'Hareket'] *= 0.2
data.loc[mask_sap, 'Durus'] = np.random.choice([0, 1], size=mask_sap.sum(), p=[0.9, 0.1]) # %90 Yatar
data.loc[mask_sap, 'Durum'] = 'Sap_Riski'

# C. Tüberküloz (%3): Kronik yorgunluk, ayakta durma süresi azalır
mask_tuberkuloz = np.random.choice([True, False], size=n_samples, p=[0.03, 0.97])
data.loc[mask_tuberkuloz, 'Vucut_Isisi'] += np.random.uniform(0.3, 0.8)
data.loc[mask_tuberkuloz, 'Hareket'] -= np.random.uniform(20, 40)
data.loc[mask_tuberkuloz, 'Durus'] = np.random.choice([0, 1, 2], size=mask_tuberkuloz.sum(), p=[0.5, 0.3, 0.2])
data.loc[mask_tuberkuloz, 'Durum'] = 'Tuberkuloz_Riski'

# 4. Temizlik
data['Vucut_Isisi'] = np.clip(data['Vucut_Isisi'], 37.5, 42.5)
data['Hareket'] = np.clip(data['Hareket'], 0, 100)

# 5. İstatistiksel Kontrol
print("Hastalık ve Duruş Dağılımı (Ortalama Hareket):")
print(data.groupby(['Durum', 'Durus'])['Hareket'].mean().unstack())

data.to_csv("gercekci_hayvan_veri_seti.csv", index=False)

# Eğer eski isme geri döneceksen okuma satırın bu olmalı:
df = pd.read_csv("gercekci_hayvan_veri_seti.csv") 

# Ama eğitimde Durus'u mutlaka eklemelisin:
X = df[['Ortam_Isisi', 'Vucut_Isisi', 'Hareket', 'Durus']]