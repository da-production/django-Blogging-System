# services/api_auth.py
import requests
from django.conf import settings
from blog.utils.redis_token import store_token, get_token

def login_to_api(username: str, password: str,base_url: str,endpoint: str):
    """
    base_url: str = "https://api.cnac.dz"
    endpoint: str = "/api/auth/login/"
    Fonction pour se connecter à l'API externe et stocker le token dans Redis
    :param username: nom d'utilisateur pour l'API
    :param password: mot de passe pour l'API
    """
    url = f"{base_url}{endpoint}"  # URL du endpoint de login
    payload = {"username": username, "password": password}  # données envoyées à l'API form

    # Requête POST pour se connecter à l'API
    response = requests.post(url, json=payload)
    response.raise_for_status()  # lève une exception si erreur HTTP

    data = response.json()  # conversion de la réponse JSON en dictionnaire Python 
    token = data.get("token")  # récupérer le token depuis la réponse (selon l'API) 
    
    if token:
        # Stocke le token dans Redis avec préfixe "external_api:bearer" et TTL de 1h
        store_token(f"Bearer {token}", ttl=3600, key_name="bearer",prefix=username)
    return data  # retourne la réponse complète de l'API (utile pour debug ou affichage)

def bearer_to_api(payload: dict,base_url: str,endpoint: str):
    """
    Fonction pour se connecter à l'API externe et stocker le token dans Redis
    """
    url = f"{base_url}{endpoint}"  # URL du endpoint de login
    payload = payload  # données envoyées à l'API

    # Requête POST pour se connecter à l'API
    response = requests.post(url, json=payload)
    response.raise_for_status()  # lève une exception si erreur HTTP

    data = response.json()  # conversion de la réponse JSON en dictionnaire Python
    token = data.get("token")  # récupérer le token depuis la réponse (selon l'API)
    if token:
        # Stocke le token dans Redis avec préfixe "external_api:bearer" et TTL de 1h
        store_token(f"Bearer {token}", ttl=3600, key_name="bearer",prefix=payload['acronym'])
    return data  # retourne la réponse complète de l'API (utile pour debug ou affichage)

