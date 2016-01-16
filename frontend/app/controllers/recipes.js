import Ember from 'ember';

export default Ember.Controller.extend({
    isShowingModal: false,
    actions: {
        generateList: function () {
            var existing = this.model.get('firstObject');
            var checklist_generator = this.store.createRecord('checklist_generator', {
                'recipes': this.get('recipes'),
                'user': existing.get('user'),
            });
            //checklist_generator.set('recipes', this.get('recipes'));
            checklist_generator.save();
        },
        createRecipe: function() {
            var existing = this.model.get('firstObject');
            var recipe = this.store.createRecord('recipe', {
                'name': this.get('inputName'),
                'user': existing.get('user'),
            });
            recipe.save().then(function(){}, function(){ alert('failure'); });
            this.send('toggleModal');
        },
        toggleModal: function() {
            this.toggleProperty('isShowingModal');
        }
    },
    selectedRecipes: function() {
        var recipes = this.get('model').filterBy('status', true);
        recipes = recipes.mapBy('id');
        this.set('recipes', recipes);
    }.observes('model.@each.status'),
    inputName: '',
});
