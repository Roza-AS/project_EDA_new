# project_EDA_new
# 📊 Automatic EDA Generator

A simple and interactive web app for performing **Exploratory Data Analysis (EDA)** using **Streamlit**. Upload your CSV file and get instant summary statistics, visualizations, and insights.

---

## 🚀 Features

- 📁 Upload any CSV dataset
- 🔍 View shape, column types, and summary statistics
- 🧼 Detect missing values
- 📊 Visualize:
  - Histograms with KDE curves
  - Correlation heatmaps
  - Pair plots
  - Box plots for outlier detection
  - Bar plots for categorical columns
- 🚫 Skips categorical variables with too many categories for clean plotting

---

## 🛠️ Tech Stack

- Python 3.11
- [Streamlit](https://streamlit.io/)
- Pandas
- Seaborn
- Matplotlib
- Poetry (for dependency and virtual environment management)

---

## ⚙️ Installation

Make sure you have Python 3.11 installed.

```bash
# Clone the repo
git clone https://github.com/YOUR-USERNAME/project-eda.git
cd project-eda

# Install Poetry (if not already installed)
curl -sSL https://install.python-poetry.org | python3.11 -

# Use Python 3.11 for this project
poetry env use python3.11

# Install dependencies
poetry install

---
## How to run the app
poetry run streamlit run app.py

---
## ENJOY exploring you data!
