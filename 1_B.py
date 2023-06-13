
#1.SORUMUN B SIKKI : 


import pandas as pd

sol_durum_olasiliklari = []
sag_durum_olasiliklari = []

for i in range(1, 9):
    bolum = i
    sol_durum = data['Sol'][i-1]
    sag_durum = data['Sağ'][i-1]
    
    sol_olasilik = len(df[df['Sol'] == sol_durum]) / len(df)
    sag_olasilik = len(df[df['Sağ'] == sag_durum]) / len(df)
    
    sol_durum_olasiliklari.append(sol_olasilik)
    sag_durum_olasiliklari.append(sag_olasilik)

sol_durum_df = pd.DataFrame({'Sol Durum': data['Sol'], 'Olasılık': sol_durum_olasiliklari})

sag_durum_df = pd.DataFrame({'Sağ Durum': data['Sağ'], 'Olasılık': sag_durum_olasiliklari})

print("Sol Durumların Olasılıksal Değerleri:")
print(sol_durum_df)

print("\nSağ Durumların Olasılıksal Değerleri:")
print(sag_durum_df)
