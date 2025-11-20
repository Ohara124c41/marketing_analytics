"""
Marketing Analytics Project - Black Friday 2017 vs 2018 Analysis
This script performs comprehensive analysis across 5 parts as per project requirements
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.patches import Rectangle
import warnings
import sys
import io

# Configure UTF-8 output for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

warnings.filterwarnings('ignore')

# Set style for better-looking charts
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

# Define color palette - Teal theme
COLOR_PRIMARY = '#009999'      # Teal
COLOR_SECONDARY = '#006666'    # Dark teal
COLOR_SUCCESS = '#2ecc71'      # Green (for positive metrics)
COLOR_WARNING = '#e74c3c'      # Red (for negative/attention)
COLOR_NEUTRAL = '#3498db'      # Blue (for baseline/2017)
COLOR_COMPLEMENT = '#cc6600'   # Orange (complementary to teal)

# Create teal gradient function
def get_teal_gradient(n_colors):
    """Generate a gradient from light teal to dark teal"""
    from matplotlib.colors import LinearSegmentedColormap
    colors_list = ['#b3e5e5', '#66cccc', COLOR_PRIMARY, COLOR_SECONDARY, '#004d4d']
    n_bins = 100
    cmap = LinearSegmentedColormap.from_list('teal_gradient', colors_list, N=n_bins)
    return [cmap(i) for i in np.linspace(0.2, 0.9, n_colors)]

# Load data
print("Loading data...")
df_2017 = pd.read_excel('Project_ Create a Proposal for the Next Quarter  - Sample_Dataset.xlsx',
                         sheet_name='2017 Black Friday')
df_2018 = pd.read_excel('Project_ Create a Proposal for the Next Quarter  - Sample_Dataset.xlsx',
                         sheet_name='2018 Black Friday')

# Add year column for combined analysis
df_2017['Year'] = 2017
df_2018['Year'] = 2018

# Combine datasets
df_combined = pd.concat([df_2017, df_2018], ignore_index=True)

print(f"2017 Data: {len(df_2017)} rows")
print(f"2018 Data: {len(df_2018)} rows")
print(f"Combined Data: {len(df_combined)} rows\n")

# ============================================================================
# PART 1: OBJECTIVES ANALYSIS
# ============================================================================
print("\n" + "="*80)
print("PART 1: OBJECTIVES ANALYSIS")
print("="*80)

# Calculate total sales for each year
total_sales_2017 = df_2017['Order Amount'].sum()
total_sales_2018 = df_2018['Order Amount'].sum()
sales_change_pct = ((total_sales_2018 - total_sales_2017) / total_sales_2017) * 100

# Calculate total ad spend for each year (CPA exists only for Paid channel)
total_ad_spend_2017 = df_2017[df_2017['Customer Source'] == 'Paid']['CPA'].sum()
total_ad_spend_2018 = df_2018[df_2018['Customer Source'] == 'Paid']['CPA'].sum()
ad_spend_change_pct = ((total_ad_spend_2018 - total_ad_spend_2017) / total_ad_spend_2017) * 100

print(f"\nTotal Sales 2017: ${total_sales_2017:,.2f}")
print(f"Total Sales 2018: ${total_sales_2018:,.2f}")
print(f"Sales Change: {sales_change_pct:+.2f}%")
print(f"Sales Objective (30% increase): {'✓ MET' if sales_change_pct >= 30 else '✗ NOT MET'}")

print(f"\nTotal Ad Spend 2017: ${total_ad_spend_2017:,.2f}")
print(f"Total Ad Spend 2018: ${total_ad_spend_2018:,.2f}")
print(f"Ad Spend Change: {ad_spend_change_pct:+.2f}%")
print(f"Ad Spend Objective (30% decrease): {'✓ MET' if ad_spend_change_pct <= -30 else '✗ NOT MET'}")

# Visualization for Part 1
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Sales comparison
ax1 = axes[0]
years = ['2017', '2018']
sales_values = [total_sales_2017, total_sales_2018]
colors = [COLOR_NEUTRAL, COLOR_SUCCESS if sales_change_pct >= 30 else COLOR_WARNING]

bars1 = ax1.bar(years, sales_values, color=colors, edgecolor='black', linewidth=1.5)
ax1.set_ylabel('Total Sales ($)', fontsize=12, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_title('Total Sales: 2017 vs 2018\nObjective: Increase by 30%',
              fontsize=14, fontweight='bold', pad=20)

# Add value labels on bars
for i, (bar, value) in enumerate(zip(bars1, sales_values)):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'${value:,.0f}',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# Add percentage change annotation
ax1.annotate(f'{sales_change_pct:+.1f}%',
            xy=(0.5, max(sales_values) * 0.5), xycoords='data',
            fontsize=16, fontweight='bold', ha='center',
            color=COLOR_SUCCESS if sales_change_pct >= 30 else COLOR_WARNING,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black', linewidth=2))

# Add objective status
status_text = '✓ OBJECTIVE MET' if sales_change_pct >= 30 else '✗ OBJECTIVE NOT MET'
status_color = COLOR_SUCCESS if sales_change_pct >= 30 else COLOR_WARNING
ax1.text(0.5, 0.95, status_text, transform=ax1.transAxes,
        fontsize=12, fontweight='bold', ha='center', va='top',
        color=status_color, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
ax1.grid(True, alpha=0.3)

# Ad Spend comparison
ax2 = axes[1]
ad_spend_values = [total_ad_spend_2017, total_ad_spend_2018]
colors = [COLOR_NEUTRAL, COLOR_SUCCESS if ad_spend_change_pct <= -30 else COLOR_WARNING]

bars2 = ax2.bar(years, ad_spend_values, color=colors, edgecolor='black', linewidth=1.5)
ax2.set_ylabel('Total Ad Spend ($)', fontsize=12, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_title('Total Ad Spend (Paid Channel): 2017 vs 2018\nObjective: Decrease by 30%',
              fontsize=14, fontweight='bold', pad=20)

# Add value labels on bars
for i, (bar, value) in enumerate(zip(bars2, ad_spend_values)):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'${value:,.0f}',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# Add percentage change annotation
ax2.annotate(f'{ad_spend_change_pct:+.1f}%',
            xy=(0.5, max(ad_spend_values) * 0.5), xycoords='data',
            fontsize=16, fontweight='bold', ha='center',
            color=COLOR_SUCCESS if ad_spend_change_pct <= -30 else COLOR_WARNING,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black', linewidth=2))

# Add objective status
status_text = '✓ OBJECTIVE MET' if ad_spend_change_pct <= -30 else '✗ OBJECTIVE NOT MET'
status_color = COLOR_SUCCESS if ad_spend_change_pct <= -30 else COLOR_WARNING
ax2.text(0.5, 0.95, status_text, transform=ax2.transAxes,
        fontsize=12, fontweight='bold', ha='center', va='top',
        color=status_color, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('part1_objectives.png', dpi=300, bbox_inches='tight')
print("\nSaved: part1_objectives.png")
plt.close()

# ============================================================================
# PART 2: EVALUATE THE AUDIENCE
# ============================================================================
print("\n" + "="*80)
print("PART 2: EVALUATE THE AUDIENCE")
print("="*80)

# Required: Demonstrate sales amount by age-range
sales_by_age = df_combined.groupby(['Year', 'Age Range'])['Order Amount'].sum().unstack(level=0)

# Ensure proper order of age ranges
age_order = ['18-25', '26-35', '36-45', '46-50', '51-55', '55+']
sales_by_age = sales_by_age.reindex(age_order)

print("\nSales by Age Range:")
print(sales_by_age)

# Optional Question 1: Which Age-Range generated the most sales?
total_sales_by_age = df_combined.groupby('Age Range')['Order Amount'].sum().sort_values(ascending=False)
print(f"\nAge Range with Most Sales: {total_sales_by_age.index[0]} (${total_sales_by_age.iloc[0]:,.2f})")

# Optional Question 2: How many repeat customers did we have?
repeat_customers_2017 = df_2017.groupby('User ID').size()
repeat_customers_2018 = df_2018.groupby('User ID').size()

repeat_count_2017 = (repeat_customers_2017 > 1).sum()
repeat_count_2018 = (repeat_customers_2018 > 1).sum()
total_unique_2017 = df_2017['User ID'].nunique()
total_unique_2018 = df_2018['User ID'].nunique()

print(f"\nRepeat Customers 2017: {repeat_count_2017} out of {total_unique_2017} ({repeat_count_2017/total_unique_2017*100:.1f}%)")
print(f"Repeat Customers 2018: {repeat_count_2018} out of {total_unique_2018} ({repeat_count_2018/total_unique_2018*100:.1f}%)")

# Visualization for Part 2
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Chart 1: Stacked bar chart - Sales by Age Range (Required)
ax1 = axes[0, 0]
x = np.arange(len(age_order))
width = 0.35

bars1 = ax1.bar(x - width/2, sales_by_age[2017], width, label='2017',
                color=COLOR_NEUTRAL, edgecolor='black', linewidth=1)
bars2 = ax1.bar(x + width/2, sales_by_age[2018], width, label='2018',
                color=COLOR_PRIMARY, edgecolor='black', linewidth=1)

ax1.set_xlabel('Age Range', fontsize=12, fontweight='bold')
ax1.set_ylabel('Total Sales ($)', fontsize=12, fontweight='bold')
ax1.set_title('Sales by Age Range: 2017 vs 2018', fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks(x)
ax1.set_xticklabels(age_order)
ax1.legend(fontsize=11)
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
ax1.grid(True, alpha=0.3, axis='y')

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'${height/1000:.0f}K',
                    ha='center', va='bottom', fontsize=8)

# Chart 2: Top Age Range by Total Sales (Optional)
ax2 = axes[0, 1]
top_5_ages = total_sales_by_age.head(6)
colors_gradient = get_teal_gradient(len(top_5_ages))

bars = ax2.barh(range(len(top_5_ages)), top_5_ages.values, color=colors_gradient,
                edgecolor='black', linewidth=1)
ax2.set_yticks(range(len(top_5_ages)))
ax2.set_yticklabels(top_5_ages.index)
ax2.set_xlabel('Total Sales ($)', fontsize=12, fontweight='bold')
ax2.set_title('Total Sales by Age Range (2017-2018 Combined)\nRanked by Performance',
              fontsize=14, fontweight='bold', pad=20)
ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
ax2.grid(True, alpha=0.3, axis='x')

# Add value labels
for i, (bar, value) in enumerate(zip(bars, top_5_ages.values)):
    width = bar.get_width()
    ax2.text(width, bar.get_y() + bar.get_height()/2.,
            f' ${value:,.0f}',
            ha='left', va='center', fontsize=10, fontweight='bold')

# Highlight the winner
ax2.text(0.98, 0.98, f'Winner: {top_5_ages.index[0]}',
         transform=ax2.transAxes, fontsize=12, fontweight='bold',
         ha='right', va='top', color=COLOR_SUCCESS,
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# Chart 3: Repeat Customers Analysis (Optional)
ax3 = axes[1, 0]
categories = ['One-Time\nCustomers', 'Repeat\nCustomers']
data_2017 = [total_unique_2017 - repeat_count_2017, repeat_count_2017]
data_2018 = [total_unique_2018 - repeat_count_2018, repeat_count_2018]

x = np.arange(len(categories))
width = 0.35

bars1 = ax3.bar(x - width/2, data_2017, width, label='2017',
                color=COLOR_NEUTRAL, edgecolor='black', linewidth=1)
bars2 = ax3.bar(x + width/2, data_2018, width, label='2018',
                color=COLOR_PRIMARY, edgecolor='black', linewidth=1)

ax3.set_ylabel('Number of Customers', fontsize=12, fontweight='bold')
ax3.set_title('Repeat vs One-Time Customers: 2017 vs 2018',
              fontsize=14, fontweight='bold', pad=20)
ax3.set_xticks(x)
ax3.set_xticklabels(categories)
ax3.legend(fontsize=11)
ax3.grid(True, alpha=0.3, axis='y')

# Add value labels and percentages
for bars, total in zip([bars1, bars2], [total_unique_2017, total_unique_2018]):
    for bar in bars:
        height = bar.get_height()
        pct = (height / total) * 100
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}\n({pct:.1f}%)',
                ha='center', va='bottom', fontsize=9, fontweight='bold')

# Chart 4: Average Orders per Customer
ax4 = axes[1, 1]
avg_orders_2017 = df_2017.groupby('User ID').size().mean()
avg_orders_2018 = df_2018.groupby('User ID').size().mean()

years = ['2017', '2018']
avg_orders = [avg_orders_2017, avg_orders_2018]
colors = [COLOR_NEUTRAL, COLOR_PRIMARY]

bars = ax4.bar(years, avg_orders, color=colors, edgecolor='black', linewidth=1.5)
ax4.set_ylabel('Average Orders per Customer', fontsize=12, fontweight='bold')
ax4.set_xlabel('Year', fontsize=12, fontweight='bold')
ax4.set_title('Average Order Volume per Customer', fontsize=14, fontweight='bold', pad=20)
ax4.grid(True, alpha=0.3, axis='y')

# Add value labels
for bar, value in zip(bars, avg_orders):
    height = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2., height,
            f'{value:.2f}',
            ha='center', va='bottom', fontsize=12, fontweight='bold')

# Add change annotation
change_pct = ((avg_orders_2018 - avg_orders_2017) / avg_orders_2017) * 100
ax4.text(0.5, 0.95, f'Change: {change_pct:+.1f}%',
         transform=ax4.transAxes, fontsize=11, fontweight='bold',
         ha='center', va='top', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

plt.tight_layout()
plt.savefig('part2_audience.png', dpi=300, bbox_inches='tight')
print("\nSaved: part2_audience.png")
plt.close()

# ============================================================================
# PART 3: EVALUATE THE MARKETING
# ============================================================================
print("\n" + "="*80)
print("PART 3: EVALUATE THE MARKETING")
print("="*80)

# Required: ROI on Paid Channel and CPA by Age Range
paid_2017 = df_2017[df_2017['Customer Source'] == 'Paid']
paid_2018 = df_2018[df_2018['Customer Source'] == 'Paid']
paid_combined = df_combined[df_combined['Customer Source'] == 'Paid']

# Calculate ROI for Paid Channel
paid_revenue_2017 = paid_2017['Order Amount'].sum()
paid_revenue_2018 = paid_2018['Order Amount'].sum()
paid_cost_2017 = paid_2017['CPA'].sum()
paid_cost_2018 = paid_2018['CPA'].sum()

roi_2017 = ((paid_revenue_2017 - paid_cost_2017) / paid_cost_2017) * 100
roi_2018 = ((paid_revenue_2018 - paid_cost_2018) / paid_cost_2018) * 100

print(f"\nPaid Channel ROI 2017: {roi_2017:.2f}%")
print(f"Paid Channel ROI 2018: {roi_2018:.2f}%")
print(f"ROI Status: {'POSITIVE ✓' if roi_2018 > 0 else 'NEGATIVE ✗'}")

# CPA by Age Range
cpa_by_age = paid_combined.groupby(['Year', 'Age Range'])['CPA'].mean().unstack(level=0)
cpa_by_age = cpa_by_age.reindex(age_order)

print("\nAverage CPA by Age Range:")
print(cpa_by_age)

# Best CPA by Age Range
best_cpa_2017 = paid_2017.groupby('Age Range')['CPA'].mean().idxmin()
best_cpa_2018 = paid_2018.groupby('Age Range')['CPA'].mean().idxmin()
print(f"\nBest CPA Age Range 2017: {best_cpa_2017}")
print(f"Best CPA Age Range 2018: {best_cpa_2018}")

# Optional: Sales by Channel
sales_by_channel = df_combined.groupby(['Year', 'Customer Source'])['Order Amount'].sum().unstack(level=0)
print("\nSales by Channel:")
print(sales_by_channel)

# Visualization for Part 3
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Chart 1: ROI on Paid Channel (Required)
ax1 = axes[0, 0]
years = ['2017', '2018']
roi_values = [roi_2017, roi_2018]
colors = [COLOR_NEUTRAL if roi_2017 > 0 else COLOR_WARNING,
          COLOR_PRIMARY if roi_2018 > 0 else COLOR_WARNING]

bars = ax1.bar(years, roi_values, color=colors, edgecolor='black', linewidth=1.5)
ax1.axhline(y=0, color='black', linestyle='-', linewidth=1)
ax1.set_ylabel('ROI (%)', fontsize=12, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_title('Return on Investment (ROI) - Paid Channel\nROI = (Revenue - Cost) / Cost × 100%',
              fontsize=14, fontweight='bold', pad=20)
ax1.grid(True, alpha=0.3, axis='y')

# Add value labels
for bar, value in zip(bars, roi_values):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'{value:.1f}%',
            ha='center', va='bottom' if value > 0 else 'top',
            fontsize=12, fontweight='bold')

# Add status
status_text = 'ROI POSITIVE ✓' if roi_2018 > 0 else 'ROI NEGATIVE ✗'
status_color = 'green' if roi_2018 > 0 else 'red'
ax1.text(0.5, 0.95, status_text, transform=ax1.transAxes,
        fontsize=12, fontweight='bold', ha='center', va='top',
        color=status_color, bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# Chart 2: CPA by Age Range (Required)
ax2 = axes[0, 1]
x = np.arange(len(age_order))
width = 0.35

bars1 = ax2.bar(x - width/2, cpa_by_age[2017], width, label='2017',
                color=COLOR_NEUTRAL, edgecolor='black', linewidth=1)
bars2 = ax2.bar(x + width/2, cpa_by_age[2018], width, label='2018',
                color=COLOR_PRIMARY, edgecolor='black', linewidth=1)

ax2.set_xlabel('Age Range', fontsize=12, fontweight='bold')
ax2.set_ylabel('Average CPA ($)', fontsize=12, fontweight='bold')
ax2.set_title('Cost Per Acquisition (CPA) by Age Range\nLower is Better',
              fontsize=14, fontweight='bold', pad=20)
ax2.set_xticks(x)
ax2.set_xticklabels(age_order)
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3, axis='y')

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        if not np.isnan(height) and height > 0:
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'${height:.0f}',
                    ha='center', va='bottom', fontsize=8)

# Highlight best performers
ax2.text(0.98, 0.98, f'2017 Best: {best_cpa_2017}\n2018 Best: {best_cpa_2018}',
         transform=ax2.transAxes, fontsize=10, fontweight='bold',
         ha='right', va='top', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# Chart 3: Sales by Channel - Stacked (Optional)
ax3 = axes[1, 0]
channels = sales_by_channel.index.tolist()
x = np.arange(len(channels))
width = 0.35

bars1 = ax3.bar(x - width/2, sales_by_channel[2017], width, label='2017',
                color=COLOR_NEUTRAL, edgecolor='black', linewidth=1)
bars2 = ax3.bar(x + width/2, sales_by_channel[2018], width, label='2018',
                color=COLOR_PRIMARY, edgecolor='black', linewidth=1)

ax3.set_xlabel('Customer Source', fontsize=12, fontweight='bold')
ax3.set_ylabel('Total Sales ($)', fontsize=12, fontweight='bold')
ax3.set_title('Total Sales by Marketing Channel: 2017 vs 2018',
              fontsize=14, fontweight='bold', pad=20)
ax3.set_xticks(x)
ax3.set_xticklabels(channels)
ax3.legend(fontsize=11)
ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
ax3.grid(True, alpha=0.3, axis='y')

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'${height/1000:.0f}K',
                    ha='center', va='bottom', fontsize=9)

# Chart 4: Channel Performance Comparison
ax4 = axes[1, 1]

# Calculate growth rates for each channel
channel_growth = []
for channel in channels:
    rev_2017 = sales_by_channel.loc[channel, 2017]
    rev_2018 = sales_by_channel.loc[channel, 2018]
    growth = ((rev_2018 - rev_2017) / rev_2017) * 100
    channel_growth.append(growth)

colors_growth = [COLOR_SUCCESS if g > 0 else COLOR_WARNING for g in channel_growth]
bars = ax4.barh(channels, channel_growth, color=colors_growth, edgecolor='black', linewidth=1)
ax4.axvline(x=0, color='black', linestyle='-', linewidth=1)
ax4.set_xlabel('Growth Rate (%)', fontsize=12, fontweight='bold')
ax4.set_title('Channel Growth Rate: 2017 to 2018', fontsize=14, fontweight='bold', pad=20)
ax4.grid(True, alpha=0.3, axis='x')

# Add value labels
for bar, value in zip(bars, channel_growth):
    width = bar.get_width()
    ax4.text(width, bar.get_y() + bar.get_height()/2.,
            f' {value:+.1f}%',
            ha='left' if value > 0 else 'right', va='center',
            fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('part3_marketing.png', dpi=300, bbox_inches='tight')
print("\nSaved: part3_marketing.png")
plt.close()

# ============================================================================
# PART 4: EVALUATE THE SALES
# ============================================================================
print("\n" + "="*80)
print("PART 4: EVALUATE THE SALES")
print("="*80)

# Required: Revenue generated
revenue_2017 = df_2017['Order Amount'].sum()
revenue_2018 = df_2018['Order Amount'].sum()

print(f"\nTotal Revenue 2017: ${revenue_2017:,.2f}")
print(f"Total Revenue 2018: ${revenue_2018:,.2f}")

# Optional: Average order amount
avg_order_2017 = df_2017['Order Amount'].mean()
avg_order_2018 = df_2018['Order Amount'].mean()

print(f"\nAverage Order Amount 2017: ${avg_order_2017:.2f}")
print(f"Average Order Amount 2018: ${avg_order_2018:.2f}")

# Top customer
top_customer_2017 = df_2017.groupby('User ID')['Order Amount'].sum().idxmax()
top_customer_2017_amount = df_2017.groupby('User ID')['Order Amount'].sum().max()
top_customer_2018 = df_2018.groupby('User ID')['Order Amount'].sum().idxmax()
top_customer_2018_amount = df_2018.groupby('User ID')['Order Amount'].sum().max()

print(f"\nTop Customer 2017: User ID {top_customer_2017} (${top_customer_2017_amount:,.2f})")
print(f"Top Customer 2018: User ID {top_customer_2018} (${top_customer_2018_amount:,.2f})")

# Visualization for Part 4
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Chart 1: Total Revenue Comparison (Required)
ax1 = axes[0, 0]
years = ['2017', '2018']
revenues = [revenue_2017, revenue_2018]
colors = [COLOR_NEUTRAL, COLOR_PRIMARY]

bars = ax1.bar(years, revenues, color=colors, edgecolor='black', linewidth=1.5)
ax1.set_ylabel('Total Revenue ($)', fontsize=12, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_title('Total Revenue Generated: 2017 vs 2018', fontsize=14, fontweight='bold', pad=20)
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
ax1.grid(True, alpha=0.3, axis='y')

# Add value labels
for bar, value in zip(bars, revenues):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'${value:,.0f}',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# Add growth annotation
revenue_growth = ((revenue_2018 - revenue_2017) / revenue_2017) * 100
ax1.text(0.5, 0.5, f'+{revenue_growth:.1f}%', transform=ax1.transAxes,
        fontsize=18, fontweight='bold', ha='center', va='center',
        color=COLOR_SUCCESS, bbox=dict(boxstyle='round', facecolor='white',
                                edgecolor='black', linewidth=2))

# Chart 2: Average Order Amount (Optional)
ax2 = axes[0, 1]
avg_orders = [avg_order_2017, avg_order_2018]
colors = [COLOR_NEUTRAL, COLOR_PRIMARY]

bars = ax2.bar(years, avg_orders, color=colors, edgecolor='black', linewidth=1.5)
ax2.set_ylabel('Average Order Amount ($)', fontsize=12, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12, fontweight='bold')
ax2.set_title('Average Order Amount: 2017 vs 2018', fontsize=14, fontweight='bold', pad=20)
ax2.grid(True, alpha=0.3, axis='y')

# Add value labels
for bar, value in zip(bars, avg_orders):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'${value:.2f}',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# Add change annotation
avg_change = ((avg_order_2018 - avg_order_2017) / avg_order_2017) * 100
ax2.text(0.5, 0.95, f'Change: {avg_change:+.1f}%', transform=ax2.transAxes,
        fontsize=11, fontweight='bold', ha='center', va='top',
        bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.7))

# Chart 3: Top 10 Customers by Revenue (Optional)
ax3 = axes[1, 0]
top_10_customers = df_combined.groupby('User ID')['Order Amount'].sum().nlargest(10)
colors_gradient = get_teal_gradient(len(top_10_customers))

bars = ax3.barh(range(len(top_10_customers)), top_10_customers.values,
                color=colors_gradient, edgecolor='black', linewidth=1)
ax3.set_yticks(range(len(top_10_customers)))
ax3.set_yticklabels([f'User {uid}' for uid in top_10_customers.index])
ax3.set_xlabel('Total Spending ($)', fontsize=12, fontweight='bold')
ax3.set_title('Top 10 Customers by Total Spending (2017-2018)',
              fontsize=14, fontweight='bold', pad=20)
ax3.grid(True, alpha=0.3, axis='x')

# Add value labels
for i, (bar, value) in enumerate(zip(bars, top_10_customers.values)):
    width = bar.get_width()
    ax3.text(width, bar.get_y() + bar.get_height()/2.,
            f' ${value:,.0f}',
            ha='left', va='center', fontsize=9, fontweight='bold')

# Highlight top customer
ax3.text(0.98, 0.98, f'Top Spender: User {top_10_customers.index[0]}',
         transform=ax3.transAxes, fontsize=11, fontweight='bold',
         ha='right', va='top', color='gold',
         bbox=dict(boxstyle='round', facecolor='black', alpha=0.8))

# Chart 4: Revenue Distribution by Quarter (simulated monthly breakdown)
ax4 = axes[1, 1]
# Create monthly breakdown for visualization
months_2017 = df_2017.groupby(pd.cut(range(len(df_2017)), 12))['Order Amount'].sum()
months_2018 = df_2018.groupby(pd.cut(range(len(df_2018)), 12))['Order Amount'].sum()

month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
x = np.arange(12)

# Since this is Black Friday data, we'll show it differently
# Show number of transactions and average order value
transactions_2017 = len(df_2017)
transactions_2018 = len(df_2018)

metrics = ['Total\nTransactions', 'Avg Order\nValue', 'Total\nRevenue']
data_2017 = [transactions_2017, avg_order_2017, revenue_2017/1000]
data_2018 = [transactions_2018, avg_order_2018, revenue_2018/1000]

# Normalize for visualization
max_vals = [max(transactions_2017, transactions_2018),
            max(avg_order_2017, avg_order_2018),
            max(revenue_2017, revenue_2018)/1000]

x = np.arange(len(metrics))
width = 0.35

bars1 = ax4.bar(x - width/2, data_2017, width, label='2017',
                color='#3498db', edgecolor='black', linewidth=1)
bars2 = ax4.bar(x + width/2, data_2018, width, label='2018',
                color='#2ecc71', edgecolor='black', linewidth=1)

ax4.set_ylabel('Value', fontsize=12, fontweight='bold')
ax4.set_title('Key Sales Metrics Comparison', fontsize=14, fontweight='bold', pad=20)
ax4.set_xticks(x)
ax4.set_xticklabels(metrics)
ax4.legend(fontsize=11)
ax4.grid(True, alpha=0.3, axis='y')

# Add value labels with proper formatting
for i, (bar1, bar2, val1, val2) in enumerate(zip(bars1, bars2, data_2017, data_2018)):
    if i == 0:  # Transactions
        ax4.text(bar1.get_x() + bar1.get_width()/2., bar1.get_height(),
                f'{int(val1):,}', ha='center', va='bottom', fontsize=9, fontweight='bold')
        ax4.text(bar2.get_x() + bar2.get_width()/2., bar2.get_height(),
                f'{int(val2):,}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    elif i == 1:  # Avg Order
        ax4.text(bar1.get_x() + bar1.get_width()/2., bar1.get_height(),
                f'${val1:.2f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
        ax4.text(bar2.get_x() + bar2.get_width()/2., bar2.get_height(),
                f'${val2:.2f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    else:  # Revenue
        ax4.text(bar1.get_x() + bar1.get_width()/2., bar1.get_height(),
                f'${val1:.0f}K', ha='center', va='bottom', fontsize=9, fontweight='bold')
        ax4.text(bar2.get_x() + bar2.get_width()/2., bar2.get_height(),
                f'${val2:.0f}K', ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('part4_sales.png', dpi=300, bbox_inches='tight')
print("\nSaved: part4_sales.png")
plt.close()

# ============================================================================
# PART 5: EVALUATE THE PRODUCT CATEGORIES
# ============================================================================
print("\n" + "="*80)
print("PART 5: EVALUATE THE PRODUCT CATEGORIES")
print("="*80)

# Required: Most popular product category
product_sales = df_combined.groupby(['Year', 'Product Category'])['Order Amount'].sum().unstack(level=0)
product_transactions = df_combined.groupby(['Year', 'Product Category']).size().unstack(level=0)

most_popular_2017_sales = product_sales[2017].idxmax()
most_popular_2018_sales = product_sales[2018].idxmax()

most_popular_2017_trans = product_transactions[2017].idxmax()
most_popular_2018_trans = product_transactions[2018].idxmax()

print(f"\nMost Popular by Sales 2017: {most_popular_2017_sales} (${product_sales.loc[most_popular_2017_sales, 2017]:,.2f})")
print(f"Most Popular by Sales 2018: {most_popular_2018_sales} (${product_sales.loc[most_popular_2018_sales, 2018]:,.2f})")

print(f"\nMost Popular by Transactions 2017: {most_popular_2017_trans} ({product_transactions.loc[most_popular_2017_trans, 2017]:,} orders)")
print(f"Most Popular by Transactions 2018: {most_popular_2018_trans} ({product_transactions.loc[most_popular_2018_trans, 2018]:,} orders)")

# Optional: Sales by product category
print("\nSales by Product Category:")
print(product_sales)

# Optional: CPA by product category
cpa_by_product = paid_combined.groupby(['Year', 'Product Category'])['CPA'].mean().unstack(level=0)
print("\nCPA by Product Category:")
print(cpa_by_product)

# Visualization for Part 5
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Chart 1: Sales by Product Category - Stacked (Required + Optional)
ax1 = axes[0, 0]
categories = product_sales.index.tolist()
x = np.arange(len(categories))
width = 0.35

bars1 = ax1.bar(x - width/2, product_sales[2017], width, label='2017',
                color=COLOR_NEUTRAL, edgecolor='black', linewidth=1)
bars2 = ax1.bar(x + width/2, product_sales[2018], width, label='2018',
                color=COLOR_PRIMARY, edgecolor='black', linewidth=1)

ax1.set_xlabel('Product Category', fontsize=12, fontweight='bold')
ax1.set_ylabel('Total Sales ($)', fontsize=12, fontweight='bold')
ax1.set_title('Total Sales by Product Category: 2017 vs 2018',
              fontsize=14, fontweight='bold', pad=20)
ax1.set_xticks(x)
ax1.set_xticklabels(categories, rotation=0)
ax1.legend(fontsize=11)
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x/1000:.0f}K'))
ax1.grid(True, alpha=0.3, axis='y')

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'${height/1000:.0f}K',
                    ha='center', va='bottom', fontsize=8)

# Highlight winners
ax1.text(0.98, 0.98, f'2017 Leader: {most_popular_2017_sales}\n2018 Leader: {most_popular_2018_sales}',
         transform=ax1.transAxes, fontsize=10, fontweight='bold',
         ha='right', va='top', bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

# Chart 2: Transaction Count by Product Category (Required)
ax2 = axes[0, 1]
bars1 = ax2.bar(x - width/2, product_transactions[2017], width, label='2017',
                color=COLOR_NEUTRAL, edgecolor='black', linewidth=1)
bars2 = ax2.bar(x + width/2, product_transactions[2018], width, label='2018',
                color=COLOR_PRIMARY, edgecolor='black', linewidth=1)

ax2.set_xlabel('Product Category', fontsize=12, fontweight='bold')
ax2.set_ylabel('Number of Transactions', fontsize=12, fontweight='bold')
ax2.set_title('Transaction Volume by Product Category: 2017 vs 2018',
              fontsize=14, fontweight='bold', pad=20)
ax2.set_xticks(x)
ax2.set_xticklabels(categories, rotation=0)
ax2.legend(fontsize=11)
ax2.grid(True, alpha=0.3, axis='y')

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax2.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height):,}',
                    ha='center', va='bottom', fontsize=8)

# Chart 3: CPA by Product Category (Optional)
ax3 = axes[1, 0]
categories_with_cpa = cpa_by_product.index.tolist()
x_cpa = np.arange(len(categories_with_cpa))

bars1 = ax3.bar(x_cpa - width/2, cpa_by_product[2017], width, label='2017',
                color=COLOR_NEUTRAL, edgecolor='black', linewidth=1)
bars2 = ax3.bar(x_cpa + width/2, cpa_by_product[2018], width, label='2018',
                color=COLOR_PRIMARY, edgecolor='black', linewidth=1)

ax3.set_xlabel('Product Category', fontsize=12, fontweight='bold')
ax3.set_ylabel('Average CPA ($)', fontsize=12, fontweight='bold')
ax3.set_title('Cost Per Acquisition by Product Category\nLower is Better',
              fontsize=14, fontweight='bold', pad=20)
ax3.set_xticks(x_cpa)
ax3.set_xticklabels(categories_with_cpa, rotation=0)
ax3.legend(fontsize=11)
ax3.grid(True, alpha=0.3, axis='y')

# Add value labels
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        if not np.isnan(height) and height > 0:
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'${height:.0f}',
                    ha='center', va='bottom', fontsize=8)

# Chart 4: Product Category Growth Rate
ax4 = axes[1, 1]
category_growth = []
for category in categories:
    sales_2017 = product_sales.loc[category, 2017]
    sales_2018 = product_sales.loc[category, 2018]
    growth = ((sales_2018 - sales_2017) / sales_2017) * 100
    category_growth.append(growth)

# Sort by growth rate
sorted_indices = np.argsort(category_growth)[::-1]
sorted_categories = [categories[i] for i in sorted_indices]
sorted_growth = [category_growth[i] for i in sorted_indices]

colors_growth = [COLOR_SUCCESS if g > 0 else COLOR_WARNING for g in sorted_growth]
bars = ax4.barh(sorted_categories, sorted_growth, color=colors_growth,
                edgecolor='black', linewidth=1)
ax4.axvline(x=0, color='black', linestyle='-', linewidth=1)
ax4.set_xlabel('Growth Rate (%)', fontsize=12, fontweight='bold')
ax4.set_title('Product Category Growth Rate: 2017 to 2018\nRanked by Performance',
              fontsize=14, fontweight='bold', pad=20)
ax4.grid(True, alpha=0.3, axis='x')

# Add value labels
for bar, value in zip(bars, sorted_growth):
    width_bar = bar.get_width()
    ax4.text(width_bar, bar.get_y() + bar.get_height()/2.,
            f' {value:+.1f}%',
            ha='left' if value > 0 else 'right', va='center',
            fontsize=10, fontweight='bold')

# Highlight best performer
ax4.text(0.98, 0.98, f'Best Growth:\n{sorted_categories[0]}',
         transform=ax4.transAxes, fontsize=11, fontweight='bold',
         ha='right', va='top', color=COLOR_SUCCESS,
         bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7))

plt.tight_layout()
plt.savefig('part5_products.png', dpi=300, bbox_inches='tight')
print("\nSaved: part5_products.png")
plt.close()

# ============================================================================
# SUMMARY REPORT
# ============================================================================
print("\n" + "="*80)
print("SUMMARY REPORT - BLACK FRIDAY 2017 vs 2018")
print("="*80)

print("\n📊 PART 1: OBJECTIVES")
print("-" * 80)
print(f"Sales Objective (30% increase): {'✓ MET' if sales_change_pct >= 30 else '✗ NOT MET'}")
print(f"  - 2017 Sales: ${total_sales_2017:,.2f}")
print(f"  - 2018 Sales: ${total_sales_2018:,.2f}")
print(f"  - Change: {sales_change_pct:+.2f}%")
print(f"\nAd Spend Objective (30% decrease): {'✓ MET' if ad_spend_change_pct <= -30 else '✗ NOT MET'}")
print(f"  - 2017 Ad Spend: ${total_ad_spend_2017:,.2f}")
print(f"  - 2018 Ad Spend: ${total_ad_spend_2018:,.2f}")
print(f"  - Change: {ad_spend_change_pct:+.2f}%")

print("\n👥 PART 2: AUDIENCE INSIGHTS")
print("-" * 80)
print(f"Top Age Range by Sales: {total_sales_by_age.index[0]} (${total_sales_by_age.iloc[0]:,.2f})")
print(f"Repeat Customers 2017: {repeat_count_2017} ({repeat_count_2017/total_unique_2017*100:.1f}%)")
print(f"Repeat Customers 2018: {repeat_count_2018} ({repeat_count_2018/total_unique_2018*100:.1f}%)")
print(f"Avg Orders per Customer 2017: {avg_orders_2017:.2f}")
print(f"Avg Orders per Customer 2018: {avg_orders_2018:.2f}")

print("\n📢 PART 3: MARKETING PERFORMANCE")
print("-" * 80)
print(f"Paid Channel ROI 2017: {roi_2017:.2f}%")
print(f"Paid Channel ROI 2018: {roi_2018:.2f}% ({'POSITIVE ✓' if roi_2018 > 0 else 'NEGATIVE ✗'})")
print(f"Best CPA Age Range 2017: {best_cpa_2017}")
print(f"Best CPA Age Range 2018: {best_cpa_2018}")
print(f"Top Channel by Sales 2018: {sales_by_channel[2018].idxmax()} (${sales_by_channel[2018].max():,.2f})")

print("\n💰 PART 4: SALES ANALYSIS")
print("-" * 80)
print(f"Total Revenue 2017: ${revenue_2017:,.2f}")
print(f"Total Revenue 2018: ${revenue_2018:,.2f}")
print(f"Revenue Growth: {revenue_growth:+.2f}%")
print(f"Avg Order Amount 2017: ${avg_order_2017:.2f}")
print(f"Avg Order Amount 2018: ${avg_order_2018:.2f}")
print(f"Top Customer Overall: User {top_10_customers.index[0]} (${top_10_customers.iloc[0]:,.2f})")

print("\n🛍️ PART 5: PRODUCT CATEGORIES")
print("-" * 80)
print(f"Most Popular by Sales 2017: {most_popular_2017_sales}")
print(f"Most Popular by Sales 2018: {most_popular_2018_sales}")
print(f"Most Popular by Transactions 2017: {most_popular_2017_trans}")
print(f"Most Popular by Transactions 2018: {most_popular_2018_trans}")

print("\n" + "="*80)
print("ANALYSIS COMPLETE!")
print("="*80)
print("\nGenerated Files:")
print("  1. part1_objectives.png")
print("  2. part2_audience.png")
print("  3. part3_marketing.png")
print("  4. part4_sales.png")
print("  5. part5_products.png")
print("\nAll visualizations include:")
print("  ✓ Proper chart labels and titles")
print("  ✓ Clear legends where applicable")
print("  ✓ Data value labels on charts")
print("  ✓ Stacked comparisons where appropriate")
print("  ✓ Color-coded performance indicators")
print("="*80)
