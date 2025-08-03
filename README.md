#  Harvard Art Museum - Paintings ETL & Visualization Project

This project is an end-to-end ETL (Extract, Transform, Load) pipeline focused on the **Paintings** classification from the Harvard Art Museums public API. It collects artwork metadata, processes it, stores it in a MySQL database, and allows interactive exploration using a Streamlit dashboard.



##  Project Overview

**Goal**:  
To demonstrate a real-world data pipeline and visualization app using public API data, focused only on **Paintings** classification.



##  Tools & Technologies

- **Python**
- **Streamlit** (for dashboard)
- **MySQL** (for structured storage)
- **Requests** (for API extraction)
- **Pandas** (for transformation)


## Features

- Fetches over 2400 paintings from the Harvard API
- Inserts data into MySQL across three normalized tables:
  - `artifact_metadata`
  - `artifact_media`
  - `artifact_colors`
- Streamlit UI allows:
  - Data download
  - Visualization
  - SQL-based query and filter



##  Library Used

- Python
- Streamlit
- MySQL
- Pandas & Requests
- Harvard Art Museum API



## To Run

## Install 
```bash
pip install -r requirements.txt

## RUN

python harvard_etl.py

##Launch

streamlit run harvard_app.py

##  Notes
This project uses only the Paintings classification .

It is modular and scalable to support additional classifications in the future.

**Credits
Data Source: Harvard Art Museums API

Project by: Balaji.k  (Data Science Portfolio)
