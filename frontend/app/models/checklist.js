import DS from 'ember-data';

export default DS.Model.extend({
    name: DS.attr(),
    checklist_ingredients: DS.hasMany('checklist_ingredient'),
    checklist_items: DS.hasMany('checklist_item'),

    combined: function() {
        var ingredients = this.get('checklist_ingredients');
        var items = this.get('checklist_items');
        var stream = [];
        stream.addObjects(ingredients);
        stream.addObjects(items);
        return stream;
    }.property('checklist_ingredients', 'checklist_items'),
});
