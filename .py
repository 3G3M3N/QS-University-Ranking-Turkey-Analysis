import pandas as pd 

df = pd.read_csv("qs-world-university-rankings-2017-to-2022-V2.csv")
df

turkey = df.loc[(df["country"]=="Turkey")]
turkey

turkey2017 = turkey.loc[(turkey["year"]==2017)]
turkey2017
turkey2017.shape
turkey2017["city"].value_counts()

turkey2018 = turkey.loc[(turkey["year"]==2018)]
turkey2018
turkey2018.shape
turkey2018["city"].value_counts()

turkey2019 = turkey.loc[(turkey["year"]==2019)]
turkey2019
turkey2019.shape
turkey2019["city"].value_counts()

turkey2020 = turkey.loc[(turkey["year"]==2020)]
turkey2020
turkey2020.shape
turkey2020["city"].value_counts()

turkey2021 = turkey.loc[(turkey["year"]==2021)]
turkey2021
turkey2021.shape
turkey2021["city"].value_counts()

turkey2022 = turkey.loc[(turkey["year"]==2022)]
turkey2022
turkey2022.shape
turkey2022["city"].value_counts()

df = pd.read_csv("2023 QS World University Rankings.csv")
Turkey2023 = df.loc[df["location code"]=="TR"]
Turkey2023

yeni_2024 = pd.read_csv("2024 QS World University Rankings 1.1 (For qs.com).csv")
turkish2024 = yeni_2024.loc[df["Country"]=="Turkey"]
turkish2024

#matplotlib

import matplotlib.pyplot as plt

# Grafik boyutlarını ayarlama
plt.figure(figsize=(15, 10))

# Çubuk grafik oluşturma
plt.barh(turkish2024['Institution Name'], turkish2024['2024 RANK'], color='blue', label='2024 Rank')
plt.barh(turkish2024['Institution Name'], turkish2024['2023 RANK'], color='orange', label='2023 Rank')

# Eksen etiketlerini ve başlığı ekleme
plt.xlabel('Rank')
plt.ylabel('University')
plt.title('Comparison of Turkish Universities Ranks in 2023 and 2024')
plt.legend()

# Grafik gösterme
plt.gca().invert_yaxis()
plt.show()

