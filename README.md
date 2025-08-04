# project_EDA_new
# Automatic EDA Generator

A simple and interactive web app for performing **Exploratory Data Analysis (EDA)** using **Streamlit**. Upload your CSV file and get instant summary statistics, visualizations, and insights.

---

## Features

-  Upload any CSV dataset
-  View shape, column types, and summary statistics
-  Detect missing values
-  Visualize:
  - Histograms with KDE curves
  - Correlation heatmaps
  - Pair plots
  - Box plots for outlier detection
  - Bar plots for categorical columns
-  Skips categorical variables with too many categories for clean plotting

---

##  Tech Stack

- Python 3.11
- [Streamlit](https://streamlit.io/)
- Pandas
- Seaborn
- Matplotlib
- Poetry (for dependency and virtual environment management)

---

##  Installation

Make sure you have Python 3.11 installed.
---

## Limitations

This works only with CSV files, and the one's who their values do not contain special chars,
due to an encoding problem. Sorry in advance.
---

```bash
Step 1: Clone the repo with GitHub Desktop
Open GitHub Desktop app.

Click File > Clone Repository.

In the URL tab, paste your repo URL, e.g.,
https://github.com/YOUR-USERNAME/project-eda.git

Choose a local path (folder) where you want to save the project.

Click Clone.

Step 2: Open cloned project in PyCharm
Launch PyCharm.

Click Open (or File > Open).

Navigate to the folder where you cloned the repo with GitHub Desktop.

Select the project folder and click Open.

PyCharm will load your project — you can now edit, run, and manage it.

# Install Poetry (if not already installed)
https://install.python-poetry.org | python3.11 -

# Use Python 3.11 for this project
poetry env use python3.11

# Install dependencies
poetry install streamlit pandas seaborn matplotlib

---
## How to run the app
execute the main.py and in the terminal run this line: poetry run streamlit run app.py

---
## ENJOY exploring you data!
