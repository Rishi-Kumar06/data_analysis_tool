"""
Data Analysis Tool using Pandas and Matplotlib
Performs comprehensive data analysis and creates visualizations
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import Dict, List, Optional, Tuple
import warnings
warnings.filterwarnings('ignore')

class DataAnalyzer:
    """Main class for data analysis and visualization"""
    
    def __init__(self, csv_file_path: str):
        """
        Initialize the DataAnalyzer with a CSV file
        
        Args:
            csv_file_path: Path to the CSV file
        """
        self.csv_file_path = csv_file_path
        self.df = None
        self.load_data()
        
    def load_data(self) -> None:
        """Load data from CSV file"""
        try:
            self.df = pd.read_csv(self.csv_file_path)
            print(f"✅ Data loaded successfully from {self.csv_file_path}")
            print(f"Dataset shape: {self.df.shape}")
        except FileNotFoundError:
            print(f"❌ Error: File {self.csv_file_path} not found")
            raise
        except Exception as e:
            print(f"❌ Error loading data: {str(e)}")
            raise
    
    def basic_info(self) -> Dict:
        """Get basic information about the dataset"""
        if self.df is None:
            return {}
        
        info = {
            'shape': self.df.shape,
            'columns': list(self.df.columns),
            'data_types': dict(self.df.dtypes),
            'missing_values': dict(self.df.isnull().sum()),
            'memory_usage': self.df.memory_usage(deep=True).sum(),
            'numeric_columns': list(self.df.select_dtypes(include=[np.number]).columns),
            'categorical_columns': list(self.df.select_dtypes(include=['object']).columns)
        }
        
        return info
    
    def display_basic_info(self) -> None:
        """Display basic information about the dataset"""
        print("\n" + "="*60)
        print("📊 DATASET OVERVIEW")
        print("="*60)
        
        info = self.basic_info()
        
        print(f"📏 Shape: {info['shape'][0]} rows × {info['shape'][1]} columns")
        print(f"💾 Memory Usage: {info['memory_usage'] / 1024:.2f} KB")
        
        print(f"\n📋 Columns ({len(info['columns'])}):")
        for i, col in enumerate(info['columns'], 1):
            dtype = info['data_types'][col]
            missing = info['missing_values'][col]
            print(f"  {i:2d}. {col:<20} ({dtype}) - Missing: {missing}")
        
        print(f"\n🔢 Numeric Columns ({len(info['numeric_columns'])}):")
        print("  " + ", ".join(info['numeric_columns']))
        
        print(f"\n📝 Categorical Columns ({len(info['categorical_columns'])}):")
        print("  " + ", ".join(info['categorical_columns']))
        
        # Display first few rows
        print(f"\n📋 First 5 rows:")
        print(self.df.head().to_string())
    
    def calculate_statistics(self, column: str = None) -> Dict:
        """
        Calculate basic statistics for numeric columns
        
        Args:
            column: Specific column to analyze (optional)
            
        Returns:
            Dictionary containing statistics
        """
        if self.df is None:
            return {}
        
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        if column and column not in numeric_cols:
            print(f"❌ Column '{column}' is not numeric or doesn't exist")
            return {}
        
        if column:
            cols_to_analyze = [column]
        else:
            cols_to_analyze = numeric_cols
        
        stats = {}
        for col in cols_to_analyze:
            stats[col] = {
                'count': self.df[col].count(),
                'mean': self.df[col].mean(),
                'median': self.df[col].median(),
                'std': self.df[col].std(),
                'min': self.df[col].min(),
                'max': self.df[col].max(),
                'q25': self.df[col].quantile(0.25),
                'q75': self.df[col].quantile(0.75),
                'range': self.df[col].max() - self.df[col].min(),
                'variance': self.df[col].var(),
                'skewness': self.df[col].skew(),
                'kurtosis': self.df[col].kurtosis()
            }
        
        return stats
    
    def display_statistics(self, column: str = None) -> None:
        """Display statistics for numeric columns"""
        print("\n" + "="*60)
        print("📈 STATISTICAL ANALYSIS")
        print("="*60)
        
        stats = self.calculate_statistics(column)
        
        for col, col_stats in stats.items():
            print(f"\n📊 Statistics for '{col}':")
            print(f"  Count:      {col_stats['count']:>10.0f}")
            print(f"  Mean:       {col_stats['mean']:>10.2f}")
            print(f"  Median:     {col_stats['median']:>10.2f}")
            print(f"  Std Dev:    {col_stats['std']:>10.2f}")
            print(f"  Min:        {col_stats['min']:>10.2f}")
            print(f"  Max:        {col_stats['max']:>10.2f}")
            print(f"  Q1 (25%):   {col_stats['q25']:>10.2f}")
            print(f"  Q3 (75%):   {col_stats['q75']:>10.2f}")
            print(f"  Range:      {col_stats['range']:>10.2f}")
            print(f"  Variance:   {col_stats['variance']:>10.2f}")
            print(f"  Skewness:   {col_stats['skewness']:>10.2f}")
            print(f"  Kurtosis:   {col_stats['kurtosis']:>10.2f}")
    
    def create_bar_chart(self, column: str, title: str = None, save_path: str = None) -> None:
        """
        Create a bar chart for categorical data
        
        Args:
            column: Column name for the bar chart
            title: Custom title for the chart
            save_path: Path to save the chart (optional)
        """
        if self.df is None or column not in self.df.columns:
            print(f"❌ Column '{column}' not found")
            return
        
        plt.figure(figsize=(12, 6))
        
        # Count values and create bar chart
        value_counts = self.df[column].value_counts()
        
        bars = plt.bar(range(len(value_counts)), value_counts.values, 
                      color='skyblue', edgecolor='navy', alpha=0.7)
        
        plt.xlabel(column.replace('_', ' ').title(), fontsize=12)
        plt.ylabel('Count', fontsize=12)
        plt.title(title or f'Distribution of {column.replace("_", " ").title()}', fontsize=14, fontweight='bold')
        plt.xticks(range(len(value_counts)), value_counts.index, rotation=45, ha='right')
        
        # Add value labels on bars
        for bar, value in zip(bars, value_counts.values):
            plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                    str(value), ha='center', va='bottom', fontweight='bold')
        
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"📊 Bar chart saved to {save_path}")
        
        plt.show()
    
    def create_scatter_plot(self, x_column: str, y_column: str, 
                          color_column: str = None, title: str = None, 
                          save_path: str = None) -> None:
        """
        Create a scatter plot
        
        Args:
            x_column: Column for x-axis
            y_column: Column for y-axis
            color_column: Column for color coding (optional)
            title: Custom title for the chart
            save_path: Path to save the chart (optional)
        """
        if self.df is None:
            print("❌ No data loaded")
            return
        
        missing_cols = [col for col in [x_column, y_column] if col not in self.df.columns]
        if missing_cols:
            print(f"❌ Columns not found: {missing_cols}")
            return
        
        plt.figure(figsize=(10, 8))
        
        if color_column and color_column in self.df.columns:
            # Color-coded scatter plot
            unique_values = self.df[color_column].unique()
            colors = plt.cm.Set3(np.linspace(0, 1, len(unique_values)))
            
            for i, value in enumerate(unique_values):
                mask = self.df[color_column] == value
                plt.scatter(self.df.loc[mask, x_column], self.df.loc[mask, y_column],
                          c=[colors[i]], label=str(value), alpha=0.7, s=60)
            
            plt.legend(title=color_column.replace('_', ' ').title(), bbox_to_anchor=(1.05, 1), loc='upper left')
        else:
            # Simple scatter plot
            plt.scatter(self.df[x_column], self.df[y_column], 
                       color='coral', alpha=0.7, s=60, edgecolors='darkred')
        
        plt.xlabel(x_column.replace('_', ' ').title(), fontsize=12)
        plt.ylabel(y_column.replace('_', ' ').title(), fontsize=12)
        plt.title(title or f'{y_column.replace("_", " ").title()} vs {x_column.replace("_", " ").title()}', 
                 fontsize=14, fontweight='bold')
        
        # Add correlation coefficient if both columns are numeric
        if (self.df[x_column].dtype in ['int64', 'float64'] and 
            self.df[y_column].dtype in ['int64', 'float64']):
            correlation = self.df[x_column].corr(self.df[y_column])
            plt.text(0.05, 0.95, f'Correlation: {correlation:.3f}', 
                    transform=plt.gca().transAxes, fontsize=12, 
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"📊 Scatter plot saved to {save_path}")
        
        plt.show()
    
    def create_heatmap(self, columns: List[str] = None, title: str = None, 
                      save_path: str = None) -> None:
        """
        Create a correlation heatmap
        
        Args:
            columns: List of columns to include (optional, defaults to all numeric)
            title: Custom title for the chart
            save_path: Path to save the chart (optional)
        """
        if self.df is None:
            print("❌ No data loaded")
            return
        
        # Get numeric columns
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        
        if columns:
            # Filter to requested columns that are numeric
            columns = [col for col in columns if col in numeric_cols]
            if not columns:
                print("❌ No valid numeric columns specified")
                return
        else:
            columns = numeric_cols
        
        if len(columns) < 2:
            print("❌ Need at least 2 numeric columns for correlation heatmap")
            return
        
        # Calculate correlation matrix
        correlation_matrix = self.df[columns].corr()
        
        plt.figure(figsize=(10, 8))
        
        # Create heatmap
        sns.heatmap(correlation_matrix, 
                   annot=True, 
                   cmap='RdYlBu_r', 
                   center=0,
                   square=True,
                   fmt='.3f',
                   cbar_kws={'shrink': 0.8})
        
        plt.title(title or 'Correlation Heatmap', fontsize=14, fontweight='bold', pad=20)
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"📊 Heatmap saved to {save_path}")
        
        plt.show()
    
    def create_histogram(self, column: str, bins: int = 20, title: str = None, 
                        save_path: str = None) -> None:
        """
        Create a histogram for numeric data
        
        Args:
            column: Column name for the histogram
            bins: Number of bins
            title: Custom title for the chart
            save_path: Path to save the chart (optional)
        """
        if self.df is None or column not in self.df.columns:
            print(f"❌ Column '{column}' not found")
            return
        
        if self.df[column].dtype not in ['int64', 'float64']:
            print(f"❌ Column '{column}' is not numeric")
            return
        
        plt.figure(figsize=(10, 6))
        
        # Create histogram
        n, bins_edges, patches = plt.hist(self.df[column], bins=bins, 
                                         color='lightblue', edgecolor='navy', 
                                         alpha=0.7)
        
        # Add statistics
        mean_val = self.df[column].mean()
        median_val = self.df[column].median()
        
        plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.2f}')
        plt.axvline(median_val, color='green', linestyle='--', linewidth=2, label=f'Median: {median_val:.2f}')
        
        plt.xlabel(column.replace('_', ' ').title(), fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.title(title or f'Distribution of {column.replace("_", " ").title()}', 
                 fontsize=14, fontweight='bold')
        plt.legend()
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"📊 Histogram saved to {save_path}")
        
        plt.show()
    
    def analyze_by_category(self, numeric_column: str, category_column: str) -> Dict:
        """
        Analyze numeric data by categories
        
        Args:
            numeric_column: Numeric column to analyze
            category_column: Categorical column for grouping
            
        Returns:
            Dictionary with analysis results
        """
        if self.df is None:
            return {}
        
        if numeric_column not in self.df.columns or category_column not in self.df.columns:
            print("❌ One or both columns not found")
            return {}
        
        grouped = self.df.groupby(category_column)[numeric_column]
        
        analysis = {
            'count': grouped.count(),
            'mean': grouped.mean(),
            'median': grouped.median(),
            'std': grouped.std(),
            'min': grouped.min(),
            'max': grouped.max()
        }
        
        return analysis
    
    def display_category_analysis(self, numeric_column: str, category_column: str) -> None:
        """Display analysis by category"""
        print(f"\n" + "="*60)
        print(f"📊 ANALYSIS OF {numeric_column.upper()} BY {category_column.upper()}")
        print("="*60)
        
        analysis = self.analyze_by_category(numeric_column, category_column)
        
        if not analysis:
            return
        
        # Create a summary DataFrame
        summary_df = pd.DataFrame(analysis)
        print(summary_df.round(2).to_string())
        
        # Create box plot
        plt.figure(figsize=(12, 6))
        self.df.boxplot(column=numeric_column, by=category_column, ax=plt.gca())
        plt.title(f'{numeric_column.replace("_", " ").title()} by {category_column.replace("_", " ").title()}')
        plt.suptitle('')  # Remove default title
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def generate_insights(self) -> List[str]:
        """Generate insights based on the data analysis"""
        if self.df is None:
            return []
        
        insights = []
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        
        # Dataset overview insights
        insights.append(f"📊 Dataset contains {self.df.shape[0]} records with {self.df.shape[1]} features")
        
        # Missing data insights
        missing_data = self.df.isnull().sum()
        if missing_data.sum() > 0:
            insights.append(f"⚠️  Found missing values in {(missing_data > 0).sum()} columns")
        else:
            insights.append("✅ No missing values detected in the dataset")
        
        # Numeric columns insights
        if len(numeric_cols) > 0:
            insights.append(f"🔢 Dataset has {len(numeric_cols)} numeric columns for quantitative analysis")
            
            # Find columns with high variance
            for col in numeric_cols:
                cv = self.df[col].std() / self.df[col].mean() if self.df[col].mean() != 0 else 0
                if cv > 0.5:
                    insights.append(f"📈 {col} shows high variability (CV: {cv:.2f})")
        
        # Categorical columns insights
        if len(categorical_cols) > 0:
            insights.append(f"📝 Dataset has {len(categorical_cols)} categorical columns")
            
            for col in categorical_cols:
                unique_count = self.df[col].nunique()
                if unique_count < 10:
                    insights.append(f"🏷️  {col} has {unique_count} unique categories")
        
        # Correlation insights
        if len(numeric_cols) >= 2:
            corr_matrix = self.df[numeric_cols].corr()
            # Find strong correlations (excluding diagonal)
            strong_corrs = []
            for i in range(len(corr_matrix.columns)):
                for j in range(i+1, len(corr_matrix.columns)):
                    corr_val = corr_matrix.iloc[i, j]
                    if abs(corr_val) > 0.7:
                        strong_corrs.append((corr_matrix.columns[i], corr_matrix.columns[j], corr_val))
            
            if strong_corrs:
                for col1, col2, corr_val in strong_corrs:
                    insights.append(f"🔗 Strong correlation between {col1} and {col2}: {corr_val:.3f}")
        
        return insights
    
    def display_insights(self) -> None:
        """Display generated insights"""
        print("\n" + "="*60)
        print("💡 DATA INSIGHTS & OBSERVATIONS")
        print("="*60)
        
        insights = self.generate_insights()
        
        for i, insight in enumerate(insights, 1):
            print(f"{i:2d}. {insight}")
        
        print("\n" + "="*60)
    
    def comprehensive_analysis(self, save_plots: bool = False) -> None:
        """
        Perform comprehensive analysis of the dataset
        
        Args:
            save_plots: Whether to save plots to files
        """
        print("🚀 Starting Comprehensive Data Analysis...")
        
        # Basic information
        self.display_basic_info()
        
        # Statistical analysis
        self.display_statistics()
        
        # Get numeric and categorical columns
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        categorical_cols = self.df.select_dtypes(include=['object']).columns.tolist()
        
        # Create visualizations
        print(f"\n📊 Creating visualizations...")
        
        # Bar charts for categorical data
        for col in categorical_cols[:2]:  # Limit to first 2 categorical columns
            save_path = f"bar_chart_{col}.png" if save_plots else None
            self.create_bar_chart(col, save_path=save_path)
        
        # Histograms for numeric data
        for col in numeric_cols[:3]:  # Limit to first 3 numeric columns
            save_path = f"histogram_{col}.png" if save_plots else None
            self.create_histogram(col, save_path=save_path)
        
        # Scatter plots
        if len(numeric_cols) >= 2:
            # Create scatter plot with first two numeric columns
            color_col = categorical_cols[0] if categorical_cols else None
            save_path = "scatter_plot.png" if save_plots else None
            self.create_scatter_plot(numeric_cols[0], numeric_cols[1], 
                                   color_column=color_col, save_path=save_path)
        
        # Correlation heatmap
        if len(numeric_cols) >= 2:
            save_path = "correlation_heatmap.png" if save_plots else None
            self.create_heatmap(save_path=save_path)
        
        # Category analysis
        if numeric_cols and categorical_cols:
            self.display_category_analysis(numeric_cols[0], categorical_cols[0])
        
        # Generate and display insights
        self.display_insights()
        
        print("✅ Comprehensive analysis completed!")


def main():
    """Main function to demonstrate the data analysis tool"""
    # Initialize the analyzer with sample data
    analyzer = DataAnalyzer('sample_data.csv')
    
    # Perform comprehensive analysis
    analyzer.comprehensive_analysis(save_plots=True)
    
    print("\n" + "="*60)
    print("🎯 ANALYSIS COMPLETE")
    print("="*60)
    print("The data analysis tool has successfully:")
    print("✅ Loaded and analyzed the CSV data")
    print("✅ Calculated statistical measures")
    print("✅ Created various visualizations")
    print("✅ Generated insights and observations")
    print("✅ Saved plots to files")


if __name__ == "__main__":
    main()
