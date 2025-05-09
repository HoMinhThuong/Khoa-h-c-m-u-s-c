import streamlit as st
st.set_page_config(
    page_title="Khoa học Màu sắc", layout="wide"
)

st.write("### Chào mừng bạn đến với project Khoa học Màu sắc của mình!")
st.write("# Mình tên là Hồ Minh Thương, MSSV 21158059")

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

