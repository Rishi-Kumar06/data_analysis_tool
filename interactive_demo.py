"""
Interactive Demo for Data Analysis Tool
Allows users to explore specific aspects of the data analysis
"""

from data_analyzer import DataAnalyzer
import matplotlib.pyplot as plt

def main():
    """Interactive demo of the data analysis tool"""
    print("🎯 Interactive Data Analysis Demo")
    print("="*50)
    
    # Initialize analyzer
    analyzer = DataAnalyzer('sample_data.csv')
    
    print("\n📊 Available Analysis Options:")
    print("1. Basic Dataset Information")
    print("2. Statistical Analysis for Specific Column")
    print("3. Create Bar Chart")
    print("4. Create Scatter Plot")
    print("5. Create Correlation Heatmap")
    print("6. Create Histogram")
    print("7. Analyze by Category")
    print("8. Generate Insights")
    print("9. Full Comprehensive Analysis")
    print("0. Exit")
    
    while True:
        try:
            choice = input("\n🔍 Enter your choice (0-9): ").strip()
            
            if choice == '0':
                print("👋 Thank you for using the Data Analysis Tool!")
                break
            elif choice == '1':
                analyzer.display_basic_info()
            elif choice == '2':
                print("\nAvailable numeric columns:", analyzer.df.select_dtypes(include=['number']).columns.tolist())
                column = input("Enter column name for statistical analysis: ").strip()
                analyzer.display_statistics(column)
            elif choice == '3':
                print("\nAvailable categorical columns:", analyzer.df.select_dtypes(include=['object']).columns.tolist())
                column = input("Enter column name for bar chart: ").strip()
                analyzer.create_bar_chart(column)
            elif choice == '4':
                numeric_cols = analyzer.df.select_dtypes(include=['number']).columns.tolist()
                print(f"\nAvailable numeric columns: {numeric_cols}")
                x_col = input("Enter X-axis column: ").strip()
                y_col = input("Enter Y-axis column: ").strip()
                
                categorical_cols = analyzer.df.select_dtypes(include=['object']).columns.tolist()
                print(f"Available categorical columns for color coding: {categorical_cols}")
                color_col = input("Enter color column (optional, press Enter to skip): ").strip()
                color_col = color_col if color_col else None
                
                analyzer.create_scatter_plot(x_col, y_col, color_column=color_col)
            elif choice == '5':
                analyzer.create_heatmap()
            elif choice == '6':
                numeric_cols = analyzer.df.select_dtypes(include=['number']).columns.tolist()
                print(f"\nAvailable numeric columns: {numeric_cols}")
                column = input("Enter column name for histogram: ").strip()
                analyzer.create_histogram(column)
            elif choice == '7':
                numeric_cols = analyzer.df.select_dtypes(include=['number']).columns.tolist()
                categorical_cols = analyzer.df.select_dtypes(include=['object']).columns.tolist()
                print(f"\nNumeric columns: {numeric_cols}")
                print(f"Categorical columns: {categorical_cols}")
                
                numeric_col = input("Enter numeric column to analyze: ").strip()
                category_col = input("Enter categorical column for grouping: ").strip()
                
                analyzer.display_category_analysis(numeric_col, category_col)
            elif choice == '8':
                analyzer.display_insights()
            elif choice == '9':
                save_plots = input("Save plots to files? (y/n): ").strip().lower() == 'y'
                analyzer.comprehensive_analysis(save_plots=save_plots)
            else:
                print("❌ Invalid choice. Please enter a number between 0-9.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")
            print("Please try again with valid inputs.")

if __name__ == "__main__":
    main()
