# Instalamos las bibliotecas que necesitaremos
import streamlit as st
import pandas as pd #Importamos esta biblioteca para poder manipular y analizar datos
import ipywidgets as widgets # Importamos el paquete de Widgets para que sea más interactivo con botones
from IPython.display import display, clear_output # Importamos para mostrar resultados o elementos (como gráficos o botones) y borrar resultados anteriores en notebooks interactivos
import matplotlib.pyplot as plt # Importamos para que se pueda generar el grafico circular
from IPython.display import display_html # Importamos la función 'display_html' para mostrar contenido HTML en notebooks de Jupyter
from IPython.display import Image, display # Importamos 'Image' para mostrar imágenes y 'display' para renderizar objetos en notebooks

df = pd.read_excel("base_de_datos.xlsx") # Carga la primera hoja del archivo Excel en un DataFrame llamado 'df'

# Generamos 3 páginas en la aplicación web de Streamlit.
# Generamos una página principal de bienvenida, otra que sea información sobre quiénes son las artistas y una tercera donde ya se podrá realizar el cuestionario

# Creamos la lista de páginas
paginas = ['Bienvenida', 'Conociendo a las artistas', 'Descubre tu canción ideal']

# Creamos botones de navegación tomando la lista de páginas
pagina_seleccionada = st.sidebar.selectbox('Selecciona una página', paginas)

# Generamos condicionales para mostrar el contenido de cada página
if pagina_seleccionada == 'Bienvenida':

    # La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
    st.markdown("<h1 style='text-align: center;'>Descubre tu match musical entre María Becerra y Taylor Swift</h1>", unsafe_allow_html=True)

    # Con esto podrá aparecer el texto 
    st.markdown("<p style='text-align: center; font-size: 20px;'>HOLAAAAAA, te damos la bienvenida a esta página hecha con mucho cariño, dedicación, risas, lágrimas, bajones y esfuerzos. Aquí podrás descubrir tu match musical ya sea con Maria becerra (reina argentina hermosa) o con Taylor Swift (reina estadounidense icónica).</p>", unsafe_allow_html=True)

    # Agregamos un subtítulo
    st.markdown("<h2 style='text-align: center;'>Las creadoras de la magia</h2>", unsafe_allow_html=True)

    st.markdown("<p style='text-align: center; font-size: 20px;'>Primero, vamos a dar una breve introducción sobre quiénes son las autoras intelectuales y pythonianas de este espacio digital:</p>", unsafe_allow_html=True)
    # <h1 style='text-align: center;'>Las creadoras de la magia</h1>: Esto es una cadena de código HTML
    # La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
    # el atributo style se utiliza para agregar estilos CSS. 
    # En este caso, el texto está alineado al centro (text-align: center;). 
    # El texto dentro de las etiquetas <h1> ("Las creadoras de la magia") es el contenido del encabezado.
    # unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
    # Por defecto, streamlit no permite HTML en el texto de Markdown.
    # Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.

    # Creamos dos columnas separadas para la imagen y el texto de la CEO Vivian
    col1, col2 = st.columns(2)

    # En la primera columna colocamos la imagen de perfil
    col1.image("foto1.jpg", caption='CEO Vivian', width=300)

    # col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
    # La función image toma como primer argumento el nombre del archivo de la imagen que se desea mostrar. 
    # En este caso, la imagen es "foto1.png". 
    # El argumento caption se utiliza para proporcionar una etiqueta a la imagen, 
    # En la segunda columna colocamos el texto de presentación personal
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

    # Creamos otras dos columnas separadas para la imagen y el texto de la CEO Adriana
    col3, col4 = st.columns(2)

    # col3, col4 = st.columns(2): Esta línea está creando otras dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col3 y col4.

    # Ahora, en la primera columna estará el texto de presentación y al costado la imagen
    col4.image("foto2.jpg", caption='CEO Adriana', width=300)

    # Escribimos el texto guardando los criterios de formato mencionados previamente
    texto_2 = """¡Holii! Soy Adriana, pero pueden decirme Adri o Adrianita. Actualmente estoy en 5to ciclo de la carrera de Publicidad. Me considero un gato negro, pero por dentro soy un schnauzer; o sea, parezco muy seria y fría, pero por dentro soy sensible, un poco miedosa de todo y me estreso rápido (tiemblo como chihuahua cuando me estreso). Me gustan los retos y soy una payasa en el buen sentido. Llevo siendo fan de Taylor Swift desde hace 5 años; las personas que me conocen saben que me gusta decir: “De hecho, Taylor tiene una canción sobre esto.” ¡Entonces, aquí estamos!"""
    # Las comillas triples (""") en Python se utilizan para definir cadenas multilínea.
    # Mostramos el texto
    col3.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_2}</div>", unsafe_allow_html=True)

elif  pagina_seleccionada == 'Conociendo a las artistas': # Posibilita pasar a la otra página

    # Agregamos un título
    st.markdown("<h1 style='text-align: center;'>Conociendo a las artistas</h1>", unsafe_allow_html=True)
    # Agregamos el texto breve
    st.markdown("<p style='text-align: center; font-size: 20px;'>Si llegaste a este cuestionario, es muy probable que ya conozcas a María Becerra y Taylor Swift. Pero, por si no es así, a continuación te ofrecemos una breve presentación de quién es cada una:</p>", unsafe_allow_html=True)

    # Creamos dos columnas separadas para la imagen y el texto
    col1, col2 = st.columns(2)
    # col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
    # La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
    # Las columnas creadas se asignan a las variables col1 y col2.

    # En la primera columna colocamos la imagen de la cantante Maria Becerra
    col1.image("foto3.jpg", caption='La nena de Argentina', width=300)
    # Agregar un  texto para su breve presentación
    texto_3 = """María Becerra es una de las mejores cantantes femeninas de Argentina. La mayoría de sus canciones se caracterizan por hablar de amores que duelen, de empoderarse después de caer, y de disfrutar el deseo sin culpa. María Becerra es el claro ejemplo de que, con perseverancia y confianza, se puede lograr todo lo que una se propone; de Quilmes para el mundo, su historia inspira a soñar en grande."""
    # Mostramos el texto
    col2.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_3}</div>", unsafe_allow_html=True)

     # Creamos otras dos columnas separadas para la imagen y el texto de Taylor Swift
    col3, col4 = st.columns(2)
    # En la primera columna colocamos el texto y en la otra la imagen de la cantante
    col4.image("foto4.jpg", caption='Tay-Tay', width=300)
    texto_4 = """Taylor Swift es una cantante y compositora estadounidense mundialmente reconocida.  A lo largo de su carrera ha explorado distintos géneros, desde el country hasta el pop, el indie y el rock alternativo. Más allá de la música, ha marcado tendencia en la industria con la regrabación de sus antiguos álbumes, defendiendo la propiedad de su arte y dejando un mensaje claro sobre el poder y la autonomía de las artistas mujeres en la industria musical."""
    # Mostramos el texto
    col3.markdown(f"<div style='text-align: justify; font-size: 15px;'>{texto_4}</div>", unsafe_allow_html=True)
    
else:

    # Agregamos un título para la página de gráficos
    st.markdown("<h1 style='text-align: center;'>Descubre tu cancion ideal</h1>", unsafe_allow_html=True)
# Convertimos los valores numéricos que vienen como texto (como '2.5M' o '300K') a enteros.
    def convertir_valor(valor):
        if isinstance(valor, str):
            valor = valor.replace(",", "").strip().upper() # Quitamos comas, espacios en blanco y convertimos a mayúsculas
            if valor.endswith("M"):
                return int(float(valor[:-1]) * 1_000_000) # Si el valor termina en 'M' (millones), lo convertimos a número multiplicando por 1,000,000
            elif valor.endswith("K"):
                return int(float(valor[:-1]) * 1_000) # Si el valor termina en 'K' (miles), lo convertimos a número multiplicando por 1,000
            elif valor.replace('.', '', 1).isdigit():
                return int(float(valor)) # Si el valor es un número decimal como string, lo convertimos a entero
        try: 
            return int(valor) # Intenta convertir el valor a entero
        except: # Captura solo errores comunes de conversión
            return 0 # Si no se puede convertir, devuelve 0

    # Creamos una diccionario con las preguntas y respuestas visibles
    preguntas = [
        ("¿Qué frase es compatible con la emoción que domina tu día hoy?",
        {
            "a": ("Hoy estoy vibrando alto, me siento joya", ["Euforia", "Amor"]), #Los corchetes son las emociones asociadas que son invisibles al espectador
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

    respuestas = [] # Lista vacía para almacenar respuestas del usuario 
    emociones = [] # Lista vacía para guardar emociones asociadas a las respuestas 

    # Mostrar preguntas y recolectar emociones
    for idx, (pregunta, opciones) in enumerate(preguntas): # Recorre cada pregunta y sus opciones con un índice
        st.subheader(f"{idx + 1}. {pregunta}") # Muestra la pregunta como subtítulo numerado en la interfaz
        opciones_ui = {texto: clave for clave, (texto, _) in opciones.items()} # Crea un diccionario con texto visible como clave y su "clave interna" como valor
        seleccion_texto = st.radio("Selecciona una opción:", list(opciones_ui.keys()), key=f"q_{idx}") # Muestra las opciones como botones de selección única (radio buttons)
        clave_elegida = opciones_ui[seleccion_texto] # Recupera la clave interna de la opción seleccionada
        respuestas.append(seleccion_texto) # Guarda la respuesta seleccionada por el usuario (el texto visible)
        emociones.extend(opciones[clave_elegida][1]) # Añade las emociones asociadas a esa opción (asumimos que es una lista)

    if st.button("🎶 Ver recomendación musical"): # Muestra un botón que al hacer clic ejecuta el siguiente bloque
        if not emociones: # Verifica si la lista de emociones está vacía
            st.warning("Por favor responde al menos una pregunta.") # Muestra una advertencia si no se respondió nada
        else:
            conteo = pd.Series(emociones).value_counts() # Cuenta cuántas veces aparece cada emoción
            emocion_top = conteo.idxmax() # Identifica la emoción más frecuente

            # Recomendación musical
            recomendacion = df[df['Sentimiento'].str.contains(emocion_top, case=False)] # Filtra el DataFrame para encontrar canciones donde la columna 'Sentimiento' contiene la emoción más frecuente (ignorando mayúsculas/minúsculas)
            if not recomendacion.empty:
                cancion = recomendacion.iloc[0] # Si hay al menos una coincidencia, toma la primera canción del resultado filtrado
                st.success(f"🎵 Canción recomendada: **{cancion['Canción']}** - *{cancion['Artista']}*") # Muestra el título y artista de la canción 
                st.video(cancion['URL video']) # Muestra el video (de YouTube u otra plataforma) usando la URL de video
                st.image(cancion['URL portada'], caption="Portada", width=300) # Muestra la imagen de la portada del álbum/canción con un ancho de 300px
                 # Convierte los valores de reproducción en Spotify y YouTube a enteros seguros usando una función personalizada
                spotify_reps = convertir_valor(cancion['Numero de reproducciones en spotify'])
                youtube_reps = convertir_valor(cancion['Cantidad de visualizaciones en youtube'])

                st.markdown(f"**🎧 Reproducciones en Spotify:** {spotify_reps:,}") # Muestra el número de reproducciones en Spotify, con formato de miles (ej: 1,000,000), usando negrita y emoji
                st.markdown(f"**📹 Reproducciones en YouTube:** {youtube_reps:,}") # Muestra las visualizaciones en YouTube con el mismo formato

                st.markdown("**🎤 Letra (fragmento):**") # Título en negrita para presentar un fragmento de la letra de la canción
                st.text(cancion['Letra'][:700] + "...") # Muestra los primeros 700 caracteres de la letra como texto plano, seguido de puntos suspensivos

                # Gráfico de pastel
                # Filtra las canciones que coinciden con las emociones detectadas, y cuenta cuántas veces aparece cada artista
                conteo_artistas = df[df['Sentimiento'].isin(conteo.index)]['Artista'].value_counts()
                fig, ax = plt.subplots() # Crea una figura y un eje con Matplotlib para graficar
                colores = ['#4a07a2', '#ff9a9a'] # Define una lista de colores personalizados para la gráfica
                conteo_artistas.plot.pie(autopct='%1.1f%%', colors=colores, ax=ax) # Dibuja la gráfica de pastel con porcentajes, usando los colores definidos y el eje creado
                ax.set_ylabel("") # Quita la etiqueta del eje Y (para que se vea más limpio)
                ax.set_title("¿Con qué artista haces más match emocional?") # Título de la gráfica
                st.pyplot(fig) # Muestra la gráfica en Streamlit
            else:
                st.error("No encontramos una canción exacta, pero igual escucha sus canciones que son las mejores!! 😉") # Si no se encontró ninguna coincidencia exacta antes, muestra un mensaje de error divertido y positivo
    
