##from utils import db_connect
##engine = db_connect()

# your code here

from pickle import load
import streamlit as st

model = load(open("models/ranfor_classifier_nestimators-100_18.pkl", "rb"))
class_dict = {"0": "No tiene probabilidad de diabetes",
              "1": "Tienes posibilidad de diabetes"}

st.title("Diabetes - Model prediction")
st.markdown("""Power by: [Anthonny maldonado]""")
st.divider()

val1 = st.slider("Embarazos", min_value=0, max_value=20, step=1)
val2 = st.slider("Glucosa", min_value=40, max_value=200, step=10)
val3 = st.slider("Presion de sangre", min_value=10, max_value=130, step=10)
val4 = st.slider("Grosor de piel", min_value=5, max_value=100, step=5)
val5 = st.slider("Insulina", min_value=5, max_value=1000, step=10)
val6 = st.slider("BMI", min_value=10, max_value=80, step=5)
val7 = st.slider("Diabetes pedigre Function", min_value=0.1, max_value=2.5, step=0.1)
val8 = st.slider("Edad", min_value=20, max_value=80, step=1)


if st.button("Predict"):
    prediction = str(model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])[0])
    pred_class = class_dict[prediction]
    st.divider()
    st.write("Prediction:", pred_class)
    st.divider()

