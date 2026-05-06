# 📊 PrimeMart Nigeria Ltd. — Business Analysis & Executive Dashboard

> **CIPS Level 3 Advanced Certificate in Procurement & Supply Operations**  
> Business Analysis Coursework Project | Faruk M. Adio & Elijah

---

## 🗂️ Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Dataset](#dataset)
- [Analysis Notebook](#analysis-notebook)
- [Executive Dashboard](#executive-dashboard)
- [Key Insights](#key-insights)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Authors](#authors)

---

## Project Overview

This repository contains the full business analysis conducted on **PrimeMart Nigeria Limited**, a fictional Nigerian retail company, as part of the **CIPS Level 3 Advanced Certificate in Procurement & Supply Operations** coursework.

The project applies core business analysis and data analytics techniques to a multi-year sales dataset (2023–2026), covering revenue performance, regional market dynamics, product category trends, and supply chain insights — all presented through an interactive executive dashboard.

**Core business questions addressed:**
- Which products and categories drive the most revenue?
- How does performance vary across Nigerian regions?
- What are the quarterly and monthly revenue trends?
- Where are the procurement and supply opportunities?

---

## Repository Structure

```
CIPS/
│
├── PrimeMartNig.csv                       # Core sales dataset
├── PrimeMart_Nigeria_Sales_2023_2026.csv  # Extended dataset (2023–2026)
├── PrimeMartNigLtd2.ipynb                 # Main analysis notebook
└── dashboard3.py                          # Streamlit executive dashboard
```

---

## Dataset

Two CSV datasets are included, covering transactional retail sales data for PrimeMart Nigeria Ltd.

| Field | Description |
|---|---|
| `Transaction_ID` | Unique identifier per transaction |
| `Date` | Transaction date |
| `Year` | Fiscal year |
| `Region` | Nigerian region (e.g. Lagos, Abuja, Port Harcourt) |
| `Category` | Product category |
| `Product` | Specific product name |
| `Units_Sold` | Quantity sold per transaction |
| `Sales_NGN` | Revenue in Nigerian Naira (₦) |

The extended dataset (`PrimeMart_Nigeria_Sales_2023_2026.csv`) spans **2023 to 2026**, enabling multi-year trend analysis.

---

## Analysis Notebook

**`PrimeMartNigLtd2.ipynb`** is the primary analytical workbook (7,199 lines). It covers:

- **Data Cleaning & Preprocessing** — date parsing, handling nulls, type normalization
- **Exploratory Data Analysis (EDA)** — descriptive statistics, distributions, outlier detection
- **Revenue Analysis** — total, average, and segmented performance metrics
- **Product Performance** — top products by revenue and volume
- **Regional Breakdown** — comparative analysis across Nigerian regions
- **Category Trends** — market share and growth by product category
- **Time Series Analysis** — monthly and quarterly revenue trajectory
- **Procurement Insights** — demand patterns relevant to supply chain decision-making

To run the notebook:

```bash
jupyter notebook PrimeMartNigLtd2.ipynb
```

---

## Executive Dashboard

**`dashboard3.py`** is an interactive Streamlit dashboard built with Plotly, presenting the analysis in an executive-ready format.

### Dashboard Sections

| Section | Description |
|---|---|
| **KPI Cards** | Total Revenue (₦), Total Units Sold, Avg. Order Value, Total Transactions |
| **I. Performance Hotspots** | Top 10 Products by Revenue (bar chart) + Region × Category Revenue Heatmap |
| **II. Market Segmentation** | Regional Revenue Contribution (bar) + Category Market Share (pie) |
| **III. Temporal Trajectory** | Monthly aggregated sales line chart with quarterly benchmark markers |
| **Audit Trail** | Raw transactional data viewer (first 100 rows) |

### Sidebar Filters

- **Year** — filter by one or more fiscal years
- **Region** — filter by specific Nigerian regions

### Run the Dashboard

```bash
# Install dependencies
pip install streamlit pandas plotly

# Launch the dashboard
streamlit run dashboard3.py
```

The dashboard will open at `http://localhost:8501` in your browser.

---

## Key Insights

> *(Generated from the analysis — representative findings)*

- Revenue is **heavily concentrated** in a small number of product lines, suggesting procurement prioritisation opportunities.
- Certain **regions significantly outperform** others, indicating potential for targeted supply chain investment.
- Sales exhibit **clear quarterly seasonality**, with revenue peaks aligning to specific periods — useful for demand forecasting.
- Category-level heatmaps reveal **underperforming region-category combinations** that represent growth or rationalisation opportunities.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.x** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **Plotly** | Interactive data visualisation |
| **Streamlit** | Dashboard framework |
| **Jupyter Notebook** | Exploratory analysis environment |

---

## Getting Started

### Prerequisites

Ensure you have Python 3.8 or above installed.

### Installation

```bash
# Clone the repository
git clone https://github.com/FK-adio/CIPS.git
cd CIPS

# Install required packages
pip install pandas plotly streamlit jupyter
```

### Usage

**For the analysis notebook:**
```bash
jupyter notebook PrimeMartNigLtd2.ipynb
```

**For the interactive dashboard:**
```bash
streamlit run dashboard3.py
```

> **Note:** Ensure `PrimeMartNig.csv` is present in the same directory as `dashboard3.py` before launching the dashboard.

---

## Authors

**Faruk M. Adio**  
Management Trainee — Nigeria LNG Limited (NLNG)  
CIPS Level 3 | Member, Nigerian Society of Engineers (NSE)  
📍 Port Harcourt, Nigeria  
🔗 [GitHub: FK-adio](https://github.com/FK-adio)

**Elijah** *(Co-author)*  
CIPS Level 3 Coursework Partner

---

## Academic Context

This project was submitted as part of the **CIPS Level 3 Advanced Certificate in Procurement & Supply Operations**. It demonstrates applied competencies in:

- Business data analysis and interpretation
- Procurement performance measurement
- Supplier and market intelligence
- Data-driven decision support for supply chain management

---

*© 2024–2026 Faruk M. Adio & Elijah. Academic use only.*
