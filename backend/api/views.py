from django.contrib.auth.models import User

from rest_framework import permissions, status, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from oauth2_provider.ext.rest_framework import TokenHasScope

from api.permissions import IsOwnerOrListing, IsRelatedOwnerOrListing
from api.serializers import UserSerializer, RecipeSerializer, RecipeIngredientSerializer, IngredientSerializer, CategorySerializer
from api.serializers import ChecklistIngredientSerializer, ChecklistItemSerializer, ChecklistSerializer, ExclusionSerializer, RepeatableSerializer, RecipeListSerializer
from checklist.models import Checklist, ChecklistIngredient, ChecklistItem, Exclusion, Repeatable
from recipes.models import Recipe, RecipeIngredient, Ingredient, Category


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows categories to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrListing]

    def get_queryset(self):
        if self.suffix == 'List':
            return self.request.user.category_set.all()
        return self.queryset


class IngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ingredients to be viewed or edited.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrListing]

    def get_queryset(self):
        if self.suffix == 'List':
            return self.request.user.ingredient_set.all()
        return self.queryset


class RecipeIngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipe items to be viewed or edited.
    """
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer
    permission_classes = [permissions.IsAuthenticated, IsRelatedOwnerOrListing]
    owner_related_field = 'recipe'

    def get_queryset(self):
        if self.suffix == 'List':
            return RecipeIngredient.objects.filter(recipe__user=self.request.user.id)
        return self.queryset


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrListing]

    def get_queryset(self):
        if self.suffix == 'List':
            return self.request.user.recipe_set.all()
        return self.queryset


class ChecklistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checklists to be viewed or edited.
    """
    queryset = Checklist.objects.all()
    serializer_class = ChecklistSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrListing]

    def get_queryset(self):
        if self.suffix == 'List':
            return self.request.user.checklist_set.all()
        return self.queryset

    @detail_route(methods=['POST'])
    def recipes(self, request, pk=None):
        checklist = self.get_object()
        serializer = RecipeListSerializer(data=request.data)
        if serializer.is_valid():
            checklist.add_recipes(serializer.data['recipes'])
            return Response({'status': 'success'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChecklistIngredientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checklist ingredients to be viewed or edited.
    """
    queryset = ChecklistIngredient.objects.all()
    serializer_class = ChecklistIngredientSerializer
    permission_classes = [permissions.IsAuthenticated, IsRelatedOwnerOrListing]
    owner_related_field = 'checklist'

    def get_queryset(self):
        if self.suffix == 'List':
            return ChecklistIngredient.objects.filter(checklist__user=self.request.user.id)
        return self.queryset


class ChecklistItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows checklist items to be viewed or edited.
    """
    queryset = ChecklistItem.objects.all()
    serializer_class = ChecklistItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsRelatedOwnerOrListing]
    owner_related_field = 'checklist'

    def get_queryset(self):
        if self.suffix == 'List':
            return ChecklistItem.objects.filter(checklist__user=self.request.user.id)
        return self.queryset


class ExclusionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows exclusions to be viewed or edited.
    """
    queryset = Exclusion.objects.all()
    serializer_class = ExclusionSerializer
    #permission_classes = [permissions.IsAuthenticated, IsRelatedOwnerOrListing]
    #owner_related_field = 'checklist'

    #def get_queryset(self):
    #    if self.suffix == 'List':
    #        return Exclusion.objects.filter(checklist__user=self.request.user.id)
    #    return self.queryset


class RepeatableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows repeatables to be viewed or edited.
    """
    queryset = Repeatable.objects.all()
    serializer_class = RepeatableSerializer
    #permission_classes = [permissions.IsAuthenticated, IsRelatedOwnerOrListing]
    #owner_related_field = 'checklist'

    #def get_queryset(self):
    #    if self.suffix == 'List':
    #        return Repeatable.objects.filter(checklist__user=self.request.user.id)
    #    return self.queryset
