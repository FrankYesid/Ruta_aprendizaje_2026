from pathlib import Path
from textwrap import dedent

root = Path(r"d:\GitHub\Ruta_aprendizaje_2024")

section_titles = {
    "01-Visualización_de_Datos": "Visualización de Datos",
    "02-Tratamiento_de_Datos": "Tratamiento de Datos",
    "03-Aplicación_de_Modelos": "Aplicación de Modelos",
    "04-Analisis_Avanzado": "Análisis Avanzado",
    "05-Proyectos_Educativos": "Proyectos Educativos",
    "06-Integración_con_el_Mundo_Real": "Integración con el Mundo Real",
}

section_descriptions = {
    "01-Visualización_de_Datos": "visualización de datos, storytelling y comunicación de hallazgos.",
    "02-Tratamiento_de_Datos": "limpieza, estandarización y preparación de datos crudos.",
    "03-Aplicación_de_Modelos": "modelado predictivo, optimización y aprendizaje automático aplicado.",
    "04-Analisis_Avanzado": "series temporales, NLP, clustering y técnicas de alto nivel.",
    "05-Proyectos_Educativos": "retos pedagógicos y aplicaciones guiadas para aprender ciencia de datos.",
    "06-Integración_con_el_Mundo_Real": "proyectos aplicados a problemas reales con foco en reproducibilidad y resultados.",
}

root_content = dedent("""\
# Portafolio de Ciencia de Datos y Aprendizaje Autónomo

Este repositorio organiza un portafolio práctico de proyectos de ciencia de datos, desde visualización y limpieza hasta modelado, análisis avanzado y soluciones aplicadas al mundo real.

## Mapa general del flujo

```mermaid
flowchart TD
    A[Datos locales] --> B[Notebooks y scripts]
    B --> C[Análisis exploratorio]
    C --> D[Modelos entrenados]
    C --> E[Reportes HTML y documentos]
    D --> F[Aplicaciones o visualizaciones]
```

## Secciones del repositorio

| Sección | Enfoque | Enlace |
| --- | --- | --- |
| Visualización de Datos | Storytelling visual y dashboards | [01-Visualización_de_Datos](./01-Visualización_de_Datos) |
| Tratamiento de Datos | Limpieza y preparación de datos | [02-Tratamiento_de_Datos](./02-Tratamiento_de_Datos) |
| Aplicación de Modelos | Modelos predictivos y optimización | [03-Aplicación_de_Modelos](./03-Aplicación_de_Modelos) |
| Análisis Avanzado | NLP, series temporales y clustering | [04-Analisis_Avanzado](./04-Analisis_Avanzado) |
| Proyectos Educativos | Ejercicios prácticos y aprendizaje guiado | [05-Proyectos_Educativos](./05-Proyectos_Educativos) |
| Integración con el Mundo Real | Proyectos aplicados y reproducibles | [06-Integración_con_el_Mundo_Real](./06-Integración_con_el_Mundo_Real) |

## Cómo navegar el repositorio

1. Elige la sección que más te interese.
2. Abre notebooks o scripts para revisar el flujo completo.
3. Revisa los datos, resultados y artefactos generados.
4. Usa los proyectos educativos como base antes de pasar a los más aplicados.

## Enlaces recomendados

- [Proyecto 5 de Integración](./06-Integración_con_el_Mundo_Real/Proyecto_5)
- [Proyecto 5 Educativo](./05-Proyectos_Educativos/Proyecto_5)
- [Proyecto 5 de Visualización](./01-Visualización_de_Datos/Proyecto_5)
""")
(root / "README.md").write_text(root_content, encoding="utf-8")

for section, title in section_titles.items():
    section_dir = root / section
    if not section_dir.exists():
        continue
    project_dirs = sorted([p for p in section_dir.iterdir() if p.is_dir() and p.name.startswith("Proyecto_")])
    project_list = "\n".join([f"- [{p.name}]({p.name})" for p in project_dirs])
    section_content = dedent(f"""\
    # {title}

    Esta sección reúne proyectos relacionados con {section_descriptions[section]}.

    ## Objetivo

    Organizar el flujo de trabajo desde los datos hasta los resultados para que cada proyecto sea fácil de revisar y extender.

    ## Proyectos incluidos

    {project_list}

    ## Estructura típica

    - [data/](./data) o subcarpetas con datos locales
    - [notebooks/](./notebooks), [notebook/](./notebook) o [src/](./src) para análisis y scripts
    - [models/](./models) para artefactos entrenados
    - [documents/](./documents), [docs/](./docs) o [html/](./html) para reportes y visualizaciones

    ## Flujo recomendado

    ```mermaid
    flowchart TD
        A[Datos] --> B[Análisis]
        B --> C[Modelado]
        C --> D[Reportes y artefactos]
    ```

    ## Enlaces relacionados

    - [Portafolio principal](../README.md)
    """)
    (section_dir / "README.md").write_text(section_content, encoding="utf-8")

# Project-specific README updates for the most relevant projects
project_readme_updates = {
    "06-Integración_con_el_Mundo_Real/Proyecto_5/README.md": dedent("""\
    # Monitorización de Transporte Público

    Este proyecto analiza retrasos y patrones de movilidad en transporte público para apoyar la toma de decisiones operativas y la mejora de la experiencia del usuario.

    ## Qué incluye

    - [notebook/](./notebook): cuadernos para carga inicial, análisis descriptivo y entrenamiento del modelo.
    - [documents/informe_descriptiva/](./documents/informe_descriptiva): reporte HTML con hallazgos del análisis exploratorio.
    - [models/](./models): modelo serializado y métricas de evaluación guardadas en formato JSON.
    - [data/](./data): conjunto de datos de retrasos de transporte público.

    ## Flujo del proyecto

    1. Carga y revisión inicial del dataset.
    2. Análisis descriptivo y generación de características.
    3. Entrenamiento de un modelo de clasificación.
    4. Guardado del modelo y del informe HTML.

    ## Enlaces relacionados

    - [Integración con el Mundo Real](../README.md)
    - [Portafolio principal](../../README.md)
    """),
    "05-Proyectos_Educativos/Proyecto_5/README.md": dedent("""\
    # Spaceship Titanic

    Este proyecto recrea una tarea de clasificación binaria inspirada en la competencia de Kaggle Spaceship Titanic.

    ## Objetivo

    Entrenar un modelo predictivo para identificar pasajeros transportados a otra dimensión y preparar una app interactiva de ejemplo.

    ## Recursos principales

    - [data/](./data): datos de entrenamiento y prueba.
    - [notebooks/](./notebooks): cuadernos para exploración y modelado.
    - [frontend/](./frontend): aplicación Streamlit para visualizar resultados.
    - [models/](./models): artefactos del modelo entrenado.

    ## Enlaces relacionados

    - [Proyectos Educativos](../README.md)
    - [Portafolio principal](../../README.md)
    """),
}

for rel_path, content in project_readme_updates.items():
    (root / rel_path).write_text(content, encoding="utf-8")
