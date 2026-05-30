import streamlit as st

st.title("Calculadora de sumas")

n1 = st.number_input("Introduce el primer número")
n2 = st.number_input("Introduce el segundo número")

if st.button("Sumar"):
    resultado = n1 + n2
    st.write(f"El resultado es: {resultado}")
