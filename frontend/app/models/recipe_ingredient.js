import Ember from 'ember';
import DS from 'ember-data';

export default DS.Model.extend({
    amount: DS.attr(),
    unit: DS.attr(),
    display_amount: DS.attr(),
    recipe: DS.belongsTo('recipe', {async: false}),
    ingredient: DS.belongsTo('ingredient', {async: false}),

    name: Ember.computed('ingredient', function() {
        return this.get('ingredient.name');
    }),
    category: Ember.computed('ingredient', function() {
        return this.get('ingredient.category');
    }),
});
