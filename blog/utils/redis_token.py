# utils/redis_token.py
import redis
from django.conf import settings

# Initialisation de la connexion Redis
r = redis.Redis(
    host=settings.REDIS_HOST,   # hôte défini dans settings.py
    port=settings.REDIS_PORT,   # port défini dans settings.py
    db=settings.REDIS_DB,       # base de données choisie
    decode_responses=True        # permet de récupérer des chaînes (str) au lieu de bytes
)
# save token
def store_token(token: str, ttl: int = 3600, key_name: str = 'bearer', prefix: str = ''):
    """
    Stocke un token dans Redis avec un préfixe et un temps d'expiration (TTL)
    :param token: le token à stocker (avec "Bearer " si nécessaire)
    :param ttl: durée de vie en secondes (par défaut 1h)
    :param key_name: nom de la clé pour identifier le token
    """
    redis_key = f"{settings.REDIS_PREFIX}{prefix}:{key_name}"  # clé complète avec préfixe exmple: cnac:bearer or cnas:bearer
    r.set(redis_key, token, ex=ttl)  # stockage avec expiration
    print(f"TOKEN STORED: {token}")
    return redis_key

# get token
def get_token(prefix: str = '', key_name: str = 'bearer'):
    """
    Récupère le token depuis Redis
    :param key_name: nom de la clé utilisée pour le stockage
    """
    redis_key = f"{settings.REDIS_PREFIX}{prefix}:{key_name}"  # clé complète avec préfixe
    return r.get(redis_key)  # retourne None si le token n'existe pas ou a expiré
