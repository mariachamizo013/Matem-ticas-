import streamlit as st

st.title("Mis Problemas de Matemáticas")

problemas = [
    ("19. Un campo de fútbol tiene un perímetro de 390 metros y se sabe que es 45m más largo que ancho. Calcula las dimensiones de dicho estadio.", "75m y 120m"),
    ("20. En un colegio hay cuatro cursos de ESO. La sexta parte de los alumnos asisten a 1º, la cuarta parte a 2º, la quinta parte a 3º y a 4º la tercera parte más nueve alumnos. ¿Cuántos alumnos cursan la ESO?", "180"),
    ("21. Por una obra, en la que han trabajado 10 albañiles y 4 peones, se pagan 2.844€. Si cada peón cobra 80€ menos que cada albañil. ¿Cuánto corresponde a cada uno?", "226€ y 146€"),
    ("22. Qué cantidad de euros corresponden a cada una de las tres amigas que les toca una quiniela de 15.000€ si a Mónica le corresponde el doble que a Berta y ésta ha cobrado tres veces más que Andrea.", "9.000, 4.500 y 1.500€"),
    ("23. La tercera parte de los árboles de un vivero son olivos, los dos quintos son almendros y los ochenta restantes son cerezos. ¿Cuántos árboles hay en el vivero?", "300"),
    ("24. Cuando mi hija cumplió 18 años yo tenía 50 ¿Cuántos años tienen que pasar para que yo tenga el doble de la edad de mi hija?", "14"),
    ("25. Divide el número 72 en dos partes de manera que al dividir, una de las partes entre seis y la otra entre ocho, el resultado de la suma de sus cocientes sea once.", "24 y 48")
]

for i, (enunciado, solucion) in enumerate(problemas):
    st.subheader(f"Problema {i + 19}")
    st.write(enunciado)
    respuesta = st.text_input(f"Escribe tu solución:", key=f"p{i}")
    if st.button(f"Comprobar", key=f"b{i}"):
        if respuesta.lower() in solucion.lower():
            st.success("¡Correcto!")
        else:
            st.error(f"Incorrecto. La solución era: {solucion}")
    st.divider()
