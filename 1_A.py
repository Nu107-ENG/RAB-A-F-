#1.SORUMUN A SIKKI : 

import pandas as pd

data = {
    'Koşullar': ['Maaş = NORMAL', 'Maaş = YÜKSEK', 'Maaş = DÜŞÜK', 'Denetim = ORTA', 'Denetim = YOK', 'Denetim = iyi', 'Görev = UZMAN', 'Görev = yönetici', 'Görev = uzman', 'Memnun = Evet', 'Memnun = Hayır'],
    'Sol Taraftaki Örnek Sayısı': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Sağ Taraftaki Örnek Sayısı': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

for i in range(len(data['Koşullar'])):
    kosul = data['Koşullar'][i]
    if 'Maaş = NORMAL' in kosul:
        data['Sol Taraftaki Örnek Sayısı'][i] = len(df[df['Sütun2'] == 'NORMAL'])
        data['Sağ Taraftaki Örnek Sayısı'][i] = len(df[df['Sütun2'].isin(['YÜKSEK', 'DÜŞÜK'])])
    elif 'Maaş = YÜKSEK' in kosul:
        data['Sol Taraftaki Örnek Sayısı'][i] = len(df[df['Sütun2'] == 'YÜKSEK'])
        data['Sağ Taraftaki Örnek Sayısı'][i] = len(df[df['Sütun2'].isin(['NORMAL', 'DÜŞÜK'])])
    elif 'Maaş = DÜŞÜK' in kosul:
        data['Sol Taraftaki Örnek Sayısı'][i] = len(df[df['Sütun2'] == 'DÜŞÜK'])
        data['Sağ Taraftaki Örnek Sayısı'][i] = len(df[df['Sütun2'].isin(['NORMAL', 'YÜKSEK'])])
    elif 'Denetim = ORTA' in kosul:
        data['Sol Taraftaki Örnek Sayısı'][i] = len(df[df['denetim'] == 'ORTA'])
        data['Sağ Taraftaki Örnek Sayısı'][i] = len(df[df['denetim'].isin(['YOK', 'iyi'])])
    elif 'Denetim = YOK' in kosul:
        data['Sol Taraftaki Örnek Sayısı'][i] = len(df[df['denetim'] == 'YOK'])
        data['Sağ Taraftaki Örnek Sayısı'][i] = len(df[df['denetim'].isin(['ORTA', 'iyi'])])
    elif 'Denetim = iyi' in kosul:
        data['Sol Taraftaki Örnek Sayısı'][i] = len(df[df['denetim'] == 'iyi'])
        data['Sağ Taraftaki Örnek Sayısı'][i] = len(df[df['denetim'].isin(['ORTA', 'YOK'])])
    elif 'Görev = UZMAN' in kosul:
        data['Sol Taraftaki Örnek Sayısı'][i] = len(df[df['görev'] == 'UZMAN'])
        data['Sağ Taraftaki Örnek Sayısı'][i] = len(df[df['görev'].isin(['yönetici', 'uzman'])])
    elif 'Görev = yönetici' in kosul:
        data['Sol Taraftaki Örnek Sayısı'][i] = len(df[df['görev'] == 'yönetici'])
        data['Sağ Taraftaki Örnek Sayısı'][i] = len(df[df['görev'].isin(['UZMAN', 'uzman'])])
    elif 'Görev = uzman' in kosul:
        data['Sol Taraftaki Örnek Sayısı'][i] = len