# ♻️ AI-Based Waste Collection Decision Support System

An intelligent waste management system that prioritizes garbage collection requests using **fill-level estimation, contamination detection, and decomposition-aware scoring**.

---

## 📌 Project Overview

This project aims to improve urban waste collection efficiency by analyzing waste conditions and generating a **priority score** for each request. The system ensures that high-risk waste (overflowing, contaminated, decomposing) is collected first.

---
## 📸 Screenshots

![Dashboard](screenshots/Screenshot 2026-03-05 114610.png)
![Prediction](Screenshots/Screenshot 2026-03-05 114658.png)

## 🎯 Key Features

* 📦 **Fill-Level Detection** – Estimates how full a bin is
* ⚠️ **Contamination Detection** – Identifies hazardous or mixed waste
* 🧪 **Decomposition Risk Analysis** – Evaluates how long waste has been sitting
* 📊 **Priority Scoring System** – Combines all factors into a final score
* 📍 **Smart Worker Assignment (Optional)** – Assigns nearest worker based on location
* 📈 **Dashboard (Streamlit)** – Displays prioritized collection requests

---

## 🧠 System Architecture

1. Input waste request (image + location + time)
2. Analyze:

   * Fill level (OpenCV)
   * Waste type (CNN model)
   * Decomposition risk (rule-based)
3. Compute priority score
4. Store results in CSV
5. Display in dashboard

---

## 🛠️ Tech Stack

* **Python**
* **OpenCV** – Fill level estimation
* **TensorFlow / Keras** – Waste classification model
* **Pandas** – Data handling
* **Streamlit** – Dashboard UI

---

## 📂 Project Structure

```
Waste_Priority_System/
│
├── app.py                # Streamlit dashboard
├── src/                  # Core modules
│   ├── data_loader.py
│   ├── fill_level.py
│   ├── decomposition.py
│   ├── predictor.py
│   ├── scoring.py
│   └── train_model.py
│
├── models/               # Trained ML model
├── requests.csv          # Stored requests
├── requirements.txt      # Dependencies
└── .gitignore
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/your-username/Waste_Priority_System.git
cd Waste_Priority_System
```

### 2. Create virtual environment

```
python -m venv waste_env
waste_env\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the application

```
streamlit run app.py
```

---

## 📊 Output

* Sorted waste collection requests based on **priority score**
* Helps municipalities take **data-driven decisions**

---

## 💡 Future Improvements

* Real-time IoT bin integration
* GPS-based route optimization
* Mobile app for workers
* Cloud deployment

---

## 👩‍💻 Author

**Fathima Hibath**
MSc Data Science Student

---

## ⭐ Note

This project is developed as part of an academic capstone to demonstrate **AI-driven decision systems for smart cities**.
