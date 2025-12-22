# 🌊 Aqua-Watch-AI

### 🔗 **Live Demo:** [https://aqua-watch-ai.streamlit.app/](https://aqua-watch-ai.streamlit.app/)

### 📘 Project Description

Aqua-Watch-AI is an AI-driven water quality monitoring and prediction system designed to help track, visualize, and forecast the condition of water bodies across India. Using **22 years of environmental data**, machine learning models, and a visually rich Streamlit dashboard, this project empowers citizens, researchers, and government bodies to make **data-driven decisions** about water pollution and sustainability.

Built with a mission to support environmental awareness and resource management, Aqua-Watch-AI transforms complex water quality metrics into clear, accessible insights — making pollution monitoring smarter, faster, and more accurate.

![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-yellow)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Maintained](https://img.shields.io/badge/maintained-yes-success)
![Contributions](https://img.shields.io/badge/contributions-welcome-orange)

### *Monitoring Water. Predicting Pollution. Protecting Life.*

---

## 🚀 Overview

Aqua-Watch-AI uses AI + Data Science to make India's water quality **predictable, accessible, and easy to understand**.

### 🔥 Highlights

* Built with **Machine Learning**, **Streamlit**, and **Plotly**
* Predicts **7 critical water quality parameters**
* Supports **100+ stations across India**
* Offers an **interactive, user-friendly dashboard**

Aqua-Watch-AI analyzes **22 years of historical water-quality data** and predicts key pollution parameters using machine learning, displayed in a rich Streamlit dashboard.

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

```
git clone https://github.com/SQUADRON-LEADER/Aqua-Watch-AI.git
cd Aqua-Watch-AI
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Dashboard

```
sstreamlit run app.py
```

👉 Open `http://localhost:8501` in your browser.

---

## 🧠 Machine Learning Model

* **Type:** RandomForest Regressor (Multi-Output)
* **Dataset:** 2000–2021 water quality data
* **Records:** 2,863+
* **Stations:** 100+ across 20+ states

### Model Strengths

* Handles nonlinear relationships well
* Robust to noisy/missing data
* Predicts all 7 parameters simultaneously

---

## 🌍 Real-World Impact & Use Cases

* Government pollution monitoring agencies
* Environmental researchers & students
* NGOs working on sustainability
* Water resource decision-making support

---

## 🚧 Roadmap — Coming Soon

* 🔗 IoT sensor real-time integration
* 📡 Satellite imagery support
* 📱 Mobile App (React Native)
* ⚠️ Pollution alerts (SMS/email)
* 🤖 Advanced deep learning models
* 🌏 Multi-language dashboard

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push & submit a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.


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




## 📸 Screenshots 

<img width="1916" height="851" alt="Screenshot 2025-10-23 180422" src="https://github.com/user-attachments/assets/309eea26-179e-401c-94e0-b2f8861bbabc" />

<img width="1904" height="838" alt="Screenshot 2025-10-23 180430" src="https://github.com/user-attachments/assets/4c948a5e-0ce3-417a-9405-8ba86b9c5945" />


---

## 🧭 Project Philosophy

* **Transparency** — Open data & open science
* **Accessibility** — Simple for everyone
* **Impact** — Strengthening environmental awareness

---

## ⭐ Star This Project!

If you like this project, please ⭐ the repo — it helps others discover it!

---

## 👨‍💻 Author

### 🧑‍💻 *Aayush Kumar*

* Developer & Machine Learning Engineer
* Passionate about environmental AI & sustainability
* GitHub: [https://github.com/SQUADRON-LEADER](https://github.com/SQUADRON-LEADER)

---

## ❤️ Acknowledgements

* Streamlit, scikit-learn, Plotly
* Environmental data providers
* Contributors supporting sustainability










