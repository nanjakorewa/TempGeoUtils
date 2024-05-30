import streamlit as st
import pandas as pd
from Geoguessr_Util.japan_heatmap import japan_heatmap_make as jhm
import japanize_matplotlib as jam


st.markdown("## Geoguessr_Util")
st.markdown("Powered by [ysdcrys/Geoguessr_Util](https://github.com/ysdcrys/Geoguessr_Util)")

col1, col2 = st.columns(2)

with col1:
    uploaded_files = st.file_uploader("CSVファイルがある場合はアップロードしてください", accept_multiple_files=False)

    st.markdown("valueを編集してください")
    if uploaded_files:
        df = pd.read_csv(uploaded_files)
        edited_df1 = st.data_editor(df, num_rows="dynamic") 
    else:
        df = pd.read_csv("input_template.csv")
        edited_df1 = st.data_editor(df.tail(47), num_rows="dynamic") 

with col2: 
    title = st.text_input("図のタイトル", "タイトル")

f = jhm.map_draw(edited_df1, title=title)
st.pyplot(f)