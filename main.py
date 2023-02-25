import streamlit as st
import pandas as pd
import sklearn.metrics

x = [1,1,2,2]
y = [0,1,2,2]

res = sklearn.metrics.cohen_kappa_score(x,y)

print(res)

uploaded_file1 = st.file_uploader("Person 1. Choose a XLSX file", type="xlsx")
uploaded_file2 = st.file_uploader("Person 2. Choose a XLSX file", type="xlsx")

if uploaded_file1 and uploaded_file2:
    df1 = pd.read_excel(uploaded_file1)
    df2 = pd.read_excel(uploaded_file2)


    st.table(df1)
    st.table(df2)

    scores = []

    for column in df1.columns[1:]:
        score = sklearn.metrics.cohen_kappa_score(df1[column], df2[column])
        st.write("Cohen kappa score for", column,":", score)
        scores.append(score)
    st.write("Average :", sum(scores)/len(scores))