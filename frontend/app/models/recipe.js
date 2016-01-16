import DS from 'ember-data';

export default DS.Model.extend({
    name: DS.attr(),
    recipe_ingredients: DS.hasMany('recipe_ingredient', {async: false}),
    user: DS.attr(),
    //status: DS.attr('boolean', { defaultValue: false }),
});
