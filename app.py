import streamlit as st

st.title("Mis Problemas de Matemáticas")

problemas = [
    ("19. Campo de fútbol (perímetro 390m, 45m más largo que ancho)", "75m y 120m"),
    ("20. Alumnos en la ESO (fracciones)", "180"),
    ("21. Obra (10 albañiles, 4 peones, 2844€ en total)", "226€ y 146€"),
    ("22. Quiniela (Mónica, Berta y Andrea)", "9000€, 4500€ y 1500€"),
    ("23. Árboles en vivero (olivos, almendros, cerezos)", "300"),
    ("24. Edades (hija 18, madre 50, ¿cuándo el doble?)", "14"),
    ("25. Dividir 72 (cocientes 6 y 8, suma 11)", "24 y 48")
]

for i, (pregunta, solucion) in enumerate(problemas):
    st.subheader(f"Problema {i + 19}")
    st.write(pregunta)
    respuesta = st.text_input(f"Tu respuesta para el {i + 19}:", key=f"p{i}")
    if st.button(f"Comprobar {i + 19}", key=f"b{i}"):
        if respuesta.lower() in solucion.lower():
            st.success("¡Correcto!")
        else:
            st.error(f"Incorrecto. La solución es: {solucion}")
    st.divider()
