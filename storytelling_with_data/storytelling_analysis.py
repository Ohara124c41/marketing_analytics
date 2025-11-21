"""
Ecommerce Data Storytelling Analysis
Visual story about UK online gift retailer
"""

import sys
import io
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Configure UTF-8 output for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# Color scheme
COLOR_BASE = '#009999'  # Teal
COLOR_HIGHLIGHT = '#663399'  # Dark purple (complementary)

print("Loading ecommerce data...")
df = pd.read_csv('Ecommerce Dataset - data.csv')

print(f"\nDataset shape: {df.shape}")
print(f"Date range: {df['InvoiceDate'].min()} to {df['InvoiceDate'].max()}")
print("\nFirst few rows:")
print(df.head())
print("\nColumn info:")
print(df.info())

# Clean data
print("\nCleaning data...")
# Remove cancelled orders (InvoiceNo starting with 'C')
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]
# Remove negative quantities and zero prices
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
# Calculate total amount
df['TotalAmount'] = df['Quantity'] * df['UnitPrice']

# Parse dates
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Month'] = df['InvoiceDate'].dt.to_period('M')
df['MonthName'] = df['InvoiceDate'].dt.strftime('%B')
df['Year'] = df['InvoiceDate'].dt.year

print(f"\nAfter cleaning: {df.shape[0]} rows")

# ================================================================================
# STORY EXPLORATION
# ================================================================================

print("\n" + "="*80)
print("EXPLORING THE DATA FOR STORY")
print("="*80)

# 1. Monthly sales trend (Seasonality)
monthly_sales = df.groupby('Month')['TotalAmount'].sum().reset_index()
monthly_sales['MonthDate'] = monthly_sales['Month'].dt.to_timestamp()
print("\nMonthly Sales:")
print(monthly_sales)

# Find peak months
top_3_months = monthly_sales.nlargest(3, 'TotalAmount')
print(f"\nTop 3 months by sales:")
print(top_3_months)

# 2. Top products by revenue
product_sales = df.groupby('Description')['TotalAmount'].sum().sort_values(ascending=False)
print(f"\nTop 10 Products by Revenue:")
print(product_sales.head(10))

# 3. Top products by quantity sold
product_quantity = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False)
print(f"\nTop 10 Products by Quantity:")
print(product_quantity.head(10))

# ================================================================================
# STORY: "When Do Gift Shoppers Buy?"
# We'll focus on seasonality - showing which months are busiest
# ================================================================================

print("\n" + "="*80)
print("CREATING VISUAL STORY: WHEN DO GIFT SHOPPERS BUY?")
print("="*80)

# Prepare monthly data with month names
monthly_data = df.groupby([df['InvoiceDate'].dt.to_period('M')])['TotalAmount'].sum().reset_index()
monthly_data['MonthDate'] = monthly_data['InvoiceDate'].dt.to_timestamp()
monthly_data['MonthName'] = monthly_data['MonthDate'].dt.strftime('%b %Y')
monthly_data = monthly_data.sort_values('MonthDate')

# Get top 3 months
sorted_by_sales = monthly_data.sort_values('TotalAmount', ascending=False)
top_month_1 = sorted_by_sales.iloc[0]['MonthDate']
top_month_2 = sorted_by_sales.iloc[1]['MonthDate']
top_month_3 = sorted_by_sales.iloc[2]['MonthDate']

print(f"\nTop 3 months:")
print(f"1st: {sorted_by_sales.iloc[0]['MonthName']} - ${sorted_by_sales.iloc[0]['TotalAmount']:,.0f}")
print(f"2nd: {sorted_by_sales.iloc[1]['MonthName']} - ${sorted_by_sales.iloc[1]['TotalAmount']:,.0f}")
print(f"3rd: {sorted_by_sales.iloc[2]['MonthName']} - ${sorted_by_sales.iloc[2]['TotalAmount']:,.0f}")

# ================================================================================
# VISUALIZATION 1: Highlight the #1 month (November 2011)
# ================================================================================

plt.rcParams['figure.figsize'] = (14, 7)
plt.rcParams['font.size'] = 11

fig, ax = plt.subplots(figsize=(14, 7))

# Create colors array - highlight only the top month
colors = [COLOR_HIGHLIGHT if date == top_month_1 else COLOR_BASE
          for date in monthly_data['MonthDate']]

bars = ax.bar(monthly_data['MonthName'], monthly_data['TotalAmount'],
              color=colors, edgecolor='black', linewidth=1)

ax.set_ylabel('Total Sales (£)', fontsize=14, fontweight='bold')
ax.set_xlabel('Month', fontsize=14, fontweight='bold')
ax.set_title('When Do Gift Shoppers Buy?', fontsize=18, fontweight='bold', pad=20)
ax.tick_params(axis='x', rotation=45)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    if height > 0:
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'£{height/1000:.0f}K',
                ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'£{x/1000:.0f}K'))
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('story_visual_1.png', dpi=300, bbox_inches='tight')
print("\n✓ Saved: story_visual_1.png (November highlighted)")
plt.close()

# ================================================================================
# VISUALIZATION 2: Highlight the #2 month (October 2011)
# ================================================================================

fig, ax = plt.subplots(figsize=(14, 7))

# Create colors array - highlight only the 2nd top month
colors = [COLOR_HIGHLIGHT if date == top_month_2 else COLOR_BASE
          for date in monthly_data['MonthDate']]

bars = ax.bar(monthly_data['MonthName'], monthly_data['TotalAmount'],
              color=colors, edgecolor='black', linewidth=1)

ax.set_ylabel('Total Sales (£)', fontsize=14, fontweight='bold')
ax.set_xlabel('Month', fontsize=14, fontweight='bold')
ax.set_title('When Do Gift Shoppers Buy?', fontsize=18, fontweight='bold', pad=20)
ax.tick_params(axis='x', rotation=45)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    if height > 0:
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'£{height/1000:.0f}K',
                ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'£{x/1000:.0f}K'))
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('story_visual_2.png', dpi=300, bbox_inches='tight')
print("✓ Saved: story_visual_2.png (October highlighted)")
plt.close()

# ================================================================================
# VISUALIZATION 3: Highlight the #3 month (September 2011)
# ================================================================================

fig, ax = plt.subplots(figsize=(14, 7))

# Create colors array - highlight only the 3rd top month
colors = [COLOR_HIGHLIGHT if date == top_month_3 else COLOR_BASE
          for date in monthly_data['MonthDate']]

bars = ax.bar(monthly_data['MonthName'], monthly_data['TotalAmount'],
              color=colors, edgecolor='black', linewidth=1)

ax.set_ylabel('Total Sales (£)', fontsize=14, fontweight='bold')
ax.set_xlabel('Month', fontsize=14, fontweight='bold')
ax.set_title('When Do Gift Shoppers Buy?', fontsize=18, fontweight='bold', pad=20)
ax.tick_params(axis='x', rotation=45)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    if height > 0:
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'£{height/1000:.0f}K',
                ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'£{x/1000:.0f}K'))
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('story_visual_3.png', dpi=300, bbox_inches='tight')
print("✓ Saved: story_visual_3.png (September highlighted)")
plt.close()

# ================================================================================
# STORY INSIGHTS FOR HTML
# ================================================================================

print("\n" + "="*80)
print("STORY SUMMARY")
print("="*80)

# Calculate insights
nov_sales = sorted_by_sales.iloc[0]['TotalAmount']
oct_sales = sorted_by_sales.iloc[1]['TotalAmount']
sep_sales = sorted_by_sales.iloc[2]['TotalAmount']

total_annual = monthly_data['TotalAmount'].sum()
top_3_total = nov_sales + oct_sales + sep_sales
top_3_percent = (top_3_total / total_annual) * 100

print(f"\n📊 KEY INSIGHTS:")
print(f"   Top month: {sorted_by_sales.iloc[0]['MonthName']} (£{nov_sales:,.0f})")
print(f"   2nd month: {sorted_by_sales.iloc[1]['MonthName']} (£{oct_sales:,.0f})")
print(f"   3rd month: {sorted_by_sales.iloc[2]['MonthName']} (£{sep_sales:,.0f})")
print(f"   Top 3 months = {top_3_percent:.1f}% of annual sales")
print(f"\n💡 STORY ANGLE:")
print(f"   Gift shoppers prepare for the holidays!")
print(f"   Sales peak in fall as customers stock up for the holiday season.")

print("\n" + "="*80)
print("ANALYSIS COMPLETE!")
print("="*80)
print("\nGenerated Files:")
print("  1. story_visual_1.png (November highlighted)")
print("  2. story_visual_2.png (October highlighted)")
print("  3. story_visual_3.png (September highlighted)")
print("="*80)
