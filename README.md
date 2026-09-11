# Financial Performance Analytics Dashboard

<img width="1161" height="662" alt="Screenshot 2026-09-10 at 9 46 55 PM" src="https://github.com/user-attachments/assets/4d1dd3bb-8c49-4a89-b125-1ab7ff1ff0dc" />



<img width="640" height="640" alt="Screenshot 2026-09-10 at 9 35 55 PM" src="https://github.com/user-attachments/assets/11de49fa-9b8f-4855-8208-fe3f4aebd1cc" />


An end-to-end financial analytics project analyzing engagement profitability,
budget performance, realization, and receivables using Python, Excel, Power BI,
and DAX.

> **Note:** This is an independent portfolio project built using synthetic data.
> It does not contain actual company or client financial information.

## Project Overview

This project simulates the type of financial performance analysis used to
monitor professional services engagements.

I analyzed 30 engagements and 60 invoices representing approximately $16.4M
in synthetic fees. The goal was to identify profitability issues, engagement
variances, and receivables risks and translate those findings into actionable
business recommendations.

The analysis focused on three questions:

1. Which engagements and practice areas are underperforming financially?
2. How do budget overruns and realization relate to profitability?
3. Where are the largest receivables and collection risks?

## Dashboard

### Case Economics

![Case Economics Dashboard](images/case-economics-dashboard.png)

The Case Economics dashboard monitors engagement performance using:

- Total Fees
- Gross Margin
- Realization
- Budget vs. Actual Hours
- Hours Variance
- Practice Area Performance
- Engagement-Level Performance

### Receivables

![Receivables Dashboard](images/receivables-dashboard.png)

The Receivables dashboard analyzes:

- Average Days Sales Outstanding (DSO)
- DSO by Client
- Outstanding Receivables
- Receivables Aging
- Invoice-Level Collection Risk

## Key Findings

### 1. Healthcare showed the greatest margin pressure

Healthcare engagements generated a **33.8% gross margin**, compared with
**42.0% across the overall portfolio** — an 8.2 percentage-point gap.

Further analysis showed that Healthcare engagements also experienced higher
hours overruns and lower realization, indicating potential margin leakage that
would warrant further investigation.

### 2. Overall realization remained relatively strong

Portfolio realization was approximately **94.4%**, meaning the majority of
the standard value of work performed was captured through fees.

However, lower realization within Healthcare contributed to weaker engagement
economics relative to other practice areas.

### 3. Receivables analysis identified collection risk

Average collection time across paid invoices was approximately **60.4 days**.

The highest-risk client averaged approximately **92 days**, substantially
above the portfolio average and indicating an opportunity for more focused
collection follow-up.

## Recommendations

Based on the analysis, I would recommend:

- Reviewing Healthcare engagements with the largest hours overruns to
  understand the underlying drivers of margin pressure.
- Monitoring realization alongside hours variance to identify potential
  margin leakage earlier in the engagement lifecycle.
- Prioritizing collection activity for high-value and aging receivables,
  particularly clients with collection cycles substantially above the
  portfolio average.
- Establishing recurring engagement-level financial reviews to identify
  profitability and receivables risks before they become material.

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| **Python** | Generated and validated synthetic engagement and invoice data |
| **Pandas / NumPy** | Data generation, transformation, and validation |
| **Excel** | Built an auditable financial model and performed variance analysis |
| **Power BI** | Developed interactive financial performance dashboards |
| **DAX** | Created profitability, realization, variance, and DSO measures |
| **Generative AI** | Drafted financial variance commentary with human validation |

## Financial Metrics

| Metric | Result |
|--------|-------:|
| Total Fees | $16.4M |
| Overall Gross Margin | 42.0% |
| Healthcare Gross Margin | 33.8% |
| Average Realization | 94.4% |
| Average DSO | 60.4 days |

### Metric Definitions

**Gross Margin**  
Measures engagement profitability after accounting for labor costs.

**Realization**  
Measures the percentage of the standard value of work performed that was
captured as actual fees.

**Hours Variance**  
Compares actual hours worked with budgeted hours to identify engagement
overruns or underruns.

**DSO / Average Collection Days**  
Measures the average number of days between invoice issuance and payment for
paid invoices. This project uses an invoice-level collection-days methodology
as a simplified DSO proxy.

## Project Workflow

The project follows an end-to-end analytics workflow:

**Python Data Generation**
→ **Excel Financial Model**
→ **Power BI Analysis**
→ **Financial Insights**
→ **Management Recommendations**

### 1. Data Generation

I created synthetic engagement and invoice datasets in Python to simulate a
professional services portfolio while avoiding the use of confidential
company or client data.

### 2. Financial Modeling

I built an Excel model separating raw data from calculations and summary
reporting.

The model calculates:

- Budget vs. actual hours
- Hours variance
- Budget vs. actual fees
- Fee variance
- Standard-rate value
- Realization
- Labor cost
- Gross profit
- Gross margin
- Invoice aging
- Collection days

### 3. Power BI Reporting

I developed an interactive Power BI dashboard with two primary views:

**Case Economics** — engagement profitability, realization, and budget
performance.

**Receivables** — collection performance, aging, and client-level receivables
risk.

### 4. AI-Assisted Commentary

Generative AI was used to accelerate first-draft financial variance
commentary.

AI-generated conclusions were manually validated against the underlying
financial data, and unsupported causal claims were removed. This maintained
human oversight over the final financial interpretation.

## Repository Structure

```text
financial-performance-analytics/
│
├── data/
│   ├── cases.xlsx
│   └── invoices.xlsx
│
├── python/
│   └── generate_data.py
│
├── excel/
│   └── Financial_Performance_Model.xlsx
│
├── images/
│   ├── case-economics-dashboard.png
│   └── receivables-dashboard.png
│
├── presentation/
│   └── financial-analysis-readout.pdf
│
└── README.md
