import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Aplikasi Visualisasi Data Tanamin")
st.write("Selamat datang di aplikasi visualisasi data Tanamin! Di sini Anda dapat menjelajahi berbagai fitur dan data terkait Tanamin.")

data = pd.DataFrame(data={
    "Kampanye": ["Kampanye A", "Kampanye B", "Kampanye C"],
    "Total Donasi (juta)": [50, 75, 100],
})

st.subheader("Data Kampanye Donasi")
st.dataframe(data)

# Bar Chart
st.bar_chart(data.set_index(keys= "Kampanye"))

# Line Chart
st.line_chart(data.set_index("Kampanye"))

# Matplotlib Plot
fig, ax = plt.subplots()
ax.bar(data["Kampanye"], data ["Total Donasi (juta)"], color="green")
ax.set_ylabel("Donasi (juta)")
st.pyplot(fig)

# Dropdown
tipe = st.selectbox("Pilih Tipe Visualisasi", ["Bar", "Pie", "Line", " Doughnut"])
if tipe == "Bar":
    st.bar_chart(data.set_index(keys= "Kampanye"))
elif tipe == "Pie":
    st.line_chart(data.set_index(keys= "Kampanye"))
else:
    fig, ax = plt.subplots()
    ax.pie(data["Total Donasi (juta)"], labels=data["Kampanye"], autopct='%1.1f%%')
    st.pyplot(fig)

# Slider
nilai = st.slider("Tampilkan data dengan donasi minimum:", 0, 150, 50)
st.dataframe(data[data["Total Donasi (juta)"] >= nilai])

# Geospasial
st.title("Peta Lokasi Penanaman")

data_peta = pd.DataFrame(data={
    'lokasi': ['Balikpapan', 'Samboja', 'Mahakam'],
    'lat': [-1.27, -1.10, -0.50],
    'lon': [116.83, 117.00, 117.25],
})

st.map(data_peta)

# Dashboard
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Dashboard Donasi Lingkungan 🌱")

data = pd.DataFrame({
    "Kampanye": ["Mangrove Balikpapan", "Pantai Samboja", "Delta Mahakam"],
    "Donasi": [120, 85, 60],
    "Target": [150, 100, 90]
})

kampanye = st.selectbox("Pilih kampanye:", data["Kampanye"])
row = data[data["Kampanye"] == kampanye].iloc[0]

st.metric("Donasi Saat Ini", f"{row['Donasi']} juta", delta=row['Donasi'] - row['Target'])
st.progress(row['Donasi'] / row['Target'])

fig, ax = plt.subplots()
ax.bar(data["Kampanye"], data["Donasi"], color="green")
ax.set_ylabel("Donasi (juta)")
st.pyplot(fig)

# Menambahkan Gambar dan Teks
st.image("https://images.pexels.com/photos/3718351/pexels-photo-3718351.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500", caption="Kegiatan Penanaman Mangrove di Balikpapan")
st.markdown("""
### Tujuan Program
Meningkatkan kesadaran masyarakat terhadap pentingnya ekosistem mangrove.
""")

