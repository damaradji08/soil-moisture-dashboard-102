import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Smart Farming Dashboard")
st.write("Monitoring Soil Moisture Sensor Data")

# Load dataset
df = pd.read_csv("plant_vase1(2).csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Soil Moisture Time Series (moisture0)")

fig, ax = plt.subplots()
ax.plot(df['moisture0'])
ax.set_xlabel("Index Data")
ax.set_ylabel("Soil Moisture")
ax.set_title("Soil Moisture Trend Over Time")

st.pyplot(fig)

st.subheader("Current Soil Moisture (moisture0)")

current_moisture = df['moisture0'].iloc[-1]

st.metric(
    label="Soil Moisture Level",
    value=round(current_moisture, 3)
)

st.subheader("Correlation Heatmap (Soil Moisture Sensors)")

# pilih kolom sensor
sensor_cols = ['moisture0','moisture1','moisture2','moisture3','moisture4']
corr = df[sensor_cols].corr()

fig, ax = plt.subplots()
cax = ax.imshow(corr, cmap='coolwarm')

ax.set_xticks(range(len(sensor_cols)))
ax.set_yticks(range(len(sensor_cols)))
ax.set_xticklabels(sensor_cols)
ax.set_yticklabels(sensor_cols)

plt.colorbar(cax)
ax.set_title("Correlation Between Soil Moisture Sensors")

st.pyplot(fig)

st.subheader("Soil Moisture Alert System")

threshold = 0.2
current_moisture = df['moisture0'].iloc[-1]

if current_moisture < threshold:
    st.error(
        f"⚠️ WARNING: Soil moisture is low ({round(current_moisture,3)}). Irrigation needed!"
    )
else:
    st.success(
        f"✅ Soil moisture is normal ({round(current_moisture,3)})."
    )
