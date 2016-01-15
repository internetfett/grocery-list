import Ember from 'ember';

export default Ember.Controller.extend({
    sortedList: Ember.computed.sort('model.recipe_ingredients', 'name:asc'),
    isShowingModal: false,
    actions: {
        createItem: function() {
            var ingredient = this.store.createRecord('ingredient', {
                'name': this.get('inputName'),
                'user': this.model.get('user'),
            });
            var recipe_ingredient = this.store.createRecord('recipe-ingredient', {
                'unit': this.get('inputUnit'),
                'amount': this.get('inputAmount'),
            });
            recipe_ingredient.set('recipe', this.model);
            recipe_ingredient.set('ingredient', ingredient);
            recipe_ingredient.save().then(function(){}, function(){ alert('failure'); });
            this.send('toggleModal');
        },
        toggleModal: function() {
            this.toggleProperty('isShowingModal');
        }
    },
    inputName: '', inputUnit: 'unit', inputAmount: 0.125,
    units: ['unit', 'cup', 'oz', 'lb', 'tsp', 'tbsp'],
    amounts: [
        {label: '1/8', value: 0.125},
        {label: '1/4', value: 0.25},
        {label: '1/2', value: 0.5},
        {label: '3/4', value: 0.75},
        {label: '1', value: 1},
        {label: '2', value: 2},
        {label: '3', value: 3},
        {label: '4', value: 4},
        {label: '5', value: 5},
        {label: '6', value: 6},
        {label: '7', value: 7},
        {label: '8', value: 8},
        {label: '9', value: 9},
        {label: '10', value: 10},
    ],
});
