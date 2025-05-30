import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load gene expression data
df = pd.read_csv("sample_data.csv")

# Set page config
st.set_page_config(page_title="Gene Expression Explorer", layout="wide")

# Toggle between light and dark theme
theme = st.sidebar.selectbox("🌗 Theme", ["Light", "Dark"])

# Custom CSS for light and dark themes
light_css = """
    <style>
    .reportview-container {
        background-color: #f9f9f9;
    }
    h1, h2, h3 {
        color: #004080;
    }
    </style>
"""

dark_css = """
    <style>
    .reportview-container {
        background-color: #1e1e1e;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #333333;
        color: white;
    }
    h1, h2, h3 {
        color: #66ccff;
    }
    </style>
"""

# Apply the chosen theme
if theme == "Dark":
    st.markdown(dark_css, unsafe_allow_html=True)
else:
    st.markdown(light_css, unsafe_allow_html=True)

# Title and welcome section
st.title("🧬 Gene Expression Explorer")
st.markdown("Welcome! This tool helps you explore gene activity in **healthy vs disease** samples using real patient data. Enter a gene to begin.")

# Sidebar input
st.sidebar.header("🔍 Search Options")
gene = st.sidebar.text_input("Enter Gene Name (e.g., TP53)").upper()

# Main expression plot section
if gene:
    gene_row = df[df['Gene'].str.upper() == gene]

    if not gene_row.empty:
        st.subheader(f"📊 Expression Levels for **{gene}**")
        expression_values = gene_row.iloc[0, 1:]
        labels = gene_row.columns[1:]

        st.dataframe(pd.DataFrame({'Sample': labels, 'Expression': expression_values.values}))

        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x=labels, y=expression_values.values, palette="deep", ax=ax)
        ax.set_ylabel("Expression Level")
        ax.set_xlabel("Sample")
        ax.set_title(f"Gene: {gene}")
        st.pyplot(fig)
    else:
        st.warning("⚠️ Gene not found in dataset. Please try another.")
else:
    st.info("Enter a gene name in the sidebar to begin.")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Gene Expression Data © GEO")
