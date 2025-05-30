import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load sample gene expression data
df = pd.read_csv("sample_data.csv")  # Example CSV: Gene,Healthy_1,Healthy_2,Disease_1,Disease_2

st.title("🧬 Gene Expression Explorer")

# User Input
gene = st.text_input("Enter Gene Name (e.g., TP53):")

if gene:
    gene_row = df[df['Gene'].str.upper() == gene.upper()]

    if not gene_row.empty:
        st.subheader(f"Expression Levels for {gene.upper()}")
        values = gene_row.iloc[0, 1:]
        labels = gene_row.columns[1:]

        st.write(pd.DataFrame({'Sample': labels, 'Expression': values.values}))

        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_ylabel("Expression Level")
        ax.set_title(f"Gene: {gene.upper()}")
        st.pyplot(fig)
    else:
        st.warning("Gene not found in dataset.")
