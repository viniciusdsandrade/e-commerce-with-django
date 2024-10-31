from django.contrib import admin
from .models import Produto, Categoria, ProdutoCategoria


# Inline para o modelo intermediário ProdutoCategoria
class ProdutoCategoriaInline(admin.TabularInline):
    model = ProdutoCategoria
    extra = 1  # Número de formulários em branco para adicionar novas associações
    autocomplete_fields = ['categoria']  # Habilita o autocomplete para o campo categoria


# Configuração do admin para Produto
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'is_ativo')  # Campos exibidos na lista de produtos
    search_fields = ('nome', 'descricao')  # Campos para pesquisa
    list_filter = ('is_ativo', 'categorias')  # Filtros disponíveis
    inlines = [ProdutoCategoriaInline]  # Adiciona o inline de ProdutoCategoria
    autocomplete_fields = ['categorias']  # Habilita o autocomplete para o campo categorias


# Configuração do admin para Categoria
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)  # Campos exibidos na lista de categorias
    search_fields = ('nome',)  # Campos para pesquisa


# Registrar os modelos com suas respectivas configurações personalizadas
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(ProdutoCategoria)
