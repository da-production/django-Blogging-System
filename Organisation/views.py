from django.shortcuts import render

# Create your views here.
def doleances(request):
    return render(request, "doleances.html")