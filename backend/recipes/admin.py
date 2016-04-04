from django.contrib import admin
from django.db.models import Sum

from recipes.models import Category, Recipe, Ingredient, RecipeIngredient


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ['name']
	ordering = ('name',)


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name','calories_per_serving')
    search_fields = ['name']
    inlines = [RecipeIngredientInline]
    actions = ['generate_checklist']

    def generate_checklist(self, request, queryset):
        checklist_id = 1
        from checklist.models import Checklist, ChecklistIngredient, Exclusion, Repeatable
        ids = queryset.values_list('id', flat=True)
        exclusions = Exclusion.objects.values_list('ingredient', flat=True)
        recipe_ingredients = RecipeIngredient.objects.filter(recipe__in=ids) \
            .values('ingredient', 'unit').annotate(amount=Sum('amount'))
        for recipe_ingredient in recipe_ingredients:
            if recipe_ingredient['ingredient'] not in exclusions:
                checklist_ingredient = ChecklistIngredient.objects.create(
                    checklist = Checklist.objects.get(id=checklist_id),
                    amount = recipe_ingredient['amount'],
                    unit = recipe_ingredient['unit'],
                    ingredient = Ingredient.objects.get(id=recipe_ingredient['ingredient'])
                )
        for repeatable in Repeatable.objects.all():
            if repeatable.ingredient:
                repeatable.ingredient.status = False
                repeatable.ingredient.save()
            if repeatable.item:
                repeatable.item.status = False
                repeatable.item.save()
    generate_checklist.short_description = "Generate a checklist from selected recipes"


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ['name']
    ordering = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
