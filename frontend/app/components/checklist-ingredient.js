import Ember from 'ember';

export default Ember.Component.extend({
    tagName: 'li',
    classNameBindings: ['checklist_ingredient.status:active', 'isEditing:editing'],

    init() {
        this._super(...arguments);
        this.set('isEditing', false);
    },

    actions: {
        edit() {
            this.set('isEditing', true);
        },

        save(checklist_ingredient, title) {
            this.set('isEditing', false);
            checklist_ingredient.set('name', name);
            checklist_ingredient.save();
        },

        remove(checklist_ingredient) {
            checklist_ingredient.destroyRecord();
        },

        toggleStatus(checklist_ingredient) {
            checklist_ingredient.toggleProperty('status');
            checklist_ingredient.save();
        }
    }
});
