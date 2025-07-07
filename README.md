# COVID-19 Data ETL & Visualization Pipeline

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit) [![protected: by-gitleaks-blue](https://img.shields.io/badge/protected%20by-gitleaks-blue)](https://github.com/gitleaks/gitleaks-action) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit) [![Uses the Cookiecutter Data Science project template](https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter)](https://cookiecutter-data-science.drivendata.org/)

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline on global COVID-19 data, sourced from Our World in Data. It includes data cleaning, transformation, and visual analysis using Python.

The goal is to simulate a real-world data engineering + AI scenario where data must be processed before feeding into models or applications.

---

## 🧩 Features

- Extracts COVID-19 case data for selected countries
- Cleans and transforms time-series data (missing values, rolling averages)
- Computes custom metrics (e.g. daily cases per 100k people)
- Creates interactive visualizations using Plotly and Matplotlib

---

## 🛠 Technologies Used

- Python 3.10+
- Pandas, NumPy
- Plotly, Matplotlib, Seaborn
- Jupyter Notebook
- GitHub

---

## 📁 Project Structure

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         covid19_visualization_pipeline and configuration for tools like black
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
└── covid19_visualization_pipeline   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes covid19_visualization_pipeline a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    └── plots.py                <- Code to create visualizations
```

---

## 🚀 How to Run

1. Clone the repo  
2. Install dependencies  
3. Build the processed dataset  
```bash
make requirements
make process
```  
4. Generate the graph figures  
```bash
make graph
```  
5. *(Or)* Open `EDA.ipynb` and run it