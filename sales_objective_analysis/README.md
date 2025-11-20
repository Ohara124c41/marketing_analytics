# Marketing Analytics Project - Black Friday Analysis

This project analyzes Black Friday sales data (2017 vs 2018) across five key areas: objectives, audience, marketing, sales, and product categories.

## 📁 Project Files

### Data
- `Project_ Create a Proposal for the Next Quarter - Sample_Dataset.xlsx` - Source data with 2017 and 2018 sheets

### Analysis
- `marketing_analysis.py` - Main Python script that performs all analyses and generates visualizations
- `PROJECT_ANALYSIS_REPORT.md` - Comprehensive findings and recommendations

### Generated Visualizations
- `part1_objectives.png` - Sales and ad spend objectives analysis
- `part2_audience.png` - Audience demographics and behavior
- `part3_marketing.png` - Marketing channel performance and ROI
- `part4_sales.png` - Revenue and sales metrics
- `part5_products.png` - Product category analysis

## 🚀 Quick Start

### Prerequisites
```bash
pip install pandas openpyxl matplotlib seaborn numpy
```

### Run Analysis
```bash
python marketing_analysis.py
```

This will:
1. Load data from both years (2017 & 2018)
2. Perform comprehensive analysis across all 5 parts
3. Generate 5 high-quality visualization files (PNG format, 300 DPI)
4. Display detailed results in the console

## 📊 Analysis Coverage

### Part 1: Objectives
- **Required**: Sales growth vs 30% target
- **Required**: Ad spend change vs -30% target
- **Visual**: Side-by-side bar charts with status indicators

### Part 2: Audience
- **Required**: Sales by age range
- **Optional 1**: Top age ranges by sales
- **Optional 2**: Repeat customer analysis
- **Optional 3**: Average order volume per customer
- **Visuals**: 4 charts showing demographic insights

### Part 3: Marketing
- **Required**: ROI on Paid Channel
- **Required**: CPA by age range
- **Optional**: Sales by channel and growth rates
- **Visuals**: 4 charts showing marketing performance

### Part 4: Sales
- **Required**: Total revenue comparison
- **Optional 1**: Average order amount
- **Optional 2**: Top customers analysis
- **Visuals**: 4 charts showing sales metrics

### Part 5: Product Categories
- **Required**: Most popular categories (both years)
- **Optional 1**: Sales by category
- **Optional 2**: CPA by category
- **Visuals**: 4 charts showing product performance

## 📈 Key Findings Summary

### ✅ Success Metrics
- **Sales Growth**: +31.19% (OBJECTIVE MET)
- **Customer Retention**: 85.4% repeat customer rate
- **All Channels Growing**: Positive growth across Blog, Paid, and Social
- **All Products Growing**: Every category showed revenue increases

### ⚠️ Areas for Improvement
- **Ad Spend**: Increased 37.78% (OBJECTIVE NOT MET - should have decreased 30%)
- **ROI Declining**: Paid channel ROI decreased from 8.03% to 6.69%
- **18-25 Segment**: Only 3.29% growth, needs attention

### 🎯 Top Performers
- **Age Group**: 26-35 (nearly 40% of total sales)
- **Channel**: Paid ($893K in 2018)
- **Product**: Grocery (most popular by transactions and revenue in 2018)
- **Growth Leader**: Toys category (+38%)

## 📋 Rubric Compliance

All project requirements are met:

✅ **Part 1**: Visual demonstrations with proper labels, percent changes, and objective status
✅ **Part 2**: Required analysis (sales by age) + 2 optional analyses with supporting visuals
✅ **Part 3**: Required analyses (ROI, CPA by age) + optional channel analysis
✅ **Part 4**: Required revenue analysis + optional analyses
✅ **Part 5**: Required (most popular categories) + 2 optional analyses (sales & CPA by category)

All visualizations include:
- Clear chart labels
- Informative headings
- Appropriate legends
- Supporting explanatory text
- Easy-to-understand formats
- Professional appearance

## 🎨 Visualization Features

- **High Resolution**: 300 DPI for presentation quality
- **Color Coding**: Green (success), Red (needs attention), Blue (baseline)
- **Data Labels**: All values clearly displayed on charts
- **Comparisons**: Side-by-side bars for year-over-year analysis
- **Rankings**: Sorted charts to highlight top/bottom performers
- **Context**: Growth rates and percentage changes prominently featured

## 💡 Using the Analysis

1. **For Presentations**: Use the PNG files directly in PowerPoint/Google Slides
2. **For Deep Dives**: Read the PROJECT_ANALYSIS_REPORT.md for detailed insights
3. **For Modifications**: Edit marketing_analysis.py to customize visualizations
4. **For Data Updates**: Replace the Excel file and re-run the script

## 🔧 Customization

### Change Color Scheme
Edit the color variables in `marketing_analysis.py`:
```python
colors = ['#3498db', '#2ecc71']  # Blue, Green
```

### Adjust Figure Size
Modify the figure size parameter:
```python
plt.rcParams['figure.figsize'] = (12, 6)  # Width, Height in inches
```

### Export Different Formats
Change the save command:
```python
plt.savefig('filename.pdf', dpi=300)  # For PDF
plt.savefig('filename.svg')  # For vector graphics
```

## 📧 Questions or Issues?

Review the PROJECT_ANALYSIS_REPORT.md for comprehensive explanations of all analyses and findings.

---

**Project Completion Date**: November 2025
**Analysis Period**: Black Friday 2017 vs 2018
**Total Transactions Analyzed**: 39,702
**Total Revenue Analyzed**: $3,687,345.31
