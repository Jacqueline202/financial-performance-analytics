import pandas as pd
import numpy as np
from pathlib import Path

# Reproducibility
np.random.seed(42)

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# Create data directory if it doesn't exist
DATA_DIR.mkdir(exist_ok=True)

# -----------------------------
# Business dimensions
# -----------------------------

practice_areas = [
    "Financial Services",
    "Healthcare",
    "Consumer",
    "Technology"
]

clients = [
    "Alpha Health",
    "Beta Bank",
    "Gamma Energy",
    "Delta Retail",
    "Epsilon Tech",
    "Zeta Financial",
    "Eta Consumer",
    "Theta Health"
]

# -----------------------------
# Generate case IDs
# -----------------------------

num_cases = 30

case_ids = [
    f"C{i:03d}"
    for i in range(1, num_cases + 1)
]

print("Number of cases:", len(case_ids))
print("First five case IDs:", case_ids[:5])

# -----------------------------
# Create case-level DataFrame
# -----------------------------

case_clients = np.random.choice(
    clients,
    num_cases
)

# Guarantee Alpha Health has multiple cases
case_clients[:4] = "Alpha Health"

cases = pd.DataFrame({
    "Case_ID": case_ids,
    "Client": case_clients,
    "Practice_Area": np.random.choice(
        practice_areas,
        num_cases
    )
})

# -----------------------------
# Generate engagement dates
# -----------------------------

start_dates = pd.to_datetime(
    np.random.choice(
        pd.date_range("2025-01-01", "2026-06-30"),
        num_cases
    )
)

cases["Start_Date"] = start_dates

# Project duration between 60 and 180 days
durations = np.random.randint(60, 181, num_cases)

cases["End_Date"] = (
    cases["Start_Date"] +
    pd.to_timedelta(durations, unit="D")
)

print("\nFirst five cases:")
print(cases.head())

print("\nDate range:")
print("Earliest start:", cases["Start_Date"].min())
print("Latest end:", cases["End_Date"].max())

# -----------------------------
# Generate budgeted hours
# -----------------------------

cases["Budget_Hours"] = np.random.randint(
    500,
    2001,
    num_cases
)

# Base actual-hour variance
hour_variance = np.random.normal(
    loc=0.05,
    scale=0.08,
    size=num_cases
)

cases["Actual_Hours"] = (
    cases["Budget_Hours"] *
    (1 + hour_variance)
).round().astype(int)

# -----------------------------
# Create Healthcare overruns
# -----------------------------

healthcare_mask = cases["Practice_Area"] == "Healthcare"

cases.loc[healthcare_mask, "Actual_Hours"] = (
    cases.loc[healthcare_mask, "Budget_Hours"] *
    np.random.uniform(
        1.15,
        1.30,
        healthcare_mask.sum()
    )
).round().astype(int)

# -----------------------------
# Validate hours performance
# -----------------------------

cases["Hours_Variance"] = (
    (cases["Actual_Hours"] - cases["Budget_Hours"])
    / cases["Budget_Hours"]
)

print("\nAverage hours variance by practice area:")
hours_summary = (
    cases.groupby("Practice_Area")["Hours_Variance"]
    .mean()
    .sort_values(ascending=False)
)

print(
    hours_summary.map(lambda x: f"{x:.1%}")
)

print("\nHealthcare cases:")
print(
    cases[cases["Practice_Area"] == "Healthcare"][
        ["Case_ID", "Client", "Budget_Hours", "Actual_Hours", "Hours_Variance"]
    ]
)

# -----------------------------
# Standard billing rates
# -----------------------------

standard_rates = {
    "Financial Services": 475,
    "Healthcare": 450,
    "Consumer": 425,
    "Technology": 500
}

cases["Standard_Rate"] = cases["Practice_Area"].map(
    standard_rates
)

# -----------------------------
# Cost rates
# -----------------------------

cost_rates = {
    "Financial Services": 250,
    "Healthcare": 260,
    "Consumer": 235,
    "Technology": 270
}

cases["Cost_Rate"] = cases["Practice_Area"].map(
    cost_rates
)

# -----------------------------
# Standard Rate Value
# -----------------------------

cases["Standard_Rate_Value"] = (
    cases["Actual_Hours"] *
    cases["Standard_Rate"]
)

# -----------------------------
# Budgeted fees
# -----------------------------

cases["Budget_Fee"] = (
    cases["Budget_Hours"] *
    cases["Standard_Rate"] *
    np.random.uniform(0.95, 1.02, num_cases)
).round(-2)

# -----------------------------
# Actual fees
# -----------------------------

fee_realization = np.random.uniform(
    0.88,
    1.02,
    num_cases
)

cases["Actual_Fee"] = (
    cases["Standard_Rate_Value"] *
    fee_realization
).round(-2)

# -----------------------------
# Lower Healthcare realization
# -----------------------------

cases.loc[healthcare_mask, "Actual_Fee"] = (
    cases.loc[healthcare_mask, "Standard_Rate_Value"] *
    np.random.uniform(
        0.82,
        0.92,
        healthcare_mask.sum()
    )
).round(-2)

# -----------------------------
# Validate realization
# -----------------------------

cases["Realization"] = (
    cases["Actual_Fee"] /
    cases["Standard_Rate_Value"]
)

print("\nAverage realization by practice area:")
realization_summary = (
    cases.groupby("Practice_Area")["Realization"]
    .mean()
    .sort_values()
)

print("\nAverage realization by practice area:")
print(
    realization_summary.map(lambda x: f"{x:.1%}")
)

# -----------------------------
# Labor cost
# -----------------------------

cases["Labor_Cost"] = (
    cases["Actual_Hours"] *
    cases["Cost_Rate"]
).round(-2)

# -----------------------------
# Gross profit
# -----------------------------

cases["Gross_Profit"] = (
    cases["Actual_Fee"] -
    cases["Labor_Cost"]
).round(-2)

# -----------------------------
# Gross margin
# -----------------------------

cases["Gross_Margin"] = (
    cases["Gross_Profit"] /
    cases["Actual_Fee"]
)

print("\nAverage gross margin by practice area:")

margin_summary = (
    cases.groupby("Practice_Area")["Gross_Margin"]
    .mean()
    .sort_values()
)

print(
    margin_summary.map(lambda x: f"{x:.1%}")
)

# -----------------------------
# Fee variance
# -----------------------------

cases["Fee_Variance"] = (
    (cases["Actual_Fee"] - cases["Budget_Fee"])
    / cases["Budget_Fee"]
)

print("\nHealthcare financial performance:")

print(
    cases[cases["Practice_Area"] == "Healthcare"][
        [
            "Case_ID",
            "Client",
            "Budget_Hours",
            "Actual_Hours",
            "Hours_Variance",
            "Actual_Fee",
            "Labor_Cost",
            "Gross_Profit",
            "Gross_Margin"
        ]
    ]
)

print("\nAverage fee variance by practice area:")

fee_summary = (
    cases.groupby("Practice_Area")["Fee_Variance"]
    .mean()
    .sort_values()
)

print(
    fee_summary.map(lambda x: f"{x:.1%}")
)

print("\nCase dataset:")
print(cases.head())
print("\nColumns:")
print(cases.columns.tolist())

# -----------------------------
# Generate invoice data
# -----------------------------

num_invoices = 60

invoice_ids = [
    f"INV{i:03d}"
    for i in range(1, num_invoices + 1)
]
# Randomly assign most invoices to existing cases
invoice_case_ids = np.random.choice(
    cases["Case_ID"],
    num_invoices
)

# Guarantee Alpha Health receives invoices
alpha_case_ids = cases.loc[
    cases["Client"] == "Alpha Health",
    "Case_ID"
].values

invoice_case_ids[:8] = np.random.choice(
    alpha_case_ids,
    8
)

invoices = pd.DataFrame({
    "Invoice_ID": invoice_ids,
    "Case_ID": invoice_case_ids
})

# Bring the client information into the invoice table
invoices = invoices.merge(
    cases[["Case_ID", "Client"]],
    on="Case_ID",
    how="left"
)

print("\nFirst five invoices:")
print(invoices.head())

# -----------------------------
# Generate invoice dates
# -----------------------------

invoice_case_dates = cases[
    ["Case_ID", "Start_Date", "End_Date"]
]

invoices = invoices.merge(
    invoice_case_dates,
    on="Case_ID",
    how="left"
)

# Invoice dates occur during or shortly after the engagement
invoice_offsets = np.random.randint(
    0,
    31,
    num_invoices
)

invoices["Invoice_Date"] = (
    invoices["Start_Date"] +
    pd.to_timedelta(invoice_offsets, unit="D")
)

# -----------------------------
# Generate invoice amounts
# -----------------------------

case_fee_lookup = cases[
    ["Case_ID", "Actual_Fee"]
]

invoices = invoices.merge(
    case_fee_lookup,
    on="Case_ID",
    how="left"
)

invoices["Amount"] = (
    invoices["Actual_Fee"] /
    2 *
    np.random.uniform(0.90, 1.10, num_invoices)
).round(-2)

# -----------------------------
# Generate payment dates
# -----------------------------

payment_days = np.random.randint(
    15,
    76,
    num_invoices
)

invoices["Payment_Date"] = (
    invoices["Invoice_Date"] +
    pd.to_timedelta(payment_days, unit="D")
)

# -----------------------------
# Create Alpha Health payment delay
# -----------------------------

alpha_mask = invoices["Client"] == "Alpha Health"

invoices.loc[alpha_mask, "Payment_Date"] = (
    invoices.loc[alpha_mask, "Invoice_Date"] +
    pd.to_timedelta(
        np.random.randint(
            65,
            121,
            alpha_mask.sum()
        ),
        unit="D"
    )
)

# -----------------------------
# Create unpaid invoices
# -----------------------------

unpaid_mask = np.random.random(num_invoices) < 0.15

invoices.loc[unpaid_mask, "Payment_Date"] = pd.NaT

print("\nInvoice summary:")
print("Total invoices:", len(invoices))
print(
    "Unpaid invoices:",
    invoices["Payment_Date"].isna().sum()
)

print("\nAverage payment days by client:")

paid_invoices = invoices[
    invoices["Payment_Date"].notna()
].copy()

paid_invoices["Payment_Days"] = (
    paid_invoices["Payment_Date"] -
    paid_invoices["Invoice_Date"]
).dt.days

client_payment_summary = (
    paid_invoices.groupby("Client")["Payment_Days"]
    .mean()
    .sort_values(ascending=False)
)

print(client_payment_summary.round(1))

# -----------------------------
# Payment status
# -----------------------------

invoices["Payment_Status"] = np.where(
    invoices["Payment_Date"].isna(),
    "Unpaid",
    "Paid"
)

# -----------------------------
# Payment days
# -----------------------------

invoices["Payment_Days"] = (
    invoices["Payment_Date"] -
    invoices["Invoice_Date"]
).dt.days

# -----------------------------
# Aging bucket
# -----------------------------

invoices["Aging_Bucket"] = np.select(
    [
        invoices["Payment_Days"].isna(),
        invoices["Payment_Days"] <= 30,
        invoices["Payment_Days"] <= 60,
        invoices["Payment_Days"] <= 90
    ],
    [
        "Unpaid",
        "0-30",
        "31-60",
        "61-90"
    ],
    default="90+"
)

print("\nInvoice aging distribution:")
print(
    invoices["Aging_Bucket"]
    .value_counts()
    .sort_index()
)

print("\nPayment status:")
print(
    invoices["Payment_Status"]
    .value_counts()
)

# -----------------------------
# Prepare raw case data
# -----------------------------

raw_cases = cases[
    [
        "Case_ID",
        "Client",
        "Practice_Area",
        "Start_Date",
        "End_Date",
        "Budget_Hours",
        "Actual_Hours",
        "Standard_Rate",
        "Cost_Rate",
        "Budget_Fee",
        "Actual_Fee"
    ]
].copy()


# -----------------------------
# Prepare raw invoice data
# -----------------------------

raw_invoices = invoices[
    [
        "Invoice_ID",
        "Case_ID",
        "Client",
        "Invoice_Date",
        "Amount",
        "Payment_Date"
    ]
].copy()

# -----------------------------
# Export raw data
# -----------------------------

cases_path = DATA_DIR / "cases.xlsx"
invoices_path = DATA_DIR / "invoices.xlsx"

raw_cases.to_excel(
    cases_path,
    index=False
)

raw_invoices.to_excel(
    invoices_path,
    index=False
)

print("\nFiles created:")
print(cases_path)
print(invoices_path)

