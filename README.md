# 🚦 Bengaluru Traffic Analysis Dashboard(2022 - 2024)

## Project Overview

An interactive data analysis & visualization project exploring traffic, average speed and congestion patterns in Bengaluru.  
This project identifies high-congestion hotspots, best-performing routes, and analyzes daily, weather-based, and monthly traffic trends using an interactive Streamlit dashboard provides a comprehensive look at traffic volume, average speeds, and congestion levels, with insights derived from a detailed analysis of traffic data from 2022 to 2024.

The primary goal is to help users understand key factors influencing traffic, such as monthly, yearly and daily seasonal patterns, weather conditions, and the impact of public transport availability.

## Dataset
- **Source:** Kaggle Dataset
- **Dataset Size:** 8000+ Rows x 16 Cols
- **Period Covered:** 2022 - 2024
- **Key Columns:**
  - `Area Name`
  - `Road/Intersection Name`
  - `Traffic Volume`
  - `Average Speed`
  - `Congestion Level`
  - `Weather Conditions`
  - `Day of Week`

## Exploratory Data Analysis (EDA)

- **Data Cleaning:** Handled missing values, duplicates, added new derived columns.
- **Traffic Trends:** Explored by month, weekday/weekend, and area.
- **Congestion Patterns:** Identified bottleneck intersections.
- **Comparative Insights:** Found top 3 most problematic and best performing traffic locations.

Complete EDA is found here: [02_eda_analysis.ipynb](Notebooks/02_eda_analysis.ipynb02_eda_analysis.ipynb)

The final dashboard is the culmination of a multi-step data analysis process:

1.  **Data Cleaning & Preprocessing:** The raw dataset was loaded and cleaned to ensure accuracy. This involved converting the 'Date' column to a proper datetime format, handling any potential missing values, and preparing the data for aggregation.
2.  **Exploratory Data Analysis (EDA):** A thorough analysis was conducted to identify key traffic patterns. This included:
    * Aggregating data to understand average traffic volume and speed by day of the week, weather condition, and public transport usage.
    * Identifying the top roads with the highest traffic and congestion levels.
    * Deriving key insights into how external factors impact traffic flow.
3.  **Data Binning:** The 'Public Transport Usage' column was binned into categorical groups to simplify analysis and visualize its impact more clearly.

## Key Features

The dashboard is organized into several tabs, each presenting a unique analytical insight with interactive elements.

* **Key Metrics:** A persistent header displays crucial overall metrics, including total traffic volume, average speed, and average congestion across all data.
* **High & Low Traffic Locations:** An interactive bar chart allows users to view and compare the top roads with the highest traffic volume and congestion, with a slider to select the number of locations to display.
* **Daily Traffic Volume:** Users can select a specific area and road to view daily traffic patterns, providing granular insights into localized traffic trends.
* **Weather Impact:** This tab features interactive line charts that show how traffic volume and average speed are affected by different weather conditions (e.g., Clear, Rain, Fog). The charts allow for a direct comparison of patterns on different days.
* **Public Transport Impact:** A bar chart visualizes the relationship between public transport usage and traffic metrics, helping to understand its role in managing traffic flow.
* **Traffic Trends Over Time:** An interactive time-series analysis allows users to select a specific year and month to view daily traffic trends, revealing long-term patterns and seasonality.

## Data Source

The analysis is based on a simulated dataset of Bengaluru traffic, containing over 26 million rows of data related to:
* Road/Intersection Name
* Date and Time
* Traffic Volume
* Average Speed (km/h)
* Congestion Level
* Weather Conditions
* Public Transport Usage

## Technical Stack

* **Python:** The core programming language for the project.
* **Streamlit:** Used to build the interactive web dashboard and create the user interface.
* **Pandas:** Essential for data loading, cleaning, manipulation, and aggregation.
* **Plotly Express:** Used for creating professional, interactive, and aesthetically pleasing data visualizations.

## How to Run the App

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)<Your GitHub Username>/<your-repo-name>.git
    cd <your-repo-name>
    ```
2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit app:**
    ```bash
    streamlit run 03_streamlit_dashboard_app.py
    ```

## Author

* **<Your Name>**
* **GitHub:** [github.com/<Your GitHub Username>](https://github.com/<Your GitHub Username>)
* **LinkedIn:** [linkedin.com/in/<Your LinkedIn Profile>](https://www.linkedin.com/in/<Your LinkedIn Profile>)