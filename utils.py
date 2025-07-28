import pandas as pd
import fitz  # PyMuPDF
from io import StringIO

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            return "\n".join([page.get_text() for page in doc])
    elif uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        return df.to_string(index=False)
    return ""

def get_dataframe_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            text = "\n".join([page.get_text() for page in doc])
            return pd.DataFrame({'text': [text]})
    elif uploaded_file.type == "text/plain":
        text = uploaded_file.read().decode("utf-8")
        return pd.DataFrame({'text': [text]})
    elif uploaded_file.type == "text/csv":
        return pd.read_csv(uploaded_file)
    return None

def get_aggregated_stats(df):
    df = df.copy()

    # First try to find financial measures
    if 'Measure' in df.columns and 'Value' in df.columns:
        agg_data = df[df['Measure'].isin(['Revenue', 'Net Income', 'EPS'])].copy()
        agg_data['Value'] = agg_data['Value'].astype(str).str.extract(r'([\d.]+)').astype(float)
        return agg_data

    # If not, try to summarize any numeric data
    numeric_cols = df.select_dtypes(include=['number']).columns

    if len(numeric_cols) > 0:
        agg_summary = df[numeric_cols].agg(['mean', 'median', 'min', 'max', 'sum', 'count']).transpose().reset_index()
        agg_summary.columns = ['Measure', 'Mean', 'Median', 'Min', 'Max', 'Sum', 'Count']
        return agg_summary

    # Fallback if no numeric data found
    return pd.DataFrame(columns=['Measure', 'Mean', 'Median', 'Min', 'Max', 'Sum', 'Count'])
