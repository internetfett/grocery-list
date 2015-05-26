from django.contrib import admin

from recipes.models import Category, Recipe, Ingredient, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ['name']


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']
    inlines = [RecipeIngredientInline]


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ['name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
