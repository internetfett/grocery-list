from django.contrib.auth.models import User

from rest_framework import viewsets

from api.serializers import UserSerializer, RecipeSerializer, RecipeIngredientSerializer, IngredientSerializer, CategorySerializer
from api.serializers import ChecklistIngredientSerializer, ChecklistItemSerializer, ChecklistSerializer, ExclusionSerializer, RepeatableSerializer
from checklist.models import Checklist, ChecklistIngredient, ChecklistItem, Exclusion, Repeatable
from recipes.models import Recipe, RecipeIngredient, Ingredient, Category


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ingredients to be viewed or edited.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeIngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipe items to be viewed or edited.
    """
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class ChecklistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checklists to be viewed or edited.
    """
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer


class ChecklistIngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checklist ingredients to be viewed or edited.
    """
    queryset = ChecklistIngredient.objects.all()
    serializer_class = ChecklistIngredientSerializer


class ChecklistItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checklist items to be viewed or edited.
    """
    queryset = ChecklistItem.objects.all()
    serializer_class = ChecklistItemSerializer


class ExclusionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows exclusions to be viewed or edited.
    """
    queryset = Exclusion.objects.all()
    serializer_class = ExclusionSerializer


class RepeatableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows repeatables to be viewed or edited.
    """
    queryset = Repeatable.objects.all()
    serializer_class = RepeatableSerializer
