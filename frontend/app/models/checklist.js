import DS from 'ember-data';

export default DS.Model.extend({
    name: DS.attr(),
    checklist_ingredients: DS.hasMany('checklist_ingredient'),
    checklist_items: DS.hasMany('checklist_item'),
});
