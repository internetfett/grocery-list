import Ember from 'ember';

export default Ember.Component.extend({
    tagName: 'li',
    classNameBindings: ['model.status:active', 'isEditing:editing'],

    init() {
        this._super(...arguments);
        this.set('isEditing', false);
    },

    actions: {
        edit() {
            this.set('isEditing', true);
        },

        save(name) {
            this.set('isEditing', false);
            var ingredient = this.model.get('ingredient');
            ingredient.set('name', name);
            ingredient.save();
        },

        remove() {
            this.model.destroyRecord();
        },

        toggleStatus() {
            this.model.toggleProperty('status');
            this.model.save();
        }
    },
    isUnit: function() {
        return this.get('units') === 'unit';
    }.property('units'),
});
