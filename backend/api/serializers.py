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
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'category', 'user')


class RecipeIngredientSerializer(serializers.HyperlinkedModelSerializer):
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())
    ingredient = IngredientSerializer(many=False, read_only=False)

    class Meta:
        model = RecipeIngredient
        fields = ('id', 'recipe', 'ingredient', 'amount', 'unit', 'display_amount')

    def create(self, validated_data):
        ingredient = Ingredient.objects.create(**validated_data['ingredient'])
        ingredient.save()
        validated_data['ingredient'] = ingredient
        return RecipeIngredient.objects.create(**validated_data)


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    recipe_ingredients = RecipeIngredientSerializer(many=True, read_only=True, source='recipeingredient_set')
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'recipe_ingredients', 'user')


class ChecklistIngredientSerializer(serializers.HyperlinkedModelSerializer):
    checklist = serializers.PrimaryKeyRelatedField(queryset=Checklist.objects.all())
    ingredient = IngredientSerializer(many=False, read_only=True)

    class Meta:
        model = ChecklistIngredient
        fields = ('id', 'status', 'ingredient', 'amount', 'unit', 'display_amount', 'checklist')


class ChecklistItemSerializer(serializers.HyperlinkedModelSerializer):
    checklist = serializers.PrimaryKeyRelatedField(queryset=Checklist.objects.all())

    class Meta:
        model = ChecklistItem
        fields = ('id', 'status', 'name', 'amount', 'unit', 'display_amount', 'checklist')


class ChecklistSerializer(serializers.HyperlinkedModelSerializer):
    checklist_ingredients = ChecklistIngredientSerializer(many=True, read_only=True, source='checklistingredient_set')
    checklist_items = ChecklistItemSerializer(many=True, read_only=True, source='checklistitem_set')
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Checklist
        fields = ('id', 'name', 'checklist_ingredients', 'checklist_items', 'user')


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


class RecipeListSerializer(serializers.Serializer):
    recipes = serializers.ListField(
        child = serializers.IntegerField()
    )
