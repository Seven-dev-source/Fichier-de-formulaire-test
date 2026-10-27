import re
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Formulaire Test", layout="wide")

dossier = Path(__file__).parent
html = (dossier / "form-1.html").read_text(encoding="utf-8")
css = (dossier / "form-1.css").read_text(encoding="utf-8")

# Remplace <link rel="stylesheet" ...> par le contenu du CSS
html = re.sub(
    r'<link[^>]*rel=["\']stylesheet["\'][^>]*>',
    f"<style>{css}</style>",
    html,
)

components.html(html, height=700, scrolling=True)