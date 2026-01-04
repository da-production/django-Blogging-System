from django.shortcuts import render, get_object_or_404
from .models import Category, Post
from Organisation.models import Organisation
from .services.api_auth import login_to_api, bearer_to_api
from .services.api_client import call_api
import json
from django.contrib import messages
# Create your views here.
def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(category_id=category_id).order_by('-updated_at')
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'category_posts.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'post_detail.html', context)


def test_api(request):
    # Récupération de l’URL de base de l’organisation
    base_url = request.user.organisation.base_url

    osts = Organisation.objects.all()
    # Endpoint "login" de l'organisation
    path = request.user.organisation.endpoints_set.filter(type='login').first()
    path2 = request.user.organisation.endpoints_set.filter(type='doleance').first()
    
    # On utilise GET à la place de POST
    if request.method == 'GET':
        # Récupération automatique de tous les paramètres passés dans l’URL
        params = request.META.get("QUERY_STRING", "").strip()
        # On filtre les paramètres pour garder seulement ceux non vides
        params_dict = {k: v.strip() for k, v in request.GET.items() if v.strip()}

        # Si aucun paramètre valide
        if not params_dict:
            messages.error(request, "Veuillez entrer un NIN ou un Nom + Prénom.")
            return render(request, "api.html")
        acronym = request.user.organisation.acronym
        # Traitement si l’authentification est de type Bearer
        if path.auth == 'bearer':
            # On prépare le payload d’authentification
            payload = {**json.loads(path.body), "acronym": acronym}
            try:
                # Appel API pour récupérer le token Bearer
                bearer_to_api(payload, base_url=base_url, endpoint=path.endpoint)
                # Appel de l’API 'doleance' avec les query strings
                result = call_api(
                    acronym,
                    endpoint=f"{base_url}doleance?{params}",
                    user=request.user
                )
            except Exception as e:
                messages.error(request, str(e))
                return render(request, f"api.html")

            # Rendu avec le résultat
            return render(request, "api.html", {"result": result, "osts": osts})

    # Affichage de la page si pas de GET
    return render(request, "api.html")


