# Visual Storytelling with Data - Ecommerce Analysis

## 📖 The Story: When Do Gift Shoppers Buy?

This project analyzes UK online gift retailer data (Dec 2010 - Dec 2011) to answer a key business question: **When do customers buy gifts throughout the year?**

## 🎯 Key Finding

**33% of annual sales occur in just three months:** September, October, and November.

Gift shoppers prepare early for the holiday season, creating a predictable fall sales surge that retailers can capitalize on.

## 📁 Project Files

### Data
- `Ecommerce Dataset - data.csv` - Transactional data from UK online gift retailer (50,082 transactions)

### Analysis
- `storytelling_analysis.py` - Python script that analyzes seasonality and generates visualizations

### Visualizations
- `story_visual_1.png` - November highlighted (busiest month)
- `story_visual_2.png` - September highlighted (2nd busiest)
- `story_visual_3.png` - October highlighted (3rd busiest)

### Presentation
- `story_presentation.html` - Simple, visual storytelling presentation

## 🚀 Quick Start

### Run Analysis
```bash
cd storytelling_with_data
python storytelling_analysis.py
```

This will:
1. Load and clean the ecommerce dataset
2. Analyze monthly sales patterns
3. Generate three visualizations (same chart with different highlights)
4. Display key insights in the console

### View Presentation
Open `story_presentation.html` in a web browser to see the complete visual story.

## 📊 Storytelling Approach

This project follows best practices for data storytelling:

### ✅ Start with a Question
"When do customers buy gifts throughout the year?"

### ✅ Repetition is a Good Thing
The same chart is shown three times with different highlights to guide attention and build understanding progressively.

### ✅ Highlight the Answer
- **Visual 1**: November highlighted (peak month)
- **Visual 2**: September highlighted (2nd busiest)
- **Visual 3**: October highlighted (3rd busiest)

Each visualization uses:
- **Teal (#009999)** for base bars
- **Dark Purple (#663399)** for highlighted months
- Clean, uncluttered design
- Minimal text to let the visual tell the story

### ✅ Call Audience to Action
The presentation concludes with three specific recommendations:
1. **Stock Up for Fall** - Increase inventory by August
2. **Plan Marketing Campaigns** - Launch promotions in late summer
3. **Hire Seasonal Staff** - Bring on extra team members by late August

## 📈 Data Insights

### Monthly Sales Pattern
- **Peak Month**: November 2011 (£125,661)
- **2nd Place**: September 2011 (£110,922)
- **3rd Place**: October 2011 (£99,002)

### Seasonality Finding
The data shows clear seasonality with fall months (Sep-Nov) accounting for one-third of annual revenue, driven by holiday shopping preparation.

### Top Products
By revenue:
1. Lunch Bag Red Retrospot (£35,752)
2. Set of 3 Regency Cake Tins (£31,178)
3. Roses Regency Teacup and Saucer (£29,095)

## 🎨 Design Principles Applied

### Avoid Chart Junk
- No unnecessary grid lines
- No decorative elements
- No 3D effects
- Clean, simple bar chart

### Maximize Data-Ink Ratio
- Every element serves a purpose
- Focus on the data, not decoration
- Values clearly labeled on bars

### Use Color Purposefully
- Base color (teal) for context
- Highlight color (dark purple) for emphasis
- Only one bar highlighted per visualization
- Color guides the viewer's attention

## 📋 Project Requirements Met

✅ **Clear Question**: When do customers buy gifts?
✅ **Focused Visualization**: Bar chart shows monthly sales pattern
✅ **Insightful Title**: "When Do Gift Shoppers Buy?"
✅ **Appropriate Chart Type**: Bar chart for time series comparison
✅ **Clean Layout**: Uncluttered, professional design
✅ **Purposeful Color**: Teal base with purple highlights
✅ **No Unnecessary Elements**: Minimal design, maximum impact
✅ **Accessible Colors**: High contrast, colorblind-friendly palette

## 🔧 Technical Details

### Libraries Used
- `pandas` - Data manipulation and analysis
- `matplotlib` - Visualization
- `numpy` - Numerical operations

### Data Cleaning Steps
1. Removed cancelled orders (InvoiceNo starting with 'C')
2. Filtered out negative quantities
3. Removed zero-price items
4. Calculated total transaction amounts

### Color Scheme
- **Primary (Teal)**: #009999
- **Highlight (Dark Purple)**: #663399
- These colors are complementary and provide strong visual contrast

## 💡 Business Recommendations

Based on this analysis, the retailer should:

1. **Inventory Planning**: Stock up on popular gift items in August to meet Sept-Nov demand
2. **Marketing**: Launch promotional campaigns in late summer to capture early holiday shoppers
3. **Staffing**: Hire and train seasonal workers by late August
4. **Cash Flow**: Plan for 33% of annual revenue in Q4
5. **Product Selection**: Focus on gift-friendly items that appeal to holiday shoppers

## 📧 Project Information

**Course**: Udacity Marketing Analytics Nanodegree
**Project**: Visual Storytelling with Data
**Author**: Christopher O'Hara, PhD, EngD
**Data Source**: UK Online Retail Dataset (Kaggle)
**Analysis Period**: December 2010 - December 2011

---

**Note**: This analysis demonstrates effective visual storytelling principles: clear question, focused visuals, purposeful repetition with highlighting, and actionable recommendations.
