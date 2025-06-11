from django.contrib import admin

from .models import EquipoFutbol, Jugador, Campeonato, CampeonatoEquipos

admin.site.register(EquipoFutbol)
admin.site.register(Jugador)
admin.site.register(Campeonato)
admin.site.register(CampeonatoEquipos)

