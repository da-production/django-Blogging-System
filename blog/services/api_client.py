# services/api_client.py
import requests
from blog.utils.redis_token import get_token

def call_api(username: str, endpoint: str, payload=None,user=None):
    """
    Appelle un endpoint de l'API externe en utilisant le token stocké dans Redis
    :param endpoint: URL complète de l'API
    :param payload: données envoyées à l'API (POST)
    """
    token = get_token(prefix=username, key_name="bearer")  # récupère le token depuis Redis
    if not token:
        raise Exception("Aucun token trouvé dans Redis. Veuillez vous connecter d'abord.")

    # TODO check token expiration
    headers = {
        "Authorization": f"Bearer {token}",  # ajoute le token au header
        "Content-Type": "application/json"  # API attend du JSON
    }

    # response = requests.post(endpoint, headers=headers, json=payload or {})  # POST avec payload
    response = requests.get(endpoint, headers=headers)  # GET avec payload
    response.raise_for_status()  # lève exception si erreur HTTP

    return response.json()  # retourne la réponse JSON
