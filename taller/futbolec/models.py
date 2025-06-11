from django.db import models

#Crear las siguientes entidades:

#    Equipo de Futbol: nombre, siglas, username twitter
#    Jugador: nombre, posición campo, número camiseta, sueldo, equipo de fútbol
#    Campeonato: nombre de campeonato, nombre de auspiciante
#    Campeonato Equipos: año, equipo de fútbol, campeonato

class EquipoFutbol(models.Model):
    nombre = models.CharField(max_length=100)
    siglas = models.CharField(max_length=10)
    twitter_username = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.siglas})"
    


class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    posicion_campo = models.CharField(max_length=50)
    numero_camiseta = models.PositiveIntegerField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    equipo_futbol = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE, related_name='jugadores')

    def __str__(self):
        return f"{self.nombre} - {self.equipo_futbol.nombre}"
    

class Campeonato(models.Model):
    nombre = models.CharField(max_length=100)
    auspiciante = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - Auspiciado por {self.auspiciante}"
    

class CampeonatoEquipos(models.Model):
    anio = models.PositiveIntegerField()
    equipo_futbol = models.ForeignKey(EquipoFutbol, on_delete=models.CASCADE, related_name='campeonatos')
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE, related_name='equipos')

    def __str__(self):
        return f"{self.equipo_futbol.nombre} en {self.campeonato.nombre} ({self.anio})"

