import Ember from 'ember';

export default Ember.Controller.extend({
    isShowingModal: false,
    actions: {
        generateList: function () {
            var _this = this;
            var date = new Date();
            var checklist_name = "Grocery List " + (date.getMonth() + 1) + "-" + date.getDate();
            var existing = this.model.get('firstObject');
            var checklist = this.store.createRecord('checklist', {
                'name': checklist_name,
                'user': existing.get('user'),
            });
            checklist.save().then(function(response) {
                var __this = _this;
                var insert_id = response.get('id');
                var recipes = {'recipes': _this.get('recipes')};
                var adapter = _this.store.adapterFor('application');
                var url = adapter.buildURL('checklist', insert_id) + 'recipes/';
                adapter.ajax(url, 'POST', {data: recipes}).then(function(response) {
                    checklist.reload();
                    __this.transitionToRoute('checklist', checklist);
                }, function(){ alert('failure'); });
            }, function(){ alert('failure'); });
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
