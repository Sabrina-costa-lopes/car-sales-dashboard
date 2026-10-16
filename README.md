# Car Sales Dashboard

## About the Project

A web application built with Python, Pandas, Plotly Express, and Streamlit to explore used car advertisement data.

This project focuses on identifying patterns in vehicle prices and characteristics through interactive visualizations and exploratory data analysis (EDA).

## Live Dashboard

Explore the interactive application:

[**Open the Car Sales Dashboard**](https://car-sales-dashboard-1cvj.onrender.com/)

## Features

- **Price Distribution:** Explore the distribution of vehicle prices using an interactive histogram.
- **Price vs. Model Year:** Analyze the relationship between vehicle model year and price using an interactive scatter plot.
- **Interactive Data Exploration:** Explore a dataset containing 51,525 vehicle advertisements.

## Technologies Used

- **Python:** Programming language.
- **Pandas:** Data manipulation and analysis.
- **Plotly Express:** Interactive data visualization.
- **Streamlit:** Web application development.
- **Jupyter Notebook:** Exploratory data analysis (EDA).

## Project Structure

```text
Car-sales-dashboard/
├── .streamlit/
│   └── config.toml
├── notebooks/
│   └── EDA.ipynb
├── app.py
├── vehicles.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## Running the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Sabrina-costa-lopes/car-sales-dashboard.git
```

### 2. Navigate to the project directory

```bash
cd car-sales-dashboard
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m streamlit run app.py
```

The application will be available at the local URL displayed in your terminal, usually `http://localhost:8501`.

## Project Goals

- Practice exploratory data analysis.
- Identify patterns and relationships in used car advertisement data.
- Create interactive data visualizations.
- Develop and deploy a web application using Python.
- Build practical skills in data analysis and data presentation.