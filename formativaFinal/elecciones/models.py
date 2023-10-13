from django.db import models

class Candidato:
    def __init__(self, nombre, apellido) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.votos = 0


class Elecciones:
    def __init__(self) -> None:
        self.candidatos = []

    # HELPERS
    def candidatoExists(self, nombre, apellido):
        for candidate in self.candidatos:
            print(candidate.nombre)
            print(candidate.apellido)
            if candidate.nombre == nombre and candidate.apellido == apellido:
                return True
        return False
            
    def fetchCandidates(self):
        return self.candidatos

    def fetchCandidateVotes(self, nombre, apellido):
        for candidate in self.candidatos:
            if candidate.nombre == nombre and candidate.apellido == apellido:
                print(f'los votos son los siguientes: {candidate.votos}')
                return candidate.votos
                
        return 'Candidato doesnt exists'




    # PRUEBA REQUIREMENTS 
    def inscribir(self, nombre, apellido):

        if self.candidatoExists(nombre, apellido) == True:
            print("Usuario ya existente")
            return 'failure'
            
        else:
            self.candidatos.append(Candidato(nombre, apellido))
            print("Usuario registrado")
            return 'success'

    def votar(self, nombre, apellido):

        for candidato in self.candidatos:
            if candidato.nombre == nombre and candidato.apellido == apellido:
                candidato.votos += 1
                print('voto hecho con exito')
                print(self.fetchCandidateVotes(nombre, apellido))
                return 'success'
                    
        print("fallo al votar")
        return 'failure'

    def results(self):

        mostVoted = Candidato("", "")
        
        for candidato in self.candidatos:
            if candidato.votos > mostVoted.votos:
                mostVoted = candidato
                

        return mostVoted