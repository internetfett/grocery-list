import Ember from 'ember';

export default Ember.Component.extend({
    tagName: 'li',
    classNameBindings: ['checklist_item.status:active', 'isEditing:editing'],

    init() {
        this._super(...arguments);
        this.set('isEditing', false);
    },

    actions: {
        edit() {
            this.set('isEditing', true);
        },

        save(checklist_item, title) {
            this.set('isEditing', false);
            checklist_item.set('name', name);
            checklist_item.save();
        },

        remove(checklist_item) {
            checklist_item.destroyRecord();
        },

        toggleStatus(checklist_item) {
            checklist_item.toggleProperty('status');
            checklist_item.save();
        }
    }
});
