"""
[APP STREAMLIT] Générateur interactif de mots de passe.

Interface web pour générer des mots de passe sécurisés avec analyse de force.
Affiche le score et le temps de craquage estimé via zxcvbn.

[USAGE]
    $ streamlit run app.py
"""
import streamlit as st
from strong_password import StrongPassword, TypePassword
from zxcvbn import zxcvbn

st.title("🔐 Générateur de Mots de Passe")

type_choice = st.radio(
    "Type de mot de passe:",
    ["Mémorable (mots)", "Aléatoire (caractères)"]
)

length = st.slider(
    "Longueur:",
    min_value=2,
    max_value=20,
    value=12
)

if st.button("Générer"):
    type_p = (TypePassword.MEMORABLE if "Mémorable" in type_choice 
              else TypePassword.RANDOM)
    gen = StrongPassword(length=length, type_p=type_p)
    password = gen.generate()
    
    # Display password
    st.code(password, language=None)
    st.success("Mot de passe copié dans le presse-papier!")
    
    # Analyze password strength
    results = zxcvbn(password)
    score = results["score"]
    crack_time = results["crack_times_display"]["offline_slow_hashing_1e4_per_second"]
    
    # Display strength metrics
    st.divider()
    st.subheader("Force du mot de passe")
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Score", f"{score}/4")
    
    with col2:
        st.metric("Temps de craquage", crack_time)
