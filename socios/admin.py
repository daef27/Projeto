from django.contrib import admin
from django.shortcuts import redirect
from .models import Esporte, Cliente, Doacao
from .models import Parceiro

@admin.register(Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Esporte)
class EsporteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ativo')
    list_filter = ('ativo',)
    search_fields = ('nome',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site')
    search_fields = ('nome',)

@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_sugerido')

from .models import (
    Socio,
    Noticia,
    Historia,
    Diretoria,
    Evento,
    Curso,
    HistoricoPagamento
)


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):

    list_display = ('nome', 'numero_socio', 'cpf', 'status_pagamento')
    list_filter = ('status_pagamento',)
    search_fields = ('nome', 'cpf')

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/login/')


admin.site.register(Noticia)
admin.site.register(Historia)
admin.site.register(Diretoria)
admin.site.register(Evento)
admin.site.register(Curso)
admin.site.register(HistoricoPagamento)
admin.site.site_header = "ASSGA Administration"
admin.site.site_title = "ASSGA Admin"
admin.site.index_title = "Dados da ASSGA"