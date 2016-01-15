import Ember from 'ember';

export default Ember.Route.extend({
    title: 'Recipe',
    model(params) {
        return this.store.findRecord('recipe', params.id);
    },
});
