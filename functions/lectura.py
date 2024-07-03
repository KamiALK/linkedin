import os
import sys

# Agrega la ruta del directorio padre al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# logica para leer los campos que necesesito
import conection.DocModul as googledocs


"""
Lectura de los documentos 
"""
document_content = googledocs.texto()
google_docs_text = googledocs.diccionario(document_content)
# print(type(google_docs_text))


"""
Datos principales
"""
mi_nombre = google_docs_text[1]
cargo_principal = google_docs_text[3]
ref_uno_academic_content = google_docs_text[17]
ref_dos_academic_content = google_docs_text[28]

perfil_profesional = """Redactar en tercera persona y no inicies con mi nombre simplemente con el cargo, 6 renglones , intentar incluir  Conocimientos inherentes al cargo tecnicos 
los escenciales,Habilidades blandas:Flexibilidad cognitiva,Gestion de crisis,Gestion de tiempo,Adaptibilidad al entorno,
Adaptabilidad al cambio,Capacidad de aprendizaje,Capacidad de seguir instrucciones,Inteligencia emocional,Comunicacion 
efectiva y comunicacion asertiva  y no coloques todas las habilidades sino las mas relevantes para el cargoNo repetir palabras y a menos que sean programas o herramientas"""

logros_cuantititativos = """" """

propuesta_de_valor = """ Lo maximo que puedo hacer por una compania  con todo lo que es sabe y ha hecho Verbo en primera persona 
presente alineado al tipo de cargo jerárquico, No verbos en infinitivo Muestra mi potencial, Que ofrece a quien como es el objetivo
y cual es mi estrategia como lo hago como lo consigo intentar incluir cualquiera de estos verbos:Consigo, Ejecuto, Lidero, 
Garantizo, Implemnento, Desarrollo, Solucion a la necesidad que esta alineada a la oferta laboral, Cumplir con esa necesidad que
pide el cargo, Objetivo del cargo, Redanctar en 4 renglones No repetir palabras y a menos que sean programas o herramientas
"""

"""
perfil profersional 
"""
titulo_perfil_profesional = google_docs_text[8]
contenido_perfil_profesional = google_docs_text[10]

# vacante 1
nombre_vacante_1 = google_docs_text[42]
contenido_vacante_1 = google_docs_text[43]
tool_uno_1 = google_docs_text[45]
tool_dos_1 = google_docs_text[46]
tools_tres_1 = google_docs_text[47]
prog_utiliozados_1 = google_docs_text[51]
teck_stash_1 = google_docs_text[54]

# vacante 2
nombre_vacante_2 = google_docs_text[64]
contenido_vacante_2 = google_docs_text[66]
tool_uno_2 = google_docs_text[67]
tool_dos_2 = google_docs_text[68]
tools_tres_2 = google_docs_text[69]
prog_utiliozados_uno_2 = google_docs_text[74]
teck_stash_2 = google_docs_text[72]

# vacante 3
nombre_vacante_3 = google_docs_text[77]
contenido_vacante_3 = google_docs_text[79]
tool_uno_3 = google_docs_text[80]
tool_dos_3 = google_docs_text[81]
tools_tres_3 = google_docs_text[82]
prog_utiliozados_3 = google_docs_text[87]
teck_stash_3 = google_docs_text[85]

titulo_skill_intereses = google_docs_text[90]
technical = google_docs_text[95]
lenguage = google_docs_text[99]
intereses = google_docs_text[102]

"""
propuesta de valor 
"""
titulo_propuesta_valor = google_docs_text[105]
contenido_propuesta_valor = google_docs_text[107]

prueba = {
    "mi_nombre": [google_docs_text[1]],
    "cargo_principal ": [google_docs_text[3]],
    "titulo_perfil_profesional": [google_docs_text[8]],
    "contenido_perfil_profesional": [google_docs_text[10]],
    "nombre_experiencia_1": [google_docs_text[3]],
    "contenido_experiencia_1": [google_docs_text[43]],
    "tool_uno_1": [google_docs_text[45]],
    "google_docs_text": [google_docs_text[46]],
    "tools_tres_1": [google_docs_text[47]],
    "prog_utiliozados_1": [google_docs_text[51]],
    "teck_stash_1": [google_docs_text[54]],
    "nombre_experiencia_2": [google_docs_text[64]],
    "contenido_experiencia_2": [google_docs_text[66]],
    "tool_uno_2": [google_docs_text[67]],
    "tool_dos_2": [google_docs_text[68]],
    "tools_tres_2": [google_docs_text[69]],
    "prog_utiliozados_uno_2": [google_docs_text[74]],
    "teck_stash_2": [google_docs_text[72]],
    "nombre_experiencia_3": [google_docs_text[77]],
    "contenido_experiencia_3": [google_docs_text[79]],
    "tool_uno_3": [google_docs_text[80]],
    "tool_dos_3": [google_docs_text[81]],
    "tools_tres_3": [google_docs_text[82]],
    "prog_utiliozados_3": [google_docs_text[87]],
    "teck_stash_3": [google_docs_text[85]],
    "titulo_skill_intereses": [google_docs_text[90]],
    "technical": [google_docs_text[95]],
    "lenguage": [google_docs_text[99]],
    "intereses": [google_docs_text[102]],
    "titulo_propuesta_valor": [google_docs_text[105]],
    "contenido_propuesta_valor": [google_docs_text[107]],
}

job_title = """"
Estamos en la búsqueda de un Data Analyst Jr. (Analista Junior)
Profesional graduado en admón, economía, ingeniería, estadística o afines con experiencia en análisis de datos, inteligencia de negocios y manejo de datos, modelos relacionales y predictivos, con excelentes habilidades de comunicación y capacidad para presentar resultados de manera clara y efectiva.
Tus Principales Funciones
Identificar temas, áreas o procesos con problemas o posibilidades de mejora.
Generar, promover e implementar Iniciativas Estratégicas
Colaborar en la automatización de procesos y reportes.
Tener la capacidad plantear hipótesis, buscar solución e implementarla
Conocimientos Obligatorios En
Excel/SQL.
Power BI.
Condiciones / Beneficios
Salario a convenir
Contrato a término indefinido
Horario Lunes a viernes de 8:00 am - 5:00 pm
Ambiente de trabajo dinámico y colaborativo
Oportunidad de crecimiento y desarrollo profesional
¡¡Esta es una gran oportunidad para que sigas construyendo tu perfil en Data!!
En Solventa, no solo creamos oportunidades financieras, también cultivamos un ambiente de trabajo vibrante donde cada individuo se siente valorado y motivado a alcanzar su máximo potencial. ¡Únete a nosotros y sé parte de esta emocionante jornada hacia un futuro financiero más inclusivo y accesible para todos!"
"""
print(prueba)
