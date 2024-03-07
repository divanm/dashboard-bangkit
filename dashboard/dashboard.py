import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#create_NO2_tabel
def create_NO2_tabel(dataset):
    NO2_per_tahun = dataset[dataset['year'] == tahun]
    NO2_tabel = NO2_per_tahun[['NO2','month']].groupby(['month']).mean()
    return NO2_tabel

dataset = pd.read_csv('https://raw.githubusercontent.com/divanm/dashboard-dicoding/master/data/cleaning.csv')
dataset.info()
# Membuat bagian pertama dashboard
st.title("Air Quality Dashboard")
st.header("Stasiun: Dongsi")

# Membuat bagian informasi rata-rata PM2.5 per tahun
st.subheader('Rata-rata PM2.5 per Tahun')
st.text("Informasi tentang Rata-rata PM2.5 per Tahun")

# Mengonversi kolom tanggal menjadi indeks datetime
dataset['datetime'] = pd.to_datetime(dataset[['year', 'month', 'day']])
dataset.set_index('datetime', inplace=True)

# Menghitung rata-rata PM2.5 per bulan untuk setiap tahun
# Assuming 'dataset' is your DataFrame
numeric_columns = [col for col in dataset.columns if np.issubdtype(dataset[col].dtype, np.number)]
numeric_dataset = dataset[numeric_columns]
df_monthly_mean = numeric_dataset.groupby([numeric_dataset.index.year, numeric_dataset.index.month]).mean()
# Tampilkan plot untuk setiap tahun dalam dashboard
unique_years = dataset.index.year.unique()

for year in unique_years:
    df_year = df_monthly_mean.loc[year]
    fig, ax = plt.subplots(figsize=(10, 6))  # Membuat objek Figure dan Axes
    ax.plot(df_year.index, df_year['PM2.5'], marker='o', linestyle='-')
    ax.set_title(f'Rata-rata PM2.5 per Bulan Tahun {year}')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Rata-rata PM2.5')
    ax.set_xticks(range(1, 13))
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax.grid(True)
    plt.tight_layout()
    st.pyplot(fig)  # Menampilkan objek Figure menggunakan st.pyplot()

#membuat tabel informasi NO2 per day
st.subheader('Number of NO2')
st.text("Information about Mean of Number of NO2 per Month in a certain year")
tahun = st.selectbox(
    label = 'Choose The Year',
    options = (2013,2014,2015,2016,2017)
    )
st.write('Your Choose: ', tahun)

#membuat chart informasi NO2 per day
fig, ax = plt.subplots(figsize=(12, 6))
plt.style.use('ggplot')
ax.plot(
    create_NO2_tabel(dataset).index,
    create_NO2_tabel(dataset)['NO2'],
    marker='o', 
    linewidth=4,
    color="#40679E"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.set_title(("Mean of Number of NO2 per Month in " + str(tahun)))
ax.set_xlabel("Month")
ax.set_ylabel("NO2")
ax.set_xlim(0,13)
ax.set_ylim(30, 80)

st.pyplot(fig)
