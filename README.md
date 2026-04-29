# 🧩 Modular ETL Pipeline (Python)

## 📌 Overview
This project is a modular ETL (Extract, Transform, Load) pipeline built using Python.  
It automates data preprocessing workflows including validation, cleaning, transformation, and logging using a scalable modular architecture.

---

## ⚙️ Features
📥 Config-driven pipeline using YAML  
🧹 Handles missing values and duplicate records  
✅ Data validation for required schema checks  
🔄 Feature scaling using StandardScaler  
🪵 Logging system for debugging and tracking  
🧩 Fully modular architecture (separation of concerns)  
📊 Supports multiple datasets dynamically  

---

## 🔄 Workflow
Load configuration from YAML file  
Read dataset (CSV)  
Validate required columns  
Handle missing values  
Remove duplicate records  
Apply data transformations (scaling)  
Save processed dataset  
Log each step of execution  

---

## 🏗️ Project Structure

```
modular_etl_pipeline/
│
├── config/        # Configuration files (YAML)
├── pipeline/      # ETL modules (cleaning, validation, transformation)
├── utils/         # Logger utilities
├── data/          # Input/output datasets
├── main.py        # Entry point
├── requirements.txt
└── README.md
```


---

## 🧠 Tech Stack
Python  
Pandas  
Scikit-learn  
PyYAML  
Logging (Python built-in)  

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py --config config/netflix.yaml
```


## 🌍 Real-World Use Cases

Automated data preprocessing pipelines in data engineering workflows
Machine learning data preparation systems
ETL automation for analytics platforms
Reusable data cleaning frameworks for scalable systems

## 👩‍💻 Author

Jaahnavi Pasupulety
📍 Hyderabad, India
