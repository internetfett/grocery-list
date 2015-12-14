from django.contrib.auth.models import User

from rest_framework import serializers

from checklist.models import Checklist, ChecklistIngredient, ChecklistItem, Exclusion, Repeatable
from recipes.models import Ingredient, Recipe, RecipeIngredient, Category


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'category')


class RecipeIngredientSerializer(serializers.HyperlinkedModelSerializer):
    ingredient = IngredientSerializer(many=False, read_only=True)

    class Meta:
        model = RecipeIngredient
        fields = ('id', 'ingredient', 'amount', 'unit', 'display_amount')


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    items = RecipeIngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'items')


class ChecklistIngredientSerializer(serializers.HyperlinkedModelSerializer):
    ingredient = IngredientSerializer(many=False, read_only=True)

    class Meta:
        model = ChecklistIngredient
        fields = ('id', 'status', 'ingredient', 'amount', 'unit', 'display_amount')


class ChecklistItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChecklistItem
        fields = ('id', 'status', 'name', 'amount', 'unit')


class ChecklistSerializer(serializers.HyperlinkedModelSerializer):
    checklistingredient_set = ChecklistIngredientSerializer(many=True, read_only=True)
    checklistitem_set = ChecklistItemSerializer(many=True, read_only=True)

    class Meta:
        model = Checklist
        fields = ('id', 'name', 'checklistingredient_set', 'checklistitem_set')


class ExclusionSerializer(serializers.HyperlinkedModelSerializer):
    ingredient = IngredientSerializer(many=False, read_only=True)

    class Meta:
        model = Repeatable
        fields = ('id', 'ingredient')


class RepeatableSerializer(serializers.HyperlinkedModelSerializer):
    ingredient = ChecklistIngredientSerializer(many=False, read_only=True)
    item = ChecklistItemSerializer(many=False, read_only=True)

    class Meta:
        model = Repeatable
        fields = ('id', 'ingredient', 'item')
