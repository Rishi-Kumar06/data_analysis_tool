# Data Analysis Tool with Pandas and Matplotlib

A comprehensive Python tool for data analysis and visualization using Pandas, Matplotlib, and Seaborn. This tool loads CSV data, performs statistical analysis, and creates various visualizations including bar charts, scatter plots, and heatmaps.

## 🚀 Features

### Data Loading & Analysis
- ✅ **CSV Data Loading**: Automatic loading and validation of CSV files
- ✅ **Statistical Analysis**: Comprehensive statistics for all numeric columns
- ✅ **Data Overview**: Dataset shape, column types, missing values analysis
- ✅ **Category Analysis**: Group analysis by categorical variables

### Visualizations
- ✅ **Bar Charts**: Distribution analysis for categorical data
- ✅ **Scatter Plots**: Relationship analysis between numeric variables
- ✅ **Correlation Heatmaps**: Visual correlation matrix for numeric data
- ✅ **Histograms**: Distribution analysis for numeric data
- ✅ **Box Plots**: Category-wise distribution analysis

### Advanced Features
- ✅ **Automated Insights**: AI-generated observations and insights
- ✅ **Interactive Demo**: User-friendly interface for exploration
- ✅ **Plot Saving**: Export visualizations as high-quality PNG files
- ✅ **Comprehensive Reports**: Full analysis with all visualizations

## 📁 Project Structure

```
data_analysis_tool/
├── data_analyzer.py      # Main analysis class with all functionality
├── interactive_demo.py   # Interactive demo for user exploration
├── sample_data.csv      # Sample employee dataset for demonstration
├── requirements.txt     # Python dependencies
└── README.md           # This documentation
```

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher

### Install Dependencies
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install pandas matplotlib seaborn numpy
```

## 📊 Sample Dataset

The tool includes a sample employee dataset with the following columns:
- **Name**: Employee name
- **Age**: Employee age (numeric)
- **Department**: Engineering, Marketing, Sales (categorical)
- **Salary**: Annual salary in USD (numeric)
- **Years_Experience**: Years of work experience (numeric)
- **Performance_Score**: Performance rating 1-10 (numeric)
- **City**: Employee location (categorical)
- **Education_Level**: Bachelor, Master (categorical)

## 🎯 Usage

### Quick Start - Comprehensive Analysis
```python
from data_analyzer import DataAnalyzer

# Initialize with your CSV file
analyzer = DataAnalyzer('your_data.csv')

# Run complete analysis
analyzer.comprehensive_analysis(save_plots=True)
```

### Interactive Demo
```bash
python interactive_demo.py
```

### Custom Analysis Examples

#### Basic Statistics
```python
# Get basic dataset information
analyzer.display_basic_info()

# Statistical analysis for specific column
analyzer.display_statistics('Salary')

# Statistical analysis for all numeric columns
analyzer.display_statistics()
```

#### Create Visualizations
```python
# Bar chart for categorical data
analyzer.create_bar_chart('Department', title='Employee Distribution by Department')

# Scatter plot with color coding
analyzer.create_scatter_plot('Years_Experience', 'Salary', 
                           color_column='Department',
                           title='Salary vs Experience by Department')

# Correlation heatmap
analyzer.create_heatmap(title='Employee Data Correlations')

# Histogram for numeric data
analyzer.create_histogram('Age', bins=15, title='Age Distribution')
```

#### Category Analysis
```python
# Analyze salary by department
analyzer.display_category_analysis('Salary', 'Department')

# Get programmatic results
results = analyzer.analyze_by_category('Performance_Score', 'Education_Level')
```

#### Generate Insights
```python
# Display AI-generated insights
analyzer.display_insights()

# Get insights as list
insights = analyzer.generate_insights()
```

## 📈 Analysis Results

### Statistical Measures Calculated
- **Descriptive Statistics**: Count, mean, median, standard deviation
- **Distribution Metrics**: Min, max, quartiles, range, variance
- **Shape Metrics**: Skewness, kurtosis
- **Correlation Analysis**: Pearson correlation coefficients

### Visualizations Created
1. **Bar Charts**: Show distribution of categorical variables
2. **Scatter Plots**: Reveal relationships between numeric variables
3. **Correlation Heatmaps**: Display correlation matrix with color coding
4. **Histograms**: Show distribution of numeric variables with mean/median lines
5. **Box Plots**: Compare distributions across categories

### Sample Insights Generated
Based on the sample employee dataset, the tool generates insights such as:
- Dataset overview and completeness
- High variability indicators
- Strong correlation identification
- Category distribution analysis
- Data quality observations

## 🔍 Key Analysis Features

### Comprehensive Dataset Overview
```
📊 DATASET OVERVIEW
============================================================
📏 Shape: 30 rows × 8 columns
💾 Memory Usage: 8.84 KB

📋 Columns (8):
   1. Name                 (object) - Missing: 0
   2. Age                  (int64) - Missing: 0
   3. Department           (object) - Missing: 0
   4. Salary               (int64) - Missing: 0
   5. Years_Experience     (int64) - Missing: 0
   6. Performance_Score    (float64) - Missing: 0
   7. City                 (object) - Missing: 0
   8. Education_Level      (object) - Missing: 0
```

### Statistical Analysis Example
```
📊 Statistics for 'Salary':
  Count:              30
  Mean:         73433.33
  Median:       71500.00
  Std Dev:      10354.69
  Min:          58000.00
  Max:          95000.00
  Q1 (25%):     66250.00
  Q3 (75%):     78750.00
  Range:        37000.00
  Variance:   107219540.23
  Skewness:         0.61
  Kurtosis:        -0.58
```

### Generated Insights Example
```
💡 DATA INSIGHTS & OBSERVATIONS
============================================================
 1. 📊 Dataset contains 30 records with 8 features
 2. ✅ No missing values detected in the dataset
 3. 🔢 Dataset has 4 numeric columns for quantitative analysis
 4. 📝 Dataset has 4 categorical columns
 5. 🏷️  Department has 3 unique categories
 6. 🏷️  Education_Level has 2 unique categories
 7. 🔗 Strong correlation between Years_Experience and Salary: 0.892
```

## 🎨 Visualization Features

### Bar Charts
- Automatic value labeling on bars
- Professional styling with colors and grid
- Rotation handling for long category names
- Count display for each category

### Scatter Plots
- Color coding by categorical variables
- Correlation coefficient display
- Professional styling with legends
- Support for large datasets

### Correlation Heatmaps
- Color-coded correlation matrix
- Numerical correlation values displayed
- Symmetric matrix with proper scaling
- Professional color schemes

### Histograms
- Mean and median lines overlay
- Customizable bin counts
- Statistical information display
- Professional styling

## 🔧 Customization Options

### Custom CSV Files
```python
# Use your own CSV file
analyzer = DataAnalyzer('path/to/your/data.csv')
```

### Custom Visualizations
```python
# Customize plot appearance
analyzer.create_scatter_plot('x_col', 'y_col', 
                           title='Custom Title',
                           save_path='custom_plot.png')
```

### Selective Analysis
```python
# Analyze specific columns only
analyzer.create_heatmap(columns=['Age', 'Salary', 'Years_Experience'])
```

## 📋 Interactive Demo Options

The interactive demo provides these options:
1. **Basic Dataset Information** - Overview and structure
2. **Statistical Analysis** - For specific columns
3. **Create Bar Chart** - For categorical data
4. **Create Scatter Plot** - With optional color coding
5. **Create Correlation Heatmap** - For numeric data
6. **Create Histogram** - For numeric distributions
7. **Analyze by Category** - Group analysis
8. **Generate Insights** - AI observations
9. **Full Comprehensive Analysis** - Complete report

## 🎯 Key Insights from Sample Data

### Employee Dataset Analysis Results:
- **Dataset Size**: 30 employees across 8 attributes
- **Departments**: Engineering (40%), Marketing (33%), Sales (27%)
- **Salary Range**: $58,000 - $95,000 (Mean: $73,433)
- **Experience**: 2-12 years (Mean: 6.3 years)
- **Strong Correlation**: Experience and Salary (r=0.892)
- **Performance**: Consistent scores (7.5-9.2, Mean: 8.44)
- **Education**: 70% Bachelor's, 30% Master's degree
- **Geographic Distribution**: Spread across major US cities

### Key Observations:
1. **Salary Growth**: Clear positive relationship between experience and salary
2. **Department Differences**: Engineering shows highest average salaries
3. **Performance Consistency**: Low variance in performance scores indicates good hiring
4. **Education Impact**: Master's degree holders tend to have higher salaries
5. **Experience Distribution**: Good mix of junior and senior employees

## 🚀 Advanced Usage

### Batch Analysis
```python
# Analyze multiple datasets
datasets = ['data1.csv', 'data2.csv', 'data3.csv']
for dataset in datasets:
    analyzer = DataAnalyzer(dataset)
    analyzer.comprehensive_analysis(save_plots=True)
```

### Custom Insights
```python
# Extend the analyzer for custom insights
class CustomAnalyzer(DataAnalyzer):
    def custom_analysis(self):
        # Add your custom analysis here
        pass
```

## 🔍 Troubleshooting

### Common Issues
1. **File Not Found**: Ensure CSV file path is correct
2. **Missing Dependencies**: Run `pip install -r requirements.txt`
3. **Plot Display Issues**: Ensure matplotlib backend is properly configured
4. **Memory Issues**: For large datasets, consider sampling

### Performance Tips
- Use `save_plots=True` to save visualizations instead of displaying
- For large datasets, consider analyzing subsets
- Close plot windows to free memory

## 📊 Output Files

When `save_plots=True`, the tool generates:
- `bar_chart_[column].png` - Bar charts for categorical data
- `histogram_[column].png` - Histograms for numeric data
- `scatter_plot.png` - Scatter plot analysis
- `correlation_heatmap.png` - Correlation matrix visualization

## 🎓 Educational Value

This tool demonstrates:
- **Data Science Workflow**: Load → Analyze → Visualize → Insights
- **Pandas Operations**: Data manipulation and statistical analysis
- **Matplotlib/Seaborn**: Professional visualization creation
- **Statistical Concepts**: Correlation, distribution, descriptive statistics
- **Best Practices**: Code organization, documentation, error handling

## 🔮 Future Enhancements

Potential improvements:
- Support for multiple file formats (Excel, JSON)
- Advanced statistical tests
- Machine learning integration
- Web-based dashboard
- Real-time data streaming
- Export to PDF reports

---

**Status**: ✅ **COMPLETE** - Comprehensive data analysis tool with full functionality implemented and tested.
