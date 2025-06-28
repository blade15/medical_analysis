<h2>Demographic Data Analyzer</h2>

This project is a Python-based demographic data analyzer that processes and visualizes adult census data to uncover insights on education, income, and more. Built as part of a data analysis challenge, it utilizes Pandas, Seaborn, and Matplotlib to explore categorical and numerical relationships within the dataset.

## 📊 Project Overview

The notebook reads and analyzes a demographic dataset (`adult.data.csv`) and performs the following tasks:

- Calculates statistical metrics such as:
  - Percentage of individuals with a Bachelor's degree
  - Percentage of people earning >50K by education, race, and sex
  - Minimum hours worked and related income analysis
  - Country-wise percentage of high earners
  - Most common occupation for high earners from specific countries

- Visualizes the data using:
  - A **categorical plot** for binary features like `cholesterol`, `gluc`, `smoke`, `alco`, `active`, and `overweight`
  - A **heatmap** of correlations between numeric features

## 🗃️ Dataset

The dataset used is based on the [Adult Census Income dataset](https://archive.ics.uci.edu/ml/datasets/adult) from the UCI Machine Learning Repository.

Make sure to place the dataset in the same directory as the notebook or modify the `pd.read_csv()` path to match your structure.

## 🛠️ Technologies Used

- Python 3.x
- Pandas
- NumPy
- Seaborn
- Matplotlib
