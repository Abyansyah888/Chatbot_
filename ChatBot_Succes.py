import streamlit as st

st.set_page_config(page_title="Chatbot")
st.title("Chatbot")
st.write("Tulis namamu di bawah ini untuk lanjut...")

# Nama pembuat (tidak boleh)
nama_pembuat = ["aby", "abyan"]

# Kata ejekan yang dilarang sebagai input
kata_terlarang = ["kamel", "elong"]

# Target nama yang akan dipetakan ke ejekan tertentu
grup_kamel = ["gap", "ghaf", "ghafran"]
grup_elong = ["irham", "ham"]

# Input dari user
jawaban = st.text_input("Siapa namamu?")

if jawaban:
    jawaban_bersih = jawaban.strip().lower()

    if jawaban_bersih in nama_pembuat:
        st.warning("Itu nama pembuat botnya, coba jawab ulang pakai namamu sendiri!")
    elif jawaban_bersih in kata_terlarang:
        st.warning("Nama itu dilarang, coba pakai nama aslimu!")
    elif jawaban_bersih in grup_kamel:
        st.markdown(f"Chatbot: Hai **{jawaban.capitalize()}**, satu kata buat kamu... **KAMEL**.")
    elif jawaban_bersih in grup_elong:
        st.markdown(f"Chatbot: Hai **{jawaban.capitalize()}**, satu kata buat kamu... **ELONG**.")
    else:
        st.info(f"Hai **{jawaban.capitalize()}**, kamu lolos dari ejekan... untuk sekarang 😏")