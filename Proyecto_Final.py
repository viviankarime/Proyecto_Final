# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# Abrimos el folder desde visual Studio Code 
# Primero creamos un entorno virtual para instalar Streamlit y otras librerías que necesitemos.
# python -m venv .venv
# Esto nos permite crear un entorno virtual donde instalaremos Streamlit y observaremos la página web que se está generando en este script.

# Luego activamos el entorno virtual.
# En Windows:
# .venv\Scripts\activate

# Acontinuación instalamos Streamlit 
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# streamlit hello

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
# streamlit run your_script.py
# python -m streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st
import pandas as pd #Importamos esta biblioteca para poder manipular y analizar datos
import ipywidgets as widgets # Importamos el paquete de Widgets para que sea más interactivo con botones
from IPython.display import display, clear_output # Importamos para mostrar resultados o elementos (como gráficos o botones) y borrar resultados anteriores en notebooks interactivos
import matplotlib.pyplot as plt # Importamos para que se pueda generar el grafico circular
from IPython.display import display_html
from IPython.display import Image, display

df = pd.read_excel("base_de_datos.xlsx")
# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal, otra donde contaran su experiencia aprendiendo a programar y una tercera donde presentarán sus gráficos.

# Creamos la lista de páginas
paginas = ['Bienvenida', 'Conociendo a las artistas', 'Descubre tu canción ideal']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Bienvenida':

    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>Descubre tu match musical entre María Becerra y Taylor Swift</h1>", unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center; font-size: 20px;'>HOLAAAAAA, te damos la bienvenida a esta página hecha con mucho cariño, dedicación, risas, lágrimas, bajones y esfuerzos. Aquí podrás descubrir tu match musical ya sea con Maria becerra (reina argentina hermosa) o con Taylor Swift (reina estadounidense icónica).</p>", unsafe_allow_html=True)

    # Agregamos un subtítulo
    st.markdown("<h2 style='text-align: center;'>Las creadoras de la magia</h2>", unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; font-size: 20px;'>Primero, vamos a dar una breve introducción sobre quiénes son las autoras intelectuales y pythonianas de este espacio digital:</p>", unsafe_allow_html=True)
    # <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # Pueden agregar emojis en el texto de Markdown utilizando códigos de emoji, por ejemplo:
    # <h1 style='text-align: center;'>Aquí escribe un nombre creativo para tu blog 📝</h1>
    # También pueden personalizar el color del texto utilizando el atributo style, por ejemplo:
    # <h1 style='text-align: center; color: blue;'>Nombre de tu blog</h1>
    # El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil
    col1.image("foto1.jpg", caption='CEO Vivian', width=300)

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

    texto = """Holaaaaaa, soy Vivian :) Al momento en el que escribo esto tengo 19 años, nací el 12 de abril, igual que Vegetta777. Tengo una perrita llamada Kiki, ella es icónica y tiene una personalidad bien definida. Disfruto estar con las personas que me hacen sentir segura y feliz: mi mamá, mi familia y mis amistades. Me encanta reflexionar sobre aspectos de la vida y ver videos hopecore. Mi artista favorita que admiro mucho es María Becerra. Soy una jubilada de Club Penguin (buenos tiempos). Me gusta bailar, cantar, escuchar música, hacer manualidades, dormir, comer, entre otras cositas lokotronas que me dan vida."""

    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    
    # Mostramos el texto
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
    # La etiqueta <div> se utiliza para agrupar contenido en HTML. 
    # En este caso, el texto está justificado (text-align: justify;). 
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto} se reemplaza por el valor de la variable texto.

    # Creamos dos columnas separadas para la imagen y el texto
    col3, col4 = st.columns(2)

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil
    col4.image("foto2.jpg", caption='CEO Adriana', width=300)

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

    texto_2 = """¡Holii! Soy Adriana, pero pueden decirme Adri o Adrianita. Actualmente estoy en 5to ciclo de la carrera de Publicidad. Me considero un gato negro, pero por dentro soy un schnauzer; o sea, parezco muy seria y fría, pero por dentro soy sensible, un poco miedosa de todo y me estreso rápido (tiemblo como chihuahua cuando me estreso). Me gustan los retos y soy una payasa en el buen sentido. Llevo siendo fan de Taylor Swift desde hace 5 años; las personas que me conocen saben que me gusta decir: “De hecho, Taylor tiene una canción sobre esto.” ¡Entonces, aquí estamos!"""

    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    
    # Mostramos el texto
    col3.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
    # La etiqueta <div> se utiliza para agrupar contenido en HTML. 
    # En este caso, el texto está justificado (text-align: justify;). 
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto} se reemplaza por el valor de la variable texto.

elif  pagina_seleccionada == 'Conociendo a las artistas':

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>Conociendo a las artistas</h1>", unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; font-size: 20px;'>Si llegaste a este cuestionario, es muy probable que ya conozcas a María Becerra y Taylor Swift. Pero, por si no es así, a continuación te ofrecemos una breve presentación de quién es cada una:</p>", unsafe_allow_html=True)

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil
    col1.image("foto3.jpg", caption='La nena de Argentina', width=300)
    # Agregar un  texto para la respuesta
    texto_3 = """María Becerra es una de las mejores cantantes femeninas de Argentina. La mayoría de sus canciones se caracterizan por hablar de amores que duelen, de empoderarse después de caer, y de disfrutar el deseo sin culpa. María Becerra es el claro ejemplo de que, con perseverancia y confianza, se puede lograr todo lo que una se propone; de Quilmes para el mundo, su historia inspira a soñar en grande."""

    # Mostramos el texto
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_3}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
    # La etiqueta <div> se utiliza para agrupar contenido en HTML.
    # En este caso, el texto está justificado (text-align: justify;).
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto_2.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto_2} se reemplaza por el valor de la variable texto.

     # Creamos dos columnas separadas para la imagen y el texto
    col3, col4 = st.columns(2)

    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de perfil
    col4.image("foto4.jpg", caption='Tay-Tay', width=300)

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "ellie.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # en este caso "Aquí puedes escribir una etiqueta debajo de la imagen". 
    # El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

    # En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
    # Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
    # ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?

    texto_4 = """Taylor Swift es una cantante y compositora estadounidense mundialmente reconocida.  A lo largo de su carrera ha explorado distintos géneros, desde el country hasta el pop, el indie y el rock alternativo. Más allá de la música, ha marcado tendencia en la industria con la regrabación de sus antiguos álbumes, defendiendo la propiedad de su arte y dejando un mensaje claro sobre el poder y la autonomía de las artistas mujeres en la industria musical."""

    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    
    # Mostramos el texto
    col3.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_4}</div>", unsafe_allow_html=True)

    # <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
    # La etiqueta <div> se utiliza para agrupar contenido en HTML. 
    # En este caso, el texto está justificado (text-align: justify;). 
    # El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
    # El texto dentro de las etiquetas <div> es la variable texto.
    # f"": Esto es un f-string en Python.
    # Permite insertar el valor de una variable directamente en la cadena. 
    # En este caso, {texto} se reemplaza por el valor de la variable texto.
    
else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'>Descubre tu cancion ideal</h1>", unsafe_allow_html=True)

    def convertir_valor(valor):
        if isinstance(valor, str):
            valor = valor.replace(",", "").strip().upper()
            if valor.endswith("M"):
                return int(float(valor[:-1]) * 1_000_000)
            elif valor.endswith("K"):
                return int(float(valor[:-1]) * 1_000)
            elif valor.replace('.', '', 1).isdigit():
                return int(float(valor))
        try:
            return int(valor)
        except:
            return 0

    # Lista de preguntas con opciones y emociones asociadas (emociones ocultas al usuario)
    preguntas = [
        ("¿Qué frase es compatible con la emoción que domina tu día hoy?",
        {
            "a": ("Hoy estoy vibrando alto, me siento joya", ["Euforia", "Amor"]),
            "b": ("Mmm la verdad no me siento del todo bien, estoy modo troste", ["Melancolía", "Tristeza"]),
            "c": ("¡Quítate tú que llegó la caballota, la perra, la diva, la potra!", ["Empoderamiento", "Coquetería"]),
            "d": ("Te amo, te amooooo (jovani reference)", ["Enamoramiento", "Amor"])
        }),
        ("¿Cómo lidias con las emociones difíciles?",
        {
            "a": ("Me fallaste, me decepcionaste, me perdiste, te odio, bye", ["Enojo", "Resentimiento"]),
            "b": ("Dénme un tiempo para procesar, necesito mi lob@ solitari@ era", ["Tristeza", "Soledad"]),
            "c": ("Vamos de fiesta, a conocer gente nueva, lokura, outfit hot", ["Coquetería", "Euforia"]),
            "d": ("Mi mente busca refugio en los recuerdos idealizados del pasado", ["Nostalgia", "Soledad"])
        }),
        ("¿Qué necesitas escuchar/hacer a veces para sentirte mejor?",
        {
            "a": ("Palabras de afirmación para recordarme mi esencia divina.", ["Empoderamiento", "Pasión"]),
            "b": ("Mis pensamientos para sobrepensar y sobreanalizar", ["Nostalgia", "Confusión"]),
            "c": ("Soltar las preocupaciones y miedos, vivir el presente con libertad", ["Libertad", "Calma"]),
            "d": ("Agradecer por lo que fue y que será, cosas buenas llegan a mi vida", ["Euforia", "Gratitud"])
        }),
        ("¿Cómo describirías tu estado amoroso actual?",
        {
            "a": ("Ando fuego uterino descontrolado intenso", ["Coquetería"]),
            "b": ("Me han dado más vueltas que un trompo", ["Confusión"]),
            "c": ("¡Extraño a cierta personita!", ["Melancolía"]),
            "d": ("Extremadamente agradecida con el de arriba que esa persona ya no es parte de mi vida", ["Gratitud"])
        }),
        ("¿Qué energía buscas en una canción ahora mismo?",
        {
            "a": ("Energía eufórica…quiero mover el esqueleto", ["Euforia"]),
            "b": ("Energía funadora… tengo ganas de funar a alguien", ["Enojo", "Resentimiento"]),
            "c": ("Energía de dios(a), ser superior, astral y poderos@", ["Empoderamiento"]),
            "d": ("Una energía donde miro a la nada y pienso en todo… TODO", ["Nostalgia"])
        }),
        ("Elige otra frase que te identifique:",
        {
            "a": ("Soy una persona libre y salvaje, soporten", ["Libertad", "Empoderamiento"]),
            "b": ("Hicieron caldo a mi corazón de pollo", ["Tristeza", "Arrepentimiento"]),
            "c": ("Soy amor y abundancia, I don't chase I attract", ["Empoderamiento", "Seguridad"]),
            "d": ("Extraño algo/alguien del pasado…lol que mal", ["Nostalgia", "Melancolía"])
        }),
    ]

    respuestas = []
    emociones = []

    # Mostrar preguntas y recolectar emociones
    for idx, (pregunta, opciones) in enumerate(preguntas):
        st.subheader(f"{idx + 1}. {pregunta}")
        opciones_ui = {texto: clave for clave, (texto, _) in opciones.items()}
        seleccion_texto = st.radio("Selecciona una opción:", list(opciones_ui.keys()), key=f"q_{idx}")
        clave_elegida = opciones_ui[seleccion_texto]
        respuestas.append(seleccion_texto)
        emociones.extend(opciones[clave_elegida][1])

    if st.button("🎶 Ver recomendación musical"):
        if not emociones:
            st.warning("Por favor responde al menos una pregunta.")
        else:
            conteo = pd.Series(emociones).value_counts()
            emocion_top = conteo.idxmax()

            # Recomendación musical
            recomendacion = df[df['Sentimiento'].str.contains(emocion_top, case=False)]
            if not recomendacion.empty:
                cancion = recomendacion.iloc[0]
                st.success(f"🎵 Canción recomendada: **{cancion['Canción']}** - *{cancion['Artista']}*")
                st.video(cancion['URL video'])
                st.image(cancion['URL portada'], caption="Portada", width=300)

                spotify_reps = convertir_valor(cancion['Numero de reproducciones en spotify'])
                youtube_reps = convertir_valor(cancion['Cantidad de visualizaciones en youtube'])

                st.markdown(f"**🎧 Reproducciones en Spotify:** {spotify_reps:,}")
                st.markdown(f"**📹 Reproducciones en YouTube:** {youtube_reps:,}")

                st.markdown("**🎤 Letra (fragmento):**")
                st.text(cancion['Letra'][:700] + "...")

                # Gráfico de pastel
                conteo_artistas = df[df['Sentimiento'].isin(conteo.index)]['Artista'].value_counts()
                fig, ax = plt.subplots()
                colores = ['#4a07a2', '#ff9a9a']
                conteo_artistas.plot.pie(autopct='%1.1f%%', colors=colores, ax=ax)
                ax.set_ylabel("")
                ax.set_title("¿Con qué artista haces más match emocional?")
                st.pyplot(fig)
            else:
                st.error("No encontramos una canción exacta, pero igual escucha sus canciones que son las mejores!! 😉")
    