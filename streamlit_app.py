from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="EDAmame",
    layout="wide"
)

st.title('EDAmame')

uploaded_csv = st.file_uploader("CSVファイルをアップロードしてください",
type="csv", key="csv_uploader")
if uploaded_csv is not None:
    df_csv = pd.read_csv(uploaded_csv)

    pyg_app = StreamlitRenderer(df_csv)
    pyg_app.explorer()

