# 🌊 Aqua-Watch-AI

### *Monitoring Water. Predicting Pollution. Protecting Life.*

---

## 🚀 Overview

**Aqua-Watch-AI** is an AI-powered water quality monitoring and forecasting system for India.
It analyzes **22 years of historical water-quality data** and uses machine learning to predict key pollution parameters.
The project includes an interactive dashboard built with **Streamlit**, offering rich visualizations and predictive analytics.

---

## ✨ Features

* 🔮 **AI Model for Water Quality Prediction**
* 📊 **Interactive Dashboard** (Plotly + Streamlit)
* 🇮🇳 **Pan-India Coverage** with 100+ monitoring stations
* 📈 **Historical Trend Analysis**
* 💧 **Water Quality Classification** based on TDS
* 🧪 **Prediction of 7 Key Water Parameters**

---

## 📦 Predicted Parameters

| Parameter | Description               | Unit |
| --------- | ------------------------- | ---- |
| **NH₄**   | Ammonium                  | mg/L |
| **BSK₅**  | Biochemical Oxygen Demand | mg/L |
| **O₂**    | Dissolved Oxygen          | mg/L |
| **NO₃**   | Nitrate                   | mg/L |
| **NO₂**   | Nitrite                   | mg/L |
| **PO₄**   | Phosphate                 | mg/L |
| **TDS**   | Total Dissolved Solids    | mg/L |

---

## 🏗️ Project Structure

```
Aqua-Watch-AI/
├── app.py                         # Streamlit application
├── Data/
│   ├── PB_All_2000_2021.csv       # Historical dataset
│   └── model_columns.pkl          # Input feature columns
├── AI_Model/
│   ├── pollution_model.pkl        # Trained ML model
│   └── WaterQualityPred.ipynb     # Training notebook
├── requirements.txt               # Dependencies
└── README.md                      # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/SQUADRON-LEADER/Aqua-Watch-AI.git
cd Aqua-Watch-AI
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Dashboard

```bash
streamlit run app.py
```

👉 Open `http://localhost:8501` in your browser.

---

## 🧠 Machine Learning Model

* Model Type: **RandomForest Regressor (Multi-Output)**
* Dataset: **2000–2021 water quality data**
* Records: **2,863+**
* Stations: **100+ across 20+ states**

### Model Strengths

* Handles nonlinear relationships well
* Robust to noisy/missing data
* Predicts all 7 parameters simultaneously

---

## 📈 Use Cases

* Government pollution monitoring agencies
* Environmental researchers & students
* NGOs working on sustainability
* Data‑driven water resource decision-making

---

## 📍 Future Enhancements

* 🔗 IoT Sensor Integration for real-time monitoring
* 📡 Satellite imagery (remote sensing) support
* 📱 Mobile App (React Native)
* ⚠️ Pollution alert notifications (SMS/email)
* 🤖 Advanced Deep Learning Models
* 🌏 Multi-language public dashboard

---

## 🤝 Contributing

Contributions are welcome!
Steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push & submit a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2025 Aqua-Watch-AI Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## ❤️ Acknowledgements

* Open-source tools: Streamlit, scikit-learn, Plotly
* Environmental agencies for historical data
* Contributors supporting water sustainability
