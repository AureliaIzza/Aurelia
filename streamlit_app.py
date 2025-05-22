import streamlit as st

st.title("🧸Aurelia app")
st.write("welcome!💙")
st.image("IMG_20250515_134118.jpg", width=200)
st.write("\n")
st.subheader("Aurel💗Heeseung")
st.write("Lee Heeseung Punya Aurel")

#with col1:
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka st.number_input("Tulis sebuah Angka:", value=0, step=1)
if (angka % 2) == 0:
  st.write(f"{angka} adalah Bilangan Genap")
else:
  st.write(f"{angka} adalah Bilangan Ganjil")
 
