# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 11:24:17 2025

@author: jahop
"""

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Portafolio - Javier Horacio Pérez Ricárdez", layout="wide")

# Encabezado
st.title("Portafolio Profesional: Analista de Categoría Bebidas")
st.subheader("Javier Horacio Pérez Ricárdez")

st.markdown("---")
st.markdown("### 📍 Ubicación: San Pedro Garza García")
st.markdown("### 💼 Vacante: Analista de Categoría Bebidas en Iconn")
st.markdown("---")

# Función 1: Reportes de desempeño
st.header("📊 1. Elaboración de Reportes de Desempeño")
df_desempeno = pd.DataFrame({
    "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas (millones)": [12.5, 15.2, 14.7, 16.8],
    "Meta (millones)": [13.0, 15.0, 15.0, 17.0]
})
fig1 = px.bar(df_desempeno, x="Mes", y=["Ventas (millones)", "Meta (millones)"],
              barmode="group", title="Comparativo de Ventas vs Meta")
st.plotly_chart(fig1, use_container_width=True)

# Función 2: Seguimiento a promociones
st.header("📈 2. Seguimiento a Promociones")
st.markdown("A continuación se muestra una simulación del impacto de promociones en la venta de bebidas:")
df_promo = pd.DataFrame({
    "Semana": [1, 2, 3, 4],
    "Ventas sin Promo": [200, 210, 205, 215],
    "Ventas con Promo": [250, 270, 260, 275]
})
fig2 = px.line(df_promo, x="Semana", y=["Ventas sin Promo", "Ventas con Promo"],
               markers=True, title="Impacto de Promociones en Ventas")
st.plotly_chart(fig2, use_container_width=True)

# Función 3: Administración de Catálogo
st.header("📦 3. Administración de Catálogo")
st.markdown("Simulación de catálogo de productos activos:")
catalogo = pd.DataFrame({
    "Código": ["B001", "B002", "B003"],
    "Producto": ["Refresco Cola", "Agua Natural", "Jugo Naranja"],
    "Precio": [18.50, 12.00, 22.00],
    "Disponibilidad": ["Disponible", "Disponible", "Agotado"]
})
st.dataframe(catalogo)

# Función 4: Benchmark y tendencias
st.header("📊 4. Benchmark y Evaluación de Tendencias del Mercado")
st.markdown("Comparativo de participación en el mercado de bebidas:")
df_market = pd.DataFrame({
    "Marca": ["Marca A", "Marca B", "Marca C"],
    "Participación (%)": [40, 35, 25]
})
fig3 = px.pie(df_market, names="Marca", values="Participación (%)", title="Participación de Mercado por Marca")
st.plotly_chart(fig3, use_container_width=True)

# Función 5: Comunicación efectiva
st.header("🗣️ 5. Comunicación Efectiva")
st.markdown("""
Como parte de mis habilidades de comunicación:
- Realizo reportes ejecutivos claros y concisos.
- Coordino reuniones con áreas de logística y marketing.
- Participo activamente en la presentación de resultados trimestrales.

✅ A continuación puedes ver un ejemplo de resumen ejecutivo generado automáticamente:
""")
st.info("""
Durante el primer trimestre se observaron crecimientos consistentes en ventas, con un pico en abril debido a una campaña promocional. 
Se requiere reforzar inventarios de jugos para evitar roturas de stock, dado su desempeño en aumento.
""")

# Contacto
st.markdown("---")
st.markdown("### 📬 Contacto:")
st.markdown("- 📧 jahoperi@gmail.com")
st.markdown("- 📄 Este portafolio fue generado con Python como demostración de mis habilidades analíticas.")

