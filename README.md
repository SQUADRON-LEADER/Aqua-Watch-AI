
<h1 align="center">🌊 Aqua-Watch-AI</h1>
<h3 align="center">AI-Powered Water Quality Monitoring & Prediction System</h3>

<p align="center">🚰💧 Protecting Water, Preserving Life — through AI and data.</p>

---

<!-- BADGES -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red" />
  <img src="https://img.shields.io/badge/Model-RandomForest-green" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

---

# 🎬 Demo GIF (Replace with your own GIF)
![Demo GIF](https://via.placeholder.com/900x450.png?text=Demo+GIF+Goes+Here)

---

# 📸 Screenshots (Replace with your real screenshots)

### 📊 Dashboard
![Dashboard](https://via.placeholder.com/900x450.png?text=Dashboard+Screenshot)

### 🤖 Prediction Output
![Prediction](https://via.placeholder.com/900x450.png?text=Prediction+Results)

### 📈 Charts & Trends
![Charts](https://via.placeholder.com/900x450.png?text=Charts+%26+Graphs)

---

# 📘 Table of Contents
- 🔍 Project Overview
- ✨ Features
- 🧪 Predicted Parameters
- 🏗️ Project Structure
- ⚡ Quick Start
- 🎮 How to Use
- 🤖 Model Details
- 📊 Dataset Info
- 🌱 Impact & Importance
- 🚀 Future Enhancements
- 🤝 Contributing
- 🩺 Troubleshooting
- 📜 License

---

# 🔍 Project Overview

Aqua-Watch-AI is an AI-driven water-quality platform built to analyze **22 years of environmental data (2000–2021)** across India.  
It predicts water parameters, visualizes pollution trends, and helps researchers & organizations make data-driven decisions.

💡 Mission: **Smarter Data → Cleaner Water → Safer Future**

---

# ✨ Features

- 🔮 Multi-parameter AI predictions  
- 📈 Live interactive visualization  
- 🗺️ Covers 100+ monitoring locations  
- 🌦️ Seasonal & long-term pollution trends  
- 🎛️ Easy-to-use Streamlit interface  
- ⚙️ Auto TDS & derived metrics  
- 📊 Clean project structure + reusable ML model  

---

# 🧪 Predicted Parameters

| Parameter | Meaning | Unit | Importance |
|----------|----------|------|-----------|
| **NH₄** | Ammonium | mg/L | Organic pollution indicator |
| **BSK₅ (BOD₅)** | Biological Oxygen Demand | mg/L | Waste decomposition |
| **O₂** | Dissolved Oxygen | mg/L | Essential for aquatic life |
| **NO₃** | Nitrate | mg/L | Agricultural runoff |
| **NO₂** | Nitrite | mg/L | Highly toxic pollutant |
| **PO₄** | Phosphate | mg/L | Causes algae bloom |
| **TDS** | Total Dissolved Solids | mg/L | Measures water purity |

---

# 🏗️ Project Structure

```
Aqua-Watch-AI/
├── Data/
│   ├── PB_All_2000_2021.csv
│   └── model_columns.pkl
├── Model/
│   ├── pollution_model.pkl
│   └── WaterQualityPred.ipynb
├── App/
│   ├── app.py
│   └── requirements.txt
└── README.md
```

---

# ⚡ Quick Start

### 1️⃣ Clone the Repo
```
git clone https://github.com/SQUADRON-LEADER/Aqua-Watch-AI.git
cd Aqua-Watch-AI
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Run the App
```
streamlit run app.py
```

Open in browser:  
👉 **http://localhost:8501**

---

# 🎮 How to Use

1. Select a monitoring location  
2. Enter optional water-quality parameters  
3. Click **Predict**  
4. Review AI-generated results  
5. Explore graphs & historical insights  

---

# 🤖 Model Details

<details>
<summary>🧠 Click to Expand Model Info</summary>

- **Dataset:** 2000–2021  
- **Total Records:** ~2,863  
- **Model:** Random Forest Regressor  
- **Accuracy:**  
  - R² Score > **0.85** for most parameters  
- **Features Used:**  
  - Year, Month, Season  
  - State/Location  
  - Environmental interactions  

</details>

---

# 📊 Dataset Info

<details>
<summary>📂 Click to Expand Dataset Details</summary>

Includes key water parameters such as:

- pH  
- Nitrate / Nitrite  
- Ammonium  
- Dissolved Oxygen  
- BOD₅  
- Phosphate  
- TDS  

Useful for:

- Environmental research  
- Water pollution forecasting  
- ML training  
- Government & policy planning  

</details>

---

# 🌱 Impact & Importance

- 💚 Protects freshwater ecosystems  
- ⚠️ Identifies pollution hotspots  
- 📉 Predicts contamination spikes  
- 📊 Helps policy makers & environmental agencies  

---

# 🚀 Future Enhancements

- 🛰️ Satellite-data integration  
- 📡 IoT real-time water-sensor connectivity  
- 🤖 Deep learning model upgrade  
- 📱 Mobile application  
- 🔔 SMS/Email alert system  
- 🌐 Public API  
- 💬 Multi-language interface  

---

# 🤝 Contributing

1. Fork the repo  
2. Create your feature branch  
3. Commit changes  
4. Push your branch  
5. Create a Pull Request  

💙 Contributions are welcome!

---

# 🩺 Troubleshooting

| Issue | Fix |
|-------|-----|
| Missing `.pkl` files | Place them in project root |
| Port already in use | `streamlit run app.py --server.port 8502` |
| Prediction slow | Close apps / upgrade RAM |
| Input errors | Verify correct numeric format |

---

# 📜 License

📝 Licensed under the **MIT License**
 MIT License

Copyright (c) 2025 SQUADRON-LEADER

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in  
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING  
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER  
DEALINGS IN THE SOFTWARE.



---

# 🌊 Aqua-Watch-AI  
### “Better Data. Cleaner Water. Safer Future.” 💧✨


