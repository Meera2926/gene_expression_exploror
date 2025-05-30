import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# Load gene expression data
df = pd.read_csv("sample_data.csv")

# Set page configuration
st.set_page_config(page_title="Gene Expression Explorer", layout="wide")

# Load DNA background image and set as background
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .glass {{
        background: rgba(0, 0, 0, 0.6);
        border-radius: 16px;
        padding: 2rem;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 2rem auto;
        max-width: 900px;
        color: #ffffff;
    }}
    h1, h2, h3 {{
        color: #00ccff;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Apply background and styling
set_background("dna_bg.png")

# Begin app content inside styled div
st.markdown('<div class="glass">', unsafe_allow_html=True)

st.title("🧬 Gene Expression Explorer")
st.markdown("Welcome! Use this tool to explore gene activity across healthy and disease samples using real datasets.")

# Sidebar input
st.sidebar.header("🔍 Search Options")
gene = st.sidebar.text_input("Enter Gene Name (e.g., TP53)").upper()

# Display expression data
if gene:
    gene_row = df[df['Gene'].str.upper() == gene]

    if not gene_row.empty:
        st.subheader(f"📊 Expression Levels for **{gene}**")
        expression_values = gene_row.iloc[0, 1:]
        labels = gene_row.columns[1:]

        st.dataframe(pd.DataFrame({'Sample': labels, 'Expression': expression_values.values}))

        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x=labels, y=expression_values.values, palette="cool", ax=ax)
        ax.set_ylabel("Expression Level")
        ax.set_xlabel("Sample")
        ax.set_title(f"Gene: {gene}")
        st.pyplot(fig)
    else:
        st.warning("⚠️ Gene not found in dataset. Please try another.")
else:
    st.info("Enter a gene name in the sidebar to begin.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Gene Expression Data © GEO")

# Close styled div
st.markdown('</div>', unsafe_allow_html=True)
