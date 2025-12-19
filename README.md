# underwriteiq_risk_platform
Portfolio risk analysis and underwriting insights

# Claims & Risk Insights Platform (Power BI + SQL + Python)

A mini analytics product that models insurance policy + claims data into a clean warehouse layer and delivers executive-ready Power BI reporting with risk segmentation insights.

## Business Problem
Legacy reporting often struggles with inconsistent data, unclear KPI definitions, and limited insight into *what drives loss ratio and claims outcomes*. This project demonstrates an end-to-end approach to turn raw policy + claims data into actionable portfolio insights.

## What I Built
- **Warehouse-style data model** (star schema) with clean dimensions + fact tables
- **Power BI dashboards** for portfolio performance, segmentation, and claims ops
- **Python analysis** for trend exploration + baseline frequency/severity modelling
- **Data quality checks** (uniqueness, null thresholds, outlier flags) + KPI definitions

## Dashboard (Power BI)
Pages:
1. Executive Overview (Loss Ratio, Frequency, Severity, Premium)
2. Risk Segmentation (Loss Ratio by product/region/age bands)
3. Claims Operations (Time-to-close, late reporting, claim status)
4. Data Quality & KPI Glossary

> Screenshots: add `/docs/dashboard_overview.png` and `/docs/segmentation.png`

## Data Model
Star schema:
- `fact_claim` (claims, amounts, dates, status)
- `dim_policy`, `dim_policyholder`, `dim_vehicle`, `dim_date` (+ optional `dim_geography`)

> Schema diagram: add `/docs/schema.png`

## Key KPIs (Definitions)
- **Claim Frequency** = Claims / Exposure (policy-years)
- **Average Severity** = Total Claim Amount / Claims
- **Loss Ratio** = Total Claim Amount / Earned Premium
- **Pure Premium** = Total Claim Amount / Exposure
- **Late Reporting Rate** = % claims reported > X days after loss date

## Tech Stack
- Python (pandas, numpy, scikit-learn optional)
- SQL (T-SQL / Postgres supported)
- Power BI (data model + DAX)
- Git (version control)

## How to Run Locally
1) Create a virtual env and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
