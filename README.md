# Smart Farming Dashboard – Soil Moisture Monitoring

## Project Overview
This project implements a Smart Farming Dashboard using Soil Moisture IoT sensor data.
The system follows the Data Lifecycle Management approach, starting from data acquisition,
processing, analysis, visualization, and data governance.

The dashboard is built using Python and Streamlit to monitor soil moisture conditions
and provide visual insights for smart irrigation decision-making.

---

## Dataset
- Dataset Name: Soil Moisture Dataset  
- Source: Kaggle  
- Data Type: IoT sensor data  
- File Format: CSV  

### Dataset Description
The dataset contains soil moisture readings from multiple sensors along with timestamp
components such as year, month, day, hour, minute, and second.

---

## Data Lifecycle Implementation

### 1. Data Acquisition
The dataset was obtained from Kaggle and loaded into the analysis environment using Pandas.

### 2. Data Processing (Cleansing)
Data cleansing was performed by:
- Checking for missing values
- Removing rows with missing values
- Formatting time-related columns into a single datetime column

The cleaned dataset was saved as `cleaned_data.csv`.

### 3. Data Analysis
Descriptive statistical analysis was conducted to understand the distribution and
characteristics of soil moisture data across sensors.

### 4. Data Visualization
Data visualization was implemented using:
- Time series plots to observe soil moisture trends
- Gauge charts to display current soil moisture levels
- Heatmap correlation analysis between sensors
- Threshold-based alert system for dry soil conditions

All visualizations are presented in an interactive Streamlit dashboard.

### 5. Documentation & Data Governance
Data quality was evaluated using three metrics:
- Accuracy
- Completeness
- Timeliness

These metrics ensure that the dataset is reliable, complete, and relevant for analysis.

---

## Data Quality Score
- Accuracy: 1.0  
- Completeness: 1.0  
- Timeliness: 1.0  

---

## Tools & Technologies
- Python  
- Pandas  
- Matplotlib  
- Streamlit  
- Google Colab  

---

## Project Structure
├── README.md
├── plant_vase1(2).csv
├── Soil_Moisture_Dashboard_102.ipynb
├── dashboard/
│ └── app.py
├── outputs/
│ └── cleaned_data.csv
│ ├── dashboard.png
│ └── analysis_report.pdf


---

## How to Run the Dashboard
1. Install the required libraries listed in `requirements.txt`
2. Run the Streamlit application:
streamlit run app.py
3. Open the generated local URL in your browser.

---


