from .models import Organisation


def organisations(request):
    return {'organisations': Organisation.objects.all()}
