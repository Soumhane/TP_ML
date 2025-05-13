print('hello Streamlit')

#cd C:\Users\dell\Downloads\TP
#python tp06.py 

#how to run streamlit app in anaconda prompt : streamlit run  tp06.py
import streamlit as st 
import pandas as pd
st.write('Hello, world! this is a Streamlit app.')
st.title('My Streamlit App')
st.text('This is a simple texte element.')

#choix dans une liste déroulante (dans la sidebar)
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

#slider
age = st.slider("Quel age avez vous ?", 0, 100, 25)
st.write(f"Vous avez {age} ans.") 

import numpy as pd
#Checkbox
if st.checkbox("Afficher un tableau aléatoire"):
    st.write(pd.DataFrame(np.random.randn(5,3), columns=['A','B','C']))
    