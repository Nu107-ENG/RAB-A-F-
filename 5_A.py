#5.SORUM A SIKKI :

import pandas as pd

data = {
    'Personel': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'Sütun2': ['NORMAL', 'YÜKSEK', 'DÜŞÜK', 'YÜKSEK', 'DÜŞÜK', 'YÜKSEK', 'DÜŞÜK', 'YÜKSEK', 'DÜŞÜK', 'YÜKSEK', 'DÜŞÜK'],
    'denetim': ['ORTA', 'YOK', 'YOK', 'ORTA', 'ORTA', 'iyi', 'iyi', 'ORTA', 'ORTA', 'iyi', 'iyi'],
    'Görev': ['UZMAN', 'UZMAN', 'yönetici', 'yönetici', 'yönetici', 'yönetici', 'yönetici', 'uzman', 'uzman', 'uzman', 'uzman'],
    'Memnun': ['Evet', 'Evet', 'Evet', 'Evet', 'Evet', 'Evet', 'Evet', 'Hayır', 'Hayır', 'Hayır', 'Hayır']
}

df = pd.DataFrame(data)
print(df)
