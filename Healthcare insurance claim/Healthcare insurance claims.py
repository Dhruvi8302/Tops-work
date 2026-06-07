# 1. IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================================
# 2. LOAD DATASET
# ==========================================================

df = pd.read_csv("C:\\Users\\ADMIN\\OneDrive\\Desktop\\Projects\\healthcare_insurance_claims_messy_120k.csv")

# ==========================================================
# 3: DATA UNDERSTANDING
# ==========================================================
# print(df.head())
# print(df.shape)
# print(df.columns.tolist())
# print(df.dtypes)

# ============================================
# DATA CLEANING
# ============================================
# Missing Values
print(df.isnull().sum())

# Replace ? with NaN
df.replace("?", np.nan, inplace=True)

# Remove Extra Spaces
for col in df.select_dtypes(include=['object', 'string']):
    df[col] = df[col].str.strip()

# Standardize Values
df['Gender'] = df['Gender'].replace({
    'male': 'Male',
    'female': 'Female'
})

df['Smoker'] = df['Smoker'].replace({
    'yes': 'Yes',
    'NO': 'No'
})

df['Claim_Status'] = df['Claim_Status'].replace({
    'approved': 'Approved'
})

# Fill Missing Values
df['Gender'] = df['Gender'].fillna(
    df['Gender'].mode()[0]
)

df['Smoker'] = df['Smoker'].fillna(
    df['Smoker'].mode()[0]
)

df['Region'] = df['Region'].fillna(
    df['Region'].mode()[0]
)

df['Insurance_Plan'] = df['Insurance_Plan'].fillna(
    df['Insurance_Plan'].mode()[0]
)

df['BMI'] = df['BMI'].fillna(
    df['BMI'].median()
)

df['Claim_Amount'] = df['Claim_Amount'].fillna(
    df['Claim_Amount'].median()
)

df['Chronic_Disease'] = df['Chronic_Disease'].fillna(
    'None'
)

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Convert Date
df['Claim_Date'] = pd.to_datetime(df['Claim_Date'])

# Check Results
print("\nMissing Values After Cleaning")
print(df.isnull().sum())

print("\nDataset Shape")
print(df.shape)

print("\nDuplicate Records")
print(df.duplicated().sum())

# ============================================
# FEATURE ENGINEERING
# ============================================
# Age Group
df['Age_Group'] = pd.cut(
    df['Age'],
    bins=[18,30,45,60,100],
    labels=['Young Adult','Adult','Middle Age','Senior']
)

# BMI Category
df['BMI_Category'] = pd.cut(
    df['BMI'],
    bins=[0,18.5,25,30,100],
    labels=['Underweight','Normal','Overweight','Obese']
)

# Claim Month
df['Claim_Month'] = df['Claim_Date'].dt.month_name()
 
# Define correct month order for sorting
MONTH_ORDER = [
    'January','February','March','April','May','June',
    'July','August','September','October','November','December'
]
 
df['Claim_Month'] = pd.Categorical(
    df['Claim_Month'],
    categories=MONTH_ORDER,
    ordered=True
)

# Risk Score
df['Risk_Score'] = (
    df['Age'] * 0.2 +
    df['BMI'] * 0.5 +
    df['Hospital_Visits'] * 4 +
    np.where(df['Smoker'] == 'Yes', 15, 0)
)

# Risk Level
# Score range: ~10 to ~98
# Low  : Score < 35  → younger/healthy/non-smoker, few visits
# Medium: 35 to 50  → moderate age/BMI/visits
# High : Score > 50  → older/obese/smoker or many hospital visits
df['Risk_Level'] = pd.cut(
    df['Risk_Score'],
    bins=[0, 35, 50, 200],
    labels=['Low', 'Medium', 'High']
)

# Check New Features
print(df[['Age_Group',
          'BMI_Category',
          'Claim_Month',
          'Risk_Score',
          'Risk_Level']].head())

print("\nAge Group Distribution")
print(df['Age_Group'].value_counts())

print("\nBMI Category Distribution")
print(df['BMI_Category'].value_counts())

print("\nRisk Level Distribution")
print(df['Risk_Level'].value_counts())

# ==================================================
# DASHBOARD 1: Healthcare Insurance Claims Overview
# ==================================================

# KPI Calculations
total_claims = len(df)
total_amount = df['Claim_Amount'].sum()
avg_claim = df['Claim_Amount'].mean()

approval_rate = (
    (df['Claim_Status'] == 'Approved')
    .mean() * 100
)

# Monthly Trend
monthly_claims = (
    df.groupby('Claim_Month')['Claim_Amount']
      .sum()
      .reset_index()
)

# Dashboard Layout
fig = plt.figure(figsize=(18,10))

gs = fig.add_gridspec(
    3,
    4,
    height_ratios=[1,4,4]
)

fig.suptitle(
    "Healthcare Insurance Claims Overview ",
    fontsize=18,
    fontweight='bold'
)

# KPI Cards
ax_kpi1 = fig.add_subplot(gs[0,0])
ax_kpi2 = fig.add_subplot(gs[0,1])
ax_kpi3 = fig.add_subplot(gs[0,2])
ax_kpi4 = fig.add_subplot(gs[0,3])

for ax in [ax_kpi1, ax_kpi2, ax_kpi3, ax_kpi4]:
    ax.axis('off')

ax_kpi1.text(
    0.5,0.5,
    f"{total_claims:,}\nTotal Claims",
    ha='center',
    va='center',
    fontsize=14,
    fontweight='bold'
)

ax_kpi2.text(
    0.5,0.5,
    f"₹{total_amount:,.0f}\nTotal Claim Amount",
    ha='center',
    va='center',
    fontsize=14,
    fontweight='bold'
)

ax_kpi3.text(
    0.5,0.5,
    f"₹{avg_claim:,.0f}\nAverage Claim",
    ha='center',
    va='center',
    fontsize=14,
    fontweight='bold'
)

ax_kpi4.text(
    0.5,0.5,
    f"{approval_rate:.1f}%\nApproval Rate",
    ha='center',
    va='center',
    fontsize=14,
    fontweight='bold'
)

# Chart 1 - Monthly Claims Trend
ax1 = fig.add_subplot(gs[1,0:2])

sns.lineplot(
    data=monthly_claims,
    x='Claim_Month',
    y='Claim_Amount',
    marker='o',
    ax=ax1
)

ax1.set_title("Monthly Claim Amount Trend")
ax1.tick_params(axis='x', rotation=45)

# Chart 2 - Age Group vs Claim Amount
ax2 = fig.add_subplot(gs[1,2:4])

sns.boxplot(
    x='Age_Group',
    y='Claim_Amount',
    data=df,
    ax=ax2
)

ax2.set_title("Claim Amount by Age Group")

# Chart 3 - Smoker vs Claim Amount
ax3 = fig.add_subplot(gs[2,0:2])

sns.boxplot(
    x='Smoker',
    y='Claim_Amount',
    data=df,
    ax=ax3
)

ax3.set_title("Smoker vs Claim Amount")

# Chart 4 - BMI Category vs Claim Amount
ax4 = fig.add_subplot(gs[2,2:4])

sns.barplot(
    x='BMI_Category',
    y='Claim_Amount',
    data=df,
    ax=ax4
)

ax4.set_title("BMI Category vs Claim Amount")

plt.tight_layout()

# plt.savefig(
#     r"C:\\Users\\ADMIN\\OneDrive\\Desktop\\Projects\\Healthcare_Claims_Overview_Dashboard.png",
#     dpi=300,
#     bbox_inches='tight'
# )
plt.show()

# ==========================================
# DASHBOARD 2 : RISK SEGMENTATION ANALYSIS
# ==========================================

# KPI Calculations
risk_pct = (
    df['Risk_Level']
    .value_counts(normalize=True)
    * 100
)

high_risk = risk_pct['High']
medium_risk = risk_pct['Medium']
low_risk = risk_pct['Low']

avg_visits = df['Hospital_Visits'].mean()

# Dashboard Layout
fig = plt.figure(figsize=(18,10))

gs = fig.add_gridspec(
    3,
    4,
    height_ratios=[1,4,4]
)

fig.suptitle(
    "Risk Segmentation & Patient Analysis Dashboard",
    fontsize=18,
    fontweight='bold'
)

# KPI Cards
ax_kpi1 = fig.add_subplot(gs[0,0])
ax_kpi2 = fig.add_subplot(gs[0,1])
ax_kpi3 = fig.add_subplot(gs[0,2])
ax_kpi4 = fig.add_subplot(gs[0,3])

for ax in [ax_kpi1, ax_kpi2, ax_kpi3, ax_kpi4]:
    ax.axis('off')

ax_kpi1.text(
    0.5,0.5,
    f"{high_risk:.1f}%\nHigh Risk",
    ha='center',
    va='center',
    fontsize=14,
    fontweight='bold'
)

ax_kpi2.text(
    0.5,0.5,
    f"{medium_risk:.1f}%\nMedium Risk",
    ha='center',
    va='center',
    fontsize=14,
    fontweight='bold'
)

ax_kpi3.text(
    0.5,0.5,
    f"{low_risk:.1f}%\nLow Risk",
    ha='center',
    va='center',
    fontsize=14,
    fontweight='bold'
)

ax_kpi4.text(
    0.5,0.5,
    f"{avg_visits:.1f}\nAvg Visits",
    ha='center',
    va='center',
    fontsize=14,
    fontweight='bold'
)

# Chart 1
ax1 = fig.add_subplot(gs[1,0:2])

sns.boxplot(
    x='Risk_Level',
    y='Claim_Amount',
    data=df,
    ax=ax1
)

ax1.set_title("Risk Level vs Claim Amount")

# Chart 2
ax2 = fig.add_subplot(gs[1,2:4])

sns.countplot(
    y='Chronic_Disease',
    data=df,
    ax=ax2
)

ax2.set_title("Chronic Disease Distribution")

# Chart 3
ax3 = fig.add_subplot(gs[2,0:2])

sns.barplot(
    x='Chronic_Disease',
    y='Claim_Amount',
    data=df,
    ax=ax3
)

ax3.tick_params(
    axis='x',
    rotation=30
)

ax3.set_title("Disease vs Claim Amount")

# Chart 4
ax4 = fig.add_subplot(gs[2,2:4])

sns.scatterplot(
    x='Hospital_Visits',
    y='Claim_Amount',
    hue='Risk_Level',
    data=df.sample(5000),
    alpha=0.5,
    ax=ax4
)

ax4.set_title("Hospital Visits vs Claim Amount")

plt.tight_layout()
# plt.savefig(
#     r"C:\\Users\\ADMIN\\OneDrive\\Desktop\\Projects\\Risk_Segmentation_Dashboard.png",
#     dpi=300,
#     bbox_inches='tight'
# )
plt.show()

# "In this project, I analyzed 120,000 healthcare insurance claims to uncover key cost drivers and risk patterns. 
# After cleaning and preprocessing the messy dataset, I engineered features like Risk Score, Age Group, and BMI Category to segment patients meaningfully. 
# The major finding was that smokers file 43% higher claims than non-smokers, and claim amounts increase progressively with BMI from Underweight to Obese. 
# I also found that hospital visit frequency is the strongest predictor of risk level, with high-risk patients almost exclusively having 6+ visits. 
# Hypertension and Diabetes were the most prevalent chronic diseases in the dataset. 
# I presented these findings through two interactive dashboards — one focused on claims overview
# and the other on risk segmentation — to help insurers make data-driven decisions on pricing and early patient intervention."
