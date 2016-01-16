import DS from 'ember-data';

export default DS.Model.extend({
    recipes: DS.attr(),
    user: DS.attr(),
});
