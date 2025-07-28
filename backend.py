import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
import io

def analyze_financial_data(file):
    try:
        # Read file into DataFrame
        df = pd.read_csv(file) if file.filename.endswith('.csv') else pd.read_excel(file)

        # Basic summary stats
        stats = df.describe(include='all').to_dict()

        # Generate graphs for numerical columns
        plots = {}
        numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

        for col in numeric_cols:
            # Histogram
            plt.figure(figsize=(6, 4))
            sns.histplot(df[col].dropna(), kde=True)
            plt.title(f"Histogram of {col}")
            hist_buffer = io.BytesIO()
            plt.savefig(hist_buffer, format='png')
            plt.close()
            hist_buffer.seek(0)
            plots[f"{col}_hist"] = base64.b64encode(hist_buffer.read()).decode('utf-8')

            # Bar Plot (Top 10 values by frequency)
            plt.figure(figsize=(6, 4))
            top_values = df[col].value_counts().nlargest(10)
            sns.barplot(x=top_values.index, y=top_values.values)
            plt.title(f"Bar Plot of {col} (Top 10)")
            plt.xticks(rotation=45)
            bar_buffer = io.BytesIO()
            plt.savefig(bar_buffer, format='png')
            plt.close()
            bar_buffer.seek(0)
            plots[f"{col}_bar"] = base64.b64encode(bar_buffer.read()).decode('utf-8')

        return {
            "raw_data": df.head(20).to_dict(orient='records'),
            "insights": stats,
            "graphs": plots
        }
    
    except Exception as e:
        return {"error": str(e)}
