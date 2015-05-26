from django.contrib import admin

from checklist.models import Checklist, ChecklistIngredient, ChecklistItem, Exclusion, Repeatable


class ChecklistIngredientInline(admin.TabularInline):
    model = ChecklistIngredient


class ChecklistItemInline(admin.TabularInline):
    model = ChecklistItem


class ChecklistAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ['name']
	inlines = [ChecklistIngredientInline, ChecklistItemInline]


class ExclusionAdmin(admin.ModelAdmin):
    list_display = ('ingredient',)


class RepeatableAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'item')


admin.site.register(Checklist, ChecklistAdmin)
admin.site.register(Exclusion, ExclusionAdmin)
admin.site.register(Repeatable, RepeatableAdmin)
