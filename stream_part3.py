import pandas as pd
import streamlit as st

from streamlit_option_menu import option_menu
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'root': {
            'Username': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,          # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

# Authentification
authenticator.login()


# Vérification de l'authentification

if st.session_state["authentication_status"]:
    # Si authentifié
    with st.sidebar:
        authenticator.logout("Déconnexion")
        st.write("Bienvenue " + st.session_state["username"])

    # Menu et contenu principal
    with st.sidebar:
        selection = option_menu(menu_title="Menu", options=["Accueil", "Photos de mes déserts préférés"])

    if selection == "Accueil":
        st.title("Bienvenue sur ma page")
        st.image("https://freerangestock.com/sample/101855/assorted-pastries-on-a-table.jpg")

    elif selection == "Photos de mes déserts préférés":
        st.title("Bienvenue sur mon album de photos de déserts !")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Un fraisier")
            st.image("https://liliebakery.fr/wp-content/uploads/2024/04/fraisier-lilie-bakery-1024x1536.jpg")

        with col2:
            st.header("Une tarte au citron")
            st.image("https://www.sunny-delices.fr/wp-content/uploads/2020/04/tarte-au-citron-meringuee-sans-gluten.jpg")

        with col3:
            st.header("Opéra")
            st.image("https://encoreungateau.com/wp-content/uploads/2019/05/recette-facile-opera-cafe.jpg")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')