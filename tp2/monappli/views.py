from django.shortcuts import render

# Create your views here.

def bonjour(request):
    return render(request, "monappli/bonjour.html")

def saisie(request):
    return render(request, "monappli/saisie.html")

def traitement(request):
    nom = request.POST["nom"]
    return render(request, "monappli/traitement.html",{"nom": nom})