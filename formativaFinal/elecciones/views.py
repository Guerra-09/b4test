from django.shortcuts import render, HttpResponse
from .models import Candidato, Elecciones

elecciones = Elecciones()

# Form section
def form(request):
    return render(request, 'candidatesForm.html')

def formMessage(request):
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    message = elecciones.inscribir(nombre, apellido)

    return render(request, 'message/candidateCreated.html', { 'message':  message })


# Votes Section
def votes(request):
    candidates = elecciones.fetchCandidates()
    return render(request, 'votesView.html', {'candidatos' : candidates})

def voteMessage(request):

    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')

    vote = elecciones.votar(nombre, apellido)

    return render(request, 'message/voteDone.html', {'vote': vote, 'candidatoNombre': nombre, 'candidatoApellido': apellido})


# Results section
def results(request):

    mostVoted = elecciones.results()

    return render(request, 'resultsView.html', { 'mostVoted': mostVoted })

