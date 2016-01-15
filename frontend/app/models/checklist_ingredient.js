import Ember from 'ember';
import DS from 'ember-data';

export default DS.Model.extend({
    status: DS.attr(),
    amount: DS.attr(),
    unit: DS.attr(),
    display_amount: DS.attr(),
    ingredient: DS.belongsTo('ingredient', {async: false}),

    name: Ember.computed('ingredient', function() {
        return this.get('ingredient.name');
    }),
    category: Ember.computed('ingredient', function() {
        return this.get('ingredient.category');
    }),
});
