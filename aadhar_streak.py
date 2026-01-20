# -----------------------------------------
# Aadhaar Drishti Visualization Code Bundle
# UIDAI Hackathon 2026
# -----------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# ✅ Common setup
plt.style.use('seaborn-v0_8-whitegrid')

# -----------------------------------------
# 1️⃣ STATE-WISE DATA (Example: Replace with yours)
# -----------------------------------------

data_up = {
    'District': ['Bahraich','Sitapur','Agra','Bareilly','Aligarh','Lucknow','Hardoi','Kanpur Nagar','Kheri','Shahjahanpur'],
    'Enrolments': [23000,21000,44000,37000,32000,43000,19000,44000,27000,21000],
    'Centres': [90,80,314,180,206,275,85,300,100,100]
}

data_mh = {
    'District': ['Thane','Pune','Nashik','Mumbai Suburban','Aurangabad','Jalgaon','Dhule','Solapur','Nanded','Nagpur'],
    'Enrolments': [44000,32000,22000,18000,17000,14000,13000,12500,12000,15000],
    'Centres': [150,300,145,200,100,100,60,100,80,120]
}

data_tn = {
    'District': ['Chennai','Coimbatore','Madurai','Salem','Tiruchirappalli','Tirunelveli','Kancheepuram','Tiruvallur','Vellore','Cuddalore'],
    'Enrolments': [10043,8986,9938,10249,9932,9675,13050,11435,9633,8630],
    'Centres': [334,224,197,206,145,140,161,140,146,120]
}

# Convert to DataFrames
df_up = pd.DataFrame(data_up)
df_mh = pd.DataFrame(data_mh)
df_tn = pd.DataFrame(data_tn)

# -----------------------------------------
# 2️⃣ GRAPH 1 – Bar Chart (District Enrolments vs Centres)
# -----------------------------------------

def plot_state(df, state_name):
    plt.figure(figsize=(13,7))
    w = 0.4
    x = np.arange(len(df))
    plt.bar(x, df['Enrolments'], width=w, label='Total Enrolments', color='#1f77b4')
    plt.bar(x+w, df['Centres'], width=w, label='Total Centres', color='#ff7f0e')
    plt.xticks(x + w/2, df['District'], rotation=45, ha='right')
    plt.title(f'Comparison: Total Aadhaar Enrolments vs Centres ({state_name})', fontsize=14, weight='bold')
    plt.ylabel('Count')
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

plot_state(df_up, "Uttar Pradesh")
plot_state(df_mh, "Maharashtra")
plot_state(df_tn, "Tamil Nadu")

# -----------------------------------------
# 3️⃣ GRAPH 2 – Per-Centre Workload (Bar)
# -----------------------------------------

def workload_chart(df, state):
    df['Workload'] = df['Enrolments'] / df['Centres']
    plt.figure(figsize=(12,6))
    sns.barplot(x='District', y='Workload', data=df, palette='coolwarm')
    plt.title(f'Per-Centre Workload (Enrolments per Centre) – {state}', fontsize=14, weight='bold')
    plt.ylabel('Enrolments per Centre')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

workload_chart(df_up, "Uttar Pradesh")
workload_chart(df_mh, "Maharashtra")
workload_chart(df_tn, "Tamil Nadu")

# -----------------------------------------
# 4️⃣ GRAPH 3 – Heatmap (Monthly Trends)
# -----------------------------------------
# Example dummy dataset – replace with real monthly enrolment totals

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
districts = ['Thane','Pune','Nashik','Aurangabad','Mumbai']
np.random.seed(42)
data = np.random.randint(800, 2500, size=(len(districts), len(months)))
df_heat = pd.DataFrame(data, index=districts, columns=months)

plt.figure(figsize=(10,6))
sns.heatmap(df_heat, cmap='YlGnBu', annot=True, fmt='d')
plt.title('Monthly Aadhaar Enrolment Trends – Example (Maharashtra)', fontsize=14, weight='bold')
plt.ylabel('District')
plt.xlabel('Month')
plt.tight_layout()
plt.show()

# -----------------------------------------
# 5️⃣ GRAPH 4 – 3-State Comparison (Efficiency)
# -----------------------------------------

states = ['Maharashtra', 'Uttar Pradesh', 'Tamil Nadu']
enrolments = [44000, 44000, 13050]
centres = [150, 300, 334]
workload = [e/c for e,c in zip(enrolments, centres)]

df_cmp = pd.DataFrame({'State': states, 'Enrolments': enrolments, 'Centres': centres, 'Workload': workload})

plt.figure(figsize=(10,6))
sns.barplot(x='State', y='Workload', data=df_cmp, palette='viridis')
plt.title('Average Enrolments per Centre – State Comparison', fontsize=14, weight='bold')
plt.ylabel('Enrolments per Centre')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# -----------------------------------------
# 6️⃣ Save All Graphs (Optional for PDF)
# -----------------------------------------

# Example: save last chart
plt.savefig("Aadhaar_Drishti_Comparison.png", dpi=300)
print("✅ All graphs generated successfully!")