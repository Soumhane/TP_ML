#Importation des librairies
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.compose import make_column_selector as selector
from sklearn.preprocessing import OrdinalEncoder
from sklearn.linear_model import  Ridge
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import plotly.express as px

st.write('This is My Streamlit App for the Exam')
st.title('Smaallah Zahra')

graph_type = st.selectbox('Choisissez un type de graphique :',["Ligne","Barres","Aucun"])
st.write(f"vous avez choisi le type graphique : {graph_type}") 

#Upload csv file:
uploaded_file= st.file_uploader("Téléchargez un fichier CSV", type=["csv"])
if uploaded_file is not None:
    #display panda dataframe 
    df = pd.read_csv(uploaded_file)
    st.write("Voici un aperçu de votre fichier :")
    st.dataframe(df.head())

    #affichae du graphique en fonction de type choisi
    if graph_type == "Ligne":
        st.line_chart(df)
    elif graph_type == "Barres" :
        st.bar_char(df)
    else :
        st.write("Aucun graphique sélectionner.")
st.write("Merci d'avoir utilisé notre application Streamlit !")

#Graphique des données 
st.title("Graphique des données")
df_raw = pd.read_csv
fig = px.scatter(df_raw, x=df_raw['Prix Unitaire'], y=df_raw['Total'])
st.plotly_chart(fig, use_container_width=True) 

#Corrélations
All_columns =  df_raw.columns
features_input_col = []
for n in range(len(All_columns)):
    col_name = All_columns[n]
    if ("eges" in col_name):
        break
    if "id" not in col_name:
        features_input_col.extend([col_name])

st.title("Numeric Correlations")
df_features_in = pd.DataFrame(df_raw, columns=features_input_col)
st.write(df_features_in.corrwith(df_raw["Total"], numeric_only=True).sort_values(ascending=True)[:5])

st.markdown("features with low correlation (But not included categorical)")
st.write(df_features_in.corrwith(df_raw["Total"], numeric_only=True).sort_values(ascending=False)[:5])

st.title("Categorical Correlations")
st.markdown('Creating dummies for categorical features')
df_d= pd.get_dummies(df_features_in)
st.dataframe(df_d.head(10))

st.markdown("features with correlation to HIGH Total:")
st.write(df_d.corrwith(df_raw["Total"]).sort_values(ascending=False)[:5])
st.markdown("features with correlation to LOW Total:")
st.write(df_d.corrwith(df_raw["Total"]).sort_values()[:5])

