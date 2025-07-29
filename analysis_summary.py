"""
Analysis Summary Script
Provides a quick overview of the data analysis results
"""

from data_analyzer import DataAnalyzer
import pandas as pd

def print_key_findings():
    """Print key findings from the employee dataset analysis"""
    
    print("🎯 DATA ANALYSIS SUMMARY")
    print("="*60)
    
    # Initialize analyzer
    analyzer = DataAnalyzer('sample_data.csv')
    
    # Key statistics
    print("\n📊 KEY STATISTICS:")
    print("-" * 30)
    
    # Salary analysis
    salary_stats = analyzer.calculate_statistics('Salary')['Salary']
    print(f"💰 Average Salary: ${salary_stats['mean']:,.2f}")
    print(f"💰 Salary Range: ${salary_stats['min']:,.0f} - ${salary_stats['max']:,.0f}")
    print(f"💰 Salary Std Dev: ${salary_stats['std']:,.2f}")
    
    # Experience analysis
    exp_stats = analyzer.calculate_statistics('Years_Experience')['Years_Experience']
    print(f"📈 Average Experience: {exp_stats['mean']:.1f} years")
    print(f"📈 Experience Range: {exp_stats['min']:.0f} - {exp_stats['max']:.0f} years")
    
    # Age analysis
    age_stats = analyzer.calculate_statistics('Age')['Age']
    print(f"👥 Average Age: {age_stats['mean']:.1f} years")
    print(f"👥 Age Range: {age_stats['min']:.0f} - {age_stats['max']:.0f} years")
    
    # Performance analysis
    perf_stats = analyzer.calculate_statistics('Performance_Score')['Performance_Score']
    print(f"⭐ Average Performance: {perf_stats['mean']:.2f}/10")
    print(f"⭐ Performance Range: {perf_stats['min']:.1f} - {perf_stats['max']:.1f}")
    
    print("\n🏢 DEPARTMENT BREAKDOWN:")
    print("-" * 30)
    dept_counts = analyzer.df['Department'].value_counts()
    for dept, count in dept_counts.items():
        percentage = (count / len(analyzer.df)) * 100
        print(f"{dept}: {count} employees ({percentage:.1f}%)")
    
    print("\n🎓 EDUCATION BREAKDOWN:")
    print("-" * 30)
    edu_counts = analyzer.df['Education_Level'].value_counts()
    for edu, count in edu_counts.items():
        percentage = (count / len(analyzer.df)) * 100
        print(f"{edu}: {count} employees ({percentage:.1f}%)")
    
    print("\n🔗 KEY CORRELATIONS:")
    print("-" * 30)
    numeric_cols = analyzer.df.select_dtypes(include=['number']).columns
    corr_matrix = analyzer.df[numeric_cols].corr()
    
    # Find strongest correlations
    correlations = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            corr_val = corr_matrix.iloc[i, j]
            correlations.append((corr_matrix.columns[i], corr_matrix.columns[j], corr_val))
    
    # Sort by absolute correlation value
    correlations.sort(key=lambda x: abs(x[2]), reverse=True)
    
    for col1, col2, corr_val in correlations[:3]:  # Top 3 correlations
        strength = "Strong" if abs(corr_val) > 0.7 else "Moderate" if abs(corr_val) > 0.5 else "Weak"
        print(f"{col1} ↔ {col2}: {corr_val:.3f} ({strength})")
    
    print("\n💡 KEY INSIGHTS:")
    print("-" * 30)
    insights = analyzer.generate_insights()
    for i, insight in enumerate(insights[:5], 1):  # Top 5 insights
        print(f"{i}. {insight}")
    
    print("\n📈 SALARY ANALYSIS BY DEPARTMENT:")
    print("-" * 30)
    dept_salary = analyzer.analyze_by_category('Salary', 'Department')
    for dept in dept_salary['mean'].index:
        avg_salary = dept_salary['mean'][dept]
        count = dept_salary['count'][dept]
        print(f"{dept}: ${avg_salary:,.0f} average ({count} employees)")
    
    print("\n🎯 PERFORMANCE BY EDUCATION:")
    print("-" * 30)
    edu_perf = analyzer.analyze_by_category('Performance_Score', 'Education_Level')
    for edu in edu_perf['mean'].index:
        avg_perf = edu_perf['mean'][edu]
        count = edu_perf['count'][edu]
        print(f"{edu}: {avg_perf:.2f}/10 average ({count} employees)")
    
    print("\n" + "="*60)
    print("✅ ANALYSIS COMPLETE")
    print("📊 Visualizations saved as PNG files")
    print("🔍 Run 'python interactive_demo.py' for detailed exploration")
    print("="*60)

if __name__ == "__main__":
    print_key_findings()
