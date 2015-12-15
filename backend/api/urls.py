from django.conf.urls import url, include

from rest_framework import routers

from api.views import UserViewSet, RecipeViewSet, RecipeIngredientViewSet, IngredientViewSet, CategoryViewSet
from api.views import ChecklistViewSet, ChecklistIngredientViewSet, ChecklistItemViewSet, ExclusionViewSet, RepeatableViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'recipe_items', RecipeIngredientViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'checklists', ChecklistViewSet)
router.register(r'checklist-ingredients', ChecklistIngredientViewSet)
router.register(r'checklist-items', ChecklistItemViewSet)
router.register(r'exclusions', ExclusionViewSet)
router.register(r'repeatables', RepeatableViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
